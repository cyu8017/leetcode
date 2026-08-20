// LeetCode 2568 - Minimum Impossible OR
// https://leetcode.com/problems/minimum-impossible-or/


func minImpossibleOR(nums []int) int {
	set := map[int]bool{}
	for _, x := range nums {
		set[x] = true
	}
	for i := 1; ; i <<= 1 {
		if !set[i] {
			return i
		}
	}
}
