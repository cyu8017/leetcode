// LeetCode 3768 - Minimum Inversion Count in Subarrays of Fixed Length
// https://leetcode.com/problems/minimum-inversion-count-in-subarrays-of-fixed-length/

import "sort"

func minInversionCount(nums []int, k int) int64 {
	vals := append([]int(nil), nums...)
	sort.Ints(vals)
	vals = unique3768(vals)
	bit := make([]int, len(vals)+1)
	add := func(i, delta int) {
		for i < len(bit) {
			bit[i] += delta
			i += i & -i
		}
	}
	sum := func(i int) int {
		res := 0
		for i > 0 {
			res += bit[i]
			i -= i & -i
		}
		return res
	}
	rank := make([]int, len(nums))
	var inv int64
	for i, x := range nums {
		rank[i] = sort.SearchInts(vals, x) + 1
		if i < k {
			inv += int64(i - sum(rank[i]))
			add(rank[i], 1)
		}
	}
	best := inv
	for r := k; r < len(nums); r++ {
		left := rank[r-k]
		inv -= int64(sum(left - 1))
		add(left, -1)
		inv += int64(k - 1 - sum(rank[r]))
		add(rank[r], 1)
		if inv < best {
			best = inv
		}
	}
	return best
}

func unique3768(a []int) []int {
	j := 0
	for _, x := range a {
		if j == 0 || a[j-1] != x {
			a[j] = x
			j++
		}
	}
	return a[:j]
}