// LeetCode 0691 - Stickers to Spell Word
// https://leetcode.com/problems/stickers-to-spell-word/

import "sort"

func minStickers(stickers []string, target string) int {
	need := map[byte]int{}
	for i := 0; i < len(target); i++ {
		need[target[i]]++
	}
	chars := make([]byte, 0, len(need))
	for ch := range need {
		chars = append(chars, ch)
	}
	sort.Slice(chars, func(i, j int) bool { return chars[i] < chars[j] })
	sticks := []map[byte]int{}
	for _, sticker := range stickers {
		counts := map[byte]int{}
		for i := 0; i < len(sticker); i++ {
			if need[sticker[i]] > 0 {
				counts[sticker[i]]++
			}
		}
		if len(counts) > 0 {
			sticks = append(sticks, counts)
		}
	}
	memo := map[string]int{}
	encode := func(state []int) string {
		b := make([]byte, len(state))
		for i, v := range state {
			b[i] = byte(v)
		}
		return string(b)
	}
	const inf = 1 << 30
	var dfs func(state []int) int
	dfs = func(state []int) int {
		key := encode(state)
		if v, ok := memo[key]; ok {
			return v
		}
		i := 0
		for i < len(state) && state[i] == 0 {
			i++
		}
		if i == len(state) {
			return 0
		}
		first := chars[i]
		best := inf
		for _, stick := range sticks {
			if stick[first] == 0 {
				continue
			}
			nxt := append([]int(nil), state...)
			for j, ch := range chars {
				nxt[j] -= stick[ch]
				if nxt[j] < 0 {
					nxt[j] = 0
				}
			}
			cand := 1 + dfs(nxt)
			if cand < best {
				best = cand
			}
		}
		memo[key] = best
		return best
	}
	start := make([]int, len(chars))
	for i, ch := range chars {
		start[i] = need[ch]
	}
	result := dfs(start)
	if result >= inf {
		return -1
	}
	return result
}
