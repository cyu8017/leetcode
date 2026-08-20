// LeetCode 0948 - Bag of Tokens
// https://leetcode.com/problems/bag-of-tokens/

import "sort"

func bagOfTokensScore(tokens []int, power int) int {
	sort.Ints(tokens)
	i, j := 0, len(tokens)-1
	score, ans := 0, 0
	for i <= j {
		if power >= tokens[i] {
			power -= tokens[i]
			i++
			score++
			if score > ans {
				ans = score
			}
		} else if score > 0 {
			power += tokens[j]
			j--
			score--
		} else {
			break
		}
	}
	return ans
}
