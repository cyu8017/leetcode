// LeetCode 2498 - Frog Jump II
// https://leetcode.com/problems/frog-jump-ii/

func maxJump(stones []int) int {
	ans := stones[1] - stones[0]
	for i := 2; i < len(stones); i++ {
		diff := stones[i] - stones[i-2]
		if diff > ans {
			ans = diff
		}
	}
	return ans
}
