// LeetCode 0768 - Max Chunks To Make Sorted II
// https://leetcode.com/problems/max-chunks-to-make-sorted-ii/

func maxChunksToSorted(arr []int) int {
	n := len(arr)
	maxLeft := make([]int, n)
	minRight := make([]int, n)
	maxLeft[0] = arr[0]
	for i := 1; i < n; i++ {
		maxLeft[i] = arr[i]
		if maxLeft[i-1] > maxLeft[i] {
			maxLeft[i] = maxLeft[i-1]
		}
	}
	minRight[n-1] = arr[n-1]
	for i := n - 2; i >= 0; i-- {
		minRight[i] = arr[i]
		if minRight[i+1] < minRight[i] {
			minRight[i] = minRight[i+1]
		}
	}
	chunks := 1
	for i := 0; i < n-1; i++ {
		if maxLeft[i] <= minRight[i+1] {
			chunks++
		}
	}
	return chunks
}
