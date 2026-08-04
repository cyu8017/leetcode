// LeetCode 1460 - Make Two Arrays Equal by Reversing Subarrays
// https://leetcode.com/problems/make-two-arrays-equal-by-reversing-subarrays/

func canBeEqual(target []int, arr []int) bool {
	count := map[int]int{}
	for _, v := range target {
		count[v]++
	}
	for _, v := range arr {
		count[v]--
		if count[v] < 0 {
			return false
		}
	}
	return true
}
