import http.client
import json
import termcolor

GENES = {
    'FRAT1': 'ENSG00000165879',
    'ADA': 'ENSG00000196839',
    'FXN': 'ENSG00000165060',
    'RNU6_269P': 'ENSG00000212379',
    'MIR633': 'ENSG00000207552',
    'TTTY4C': 'ENSG00000228296',
    'RBMY2YP': 'ENSG00000227633',
    'FGFR3': 'ENSG00000068078',
    'KDR': 'ENSG00000128052',
    'ANK2': 'ENSG00000145362',
}

gene = 'MIR633'
SERVER = 'rest.ensembl.org'
ENDPOINT = '/sequence/id/'
PARAMETERS = '?content-type=application/json'
URL = SERVER + ENDPOINT + GENES[gene] + PARAMETERS

print()
print(f"Server: {SERVER}")
print(f"URL: {URL}")

# Connect with the server
conn = http.client.HTTPConnection(SERVER)

try:
    conn.request("GET", ENDPOINT+GENES[gene]+PARAMETERS)

except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

# -- Read the response message from the server
r1 = conn.getresponse()

# -- Print the status line
print(f"Response received!: {r1.status} {r1.reason}\n")

# -- Read the response's body
data1 = r1.read().decode()

# -- Create a variable with the data,
# -- form the JSON received
info = json.loads(data1)

# Obtain the information
description = info['desc']
sequence = info['seq']

termcolor.cprint("Gene: ", 'green', end="")
print(gene)
termcolor.cprint("Description: ", 'green', end="")
print(description)
termcolor.cprint("Bases: ", 'green', end="")
print(sequence)