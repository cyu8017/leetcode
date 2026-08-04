// LeetCode 1545 - Find Kth Bit in Nth Binary String
// https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

func findKthBit(n int, k int) byte {
	invert := false
	length := (1 << n) - 1
	for k != 1 {
		middle := length/2 + 1
		if k == middle {
			if invert {
				return '0'
			}
			return '1'
		}
		if k > middle {
			k = length - k + 1
			invert = !invert
		}
		length /= 2
	}
	if invert {
		return '1'
	}
	return '0'
}
