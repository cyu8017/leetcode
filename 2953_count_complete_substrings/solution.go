// LeetCode 2953 - Count Complete Substrings
// https://leetcode.com/problems/count-complete-substrings/

func countCompleteSubstrings(word string, k int) int {
	n := len(word)
	ans := 0
	isOk := func(l, r int) bool {
		freq := [26]int{}
		for i := l; i <= r; i++ {
			freq[word[i]-'a']++
		}
		for _, f := range freq {
			if f != 0 && f != k {
				return false
			}
		}
		return true
	}
	for i := 0; i < n; {
		j := i
		for j+1 < n && abs(int(word[j+1])-int(word[j])) <= 2 {
			j++
		}
		// segment [i,j]
		seg := word[i : j+1]
		m := len(seg)
		for chars := 1; chars <= 26; chars++ {
			length := chars * k
			if length > m {
				break
			}
			freq := [26]int{}
			unique := 0
			for r := 0; r < m; r++ {
				c := seg[r] - 'a'
				freq[c]++
				if freq[c] == 1 {
					unique++
				}
				if r >= length {
					c2 := seg[r-length] - 'a'
					freq[c2]--
					if freq[c2] == 0 {
						unique--
					}
				}
				if r >= length-1 && unique == chars {
					ok := true
					for _, f := range freq {
						if f != 0 && f != k {
							ok = false
							break
						}
					}
					if ok {
						ans++
					}
				}
			}
		}
		_ = isOk
		i = j + 1
	}
	return ans
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}
