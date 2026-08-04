// LeetCode 1250 - Check If It Is a Good Array
// https://leetcode.com/problems/check-if-it-is-a-good-array/

func isGoodArray(nums []int) bool {
	g := nums[0]
	for i := 1; i < len(nums); i++ {
		g = gcd(g, nums[i])
	}
	return g == 1
}

func gcd(a, b int) int {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}
