'''
Test Cases for mmf_problem

'''
import pytest

import mmf_problem


# PyTest Fixtures
@pytest.fixture(scope="module")
def pass_list(request):

	return ['[]', '()', '()[]', 'a(b[c]d)e', '[[[((()))]]]', '([([])])', '{[]}']

@pytest.fixture(scope="module")
def fail_list(request):
	return ['([([)])' , '[', ']', '(', '[(])', 'asdfasdf]]]', '(((adsfb]]]', '{{[()]}']

#Start Test
class TestV1():
	def test_pass_v1(self, pass_list):
		'''
		Loop through test_pass cases and test if string is valid. 
		Throw an assertionerror if failed.
		'''

		for s in pass_list:
			val = mmf_problem.is_string_valid_v1(s)

			assert val == True


	def test_fail_v1(self, fail_list):
		'''
		Loop through test_fail cases and test if string is invalid
		Throw an assertionerror if failed
		'''

		for s in fail_list:
			val = mmf_problem.is_string_valid_v1(s)

			assert val == False


class TestStack():

	def test_pass_optimized(self, pass_list):
		'''
		Loop through test_pass cases and test if string is valid. 
		Throw an assertionerror if failed.
		'''

		for s in pass_list:
			val = mmf_problem.is_string_valid(s)

			assert val == True


	def test_fail_optimized(self, fail_list):
		'''
		Loop through test_fail cases and test if string is invalid. 
		Throw an assertionerror if failed.
		'''

		for s in fail_list:
			val = mmf_problem.is_string_valid(s)
			
			assert val == False



def main():
	pass

if __name__ == '__main__':
	main()