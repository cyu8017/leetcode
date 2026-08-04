// LeetCode 1415 - The k-th Lexicographical String of All Happy Strings of Length n
// https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/

func getHappyString(n int, k int) string {
	var answer []string
	var build func(path string)
	build = func(path string) {
		if len(path) == n {
			answer = append(answer, path)
			return
		}
		for _, char := range "abc" {
			if len(path) == 0 || path[len(path)-1] != byte(char) {
				build(path + string(char))
			}
		}
	}
	build("")
	if k <= len(answer) {
		return answer[k-1]
	}
	return ""
}
