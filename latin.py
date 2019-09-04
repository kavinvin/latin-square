#!/usr/bin/env python
from random import Random

def shift(xs):
    head, *tail = xs
    return tail + [head]

def standard_latin(n):
    def gen(xs, repeat):
        if repeat == 0:
            return []
        return [xs] + gen(shift(xs), repeat - 1)

    return gen(list(range(1, n + 1)), n)

def latin(n, seed):
    shuffle = lambda xs: Random(seed).sample(xs, len(xs))
    return shuffle([shuffle(x) for x in standard_latin(n)])

def matrix_printer(m, formatter, separator='\t'):
    for row in m:
        print(separator.join(formatter % x for x in row))

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('n', type=int, help='Size of latin square')
    parser.add_argument('--seed', type=int, default=0, help='Seed for random generator')
    parser.add_argument('--standard', action='store_true', help='Generate standard latin square. Ignoring seed.')
    parser.add_argument('--formatter', default='%d', help='Text formatter for each element of latin square')

    args = parser.parse_args()

    if args.standard:
        matrix_printer(standard_latin(args.n), args.formatter)
    else:
        matrix_printer(latin(args.n, args.seed), args.formatter)
