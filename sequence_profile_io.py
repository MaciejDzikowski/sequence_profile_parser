import copy
import argparse


parser = argparse.ArgumentParser(description='scratch_1')
parser.add_argument('file', help='file')
args = parser.parse_args()


def opening(file):
    """opening the file"""
    rows = []  # creating a list of rows
    for line in open(file):
        row = line.strip().split()
        rows.append(row)

    return rows


def symbols(file):
    """creating a list of amino acids' symbols"""
    names = opening(file)[0][:]

    del names[0:2]  # deleting '#id' and 'aa'

    return names


def aminoacids(file):
    """creating a list of amino acids"""
    aa = [row[1] for row in opening(file)]

    del aa[0]  # deleting 'aa'

    return aa


def convert(m):
    """converting strings to float"""
    m2 = copy.deepcopy(m)
    for row in range(len(m2)):
        for column in range(len(m2[row])):
            m2[row][column] = float(m2[row][column])

    return m2


def matrix(file):
    """creating a matrix"""
    mat = copy.deepcopy(opening(file))

    del mat[0]  # deleting line with aa' names
    for row in mat:
        del row[0:2]

    return convert(matrix)


def r_matrix(file):
    """creating a reversed matrix"""
    r_mat = []
    for i in range(2, len(opening(file)[0])):
        r_mat.append([opening(file)[j][i] for j in range(1, len(opening(file)))])

    return convert(r_mat)


def match(file):
    """matching the matrix to prefered order of amino acids' symbols"""
    eg_symbols = ('ALA', 'VAL', 'PRO', 'ILE', 'LEU', 'MET', 'GLU', 'ASP',
                  'ARG', 'LYS', 'THR', 'SER', 'HIS', 'CYS', 'GLN', 'ASN',
                  'PHE', 'TYR', 'TRP', 'GLY', 'UNK', 'GAP', 'GPE')

    sym = copy.deepcopy(symbols(file))
    r_m = copy.deepcopy(r_matrix(file))

    if sym == eg_symbols:
        return r_m
    else:
        new_matrix = []
        for symbol in sym:
            new_matrix.append(r_m[eg_symbols.index(symbol)])
        return new_matrix


def parse_sequence_profile(file):
    """returning a tuple:
    ([amino acids' symbols], [amino acids], [reversed matrix])
    """
    tuple3 = (symbols(file), aminoacids(file), match(file))
    return tuple3


data(args.file)