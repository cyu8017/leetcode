// LeetCode 2251 - Number of Flowers in Full Bloom
// https://leetcode.com/problems/number-of-flowers-in-full-bloom/

import "sort"

func fullBloomFlowers(flowers [][]int, people []int) []int {
	start := make([]int, len(flowers))
	end := make([]int, len(flowers))
	for i, f := range flowers {
		start[i] = f[0]
		end[i] = f[1]
	}
	sort.Ints(start)
	sort.Ints(end)
	ans := make([]int, len(people))
	for i, t := range people {
		started := sort.Search(len(start), func(j int) bool { return start[j] > t })
		ended := sort.Search(len(end), func(j int) bool { return end[j] >= t })
		ans[i] = started - ended
	}
	return ans
}
