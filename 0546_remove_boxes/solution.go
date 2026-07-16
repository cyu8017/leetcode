// LeetCode 0546 - Remove Boxes
// https://leetcode.com/problems/remove-boxes/

func removeBoxes(boxes []int) int {
	n := len(boxes)
	memo := make([][][]int, n)
	for left := 0; left < n; left++ {
		memo[left] = make([][]int, n)
		for right := 0; right < n; right++ {
			memo[left][right] = make([]int, n+1)
			for streak := 0; streak <= n; streak++ {
				memo[left][right][streak] = -1
			}
		}
	}

	var dp func(left, right, streak int) int
	dp = func(left, right, streak int) int {
		if left > right {
			return 0
		}
		if memo[left][right][streak] >= 0 {
			return memo[left][right][streak]
		}

		for right > left && boxes[right] == boxes[right-1] {
			right--
			streak++
		}

		best := (streak+1)*(streak+1) + dp(left, right-1, 0)
		for index := left; index < right; index++ {
			if boxes[index] == boxes[right] {
				candidate := dp(left, index, streak+1) + dp(index+1, right-1, 0)
				if candidate > best {
					best = candidate
				}
			}
		}

		memo[left][right][streak] = best
		return best
	}

	return dp(0, n-1, 0)
}
