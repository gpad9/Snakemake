rule count:
    input:
        'data/{x}.txt'
    output:
        'results/{x}_c.txt'
    script:
        'scripts/c.py'
