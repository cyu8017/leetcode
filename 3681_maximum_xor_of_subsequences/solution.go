// LeetCode 3681 - Maximum XOR of Subsequences
// https://leetcode.com/problems/maximum-xor-of-subsequences/

func maxXorSubsequences(nums []int) int {
	basis := make([]int, 32)
	for _, x := range nums {
		cur := x
		for b := 31; b >= 0; b-- {
			if cur&(1<<b) == 0 {
				continue
			}
			if basis[b] == 0 {
				basis[b] = cur
				break
			}
			cur ^= basis[b]
		}
	}
	ans := 0
	for b := 31; b >= 0; b-- {
		if ans^basis[b] > ans {
			ans ^= basis[b]
		}
	}
	return ans
}
