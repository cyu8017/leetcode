// LeetCode 2531 - Make Number of Distinct Characters Equal
// https://leetcode.com/problems/make-number-of-distinct-characters-equal/

func isItPossible(word1 string, word2 string) bool {
	c1, c2 := [26]int{}, [26]int{}
	for i := 0; i < len(word1); i++ {
		c1[word1[i]-'a']++
	}
	for i := 0; i < len(word2); i++ {
		c2[word2[i]-'a']++
	}
	d1, d2 := 0, 0
	for i := 0; i < 26; i++ {
		if c1[i] > 0 {
			d1++
		}
		if c2[i] > 0 {
			d2++
		}
	}
	for a := 0; a < 26; a++ {
		if c1[a] == 0 {
			continue
		}
		for b := 0; b < 26; b++ {
			if c2[b] == 0 {
				continue
			}
			nd1, nd2 := d1, d2
			if a == b {
				if nd1 == nd2 {
					return true
				}
				continue
			}
			if c1[a] == 1 {
				nd1--
			}
			if c1[b] == 0 {
				nd1++
			}
			if c2[b] == 1 {
				nd2--
			}
			if c2[a] == 0 {
				nd2++
			}
			if nd1 == nd2 {
				return true
			}
		}
	}
	return false
}
