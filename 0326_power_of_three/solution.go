// LeetCode 0326 - Power of Three
// https://leetcode.com/problems/power-of-three/

func isPowerOfThree(n int) bool {
	if n <= 0 {
		return false
	}
	for n%3 == 0 {
		n /= 3
	}
	return n == 1
}
