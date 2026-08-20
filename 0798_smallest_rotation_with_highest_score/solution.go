// LeetCode 0798 - Smallest Rotation with Highest Score
// https://leetcode.com/problems/smallest-rotation-with-highest-score/

func bestRotation(nums []int) int {
	n := len(nums)
	change := make([]int, n)
	for i := range change {
		change[i] = 1
	}
	for i, value := range nums {
		change[(i-value+1+n)%n]--
	}
	for i := 1; i < n; i++ {
		change[i] += change[i-1]
	}
	best, idx := change[0], 0
	for i := 1; i < n; i++ {
		if change[i] > best {
			best = change[i]
			idx = i
		}
	}
	return idx
}
