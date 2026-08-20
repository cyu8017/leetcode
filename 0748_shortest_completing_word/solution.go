// LeetCode 0748 - Shortest Completing Word
// https://leetcode.com/problems/shortest-completing-word/

func shortestCompletingWord(licensePlate string, words []string) string {
	need := map[byte]int{}
	for i := 0; i < len(licensePlate); i++ {
		ch := licensePlate[i]
		if ch >= 'A' && ch <= 'Z' {
			ch += 32
		}
		if ch >= 'a' && ch <= 'z' {
			need[ch]++
		}
	}
	best := ""
	for _, word := range words {
		counts := map[byte]int{}
		for i := 0; i < len(word); i++ {
			counts[word[i]]++
		}
		ok := true
		for ch, cnt := range need {
			if counts[ch] < cnt {
				ok = false
				break
			}
		}
		if ok && (best == "" || len(word) < len(best)) {
			best = word
		}
	}
	return best
}
