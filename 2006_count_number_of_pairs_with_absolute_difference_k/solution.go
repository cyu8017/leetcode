// LeetCode 2006 - Count Number of Pairs With Absolute Difference K
// https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/

func countKDifference(nums []int, k int) int {
	freq := map[int]int{}
	ans := 0
	for _, x := range nums {
		ans += freq[x-k] + freq[x+k]
		freq[x]++
	}
	return ans
}
