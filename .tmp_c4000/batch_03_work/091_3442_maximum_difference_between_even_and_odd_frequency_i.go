// LeetCode 3442 - Maximum Difference Between Even and Odd Frequency I
// https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-i/

func maxDifference(s string) int {
	freq := [26]int{}
	for _, c := range s {
		freq[c-'a']++
	}
	maxOdd, minEven := 0, int(1e9)
	for _, f := range freq {
		if f == 0 {
			continue
		}
		if f%2 == 1 {
			if f > maxOdd {
				maxOdd = f
			}
		} else if f < minEven {
			minEven = f
		}
	}
	return maxOdd - minEven
}
