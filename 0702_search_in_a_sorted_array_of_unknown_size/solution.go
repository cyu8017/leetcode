// LeetCode 0702 - Search in a Sorted Array of Unknown Size
// https://leetcode.com/problems/search-in-a-sorted-array-of-unknown-size/

type ArrayReader interface {
	Get(index int) int
}

func search(reader ArrayReader, target int) int {
	right := 1
	for reader.Get(right) < target {
		right <<= 1
	}
	left := right >> 1
	for left <= right {
		mid := (left + right) / 2
		value := reader.Get(mid)
		if value == target {
			return mid
		}
		if value > target {
			right = mid - 1
		} else {
			left = mid + 1
		}
	}
	return -1
}
