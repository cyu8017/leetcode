// LeetCode 1128 - Number of Equivalent Domino Pairs
// https://leetcode.com/problems/number-of-equivalent-domino-pairs/

func numEquivDominoPairs(dominoes [][]int) int {
	count := map[int]int{}
	ans := 0
	for _, d := range dominoes {
		a, b := d[0], d[1]
		if a > b {
			a, b = b, a
		}
		key := a*10 + b
		ans += count[key]
		count[key]++
	}
	return ans
}
