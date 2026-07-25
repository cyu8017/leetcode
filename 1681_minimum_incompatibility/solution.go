// LeetCode 1681 - Minimum Incompatibility
// https://leetcode.com/problems/minimum-incompatibility/

import "math/bits"

func minimumIncompatibility(nums []int, k int) int {
	n := len(nums)
	size := n / k
	full := (1 << n) - 1
	groups := map[int]int{}
	for mask := 0; mask < 1<<n; mask++ {
		if bits.OnesCount(uint(mask)) != size {
			continue
		}
		vals := []int{}
		seen := map[int]bool{}
		ok := true
		mn, mx := int(1e9), 0
		for i := 0; i < n; i++ {
			if mask>>i&1 == 0 {
				continue
			}
			v := nums[i]
			if seen[v] {
				ok = false
				break
			}
			seen[v] = true
			vals = append(vals, v)
			if v < mn {
				mn = v
			}
			if v > mx {
				mx = v
			}
		}
		if ok && len(vals) == size {
			groups[mask] = mx - mn
		}
	}
	const inf = int(1e9)
	memo := map[int]int{}
	var dp func(mask int) int
	dp = func(mask int) int {
		if mask == full {
			return 0
		}
		if v, ok := memo[mask]; ok {
			return v
		}
		first := 0
		for i := 0; i < n; i++ {
			if mask>>i&1 == 0 {
				first = i
				break
			}
		}
		best := inf
		for g, c := range groups {
			if g>>first&1 != 0 && g&mask == 0 {
				v := c + dp(mask|g)
				if v < best {
					best = v
				}
			}
		}
		memo[mask] = best
		return best
	}
	ans := dp(0)
	if ans >= inf {
		return -1
	}
	return ans
}
