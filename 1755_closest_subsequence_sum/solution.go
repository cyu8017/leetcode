// LeetCode 1755 - Closest Subsequence Sum
// https://leetcode.com/problems/closest-subsequence-sum/

import "sort"

func minAbsDifference(nums []int, goal int) int {
	n := len(nums)
	left := nums[:n/2]
	right := nums[n/2:]

	sums := func(arr []int) []int {
		vals := make([]int, 1, 1<<len(arr))
		for _, x := range arr {
			size := len(vals)
			for i := 0; i < size; i++ {
				vals = append(vals, vals[i]+x)
			}
		}
		sort.Ints(vals)
		return vals
	}

	abs := func(v int) int {
		if v < 0 {
			return -v
		}
		return v
	}

	a := sums(left)
	b := sums(right)
	best := -1
	j := len(b) - 1
	for _, x := range a {
		for j > 0 && abs(x+b[j]-goal) >= abs(x+b[j-1]-goal) {
			j--
		}
		diff := abs(x + b[j] - goal)
		if best < 0 || diff < best {
			best = diff
		}
	}
	return best
}
