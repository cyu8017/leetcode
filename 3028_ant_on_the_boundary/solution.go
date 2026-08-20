// LeetCode 3028 - Ant on the Boundary
// https://leetcode.com/problems/ant-on-the-boundary/

func returnToBoundaryCount(nums []int) (ans int) {
	s := 0
	for _, x := range nums {
		s += x
		if s == 0 {
			ans++
		}
	}
	return
}
