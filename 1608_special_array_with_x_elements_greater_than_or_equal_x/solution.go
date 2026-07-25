// LeetCode 1608 - Special Array With X Elements Greater Than or Equal X
// https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/

func specialArray(nums []int) int {
	for x := 0; x <= len(nums); x++ {
		cnt := 0
		for _, v := range nums {
			if v >= x {
				cnt++
			}
		}
		if cnt == x {
			return x
		}
	}
	return -1
}
