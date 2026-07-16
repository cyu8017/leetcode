// LeetCode 0389 - Find the Difference
// https://leetcode.com/problems/find-the-difference/

func findTheDifference(s string, t string) byte {
	xorValue := 0

	for _, ch := range s {
		xorValue ^= int(ch)
	}
	for _, ch := range t {
		xorValue ^= int(ch)
	}

	return byte(xorValue)
}
