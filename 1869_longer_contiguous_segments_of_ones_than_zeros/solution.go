// LeetCode 1869 - Longer Contiguous Segments of Ones than Zeros
// https://leetcode.com/problems/longer-contiguous-segments-of-ones-than-zeros/

func checkZeroOnes(s string) bool {
	maxZeros, maxOnes := 0, 0
	zeros, ones := 0, 0

	for i := 0; i < len(s); i++ {
		if s[i] == '0' {
			zeros++
			ones = 0
			if zeros > maxZeros {
				maxZeros = zeros
			}
		} else {
			ones++
			zeros = 0
			if ones > maxOnes {
				maxOnes = ones
			}
		}
	}

	return maxOnes > maxZeros
}
