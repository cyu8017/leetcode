// LeetCode 1007 - Minimum Domino Rotations For Equal Row
// https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/

func minDominoRotations(tops []int, bottoms []int) int {
	check := func(target int) int {
		rotTop, rotBot := 0, 0
		for i := 0; i < len(tops); i++ {
			t, b := tops[i], bottoms[i]
			if t != target && b != target {
				return 1 << 30
			}
			if t != target {
				rotTop++
			}
			if b != target {
				rotBot++
			}
		}
		if rotTop < rotBot {
			return rotTop
		}
		return rotBot
	}
	ans := check(tops[0])
	if v := check(bottoms[0]); v < ans {
		ans = v
	}
	if ans == 1<<30 {
		return -1
	}
	return ans
}
