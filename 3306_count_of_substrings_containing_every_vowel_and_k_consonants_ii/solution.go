// LeetCode 3306 - Count of Substrings Containing Every Vowel and K Consonants II
// https://leetcode.com/problems/count-of-substrings-containing-every-vowel-and-k-consonants-ii/

func countOfSubstrings(word string, k int) int64 {
	return int64(atLeast3306(word, k) - atLeast3306(word, k+1))
}

func atLeast3306(word string, k int) int {
	vow := map[byte]bool{'a': true, 'e': true, 'i': true, 'o': true, 'u': true}
	cnt := map[byte]int{}
	cons, l, ans := 0, 0, 0
	for r := 0; r < len(word); r++ {
		c := word[r]
		if vow[c] {
			cnt[c]++
		} else {
			cons++
		}
		for len(cnt) == 5 && cons >= k {
			ans += len(word) - r
			c2 := word[l]
			if vow[c2] {
				cnt[c2]--
				if cnt[c2] == 0 {
					delete(cnt, c2)
				}
			} else {
				cons--
			}
			l++
		}
	}
	return ans
}
