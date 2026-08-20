// LeetCode 3314 - Construct the Minimum Bitwise Array I
// https://leetcode.com/problems/construct-the-minimum-bitwise-array-i/

func minBitwiseArray(nums []int) []int {
	ans := make([]int, len(nums))
	for i, n := range nums {
		ans[i] = -1
		for x := 0; x < n; x++ {
			if x|(x+1) == n {
				ans[i] = x
				break
			}
		}
	}
	return ans
}
