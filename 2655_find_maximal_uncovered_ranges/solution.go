// LeetCode 2655 - Find Maximal Uncovered Ranges
// https://leetcode.com/problems/find-maximal-uncovered-ranges/


import "sort"

func findMaximalUncoveredRanges(n int, ranges [][]int) [][]int {
	sort.Slice(ranges, func(i, j int) bool {
		if ranges[i][0] != ranges[j][0] {
			return ranges[i][0] < ranges[j][0]
		}
		return ranges[i][1] < ranges[j][1]
	})
	ans := [][]int{}
	cur := 0
	for _, r := range ranges {
		if r[0] > cur {
			ans = append(ans, []int{cur, r[0] - 1})
		}
		if r[1]+1 > cur {
			cur = r[1] + 1
		}
	}
	if cur < n {
		ans = append(ans, []int{cur, n - 1})
	}
	return ans
}
