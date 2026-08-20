// LeetCode 2395 - Find Subarrays With Equal Sum
// https://leetcode.com/problems/find-subarrays-with-equal-sum/

func findSubarrays(nums []int) bool {
	seen := map[int]bool{}
	for i := 0; i+1 < len(nums); i++ {
		s := nums[i] + nums[i+1]
		if seen[s] {
			return true
		}
		seen[s] = true
	}
	return false
}
