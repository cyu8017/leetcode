// LeetCode 2348 - Number of Zero-Filled Subarrays
// https://leetcode.com/problems/number-of-zero-filled-subarrays/

func zeroFilledSubarray(nums []int) int64 {
	var ans, streak int64
	for _, x := range nums {
		if x == 0 {
			streak++
			ans += streak
		} else {
			streak = 0
		}
	}
	return ans
}
