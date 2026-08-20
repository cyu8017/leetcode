// LeetCode 2926 - Maximum Balanced Subsequence Sum
// https://leetcode.com/problems/maximum-balanced-subsequence-sum/

import "sort"

func maxBalancedSubsequenceSum(nums []int) int64 {
	n := len(nums)
	keys := make([]int, n)
	for i := 0; i < n; i++ {
		keys[i] = nums[i] - i
	}
	sorted := append([]int{}, keys...)
	sort.Ints(sorted)
	uniq := sorted[:0]
	for _, v := range sorted {
		if len(uniq) == 0 || uniq[len(uniq)-1] != v {
			uniq = append(uniq, v)
		}
	}
	idxOf := func(v int) int {
		return sort.SearchInts(uniq, v) + 1
	}
	bit := make([]int64, len(uniq)+2)
	const negInf = int64(-1) << 60
	for i := range bit {
		bit[i] = negInf
	}
	update := func(i int, val int64) {
		for i < len(bit) {
			if val > bit[i] {
				bit[i] = val
			}
			i += i & -i
		}
	}
	query := func(i int) int64 {
		best := negInf
		for i > 0 {
			if bit[i] > best {
				best = bit[i]
			}
			i -= i & -i
		}
		return best
	}
	var ans int64 = negInf
	for i := 0; i < n; i++ {
		id := idxOf(keys[i])
		best := query(id)
		cur := int64(nums[i])
		if best > negInf/2 {
			cand := best + int64(nums[i])
			if cand > cur {
				cur = cand
			}
		}
		update(id, cur)
		if cur > ans {
			ans = cur
		}
	}
	return ans
}
