// LeetCode 2434 - Using a Robot to Print the Lexicographically Smallest String
// https://leetcode.com/problems/using-a-robot-to-print-the-lexicographically-smallest-string/

func robotWithString(s string) string {
	n := len(s)
	minSuf := make([]byte, n+1)
	minSuf[n] = 'z' + 1
	for i := n - 1; i >= 0; i-- {
		minSuf[i] = s[i]
		if minSuf[i+1] < minSuf[i] {
			minSuf[i] = minSuf[i+1]
		}
	}
	stack := []byte{}
	ans := []byte{}
	for i := 0; i < n; i++ {
		stack = append(stack, s[i])
		for len(stack) > 0 && stack[len(stack)-1] <= minSuf[i+1] {
			ans = append(ans, stack[len(stack)-1])
			stack = stack[:len(stack)-1]
		}
	}
	for len(stack) > 0 {
		ans = append(ans, stack[len(stack)-1])
		stack = stack[:len(stack)-1]
	}
	return string(ans)
}
