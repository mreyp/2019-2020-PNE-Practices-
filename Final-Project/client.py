import http.client

SERVER = 'localhost'
PORT = 8080
endpoints = ['/', '/listSpecies?limit=10', '/listSpecies?limit=', '/listSpecies?limit=0', '/listSpecies?limit=wrong',
             '/listSpecies?limit=10&json=1', '/listSpecies?limit=&json=1', '/listSpecies?limit=wrong&json=1',
             '/listSpecies?limit=400', '/listSpecies?limit=400&json=1',
             '/karyotype?specie=mouse', '/karyotype?specie=human', '/karyotype?specie=homo+sapiens',
             '/karyotype?specie=coronavirus', '/karyotype?specie=coronavirus&json=1',
             '/karyotype?specie=human&json=1', '/karyotype?specie=homo+sapiens&json=1',
             '/chromosomeLength?specie=mouse&chromo=1', '/chromosomeLength?specie=homo+sapiens&chromo=1',
             '/chromosomeLength?specie=mouse&chromo=abc', '/chromosomeLength?specie=coronavirus&chromo=1',
             '/chromosomeLength?specie=mouse&chromo=1&json=1', '/chromosomeLength?specie=mouse&chromo=abc&json=1'
             '/geneSeq?gene=FRAT1', '/geneSeq?gene=12', '/geneSeq?gene=abcd',
             '/geneSeq?gene=FRAT1&json=1', '/geneSeq?gene=abcd&json=1',
             '/geneInfo?gene=FRAT1', '/geneInfo?gene=20', '/geneInfo?gene=abcd',
             '/geneInfo?gene=FRAT1&json=1', '/geneInfo?gene=abcd&json=1',
             '/geneCalc?gene=FRAT1', '/geneCalc?gene=29', '/geneCalc?gene=abcd',
             '/geneCalc?gene=FRAT1&json=1', '/geneCalc?gene=wrong&json=1',
             '/geneList?chromo=1&start=0&end=30000', '/geneList?chromo=abcd&start=0&end=30000',
             '/geneList?chromo=1&start=0&end=1', '/geneList?chromo=1&start=0&end=30000&json=1',
             '/geneList?chromo=1&start=0&end=1&json=1', '/geneList?chromo=abcd&start=0&end=30000&json=1', '/error']

counter = 0

for ENDPOINT in endpoints:
    counter += 1
    URL = SERVER + ENDPOINT

    print()
    print('* TEST', counter ,':\n')
    print('* INPUT: ')
    print(URL, '\n')
    print('* OUTPUT: ')

    # Connect with the server
    conn = http.client.HTTPConnection(SERVER, PORT)

    # -- Send the request message, using the GET method.
    try:
        conn.request("GET", ENDPOINT)

    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()

    # -- Read the response message from the server
    r1 = conn.getresponse()

    # -- Print the status line
    print(f"Response received!: {r1.status} {r1.reason}\n")

    # -- Read the response's body
    data1 = r1.read().decode("utf-8")
    print(data1, '\n')