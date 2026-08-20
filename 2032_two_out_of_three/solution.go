// LeetCode 2032 - Two Out of Three
// https://leetcode.com/problems/two-out-of-three/

func twoOutOfThree(nums1 []int, nums2 []int, nums3 []int) []int {
	seen := [3]map[int]bool{{}, {}, {}}
	for _, x := range nums1 {
		seen[0][x] = true
	}
	for _, x := range nums2 {
		seen[1][x] = true
	}
	for _, x := range nums3 {
		seen[2][x] = true
	}
	ans := []int{}
	for v := 1; v <= 100; v++ {
		c := 0
		for i := 0; i < 3; i++ {
			if seen[i][v] {
				c++
			}
		}
		if c >= 2 {
			ans = append(ans, v)
		}
	}
	return ans
}
