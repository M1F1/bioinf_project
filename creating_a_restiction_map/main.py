import numpy as np
import math
import argparse


def compute_X(differances):
    print(len(differances))
    # assumption that 0 is in our set
    X = np.array([])
    first_max_el = max(differances)
    X = np.append(0, X)
    X = np.append(X, first_max_el)
    differances.remove(first_max_el)

    for unique_diff in np.unique(differances):
        temp_differences = np.absolute(unique_diff - X)
        if np.sum(np.isin(temp_differences, np.array(differances))) == X.size:
            [differances.remove(diff) for diff in temp_differences]
            X = np.append(X, unique_diff)

    return X


def prepare_data(args: str):
    strings = args.infile.readlines()[0].split()
    data = [int(s) for s in strings]
    return data


def main(args):
    differences = prepare_data(args)
    print(differences)
    X = compute_X(differences)
    X.sort()

    print(X)
    print(X.shape)
    np.savetxt('result.txt', fmt='%i', X=X, newline='\n', delimiter=' ')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="...")
    parser.add_argument('infile', type=argparse.FileType('r', encoding='UTF-8'))
    args = parser.parse_args()
    main(args)
