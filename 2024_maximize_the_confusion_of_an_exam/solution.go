// LeetCode 2024 - Maximize the Confusion of an Exam
// https://leetcode.com/problems/maximize-the-confusion-of-an-exam/

func maxConsecutiveAnswers(answerKey string, k int) int {
	maxWith := func(ch byte) int {
		left, bad, best := 0, 0, 0
		for right := 0; right < len(answerKey); right++ {
			if answerKey[right] != ch {
				bad++
			}
			for bad > k {
				if answerKey[left] != ch {
					bad--
				}
				left++
			}
			if right-left+1 > best {
				best = right - left + 1
			}
		}
		return best
	}
	a, b := maxWith('T'), maxWith('F')
	if a > b {
		return a
	}
	return b
}
