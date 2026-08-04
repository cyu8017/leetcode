// LeetCode 1512 - Number of Good Pairs
// https://leetcode.com/problems/number-of-good-pairs/

func numIdenticalPairs(nums []int) int {
	freq := map[int]int{}
	ans := 0
	for _, x := range nums {
		ans += freq[x]
		freq[x]++
	}
	return ans
}
