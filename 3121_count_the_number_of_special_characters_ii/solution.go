// LeetCode 3121 - Count the Number of Special Characters II
// https://leetcode.com/problems/count-the-number-of-special-characters-ii/

func numberOfSpecialChars(word string) (ans int) {
	first := make([]int, 'z'+1)
	last := make([]int, 'z'+1)
	for i, c := range word {
		if first[c] == 0 {
			first[c] = i + 1
		}
		last[c] = i + 1
	}
	for i := 0; i < 26; i++ {
		if last['a'+i] > 0 && last['a'+i] < first['A'+i] {
			ans++
		}
	}
	return
}
