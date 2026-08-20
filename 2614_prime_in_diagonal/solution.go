// LeetCode 2614 - Prime In Diagonal
// https://leetcode.com/problems/prime-in-diagonal/


func diagonalPrime(nums [][]int) int {
	isPrime := func(x int) bool {
		if x < 2 {
			return false
		}
		for i := 2; i*i <= x; i++ {
			if x%i == 0 {
				return false
			}
		}
		return true
	}
	n := len(nums)
	best := 0
	for i := 0; i < n; i++ {
		for _, v := range []int{nums[i][i], nums[i][n-1-i]} {
			if isPrime(v) && v > best {
				best = v
			}
		}
	}
	return best
}
