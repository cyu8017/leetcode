// LeetCode 2950 - Number of Divisible Substrings
// https://leetcode.com/problems/number-of-divisible-substrings/

func countDivisibleSubstrings(word string) int {
	mapping := [26]int{}
	vals := []int{1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9}
	for i := 0; i < 26; i++ {
		mapping[i] = vals[i]
	}
	ans := 0
	n := len(word)
	for i := 0; i < n; i++ {
		sum := 0
		for j := i; j < n; j++ {
			sum += mapping[word[j]-'a']
			if sum%(j-i+1) == 0 {
				ans++
			}
		}
	}
	return ans
}
