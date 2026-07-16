// LeetCode 0393 - UTF-8 Validation
// https://leetcode.com/problems/utf-8-validation/

func validUtf8(data []int) bool {
	remaining := 0

	for _, value := range data {
		byte := value & 0xFF
		if remaining == 0 {
			switch {
			case byte>>7 == 0b0:
				continue
			case byte>>5 == 0b110:
				remaining = 1
			case byte>>4 == 0b1110:
				remaining = 2
			case byte>>3 == 0b11110:
				remaining = 3
			default:
				return false
			}
		} else {
			if byte>>6 != 0b10 {
				return false
			}
			remaining--
		}
	}

	return remaining == 0
}
