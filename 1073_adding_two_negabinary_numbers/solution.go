// LeetCode 1073 - Adding Two Negabinary Numbers
// https://leetcode.com/problems/adding-two-negabinary-numbers/

func addNegabinary(arr1 []int, arr2 []int) []int {
	i, j := len(arr1)-1, len(arr2)-1
	carry := 0
	ans := []int{}
	for i >= 0 || j >= 0 || carry != 0 {
		total := carry
		if i >= 0 {
			total += arr1[i]
			i--
		}
		if j >= 0 {
			total += arr2[j]
			j--
		}
		ans = append(ans, total&1)
		carry = -(total >> 1)
	}
	for len(ans) > 1 && ans[len(ans)-1] == 0 {
		ans = ans[:len(ans)-1]
	}
	for l, r := 0, len(ans)-1; l < r; l, r = l+1, r-1 {
		ans[l], ans[r] = ans[r], ans[l]
	}
	return ans
}
