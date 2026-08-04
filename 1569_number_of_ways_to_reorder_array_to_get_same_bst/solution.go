// LeetCode 1569 - Number of Ways to Reorder Array to Get Same BST
// https://leetcode.com/problems/number-of-ways-to-reorder-array-to-get-same-bst/

func numOfWays(nums []int) int {
	const MOD = 1_000_000_007
	n := len(nums)
	choose := make([][]int, n+1)
	for i := 0; i <= n; i++ {
		choose[i] = make([]int, n+1)
		choose[i][0] = 1
		if i <= n {
			choose[i][i] = 1
		}
		for j := 1; j < i; j++ {
			choose[i][j] = (choose[i-1][j-1] + choose[i-1][j]) % MOD
		}
	}
	var ways func([]int) int
	ways = func(values []int) int {
		if len(values) < 3 {
			return 1
		}
		left, right := []int{}, []int{}
		for _, x := range values[1:] {
			if x < values[0] {
				left = append(left, x)
			} else {
				right = append(right, x)
			}
		}
		return choose[len(values)-1][len(left)] * ways(left) % MOD * ways(right) % MOD
	}
	return (ways(nums) - 1 + MOD) % MOD
}
