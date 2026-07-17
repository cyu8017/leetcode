// LeetCode 1864 - Minimum Number of Swaps to Make the Binary String Alternating
// https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-binary-string-alternating/

func minSwaps(s string) int {
	zeros := 0
	for i := 0; i < len(s); i++ {
		if s[i] == '0' {
			zeros++
		}
	}
	ones := len(s) - zeros
	if abs(zeros-ones) > 1 {
		return -1
	}

	mismatches := func(pattern byte) int {
		mismatch := 0
		for i := 0; i < len(s); i++ {
			if s[i] != pattern {
				mismatch++
			}
			if pattern == '0' {
				pattern = '1'
			} else {
				pattern = '0'
			}
		}
		return mismatch / 2
	}

	if zeros == ones {
		left := mismatches('0')
		right := mismatches('1')
		if left < right {
			return left
		}
		return right
	}
	if zeros > ones {
		return mismatches('0')
	}
	return mismatches('1')
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}
