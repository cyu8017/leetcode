// LeetCode 2201 - Count Artifacts That Can Be Extracted
// https://leetcode.com/problems/count-artifacts-that-can-be-extracted/

func digArtifacts(n int, artifacts [][]int, dig [][]int) int {
	dug := map[[2]int]bool{}
	for _, d := range dig {
		dug[[2]int{d[0], d[1]}] = true
	}
	ans := 0
	for _, a := range artifacts {
		ok := true
		for r := a[0]; r <= a[2]; r++ {
			for c := a[1]; c <= a[3]; c++ {
				if !dug[[2]int{r, c}] {
					ok = false
				}
			}
		}
		if ok {
			ans++
		}
	}
	return ans
}
