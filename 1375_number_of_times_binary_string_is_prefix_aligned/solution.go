// LeetCode 1375 - Number of Times Binary String Is Prefix-Aligned
// https://leetcode.com/problems/number-of-times-binary-string-is-prefix-aligned/

func numTimesAllBlue(flips []int) int {
	ans, mx := 0, 0
	for i, x := range flips {
		if x > mx {
			mx = x
		}
		if mx == i+1 {
			ans++
		}
	}
	return ans
}
