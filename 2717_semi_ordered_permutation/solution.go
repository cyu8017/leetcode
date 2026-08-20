// LeetCode 2717 - Semi-Ordered Permutation
// https://leetcode.com/problems/semi-ordered-permutation/


func semiOrderedPermutation(nums []int) int {
	n := len(nums)
	pos1, posN := 0, 0
	for i, x := range nums {
		if x == 1 {
			pos1 = i
		}
		if x == n {
			posN = i
		}
	}
	ans := pos1 + (n - 1 - posN)
	if pos1 > posN {
		ans--
	}
	return ans
}
