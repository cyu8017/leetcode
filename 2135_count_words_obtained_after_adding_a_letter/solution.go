// LeetCode 2135 - Count Words Obtained After Adding a Letter
// https://leetcode.com/problems/count-words-obtained-after-adding-a-letter/

func wordCount(startWords []string, targetWords []string) int {
	mask := func(w string) int {
		m := 0
		for i := 0; i < len(w); i++ {
			m |= 1 << (w[i] - 'a')
		}
		return m
	}
	have := map[int]bool{}
	for _, w := range startWords {
		have[mask(w)] = true
	}
	ans := 0
	for _, w := range targetWords {
		m := mask(w)
		for i := 0; i < len(w); i++ {
			if have[m^(1<<(w[i]-'a'))] {
				ans++
				break
			}
		}
	}
	return ans
}
