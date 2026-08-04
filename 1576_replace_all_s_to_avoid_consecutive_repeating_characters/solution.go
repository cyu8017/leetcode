// LeetCode 1576 - Replace All ?'s to Avoid Consecutive Repeating Characters
// https://leetcode.com/problems/replace-all-s-to-avoid-consecutive-repeating-characters/

func modifyString(s string) string {
	chars := []byte(s)
	for i := 0; i < len(chars); i++ {
		if chars[i] != '?' {
			continue
		}
		for _, c := range []byte{'a', 'b', 'c'} {
			if (i == 0 || chars[i-1] != c) && (i+1 == len(chars) || chars[i+1] != c) {
				chars[i] = c
				break
			}
		}
	}
	return string(chars)
}
