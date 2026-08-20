// LeetCode 2094 - Finding 3-Digit Even Numbers
// https://leetcode.com/problems/finding-3-digit-even-numbers/

func findEvenNumbers(digits []int) []int {
	freq := [10]int{}
	for _, d := range digits {
		freq[d]++
	}
	ans := []int{}
	for x := 100; x <= 998; x += 2 {
		a, b, c := x/100, (x/10)%10, x%10
		freq[a]--
		freq[b]--
		freq[c]--
		if freq[a] >= 0 && freq[b] >= 0 && freq[c] >= 0 {
			ans = append(ans, x)
		}
		freq[a]++
		freq[b]++
		freq[c]++
	}
	return ans
}
