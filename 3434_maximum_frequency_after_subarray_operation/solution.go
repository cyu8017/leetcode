// LeetCode 3434 - Maximum Frequency After Subarray Operation
// https://leetcode.com/problems/maximum-frequency-after-subarray-operation/

func maxFrequency(nums []int, k int) int {
	base := 0
	for _, x := range nums {
		if x == k {
			base++
		}
	}
	ans := base
	// for each candidate value v != k, convert a subarray of v's to k: kadane on (v->+1, k->-1)
	uniq := map[int]bool{}
	for _, x := range nums {
		uniq[x] = true
	}
	for v := range uniq {
		if v == k {
			continue
		}
		best, cur := 0, 0
		for _, x := range nums {
			delta := 0
			if x == v {
				delta = 1
			} else if x == k {
				delta = -1
			}
			cur += delta
			if cur < 0 {
				cur = 0
			}
			if cur > best {
				best = cur
			}
		}
		if base+best > ans {
			ans = base + best
		}
	}
	return ans
}
