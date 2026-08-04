// LeetCode 1542 - Find Longest Awesome Substring
// https://leetcode.com/problems/find-longest-awesome-substring/

func longestAwesome(s string) int {
	first := map[int]int{0: -1}
	mask, answer := 0, 0
	for i := 0; i < len(s); i++ {
		mask ^= 1 << (s[i] - '0')
		if idx, ok := first[mask]; ok {
			if i-idx > answer {
				answer = i - idx
			}
		} else {
			first[mask] = i
		}
		for bit := 0; bit < 10; bit++ {
			candidate := mask ^ (1 << bit)
			if idx, ok := first[candidate]; ok {
				if i-idx > answer {
					answer = i - idx
				}
			}
		}
	}
	return answer
}
