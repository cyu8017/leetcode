// LeetCode 0835 - Image Overlap
// https://leetcode.com/problems/image-overlap/

func largestOverlap(img1 [][]int, img2 [][]int) int {
	n := len(img1)
	ones1, ones2 := [][2]int{}, [][2]int{}
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			if img1[i][j] == 1 {
				ones1 = append(ones1, [2]int{i, j})
			}
			if img2[i][j] == 1 {
				ones2 = append(ones2, [2]int{i, j})
			}
		}
	}
	if len(ones1) == 0 || len(ones2) == 0 {
		return 0
	}
	shifts := map[[2]int]int{}
	best := 0
	for _, a := range ones1 {
		for _, b := range ones2 {
			key := [2]int{a[0] - b[0], a[1] - b[1]}
			shifts[key]++
			if shifts[key] > best {
				best = shifts[key]
			}
		}
	}
	return best
}
