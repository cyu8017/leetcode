// LeetCode 2980 - Check if Bitwise OR Has Trailing Zeros
// https://leetcode.com/problems/check-if-bitwise-or-has-trailing-zeros/

func hasTrailingZeros(nums []int) bool {
	even := 0
	for _, v := range nums {
		if v%2 == 0 {
			even++
			if even >= 2 {
				return true
			}
		}
	}
	return false
}
