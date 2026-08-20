// LeetCode 2520 - Count the Digits That Divide a Number
// https://leetcode.com/problems/count-the-digits-that-divide-a-number/

func countDigits(num int) int {
	ans, x := 0, num
	for x > 0 {
		d := x % 10
		if d != 0 && num%d == 0 {
			ans++
		}
		x /= 10
	}
	return ans
}
