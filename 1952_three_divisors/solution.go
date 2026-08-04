// LeetCode 1952 - Three Divisors
// https://leetcode.com/problems/three-divisors/

func isThree(n int) bool {
	root := 0
	for root*root < n {
		root++
	}
	if root*root != n || root < 2 {
		return false
	}
	for i := 2; i*i <= root; i++ {
		if root%i == 0 {
			return false
		}
	}
	return true
}
