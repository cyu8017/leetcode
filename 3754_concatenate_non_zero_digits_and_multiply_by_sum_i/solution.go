// LeetCode 3754 - Concatenate Non Zero Digits And Multiply By Sum I
// https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-i/

func sumAndMultiply(n int) int64 {
	p := 1
	x := 0
	s := 0
	for n > 0 {
		v := n % 10
		if v != 0 {
			s += v
			x += p * v
			p *= 10
		}
		n /= 10
	}
	return int64(x) * int64(s)
}
