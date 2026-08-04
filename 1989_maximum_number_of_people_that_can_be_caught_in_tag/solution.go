// LeetCode 1989 - Maximum Number of People That Can Be Caught in Tag
// https://leetcode.com/problems/maximum-number-of-people-that-can-be-caught-in-tag/

func catchMaximumAmountofPeople(team []int, dist int) int {
	ans, j := 0, 0
	n := len(team)
	for i, x := range team {
		if x == 0 {
			continue
		}
		for j < n && (team[j] == 1 || i-j > dist) {
			j++
		}
		if j < n {
			d := i - j
			if d < 0 {
				d = -d
			}
			if d <= dist {
				ans++
				j++
			}
		}
	}
	return ans
}
