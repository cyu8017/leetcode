// LeetCode 2183 - Count Array Pairs Divisible by K
// https://leetcode.com/problems/count-array-pairs-divisible-by-k/

func countPairs(nums []int, k int) int64 {
	gcd := func(a, b int) int {
		for b != 0 {
			a, b = b, a%b
		}
		return a
	}
	freq := map[int]int{}
	var ans int64
	for _, x := range nums {
		g1 := gcd(x, k)
		for g2, c := range freq {
			if g1*g2%k == 0 {
				ans += int64(c)
			}
		}
		freq[g1]++
	}
	return ans
}
