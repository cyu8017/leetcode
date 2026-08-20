// LeetCode 2149 - Rearrange Array Elements by Sign
// https://leetcode.com/problems/rearrange-array-elements-by-sign/

func rearrangeArray(nums []int) []int {
	ans := make([]int, len(nums))
	pos, neg := 0, 1
	for _, x := range nums {
		if x > 0 {
			ans[pos] = x
			pos += 2
		} else {
			ans[neg] = x
			neg += 2
		}
	}
	return ans
}
