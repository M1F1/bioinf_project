import argparse
import numpy as np


def fill_interwoven_matrix(super_string: str, subsequenses: [str]):
    """ Fill matrix with bool values using is_intervwoven function.
        First and second loop iterate over matrix elements, third loop iterate over super_string chars;
        if interwoven string is found, within condition statement, element of the matrix is filled
        with true value and iteration stops.
        In the end function return symmetric matrix to doesnt repeat computing the same values.
    """
    n = len(subsequenses)
    interwoven_matrix = np.zeros((n, n))
    start_interwoven = False
    for i in range(n):
        for j in range(n - i):
            for k in range(len(super_string)):
                res = is_interwoven(super_string[k:], subsequenses[i], subsequenses[i + j])
                if res:
                    interwoven_matrix[i][i + j] = res
                    break
    return symmetrize(interwoven_matrix)


def is_interwoven(super_string: str, dna1_string: str, dna2_string: str):
    """ Check if two dna strings can be interwoven into super_string using recursion.
        Every time string are sliced with 1 element and the comparison is made.
    """
    c = super_string[:1]
    s1c = dna1_string[:1]
    s2c = dna2_string[:1]
    new_substring1 = dna1_string[1:]
    new_substring2 = dna2_string[1:]
    new_super_string = super_string[1:]
    if dna1_string == '' and dna2_string == '':
        return True
    elif super_string == '':
        return False
    elif c == s1c and c == s2c:
        return is_interwoven(new_super_string, new_substring1, dna2_string) or\
               is_interwoven(new_super_string, dna1_string, new_substring2)
    elif c == s1c:
        return is_interwoven(new_super_string, new_substring1, dna2_string)
    elif c == s2c:
        return is_interwoven(new_super_string, dna1_string, new_substring2)
    else:
        return False


def symmetrize(m: np.ndarray):
    """ Create symetric matrix"""
    return m + m.T - np.diag(m.diagonal())


def prepare_data(args: str):
    file_content = args.infile.readlines()
    super_string = file_content[0]
    disjoint_subsequences = file_content[1:]
    processed_disjoint_subsequences = list(map(remove_new_line_from_string, disjoint_subsequences))
    return super_string, processed_disjoint_subsequences


def remove_new_line_from_string(string: str):
    return string.replace('\n', '')


def main(args):
    super_string, disjoint_subsequences = prepare_data(args)

    print(F'superstring: {super_string}')
    print(F'subsequences: {disjoint_subsequences}')
    matrix = fill_interwoven_matrix(super_string, disjoint_subsequences)
    print(matrix)
    np.savetxt('result.txt', fmt='%i', X=matrix, newline='\n', delimiter=' ')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Compute interwoven matrix")
    parser.add_argument('infile', type=argparse.FileType('r', encoding='UTF-8'))
    args = parser.parse_args()
    main(args)
