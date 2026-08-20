// LeetCode 0949 - Largest Time for Given Digits
// https://leetcode.com/problems/largest-time-for-given-digits/

import "fmt"

func largestTimeFromDigits(arr []int) string {
	best := ""
	used := [4]bool{}
	var dfs func([]int)
	dfs = func(cur []int) {
		if len(cur) == 4 {
			hours := 10*cur[0] + cur[1]
			minutes := 10*cur[2] + cur[3]
			if hours < 24 && minutes < 60 {
				cand := fmt.Sprintf("%02d:%02d", hours, minutes)
				if cand > best {
					best = cand
				}
			}
			return
		}
		for i := 0; i < 4; i++ {
			if used[i] {
				continue
			}
			used[i] = true
			dfs(append(cur, arr[i]))
			used[i] = false
		}
	}
	dfs(nil)
	return best
}
