// LeetCode 1805 - Number of Different Integers in a String
// https://leetcode.com/problems/number-of-different-integers-in-a-string/

func numDifferentIntegers(word string) int {
	seen := make(map[int]struct{})
	i := 0
	for i < len(word) {
		if word[i] < '0' || word[i] > '9' {
			i++
			continue
		}
		j := i
		for j < len(word) && word[j] >= '0' && word[j] <= '9' {
			j++
		}
		value := 0
		k := i
		for k < j && word[k] == '0' {
			k++
		}
		if k < j {
			for k < j {
				value = value*10 + int(word[k]-'0')
				k++
			}
		}
		seen[value] = struct{}{}
		i = j
	}
	return len(seen)
}
