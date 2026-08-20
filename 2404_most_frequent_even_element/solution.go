// LeetCode 2404 - Most Frequent Even Element
// https://leetcode.com/problems/most-frequent-even-element/

func mostFrequentEven(nums []int) int {
	cnt := map[int]int{}
	ans, best := -1, 0
	for _, x := range nums {
		if x%2 != 0 {
			continue
		}
		cnt[x]++
		if cnt[x] > best || (cnt[x] == best && (ans == -1 || x < ans)) {
			best = cnt[x]
			ans = x
		}
	}
	return ans
}
