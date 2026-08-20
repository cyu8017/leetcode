// LeetCode 2537 - Count the Number of Good Subarrays
// https://leetcode.com/problems/count-the-number-of-good-subarrays/

func countGood(nums []int, k int) int64 {
	freq := map[int]int{}
	var pairs, ans int64
	left := 0
	for right, x := range nums {
		pairs += int64(freq[x])
		freq[x]++
		for pairs >= int64(k) {
			ans += int64(len(nums) - right)
			freq[nums[left]]--
			pairs -= int64(freq[nums[left]])
			left++
		}
	}
	return ans
}
