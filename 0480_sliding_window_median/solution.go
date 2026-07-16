// LeetCode 0480 - Sliding Window Median
// https://leetcode.com/problems/sliding-window-median/

import "sort"

func medianSlidingWindow(nums []int, k int) []float64 {
	window := append([]int(nil), nums[:k]...)
	sort.Ints(window)
	result := make([]float64, 0, len(nums)-k+1)

	appendMedian := func() {
		if k%2 == 1 {
			result = append(result, float64(window[k/2]))
			return
		}
		result = append(result, float64(window[k/2-1]+window[k/2])/2.0)
	}

	appendMedian()
	for index := k; index < len(nums); index++ {
		outgoing := nums[index-k]
		incoming := nums[index]
		removeIndex := sort.SearchInts(window, outgoing)
		window = append(window[:removeIndex], window[removeIndex+1:]...)
		insertIndex := sort.SearchInts(window, incoming)
		window = append(window, 0)
		copy(window[insertIndex+1:], window[insertIndex:])
		window[insertIndex] = incoming
		appendMedian()
	}
	return result
}
