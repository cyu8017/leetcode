// LeetCode 2957 - Remove Adjacent Almost-Equal Characters
// https://leetcode.com/problems/remove-adjacent-almost-equal-characters/

func removeAlmostEqualCharacters(word string) int {
	ans := 0
	n := len(word)
	i := 1
	for i < n {
		d := int(word[i]) - int(word[i-1])
		if d < 0 {
			d = -d
		}
		if d <= 1 {
			ans++
			i += 2
		} else {
			i++
		}
	}
	return ans
}
