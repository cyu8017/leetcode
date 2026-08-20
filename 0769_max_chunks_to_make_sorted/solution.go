// LeetCode 0769 - Max Chunks To Make Sorted
// https://leetcode.com/problems/max-chunks-to-make-sorted/

func maxChunksToSorted(arr []int) int {
	chunks, maxSoFar := 0, 0
	for i, value := range arr {
		if value > maxSoFar {
			maxSoFar = value
		}
		if maxSoFar == i {
			chunks++
		}
	}
	return chunks
}
