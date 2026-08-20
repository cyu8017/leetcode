// LeetCode 2748 - Number of Beautiful Pairs
// https://leetcode.com/problems/number-of-beautiful-pairs/


func countBeautifulPairs(nums []int) int {
	gcd := func(a, b int) int {
		for b != 0 {
			a, b = b, a%b
		}
		return a
	}
	firstDigit := func(x int) int {
		for x >= 10 {
			x /= 10
		}
		return x
	}
	ans := 0
	freq := [10]int{}
	for _, x := range nums {
		last := x % 10
		for d := 1; d <= 9; d++ {
			if freq[d] > 0 && gcd(d, last) == 1 {
				ans += freq[d]
			}
		}
		freq[firstDigit(x)]++
	}
	return ans
}
