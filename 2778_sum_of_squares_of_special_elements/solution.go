// LeetCode 2778 - Sum of Squares of Special Elements
// https://leetcode.com/problems/sum-of-squares-of-special-elements/

func sumOfSquares(nums []int) int {
	n := len(nums)
	ans := 0
	for i, v := range nums {
		if n%(i+1) == 0 {
			ans += v * v
		}
	}
	return ans
}
