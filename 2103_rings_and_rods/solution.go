// LeetCode 2103 - Rings and Rods
// https://leetcode.com/problems/rings-and-rods/

func countPoints(rings string) int {
	mask := [10]int{}
	for i := 0; i < len(rings); i += 2 {
		c, r := rings[i], rings[i+1]-'0'
		bit := 0
		if c == 'R' {
			bit = 1
		} else if c == 'G' {
			bit = 2
		} else {
			bit = 4
		}
		mask[r] |= bit
	}
	ans := 0
	for _, m := range mask {
		if m == 7 {
			ans++
		}
	}
	return ans
}
