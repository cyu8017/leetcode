// LeetCode 2091 - Removing Minimum and Maximum From Array
// https://leetcode.com/problems/removing-minimum-and-maximum-from-array/

func minimumDeletions(nums []int) int {
	n := len(nums)
	mi, ma := 0, 0
	for i, v := range nums {
		if v < nums[mi] {
			mi = i
		}
		if v > nums[ma] {
			ma = i
		}
	}
	if mi > ma {
		mi, ma = ma, mi
	}
	a := ma + 1
	b := n - mi
	c := mi + 1 + n - ma
	ans := a
	if b < ans {
		ans = b
	}
	if c < ans {
		ans = c
	}
	return ans
}
