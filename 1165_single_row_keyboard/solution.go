// LeetCode 1165 - Single-Row Keyboard
// https://leetcode.com/problems/single-row-keyboard/

func calculateTime(keyboard string, word string) int {
	pos := [26]int{}
	for i := 0; i < len(keyboard); i++ {
		pos[keyboard[i]-'a'] = i
	}
	ans, cur := 0, 0
	for i := 0; i < len(word); i++ {
		next := pos[word[i]-'a']
		diff := next - cur
		if diff < 0 {
			diff = -diff
		}
		ans += diff
		cur = next
	}
	return ans
}
