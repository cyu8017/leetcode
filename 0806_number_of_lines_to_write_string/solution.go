// LeetCode 0806 - Number of Lines To Write String
// https://leetcode.com/problems/number-of-lines-to-write-string/

func numberOfLines(widths []int, s string) []int {
	lines, width := 1, 0
	for i := 0; i < len(s); i++ {
		w := widths[s[i]-'a']
		if width+w > 100 {
			lines++
			width = w
		} else {
			width += w
		}
	}
	return []int{lines, width}
}
