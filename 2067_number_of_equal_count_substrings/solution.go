// LeetCode 2067 - Number of Equal Count Substrings
// https://leetcode.com/problems/number-of-equal-count-substrings/

func equalCountSubstrings(s string, count int) int {
	ans := 0
	n := len(s)
	unique := map[byte]bool{}
	for i := 0; i < n; i++ {
		unique[s[i]] = true
	}
	maxUnique := len(unique)
	for u := 1; u <= maxUnique; u++ {
		needLen := u * count
		if needLen > n {
			break
		}
		freq := [26]int{}
		have := 0
		for i := 0; i < n; i++ {
			c := s[i] - 'a'
			freq[c]++
			if freq[c] == count {
				have++
			} else if freq[c] == count+1 {
				have--
			}
			if i >= needLen {
				p := s[i-needLen] - 'a'
				if freq[p] == count {
					have--
				} else if freq[p] == count+1 {
					have++
				}
				freq[p]--
			}
			if i+1 >= needLen && have == u {
				ans++
			}
		}
	}
	return ans
}
