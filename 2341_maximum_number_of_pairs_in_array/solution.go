// LeetCode 2341 - Maximum Number of Pairs in Array
// https://leetcode.com/problems/maximum-number-of-pairs-in-array/

func numberOfPairs(nums []int) []int {
	cnt := map[int]int{}
	pairs := 0
	for _, x := range nums {
		cnt[x]++
	}
	left := 0
	for _, c := range cnt {
		pairs += c / 2
		left += c % 2
	}
	return []int{pairs, left}
}
