// LeetCode 3307 - Find the K-th Character in String Game II
// https://leetcode.com/problems/find-the-k-th-character-in-string-game-ii/

func kthCharacter(k int64, operations []int) byte {
	// find which char by reversing operations
	shift := 0
	for len(operations) > 0 {
		op := operations[len(operations)-1]
		operations = operations[:len(operations)-1]
		half := int64(1) << uint(len(operations))
		if k > half {
			k -= half
			if op == 1 {
				shift++
			}
		}
	}
	return byte('a' + shift%26)
}
