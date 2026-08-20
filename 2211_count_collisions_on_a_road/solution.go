// LeetCode 2211 - Count Collisions on a Road
// https://leetcode.com/problems/count-collisions-on-a-road/

func countCollisions(directions string) int {
	s := []byte(directions)
	i, j := 0, len(s)-1
	for i < len(s) && s[i] == 'L' {
		i++
	}
	for j >= 0 && s[j] == 'R' {
		j--
	}
	ans := 0
	for k := i; k <= j; k++ {
		if s[k] != 'S' {
			ans++
		}
	}
	return ans
}
