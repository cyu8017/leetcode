// LeetCode 2302 - Count Subarrays With Score Less Than K
// https://leetcode.com/problems/count-subarrays-with-score-less-than-k/

func countSubarrays(nums []int, k int64) int64 {
	var ans, sum int64
	left := 0
	for right := 0; right < len(nums); right++ {
		sum += int64(nums[right])
		for sum*int64(right-left+1) >= k {
			sum -= int64(nums[left])
			left++
		}
		ans += int64(right - left + 1)
	}
	return ans
}
