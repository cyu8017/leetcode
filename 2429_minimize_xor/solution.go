// LeetCode 2429 - Minimize XOR
// https://leetcode.com/problems/minimize-xor/

func minimizeXor(num1 int, num2 int) int {
	bits := 0
	for x := num2; x > 0; x >>= 1 {
		bits += x & 1
	}
	ans := 0
	for i := 31; i >= 0 && bits > 0; i-- {
		if (num1>>i)&1 == 1 {
			ans |= 1 << i
			bits--
		}
	}
	for i := 0; i < 32 && bits > 0; i++ {
		if (ans>>i)&1 == 0 {
			ans |= 1 << i
			bits--
		}
	}
	return ans
}
