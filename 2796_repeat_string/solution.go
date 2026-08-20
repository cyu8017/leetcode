// LeetCode 2796 - Repeat String
// https://leetcode.com/problems/repeat-string/

func replicate(str string, times int) string {
	if times <= 0 {
		return ""
	}
	b := make([]byte, 0, len(str)*times)
	for i := 0; i < times; i++ {
		b = append(b, str...)
	}
	return string(b)
}
