import numpy as np


def symmetrize(m):
	return m + m.T - np.diag(m.diagonal())


def fill_interwoven_matrix(super_string, subsequenses):
	n = len(subsequenses)
	interwoven_matrix = np.zeros((n, n))
	for i in range(n):
		for j in range(n - i):
			global s1
			s1 = subsequenses[i]
			global s2
			s2 = subsequenses[i + j]
			interwoven_matrix[i][i + j] = is_interwoven2(super_string, subsequenses[i], subsequenses[i + j])

	return symmetrize(interwoven_matrix)


def check_interweave(superstr, dna1, dna2):
	'''Checks if two dna stands can be interwoven into a superstring.'''
	if len(superstr) == 0:
		return True
	elif dna1[0] == dna2[0] == superstr[0]:
		return check_interweave(dna1[1:], dna2, superstr[1:]) or check_interweave(dna1, dna2[1:], superstr[1:])
	elif dna1[0] == superstr[0]:
		return check_interweave(dna1[1:], dna2, superstr[1:])
	elif dna2[0] == superstr[0]:
		return check_interweave(dna1, dna2[1:], superstr[1:])
	else:
		return False


def is_interwoven2(super_string, dna1_string, dna2_string):

	def restart_sequences():
		return s1, s2
		# dna1_string, dna2_string = restart_sequences()
	c = super_string[:1]
	s1c = dna1_string[:1]
	s2c = dna2_string[:1]
	new_substring1 = dna1_string[1:]
	new_substring2 = dna2_string[1:]
	new_super_string = super_string[1:]
	if (dna1_string != '' or dna2_string != '') and super_string == '':
		return False
	if dna1_string == '' and dna2_string == '':
		return True
	if c == s1c and c == s2c:
		return is_interwoven(new_super_string, new_substring1, dna2_string) or \
			   is_interwoven(new_super_string, dna1_string, new_substring2)
	elif c == s1c:
		return is_interwoven(new_super_string, new_substring1, dna2_string)
	elif c == s2c:
		return is_interwoven(new_super_string, dna1_string, new_substring2)
	else:
		dna1_string, dna2_string = restart_sequences()
		return is_interwoven(new_super_string, dna1_string, dna2_string)


def is_interwoven(super_string, dna1_string, dna2_string):
	def restart_sequences():
		temp_dna1_string = dna1_string
		temp_dna2_string = dna2_string
		return temp_dna1_string, temp_dna2_string

	temp_dna1_string, temp_dna2_string = restart_sequences()
	for c in super_string:
		if temp_dna1_string == '' and temp_dna2_string == '':
			return True
		if c == temp_dna1_string[:1]:
			temp_dna1_string = temp_dna1_string[1:]
		elif c == temp_dna2_string[:1]:
			temp_dna2_string = temp_dna2_string[1:]
		else:
			temp_dna1_string, temp_dna2_string = restart_sequences()

	if temp_dna1_string == '' and temp_dna2_string == '':
		return True
	else:
		return False

if __name__ == '__main__':
	super_string = 'GACCACGGTT'
	dna1_string = 'ACAG'
	dna2_string = 'GT'
	dna3_string = 'CCG'
	subsequences = [dna1_string, dna2_string, dna3_string]
	print(fill_interwoven_matrix(super_string, subsequences))
	# print(is_interwoven(super_string, dna1_string, dna3_string))
