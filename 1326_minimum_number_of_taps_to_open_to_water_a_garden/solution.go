// LeetCode 1326 - Minimum Number of Taps to Open to Water a Garden
// https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/

func minTaps(n int, ranges []int) int {
	farthest := make([]int, n+1)
	for center, radius := range ranges {
		left := center - radius
		if left < 0 {
			left = 0
		}
		right := center + radius
		if right > n {
			right = n
		}
		if right > farthest[left] {
			farthest[left] = right
		}
	}
	taps, end, reach := 0, 0, 0
	for position := 0; position < n; position++ {
		if farthest[position] > reach {
			reach = farthest[position]
		}
		if position == end {
			if reach <= position {
				return -1
			}
			taps++
			end = reach
		}
	}
	return taps
}
