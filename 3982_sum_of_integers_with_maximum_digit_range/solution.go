// LeetCode 3982 - Sum Of Integers With Maximum Digit Range
// https://leetcode.com/problems/sum-of-integers-with-maximum-digit-range/

func maxDigitRange(nums []int) (ans int) {
	mx := 0
	for _, x := range nums {
		a, b := 10, 0
		for y := x; y > 0; y /= 10 {
			v := y % 10
			a = min(a, v)
			b = max(b, v)
		}
		r := b - a
		if mx < r {
			mx = r
			ans = x
		} else if mx == r {
			ans += x
		}
	}
	return
}
