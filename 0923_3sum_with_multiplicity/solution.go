// LeetCode 0923 - 3Sum With Multiplicity
// https://leetcode.com/problems/3sum-with-multiplicity/

import "sort"

func threeSumMulti(arr []int, target int) int {
	const MOD = 1000000007
	count := map[int]int{}
	for _, x := range arr {
		count[x]++
	}
	keys := make([]int, 0, len(count))
	for k := range count {
		keys = append(keys, k)
	}
	sort.Ints(keys)
	ans := 0
	for i, a := range keys {
		for j := i; j < len(keys); j++ {
			b := keys[j]
			c := target - a - b
			if c < b {
				break
			}
			if _, ok := count[c]; !ok {
				continue
			}
			if a == b && b == c {
				ans += count[a] * (count[a] - 1) * (count[a] - 2) / 6
			} else if a == b {
				ans += count[a] * (count[a] - 1) / 2 * count[c]
			} else if b == c {
				ans += count[a] * count[b] * (count[b] - 1) / 2
			} else {
				ans += count[a] * count[b] * count[c]
			}
		}
	}
	return ans % MOD
}
