// LeetCode 2275 - Largest Combination With Bitwise AND Greater Than Zero
// https://leetcode.com/problems/largest-combination-with-bitwise-and-greater-than-zero/

func largestCombination(candidates []int) int {
	ans := 0
	for bit := 0; bit < 24; bit++ {
		cnt := 0
		for _, x := range candidates {
			if (x>>bit)&1 == 1 {
				cnt++
			}
		}
		if cnt > ans {
			ans = cnt
		}
	}
	return ans
}
