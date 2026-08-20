// LeetCode 3542 - Minimum Operations to Convert All Elements to Zero
// https://leetcode.com/problems/minimum-operations-to-convert-all-elements-to-zero/

func minOperations(nums []int) int {
	stk := []int{}
	ans := 0
	for _, x := range nums {
		for len(stk) > 0 && stk[len(stk)-1] > x {
			ans++
			stk = stk[:len(stk)-1]
		}
		if x != 0 && (len(stk) == 0 || stk[len(stk)-1] != x) {
			stk = append(stk, x)
		}
	}
	ans += len(stk)
	return ans
}
