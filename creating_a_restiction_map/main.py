import numpy as np
import argparse


def compute_X(differances: [int]):
    """ Function "inverts" process of creating difference multiset and return X set.
        To create X set it is necessery to make initial assumption about smallest
        element in the X set - picking 0.
        Then max element of differences multiset would be the biggest element of the set X.
        To get another elements function iterates over unique values in differences multiset,
        and subtract all current elements of set X. If such differences exists in multiset,
        new element is added to X set and removed from differences multi set.
    """
    # assumption that 0 is in our set
    X = np.array([])
    first_max_el = max(differances)
    X = np.append(0, X)
    X = np.append(X, first_max_el)
    differances.remove(first_max_el)

    for unique_diff in np.unique(differances):
        temp_differences = np.absolute(unique_diff - X)
        if np.sum(np.isin(temp_differences, np.array(differances))) == X.size:
            for diff in temp_differences:
                differances.remove(diff)
            X = np.append(X, unique_diff)

    return X


def prepare_data(args: str):
    strings = args.infile.readlines()[0].split()
    data = [int(s) for s in strings]
    return data


def main(args):
    differences = prepare_data(args)
    X = compute_X(differences)
    X.sort()
    np.savetxt('result.txt', fmt='%i', X=X, newline='\n', delimiter=' ')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=" Comute set X based on difference multiset")
    parser.add_argument('infile', type=argparse.FileType('r', encoding='UTF-8'))
    args = parser.parse_args()
    main(args)
