import argparse
import copy

def pref_order():
    """preferd order of amino acids"""
    order = ['HIS', 'ARG', 'LYS', 'GLU', 'ASP', 'GLN', 'ASN', 'SER', 'THR',
             'TRP', 'TYR', 'PHE', 'LEU', 'ILE', 'VAL', 'MET', 'CYS', 'ALA',
             'GLY', 'PRO', 'UNK', 'GAP', 'GPE']
    return order

def opening(file):
    """opening the file"""
    rows = []  # creating a list of rows
    for line in open(file):
        row = line.strip().split()
        rows.append(row)
    return rows

def file_order(rows):
    """creating a list of amino acids' order"""
    names = rows[0][:]
    del names[0:2]  # deleting '#id' and 'aa'
    return names

def sequence(rows):
    """creating a list of amino acids in sequence"""
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

def match(file_order, rmatrix, new_order):
    """matching the matrix to prefered order of amino acids' symbols"""
    eg_symbols = new_order
    f_o = copy.deepcopy(file_order)

    if f_o == eg_symbols:
        return rmatrix
    else:
        r_m = copy.deepcopy(rmatrix)
        new_matrix = []
        for symbol in f_o:
            new_matrix.append(r_m[eg_symbols.index(symbol)])
        return new_matrix

def parse_sequence_profile(file, new_order=False):
    """returning a tuple:
    ([order], [sequence], [reversed matrix])
    """
    if new_order:
        t_pref_order = new_order
    else:
        t_pref_order = pref_order()
    t_rows = opening(file)
    t_file_order = file_order(t_rows)
    t_sequence = sequence(t_rows)
    t_rmatrix = r_matrix(t_rows)
    t_match = match(t_file_order, t_rmatrix, t_pref_order)
    tuple3 = (t_pref_order, t_sequence, t_match)
    return tuple3



if __name__ == "__main__" :
    parser = argparse.ArgumentParser(description="Reads .profile file, prints\
                                                  tuple with three elements:\
                                                  ([amino acids' symbols],\
                                                  [amino acids],\
                                                  [reversed matrix]).")
    parser.add_argument("-f", "--file", help="input .profile file",
                        required=True)
    parser.add_argument("-o", "--order",
                        help="input a list of amino acids' order",
                        required=False)
    args = parser.parse_args()

    print(parse_sequence_profile(args.file, args.order))