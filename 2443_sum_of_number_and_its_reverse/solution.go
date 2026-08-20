// LeetCode 2443 - Sum of Number and Its Reverse
// https://leetcode.com/problems/sum-of-number-and-its-reverse/

func sumOfNumberAndReverse(num int) bool {
	rev := func(x int) int {
		r := 0
		for x > 0 {
			r = r*10 + x%10
			x /= 10
		}
		return r
	}
	for i := 0; i <= num; i++ {
		if i+rev(i) == num {
			return true
		}
	}
	return false
}
