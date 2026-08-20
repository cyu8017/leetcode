// LeetCode 2958 - Length of Longest Subarray With at Most K Frequency
// https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/

func maxSubarrayLength(nums []int, k int) int {
	freq := map[int]int{}
	ans, left := 0, 0
	for right, v := range nums {
		freq[v]++
		for freq[v] > k {
			freq[nums[left]]--
			left++
		}
		if right-left+1 > ans {
			ans = right - left + 1
		}
	}
	return ans
}
