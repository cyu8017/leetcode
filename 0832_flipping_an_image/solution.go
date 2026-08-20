// LeetCode 0832 - Flipping an Image
// https://leetcode.com/problems/flipping-an-image/

func flipAndInvertImage(image [][]int) [][]int {
	for _, row := range image {
		for i, j := 0, len(row)-1; i <= j; i, j = i+1, j-1 {
			row[i], row[j] = 1-row[j], 1-row[i]
		}
	}
	return image
}
