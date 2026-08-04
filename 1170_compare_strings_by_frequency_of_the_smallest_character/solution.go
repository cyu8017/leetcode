// LeetCode 1170 - Compare Strings by Frequency of the Smallest Character
// https://leetcode.com/problems/compare-strings-by-frequency-of-the-smallest-character/

func numSmallerByFrequency(queries []string, words []string) []int {
	f := func(s string) int {
		best := byte('z' + 1)
		cnt := 0
		for i := 0; i < len(s); i++ {
			if s[i] < best {
				best = s[i]
				cnt = 1
			} else if s[i] == best {
				cnt++
			}
		}
		return cnt
	}
	wf := make([]int, len(words))
	for i, w := range words {
		wf[i] = f(w)
	}
	ans := make([]int, len(queries))
	for i, q := range queries {
		fq := f(q)
		for _, w := range wf {
			if w > fq {
				ans[i]++
			}
		}
	}
	return ans
}
