// LeetCode 2423 - Remove Letter To Equalize Frequency
// https://leetcode.com/problems/remove-letter-to-equalize-frequency/

func equalFrequency(word string) bool {
	for skip := 0; skip < len(word); skip++ {
		cnt := [26]int{}
		for i := 0; i < len(word); i++ {
			if i == skip {
				continue
			}
			cnt[word[i]-'a']++
		}
		freq := map[int]int{}
		for _, c := range cnt {
			if c > 0 {
				freq[c]++
			}
		}
		if len(freq) == 1 {
			return true
		}
	}
	return false
}
