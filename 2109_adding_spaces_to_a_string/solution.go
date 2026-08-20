// LeetCode 2109 - Adding Spaces to a String
// https://leetcode.com/problems/adding-spaces-to-a-string/

func addSpaces(s string, spaces []int) string {
	b := make([]byte, 0, len(s)+len(spaces))
	j := 0
	for i := 0; i < len(s); i++ {
		if j < len(spaces) && spaces[j] == i {
			b = append(b, ' ')
			j++
		}
		b = append(b, s[i])
	}
	return string(b)
}
