// LeetCode 2364 - Count Number of Bad Pairs
// https://leetcode.com/problems/count-number-of-bad-pairs/

func countBadPairs(nums []int) int64 {
	n := int64(len(nums))
	total := n * (n - 1) / 2
	freq := map[int]int64{}
	var good int64
	for i, x := range nums {
		key := x - i
		good += freq[key]
		freq[key]++
	}
	return total - good
}
