// LeetCode 2148 - Count Elements With Strictly Smaller and Greater Elements
// https://leetcode.com/problems/count-elements-with-strictly-smaller-and-greater-elements/

func countElements(nums []int) int {
	mn, mx := nums[0], nums[0]
	for _, x := range nums {
		if x < mn {
			mn = x
		}
		if x > mx {
			mx = x
		}
	}
	ans := 0
	for _, x := range nums {
		if x > mn && x < mx {
			ans++
		}
	}
	return ans
}
