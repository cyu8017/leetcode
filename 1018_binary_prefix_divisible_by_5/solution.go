// LeetCode 1018 - Binary Prefix Divisible By 5
// https://leetcode.com/problems/binary-prefix-divisible-by-5/

func prefixesDivBy5(nums []int) []bool {
	ans := make([]bool, len(nums))
	rem := 0
	for i, bit := range nums {
		rem = (rem*2 + bit) % 5
		ans[i] = rem == 0
	}
	return ans
}
