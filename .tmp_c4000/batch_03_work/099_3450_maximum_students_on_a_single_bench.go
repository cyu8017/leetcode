// LeetCode 3450 - Maximum Students on a Single Bench
// https://leetcode.com/problems/maximum-students-on-a-single-bench/

func maxStudentsOnBench(students [][]int) int {
	bench := map[int]map[int]bool{}
	for _, s := range students {
		sid, b := s[0], s[1]
		if bench[b] == nil {
			bench[b] = map[int]bool{}
		}
		bench[b][sid] = true
	}
	ans := 0
	for _, set := range bench {
		if len(set) > ans {
			ans = len(set)
		}
	}
	return ans
}
