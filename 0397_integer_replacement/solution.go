// LeetCode 0397 - Integer Replacement
// https://leetcode.com/problems/integer-replacement/

func integerReplacement(n int) int {
	value := int64(n)
	steps := 0

	for value != 1 {
		if value%2 == 0 {
			value /= 2
		} else if value == 3 || value%4 == 1 {
			value--
		} else {
			value++
		}
		steps++
	}

	return steps
}
