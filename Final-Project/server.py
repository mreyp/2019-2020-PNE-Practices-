import http.server
import http.client
import socketserver
import termcolor
import json
from pathlib import Path
from Seq1 import Seq

PORT = 8080
HOSTNAME = "rest.ensembl.org"
PARAMETERS = '?content-type=application/json'

print(f"Connection to Server: {HOSTNAME}")

conn = http.client.HTTPConnection(HOSTNAME)

# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True

# -- Create a function for our general HTML response, we will personalize it in each option
def html_response(title="", body="", color='white'):
    default_body = f"""
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>{title}</title>
  </head>
  <body style="background-color: {color};">{body} 
    </body>
    <body>
    <a href="http://127.0.0.1:8080/">Main Page </a>
  </body>
</html>
"""
    return default_body

# -- Function to obtain the ID of a specie
def gene_seq(gene):
    connection = http.client.HTTPConnection(HOSTNAME)
    ENDPOINT1 = '/xrefs/symbol/human/'
    NEW_PARAMETERS = gene + PARAMETERS

    try:
        connection.request("GET", ENDPOINT1 + NEW_PARAMETERS)

    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()

    # -- Read the response message from the server
    r1 = connection.getresponse()

    # -- Read the response's body
    data1 = r1.read().decode()

    # -- Create a variable with the species data from the JSON received
    info = json.loads(data1)[0]
    id_gene = info['id']
    return id_gene

# -- Function to obtain the sequence of a given specie ID
def get_seq(id_gene):
    connection = http.client.HTTPConnection(HOSTNAME)
    ENDPOINT1 = '/sequence/id/'
    NEW_PARAMETERS = id_gene + PARAMETERS

    try:
        connection.request("GET", ENDPOINT1 + NEW_PARAMETERS)

    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()

    # -- Read the response message from the server
    r1 = connection.getresponse()

    # -- Read the response's body
    data1 = r1.read().decode()

    # -- Create a variable with the species data from the JSON received
    seq = json.loads(data1)['seq']

    return seq


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""
        # Print the request line
        termcolor.cprint(self.requestline, 'green')

        # Divide the request line to get the info
        if '?' in self.path:
            arguments = self.path.split('?')

        else:
            arguments = [self.path]
        # First part of the arguments
        resource = arguments[0]

        if resource == "/":
            contents = Path('index.html').read_text()
            code = 200

        elif "/listSpecies" in resource:
            try:
                ENDPOINT = '/info/species/'
                URL = HOSTNAME + ENDPOINT + PARAMETERS
                print(f"URL: {URL}")
                counter = 0

                try:
                    conn.request("GET", ENDPOINT + PARAMETERS)

                except ConnectionRefusedError:
                    print("ERROR! Cannot connect to the Server")
                    exit()

                # -- Read the response message from the server
                r1 = conn.getresponse()

                # -- Print the status line
                print(f"Response received!: {r1.status} {r1.reason}\n")

                # -- Read the response's body
                data1 = r1.read().decode()

                # -- Create a variable with the species data from the JSON received
                info = json.loads(data1)

                # Take the data of the species
                species = info['species']

                if 'json=1' in self.path:
                    li_specie = []                   # Create a list where appending all the species
                    separate = self.path.split('&')  # Separate the specie from the json=1
                    pairs = separate[0].find('=')
                    limit = separate[0][pairs + 1:]  # Take just the number of limit

                    if 'limit=' not in self.path or limit == "":
                        for specie in species:
                            SPECIE = specie['display_name']
                            li_specie.append(SPECIE)
                            order_list = sorted(li_specie)    # Order alphabetically
                            d_json = {'Species': order_list}
                            contents = json.dumps(d_json)     # Convert into JSON

                    else:
                        while counter < int(limit):
                            SPECIE = species[counter]['display_name']
                            li_specie.append(SPECIE)
                            order_list = sorted(li_specie)    # Order alphabetically
                            d_json = {'Species': order_list}
                            contents = json.dumps(d_json)     # Convert into JSON
                            counter += 1

                else:
                    pairs = self.path.find('=')
                    limit = self.path[pairs + 1:]
                    html = f"<p>The total number of species in ensembl is: {len(species)}</p>"

                    if len(arguments)==1 or 'limit=' not in self.path or limit == "":
                        html += f"<p>The names of the species are:<p/>"
                        for specie in species:
                            html += f"<ul><li>{specie['display_name']}</ul></li>"

                    else:
                        html += f"<p>The limit you have selected is: {limit}<p/>"
                        html += f"<p>The names of the species are:<p/>"
                        while counter < int(limit):
                            specie = species[counter]['display_name']
                            html += f"<ul><li>{specie}</ul></li>"
                            counter += 1
                    contents = html_response("LIST OF SPECIES", html, 'lightpink')
                code = 200

            except ValueError:
                contents = Path('limit_error.html').read_text()
                code = 404

            except IndexError:
                contents = Path('limit_error.html').read_text()
                code = 404

        elif "/karyotype" in resource:
            try:
                ENDPOINT = '/info/assembly/'
                pairs = self.path.find('=')
                specie = self.path[pairs + 1:]        # Take just the name of the specie
                if '+' in specie:
                    specie = specie.replace("+", "_")
                if '&' in specie:                     # (When json=1 appears)
                    argument = specie.split('&')
                    arg = argument[0]                 # Take just the name of the specie
                else:
                    arg = specie

                NEW_PARAMETERS = arg + PARAMETERS
                URL = HOSTNAME + ENDPOINT + arg + PARAMETERS
                print(f"URL: {URL}")

                try:
                    conn.request("GET", ENDPOINT + NEW_PARAMETERS)

                except ConnectionRefusedError:
                    print("ERROR! Cannot connect to the Server")
                    exit()

                # -- Read the response message from the server
                r1 = conn.getresponse()

                # -- Print the status line
                print(f"Response received!: {r1.status} {r1.reason}\n")

                # -- Read the response's body
                data1 = r1.read().decode()

                # -- Create a variable with the species data from the JSON received
                info = json.loads(data1)
                kary = info['karyotype']

                if 'json=1' in self.path:
                    l_kary = []              # Create a list where appending all the chromosomes of the karyotype
                    for chrom in kary:
                        l_kary.append(chrom)
                        d_json = {'Species': arg, 'Chromosomes': l_kary}
                        contents = json.dumps(d_json)  # Convert into JSON

                else:
                    html = f"<h3> The names of the chromosomes of the {specie} specie are:</h3>"

                    for chromosome in kary:
                        html += f"<p>{chromosome}</p>"
                    contents = html_response("INFORMATION ABOUT KARYOTYPE", html, 'lightsalmon')
                code = 200

            except KeyError:
                contents = Path("inputs_error.html").read_text()
                code = 404

        elif "/chromosomeLength" in resource:
            try:
                ENDPOINT = '/info/assembly/'
                separate = self.path.split('&')       # Separate the specie from the chromosome
                pairs = separate[0].find('=')
                specie = separate[0][pairs + 1:]      # Take just the name of the specie
                if '+' in specie:
                    specie = specie.replace("+", "_")
                pairs2 = separate[1].find('=')
                chromosome = separate[1][pairs2 + 1:]  # Take just the name of chromosome

                NEW_PARAMETERS = specie + '/' + chromosome + PARAMETERS
                URL = HOSTNAME + ENDPOINT + NEW_PARAMETERS
                print(f"URL: {URL}")

                try:
                    conn.request("GET", ENDPOINT + NEW_PARAMETERS)

                except ConnectionRefusedError:
                    print("ERROR! Cannot connect to the Server")
                    exit()

                # -- Read the response message from the server
                r1 = conn.getresponse()

                # -- Print the status line
                print(f"Response received!: {r1.status} {r1.reason}\n")

                # -- Read the response's body
                data1 = r1.read().decode()

                # -- Create a variable with the species data from the JSON received
                info = json.loads(data1)

                if 'json=1' in self.path:
                    d_json = {'Specie': specie, 'Chromosome': chromosome, 'Length': info['length']}
                    contents = json.dumps(d_json)
                else:
                    html = f"<p> The length of the chromosome {chromosome}" \
                           f" of the {specie} specie is: {info['length']}</p>"
                    contents = html_response("LENGTH OF CHROMOSOME", html, 'lightblue')
                code = 200

            except KeyError:
                contents = Path("inputs_error.html").read_text()
                code = 404

        elif "/geneSeq" in resource:
            try:
                pairs = self.path.find('=')
                arg = self.path[pairs + 1:]

                if '&' in arg:                 # (When json=1 appears)
                    argument = arg.split('&')
                    gene = argument[0]         # Take just the name of the gene
                else:
                    gene = arg

                GENE = gene_seq(gene)
                sequence = get_seq(GENE)
                NEW_PARAMETERS = GENE + PARAMETERS
                URL = HOSTNAME + '/sequence/id/' + NEW_PARAMETERS
                print(f"URL: {URL}")

                if 'json=1' in self.path:
                    d_json = {'Gene name': gene, 'Sequence': sequence}
                    contents = json.dumps(d_json)  # Convert into JSON
                else:
                    html = f"<h3> The sequence of the {gene} gene is: </h3>"
                    html += f"<p><textarea readonly rows = '35' cols = '80'>{sequence}</textarea></p>"
                    contents = html_response("SEQUENCE OF A HUMAN GENE", html, 'yellow')
                code = 200

            except IndexError:
                contents = Path("inputs_error.html").read_text()
                code = 404

            except KeyError:
                contents = Path("inputs_error.html").read_text()
                code = 404

        elif "/geneInfo" in resource:
            try:
                ENDPOINT = '/lookup/id/'
                pairs = self.path.find('=')
                arg = self.path[pairs + 1:]

                if '&' in arg:                     # (When json=1 appears)
                    argument = arg.split('&')
                    gene = argument[0]             # Take just the name of the gene

                else:
                    gene = arg
                GENE = gene_seq(gene)
                sequence = get_seq(GENE)
                NEW_PARAMETERS = GENE + PARAMETERS

                try:
                    conn.request("GET", ENDPOINT + NEW_PARAMETERS)

                except ConnectionRefusedError:
                    print("ERROR! Cannot connect to the Server")
                    exit()

                # -- Read the response message from the server
                r1 = conn.getresponse()

                # -- Print the status line
                print(f"Response received!: {r1.status} {r1.reason}\n")

                # -- Read the response's body
                data1 = r1.read().decode()

                # -- Create a variable with the species data from the JSON received
                info = json.loads(data1)
                seq = Seq(sequence)

                if 'json=1' in self.path:
                    d_json = {'Gene': gene, 'Starting point': info['start'], 'Ending point': info['end'],
                              'Length': seq.len(), 'ID': info['id'],
                              'Chromosome': info['seq_region_name']}
                    contents = json.dumps(d_json)  # Convert into JSON

                else:
                    html = f"<h3>Information about the {gene} gene:</h3>"
                    html += f"<p>Starting point: {info['start']}</p>"
                    html += f"<p>Ending point: {info['end']}</p>"
                    html += f"<p>The length of the gene's sequence is: {seq.len()}</p>"
                    html += f"<p>The ID of the gene is: {info['id']}</p>"
                    html += f"<p>This gene is located in the chromosome: {info['seq_region_name']}</p>"

                    contents = html_response("INFORMATION ABOUT A HUMAN GENE", html, 'salmon')
                code = 200

            except IndexError:
                contents = Path("inputs_error.html").read_text()
                code = 404

            except KeyError:
                contents = Path("inputs_error.html").read_text()
                code = 404

        elif "/geneCalc" in resource:
            try:
                pairs = self.path.find('=')
                arg = self.path[pairs + 1:]

                if '&' in arg:                 # (When json=1 appears)
                    argument = arg.split('&')
                    gene = argument[0]         # Take just the name of the gene

                else:
                    gene = arg
                GENE = gene_seq(gene)
                sequence = get_seq(GENE)
                seq = Seq(sequence)
                NEW_PARAMETERS = GENE + PARAMETERS
                URL = HOSTNAME + '/sequence/id/' + NEW_PARAMETERS
                print(f"URL: {URL}")
                bases = ['A', 'C', 'T', 'G']

                if 'json=1' in self.path:
                    list_bases = []       # Create a list where appending all the calculations for the different bases
                    for base in bases:
                        calculation = f" {base}: {round(seq.count_base(base) * (100 / seq.len()), 2)}%"
                        list_bases.append(calculation)

                    d_json = {'Length': seq.len(), 'Percentage of bases': list_bases}
                    contents = json.dumps(d_json)   # Convert into JSON

                else:
                    html = f"<p> The length is : {seq.len()}</p>"
                    for base in bases:
                        html += f"The percentage of the base {base} is:" \
                                f" {round(seq.count_base(base) * (100 / seq.len()), 2)}% </p> "
                    contents = html_response("GET", html, 'beige')

                code = 200

            except IndexError:
                contents = Path("inputs_error.html").read_text()
                code = 404

        elif "/geneList" in resource:
            try:
                ENDPOINT = '/overlap/region/human/'
                separate = self.path.split('&')       # Separate chromosome from start-end
                pairs = separate[0].find('=')
                chromosome = separate[0][pairs + 1:]  # Take just the name of chromosome
                pairs2 = separate[1].find('=')
                start = separate[1][pairs2 + 1:]      # Take just the number of start
                pairs3 = separate[2].find('=')
                end = separate[2][pairs3 + 1:]        # Take just the number of ending
                PARAMETER = 'content-type=application/json'
                NEW_PARAMETERS = chromosome + ':' + start + '-' + end + '?' + 'feature=gene;' + PARAMETER
                URL = HOSTNAME + ENDPOINT + NEW_PARAMETERS
                print(f"URL: {URL}")

                try:
                    conn.request("GET", ENDPOINT + NEW_PARAMETERS)

                except ConnectionRefusedError:
                    print("ERROR! Cannot connect to the Server")
                    exit()

                # -- Read the response message from the server
                r1 = conn.getresponse()

                # -- Print the status line
                print(f"Response received!: {r1.status} {r1.reason}\n")

                # -- Read the response's body
                data1 = r1.read().decode()

                # -- Create a variable with the species data from the JSON received
                info = json.loads(data1)

                if 'json=1' in self.path:
                    li_genes = []    # Create a list where appending all the genes
                    for gene in info:
                        li_genes.append(gene['external_name'])
                    d_json = {'Chromosome chosen': chromosome, 'Starting point': start,
                              'Ending point': end, 'Genes': li_genes}
                    contents = json.dumps(d_json)  # Convert into JSON

                else:
                    html = f"<p>The genes that are in the chromosome {chromosome} " \
                           f"starting at {start} and ending at {end} are: </p> "
                    for gene in info:
                        html += f"<ul><li>{gene['external_name']}</ul></li>"

                    contents = html_response("LIST OF GENES IN A CHROMOSOME", html, 'lavender')

                code = 200

            except TypeError or IndexError or KeyError:
                contents = Path("inputs_error.html").read_text()
                code = 404

        else:
            contents = Path("error.html").read_text()
            code = 404

        self.send_response(code)

        if 'json=1' in resource:    # JSON type
            self.send_header('Content-Type', 'application/json')

        else:   # HTML type
            self.send_header('Content-Type', 'text/html')

        self.send_header('Content-Length', len(str.encode(contents)))
        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(str.encode(contents))

        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new client, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()