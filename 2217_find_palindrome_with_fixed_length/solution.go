// LeetCode 2217 - Find Palindrome With Fixed Length
// https://leetcode.com/problems/find-palindrome-with-fixed-length/

func kthPalindrome(queries []int, intLength int) []int64 {
	half := (intLength + 1) / 2
	start := 1
	for i := 1; i < half; i++ {
		start *= 10
	}
	total := start * 9
	ans := make([]int64, len(queries))
	for i, q := range queries {
		if q > total {
			ans[i] = -1
			continue
		}
		left := start + q - 1
		pal := int64(left)
		x := left
		if intLength%2 == 1 {
			x /= 10
		}
		for x > 0 {
			pal = pal*10 + int64(x%10)
			x /= 10
		}
		ans[i] = pal
	}
	return ans
}
