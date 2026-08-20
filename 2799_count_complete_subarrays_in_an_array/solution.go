// LeetCode 2799 - Count Complete Subarrays in an Array
// https://leetcode.com/problems/count-complete-subarrays-in-an-array/

func countCompleteSubarrays(nums []int) int {
	uniq := map[int]bool{}
	for _, v := range nums {
		uniq[v] = true
	}
	need := len(uniq)
	ans := 0
	n := len(nums)
	for i := 0; i < n; i++ {
		seen := map[int]bool{}
		for j := i; j < n; j++ {
			seen[nums[j]] = true
			if len(seen) == need {
				ans += n - j
				break
			}
		}
	}
	return ans
}
