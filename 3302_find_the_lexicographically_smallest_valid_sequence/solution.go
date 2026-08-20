// LeetCode 3302 - Find the Lexicographically Smallest Valid Sequence
// https://leetcode.com/problems/find-the-lexicographically-smallest-valid-sequence/

func validSequence(word1 string, word2 string) []int {
	n, m := len(word1), len(word2)
	// next match from right for suffix of word2
	right := make([]int, m+1)
	right[m] = n
	j := m - 1
	for i := n - 1; i >= 0 && j >= 0; i-- {
		if word1[i] == word2[j] {
			right[j] = i
			j--
		}
	}
	for ; j >= 0; j-- {
		right[j] = -1
	}
	ans := make([]int, m)
	usedSkip := false
	i := 0
	for j := 0; j < m; j++ {
		found := false
		for i < n {
			if word1[i] == word2[j] {
				// check rest can match with remaining skip
				if canFinish(word1, word2, i+1, j+1, usedSkip, right) {
					ans[j] = i
					i++
					found = true
					break
				}
			} else if !usedSkip {
				if canFinish(word1, word2, i+1, j+1, true, right) {
					ans[j] = i
					i++
					usedSkip = true
					found = true
					break
				}
			}
			i++
		}
		if !found {
			return []int{}
		}
	}
	return ans
}

func canFinish(w1, w2 string, i, j int, usedSkip bool, right []int) bool {
	m := len(w2)
	if j >= m {
		return true
	}
	if !usedSkip {
		// need either exact match suffix starting at i, or skip once
		// simplified: check if right[j] >= i for exact, or try skip
		if right[j] >= i {
			return true
		}
		// with one skip: match w2[j+1:] after some position > i
		if j+1 <= m && right[j+1] > i {
			return true
		}
		// or match w2[j:] after i+1 (skip char at i)
		if right[j] > i {
			return true
		}
		return false
	}
	return right[j] >= i
}
