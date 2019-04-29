import argparse
import copy

parser = argparse.ArgumentParser(description="Reads .profile file and prints\
                                              tuple with three elements:\
                                              ([amino acids' symbols],\
                                              [amino acids],\
                                              [reversed matrix]).")
parser.add_argument('-f', '--file', help='input .profile file', required=True)
args = parser.parse_args()

def opening(file):
    """opening the file"""
    rows = []  # creating a list of rows
    for line in open(file):
        row = line.strip().split()
        rows.append(row)

    return rows

def symbols(rows):
    """creating a list of amino acids' symbols"""
    names = rows[0][:]

    del names[0:2]  # deleting '#id' and 'aa'

    return names

def aminoacids(rows):
    """creating a list of amino acids"""
    aa = [row[1] for row in rows]

    del aa[0]  # deleting 'aa'

    return aa

def convert(m):
    """converting strings to float"""
    m2 = copy.deepcopy(m)
    for row in range(len(m2)):
        for column in range(len(m2[row])):
            m2[row][column] = float(m2[row][column])

    return m2

def r_matrix(rows):
    """creating a reversed matrix"""
    r_mat = []
    for i in range(2, len(rows[0])):
        r_mat.append([rows[j][i] for j in range(1, len(rows))])

    return convert(r_mat)

def match(input_sym, rmatrix):
    """matching the matrix to prefered order of amino acids' symbols"""
    eg_symbols = ('ALA', 'VAL', 'PRO', 'ILE', 'LEU', 'MET', 'GLU', 'ASP',
                  'ARG', 'LYS', 'THR', 'SER', 'HIS', 'CYS', 'GLN', 'ASN',
                  'PHE', 'TYR', 'TRP', 'GLY', 'UNK', 'GAP', 'GPE')
    sym = copy.deepcopy(input_sym)
    r_m = copy.deepcopy(rmatrix)

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
    t_rows = opening(file)
    t_symbols = symbols(t_rows)
    t_aminoacids = aminoacids(t_rows)
    t_match = match(t_symbols, t_aminoacids)
    tuple3 = (t_symbols, t_aminoacids, t_match)
    return tuple3

print(parse_sequence_profile(args.file))