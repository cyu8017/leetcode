// LeetCode 1815 - Maximum Number of Groups Getting Fresh Donuts
// https://leetcode.com/problems/maximum-number-of-groups-getting-fresh-donuts/

import (
	"strconv"
	"strings"
)

func maxHappyGroups(batchSize int, groups []int) int {
	count := make([]int, batchSize)
	for _, size := range groups {
		count[size%batchSize]++
	}

	memo := make(map[string]int)

	var dfs func(remainder int, state []int) int
	dfs = func(remainder int, state []int) int {
		key := stateKey(remainder, state)
		if val, ok := memo[key]; ok {
			return val
		}

		best := 0
		for mod := 1; mod < batchSize; mod++ {
			if state[mod] == 0 {
				continue
			}
			state[mod]--
			cand := dfs((remainder+mod)%batchSize, state)
			if cand > best {
				best = cand
			}
			state[mod]++
		}
		if remainder == 0 {
			best++
		}
		memo[key] = best
		return best
	}

	ans := dfs(0, count)
	if count[0] > 0 {
		ans += count[0] - 1
	}
	return ans
}

func stateKey(remainder int, state []int) string {
	var b strings.Builder
	b.WriteString(strconv.Itoa(remainder))
	b.WriteByte('#')
	for i, v := range state {
		if i > 0 {
			b.WriteByte(',')
		}
		b.WriteString(strconv.Itoa(v))
	}
	return b.String()
}
