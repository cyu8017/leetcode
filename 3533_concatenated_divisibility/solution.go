// LeetCode 3533 - Concatenated Divisibility
// https://leetcode.com/problems/concatenated-divisibility/

import (
	"sort"
)

func concatenatedDivisibility(nums []int, k int) []int {
	sort.Ints(nums)
	n := len(nums)
	pows := make([]int, n)
	for i, num := range nums {
		p := 1
		for x := num; x > 0; x /= 10 {
			p = p * 10 % k
		}
		if num == 0 {
			p = 10 % k
		}
		pows[i] = p
	}
	type key struct{ mask, mod int }
	memo := map[key]bool{}
	var dp func(mask, mod int) bool
	dp = func(mask, mod int) bool {
		if mask == (1<<n)-1 {
			return mod == 0
		}
		kk := key{mask, mod}
		if v, ok := memo[kk]; ok {
			return v
		}
		for i := 0; i < n; i++ {
			if mask>>i&1 == 0 {
				nm := (mod*pows[i] + nums[i]) % k
				if dp(mask|1<<i, nm) {
					memo[kk] = true
					return true
				}
			}
		}
		memo[kk] = false
		return false
	}
	var reconstruct func(mask, mod int) []int
	reconstruct = func(mask, mod int) []int {
		for i := 0; i < n; i++ {
			if mask>>i&1 == 0 {
				nm := (mod*pows[i] + nums[i]) % k
				if dp(mask|1<<i, nm) {
					return append([]int{nums[i]}, reconstruct(mask|1<<i, nm)...)
				}
			}
		}
		return nil
	}
	if !dp(0, 0) {
		return []int{}
	}
	return reconstruct(0, 0)
}
