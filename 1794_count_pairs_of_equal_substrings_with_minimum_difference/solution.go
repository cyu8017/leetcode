// LeetCode 1794 - Count Pairs of Equal Substrings With Minimum Difference
// https://leetcode.com/problems/count-pairs-of-equal-substrings-with-minimum-difference/

func countQuadruples(firstString string, secondString string) int {
	var first, lastF, lastS [26]int
	for c := 0; c < 26; c++ {
		first[c] = -1
		lastF[c] = -1
		lastS[c] = -1
	}
	for i := 0; i < len(firstString); i++ {
		c := firstString[i] - 'a'
		if first[c] == -1 {
			first[c] = i
		}
		lastF[c] = i
	}
	for i := 0; i < len(secondString); i++ {
		lastS[secondString[i]-'a'] = i
	}
	const maxInt = int(^uint(0) >> 1)
	best := maxInt
	for c := 0; c < 26; c++ {
		if first[c] != -1 && lastS[c] != -1 && lastF[c]-lastS[c] < best {
			best = lastF[c] - lastS[c]
		}
	}
	if best == maxInt {
		return 0
	}
	ans := 0
	for c := 0; c < 26; c++ {
		if first[c] == -1 || lastS[c] == -1 || lastF[c]-lastS[c] != best {
			continue
		}
		iCount := 0
		for k := first[c]; k <= lastF[c]; k++ {
			if int(firstString[k]-'a') == c {
				iCount++
			}
		}
		aCount := 0
		for k := 0; k <= lastS[c]; k++ {
			if int(secondString[k]-'a') == c {
				aCount++
			}
		}
		ans += iCount * aCount
	}
	return ans
}
