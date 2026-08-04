// LeetCode 1906 - Minimum Absolute Difference Queries
// https://leetcode.com/problems/minimum-absolute-difference-queries/

func minDifference(nums []int, queries [][]int) []int {
	n := len(nums)
	pref := make([][101]int, n+1)
	for i, x := range nums {
		pref[i+1] = pref[i]
		pref[i+1][x]++
	}
	ans := make([]int, len(queries))
	for qi, q := range queries {
		left, right := q[0], q[1]
		prev := -1
		best := 1 << 30
		for value := 1; value <= 100; value++ {
			if pref[right+1][value]-pref[left][value] > 0 {
				if prev != -1 && value-prev < best {
					best = value - prev
				}
				prev = value
			}
		}
		if best == 1<<30 {
			ans[qi] = -1
		} else {
			ans[qi] = best
		}
	}
	return ans
}
