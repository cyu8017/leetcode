// LeetCode 1024 - Video Stitching
// https://leetcode.com/problems/video-stitching/

func videoStitching(clips [][]int, time int) int {
	furthest := make([]int, time+1)
	for _, clip := range clips {
		start, end := clip[0], clip[1]
		if start <= time && end > furthest[start] {
			furthest[start] = end
		}
	}
	ans, reach, nextReach := 0, 0, 0
	for i := 0; i < time; i++ {
		if furthest[i] > nextReach {
			nextReach = furthest[i]
		}
		if i == reach {
			if nextReach <= i {
				return -1
			}
			ans++
			reach = nextReach
		}
	}
	return ans
}
