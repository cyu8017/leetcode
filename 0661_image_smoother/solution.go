// LeetCode 0661 - Image Smoother
// https://leetcode.com/problems/image-smoother/

func imageSmoother(img [][]int) [][]int {
	m, n := len(img), len(img[0])
	out := make([][]int, m)
	for i := range out {
		out[i] = make([]int, n)
	}
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			total, count := 0, 0
			for di := -1; di <= 1; di++ {
				for dj := -1; dj <= 1; dj++ {
					ni, nj := i+di, j+dj
					if ni >= 0 && ni < m && nj >= 0 && nj < n {
						total += img[ni][nj]
						count++
					}
				}
			}
			out[i][j] = total / count
		}
	}
	return out
}
