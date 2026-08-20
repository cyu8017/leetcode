// LeetCode 2951 - Find the Peaks
// https://leetcode.com/problems/find-the-peaks/

func findPeaks(mountain []int) []int {
	ans := []int{}
	for i := 1; i+1 < len(mountain); i++ {
		if mountain[i] > mountain[i-1] && mountain[i] > mountain[i+1] {
			ans = append(ans, i)
		}
	}
	return ans
}
