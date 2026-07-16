// LeetCode 0443 - String Compression
// https://leetcode.com/problems/string-compression/

import "strconv"

func compress(chars []byte) int {
	write := 0
	read := 0
	for read < len(chars) {
		ch := chars[read]
		count := 0
		for read < len(chars) && chars[read] == ch {
			read++
			count++
		}
		chars[write] = ch
		write++
		if count > 1 {
			for _, digit := range strconv.Itoa(count) {
				chars[write] = byte(digit)
				write++
			}
		}
	}
	return write
}
