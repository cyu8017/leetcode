// LeetCode 1957 - Delete Characters to Make Fancy String
// https://leetcode.com/problems/delete-characters-to-make-fancy-string/

func makeFancyString(s string) string {
	ans := make([]byte, 0, len(s))
	for i := 0; i < len(s); i++ {
		c := s[i]
		if len(ans) >= 2 && ans[len(ans)-1] == c && ans[len(ans)-2] == c {
			continue
		}
		ans = append(ans, c)
	}
	return string(ans)
}
