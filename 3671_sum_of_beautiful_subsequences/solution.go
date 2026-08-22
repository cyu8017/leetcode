// LeetCode 3671 - Sum of Beautiful Subsequences
// https://leetcode.com/problems/sum-of-beautiful-subsequences/

import "sort"

func totalBeauty(nums []int) int {
	const MOD = 1_000_000_007
	mx := 0
	for _, v := range nums {
		if v > mx {
			mx = v
		}
	}
	pos := make([][]int, mx+1)
	for i, v := range nums {
		pos[v] = append(pos[v], i)
	}
	cnt := make([]int, mx+1)
	for g := 1; g <= mx; g++ {
		seq := []int{}
		for m := g; m <= mx; m += g {
			seq = append(seq, pos[m]...)
		}
		if len(seq) == 0 {
			continue
		}
		sort.Ints(seq)
		ways := 1
		for range seq {
			ways = ways * 2 % MOD
		}
		cnt[g] = (ways - 1 + MOD) % MOD
	}
	ans := 0
	for g := mx; g >= 1; g-- {
		for m := 2 * g; m <= mx; m += g {
			cnt[g] = (cnt[g] - cnt[m] + MOD) % MOD
		}
		ans = (ans + cnt[g]*g) % MOD
	}
	return ans
}
