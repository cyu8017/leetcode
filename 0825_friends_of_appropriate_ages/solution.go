// LeetCode 0825 - Friends Of Appropriate Ages
// https://leetcode.com/problems/friends-of-appropriate-ages/

func numFriendRequests(ages []int) int {
	count := make([]int, 121)
	for _, age := range ages {
		count[age]++
	}
	ans := 0
	for x := 1; x <= 120; x++ {
		if count[x] == 0 {
			continue
		}
		for y := 1; y <= 120; y++ {
			if count[y] == 0 {
				continue
			}
			if float64(y) <= 0.5*float64(x)+7 || y > x || (y > 100 && x < 100) {
				continue
			}
			ans += count[x] * count[y]
			if x == y {
				ans -= count[x]
			}
		}
	}
	return ans
}
