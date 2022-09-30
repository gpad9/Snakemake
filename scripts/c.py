d = {'A':0, 'G':0, 'C':0, 'T':0}
def count_nucleotide(x):
    for i in x[0]:
        if i in 'ACGT':
            d[i] += 1
    return d

def length(x):
    return len(x[0])

def gc_content(x):
    d = count_nucleotide(x)
    gc = (d['G'] + d['C'])/(d['G'] + d['C'] + d['A'] + d['T'])
    return gc

l = []
def input_to_output(x, y):
    with open(x, 'r') as f:
        for line in f.readlines():
            l.append(line.rstrip())
    d = count_nucleotide(l)
    len = length(l)
    gc = gc_content(l)
    with open(y, 'w') as f1:
        f1.write("nucleotide_count: " + str(d) + '\n' + 'length: ' + str(len) + '\n' + 'GC content: ' + str(gc))

input_to_output(snakemake.input[0],snakemake.output[0])
