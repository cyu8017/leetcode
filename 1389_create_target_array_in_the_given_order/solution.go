// LeetCode 1389 - Create Target Array in the Given Order
// https://leetcode.com/problems/create-target-array-in-the-given-order/

func createTargetArray(nums []int, index []int) []int {
	out := []int{}
	for i, x := range nums {
		idx := index[i]
		out = append(out, 0)
		copy(out[idx+1:], out[idx:])
		out[idx] = x
	}
	return out
}
