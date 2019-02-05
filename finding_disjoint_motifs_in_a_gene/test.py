import numpy as np
import unittest
from finding_disjoint_motifs_in_a_gene.main import is_interwoven
from finding_disjoint_motifs_in_a_gene.main import fill_interwoven_matrix
from finding_disjoint_motifs_in_a_gene.main import symmetrize


class TestMain(unittest.TestCase):

	def test_is_interwoven_1(self):
		super_string = 'ACCACGGTT'
		dna_string1 = 'ACAG'
		dna_string2 = 'CCG'

		result = is_interwoven(super_string, dna_string1, dna_string2)
		print(result)
		self.assertEqual(result, True)

	def test_is_interwoven_2(self):
		super_string = 'GACCACAAAAGGTT'
		dna_string1 = 'ACAG'
		dna_string2 = 'CCG'

		result = is_interwoven(super_string, dna_string1, dna_string2)
		self.assertEqual(result, False)

	def test_symmetrize(self):
		init_matrix = np.array([[0, 0, 1],
								[0, 1, 0],
								[0, 0, 0]])
		result = symmetrize(init_matrix)
		np.testing.assert_array_equal(result, np.array([[0, 0, 1],
														[0, 1, 0],
														[1, 0, 0]]))

	def test_fill_interwoven_matrix(self):
		super_string = 'GACCACGGTT'
		dna_strings = ['ACAG', 'GT', 'CCG']
		result = fill_interwoven_matrix(super_string, dna_strings)
		np.testing.assert_array_equal(result, np.array([[0, 0, 1],
														[0, 1, 0],
														[1, 0, 0]]))


if __name__ == '__main__':
	unittest.main()

