// LeetCode 3499 - Maximize Active Section with Trade I
// https://leetcode.com/problems/maximize-active-section-with-trade-i/

func maxActiveSectionsAfterTrade(s string) int {
	ones := 0
	for _, c := range s {
		if c == '1' {
			ones++
		}
	}
	// find zero segments
	type seg struct{ l, r int }
	zeros := []seg{}
	n := len(s)
	for i := 0; i < n; {
		if s[i] != '0' {
			i++
			continue
		}
		j := i
		for j < n && s[j] == '0' {
			j++
		}
		zeros = append(zeros, seg{i, j - 1})
		i = j
	}
	best := 0
	for i := 0; i+1 < len(zeros); i++ {
		// trade converts ones between two zero segments and those zeros become ones
		gain := (zeros[i].r - zeros[i].l + 1) + (zeros[i+1].r - zeros[i+1].l + 1)
		if gain > best {
			best = gain
		}
	}
	return ones + best
}
