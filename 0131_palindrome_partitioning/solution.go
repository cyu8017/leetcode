// LeetCode 0131 - Palindrome Partitioning
func partition(s string) [][]string {
	result := make([][]string, 0)
	path := make([]string, 0)
	var isPalindrome func(int, int) bool
	isPalindrome = func(left, right int) bool {
		for left < right {
			if s[left] != s[right] { return false }
			left++; right--
		}
		return true
	}
	var dfs func(int)
	dfs = func(start int) {
		if start == len(s) {
			result = append(result, append([]string(nil), path...))
			return
		}
		for end := start; end < len(s); end++ {
			if isPalindrome(start, end) {
				path = append(path, s[start:end+1])
				dfs(end + 1)
				path = path[:len(path)-1]
			}
		}
	}
	dfs(0)
	return result
}