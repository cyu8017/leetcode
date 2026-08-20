// LeetCode 0791 - Custom Sort String
// https://leetcode.com/problems/custom-sort-string/

func customSortString(order string, s string) string {
	counts := map[byte]int{}
	for i := 0; i < len(s); i++ {
		counts[s[i]]++
	}
	parts := make([]byte, 0, len(s))
	for i := 0; i < len(order); i++ {
		ch := order[i]
		for counts[ch] > 0 {
			parts = append(parts, ch)
			counts[ch]--
		}
	}
	for ch, count := range counts {
		for c := 0; c < count; c++ {
			parts = append(parts, ch)
		}
	}
	return string(parts)
}
