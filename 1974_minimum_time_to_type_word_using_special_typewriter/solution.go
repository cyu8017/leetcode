// LeetCode 1974 - Minimum Time to Type Word Using Special Typewriter
// https://leetcode.com/problems/minimum-time-to-type-word-using-special-typewriter/

func minTimeToType(word string) int {
	cur := byte('a')
	ans := 0
	for i := 0; i < len(word); i++ {
		ch := word[i]
		d := int(ch) - int(cur)
		if d < 0 {
			d = -d
		}
		if 26-d < d {
			d = 26 - d
		}
		ans += d + 1
		cur = ch
	}
	return ans
}
