// LeetCode 1529 - Minimum Suffix Flips
// https://leetcode.com/problems/minimum-suffix-flips/

func minFlips(target string) int {
	ans := 0
	prev := byte('0')
	for i := 0; i < len(target); i++ {
		if target[i] != prev {
			ans++
			prev = target[i]
		}
	}
	return ans
}
