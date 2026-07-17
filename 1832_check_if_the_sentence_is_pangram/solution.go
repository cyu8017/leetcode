// LeetCode 1832 - Check if the Sentence Is Pangram
// https://leetcode.com/problems/check-if-the-sentence-is-pangram/

func checkIfPangram(sentence string) bool {
	mask := 0
	for i := 0; i < len(sentence); i++ {
		mask |= 1 << (sentence[i] - 'a')
	}
	return mask == (1<<26)-1
}
