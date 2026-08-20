// LeetCode 2180 - Count Integers With Even Digit Sum
// https://leetcode.com/problems/count-integers-with-even-digit-sum/

func countEven(num int) int {
	ans := 0
	for x := 1; x <= num; x++ {
		s, y := 0, x
		for y > 0 {
			s += y % 10
			y /= 10
		}
		if s%2 == 0 {
			ans++
		}
	}
	return ans
}
