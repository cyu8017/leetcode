// LeetCode 2611 - Mice and Cheese
// https://leetcode.com/problems/mice-and-cheese/


import "sort"
func miceAndCheese(reward1 []int, reward2 []int, k int) int {
	n := len(reward1)
	diff := make([]int, n)
	ans := 0
	for i := 0; i < n; i++ {
		ans += reward2[i]
		diff[i] = reward1[i] - reward2[i]
	}
	sort.Slice(diff, func(i, j int) bool { return diff[i] > diff[j] })
	for i := 0; i < k; i++ {
		ans += diff[i]
	}
	return ans
}
