def count(x):
    with open(x, 'w') as f:
        return f.readlines()

count(snakemake.input[0])
