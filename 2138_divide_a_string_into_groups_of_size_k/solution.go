// LeetCode 2138 - Divide a String Into Groups of Size k
// https://leetcode.com/problems/divide-a-string-into-groups-of-size-k/

func divideString(s string, k int, fill byte) []string {
	ans := []string{}
	for i := 0; i < len(s); i += k {
		if i+k <= len(s) {
			ans = append(ans, s[i:i+k])
		} else {
			chunk := []byte(s[i:])
			for len(chunk) < k {
				chunk = append(chunk, fill)
			}
			ans = append(ans, string(chunk))
		}
	}
	return ans
}
