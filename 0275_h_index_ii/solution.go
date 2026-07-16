// LeetCode 0275 - H-Index II
// https://leetcode.com/problems/h-index-ii/

func hIndex(citations []int) int {
	left := 0
	right := len(citations) - 1
	length := len(citations)
	for left <= right {
		mid := (left + right) / 2
		papers := length - mid
		if citations[mid] >= papers {
			right = mid - 1
		} else {
			left = mid + 1
		}
	}
	return length - left
}
