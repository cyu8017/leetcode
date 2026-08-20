// LeetCode 2168 - Unique Substrings With Equal Digit Frequency
// https://leetcode.com/problems/unique-substrings-with-equal-digit-frequency/

func equalDigitFrequency(s string) int {
	n := len(s)
	seen := map[string]bool{}
	for i := 0; i < n; i++ {
		freq := [10]int{}
		maxf, kinds := 0, 0
		for j := i; j < n; j++ {
			d := s[j] - '0'
			if freq[d] == 0 {
				kinds++
			}
			freq[d]++
			if freq[d] > maxf {
				maxf = freq[d]
			}
			if maxf*kinds == j-i+1 {
				seen[s[i:j+1]] = true
			}
		}
	}
	return len(seen)
}
