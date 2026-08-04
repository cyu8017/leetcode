// LeetCode 1374 - Generate a String With Characters That Have Odd Counts
// https://leetcode.com/problems/generate-a-string-with-characters-that-have-odd-counts/

func generateTheString(n int) string {
	b := make([]byte, n)
	for i := range b {
		b[i] = 'a'
	}
	if n%2 == 0 {
		b[n-1] = 'b'
	}
	return string(b)
}
