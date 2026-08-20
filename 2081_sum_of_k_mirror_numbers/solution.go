// LeetCode 2081 - Sum of k-Mirror Numbers
// https://leetcode.com/problems/sum-of-k-mirror-numbers/

func kMirror(k int, n int) int64 {
	isPalBase := func(x int64, base int) bool {
		digits := []int{}
		for x > 0 {
			digits = append(digits, int(x%int64(base)))
			x /= int64(base)
		}
		for l, r := 0, len(digits)-1; l < r; l, r = l+1, r-1 {
			if digits[l] != digits[r] {
				return false
			}
		}
		return true
	}
	var ans int64
	count := 0
	// generate decimal palindromes in order
	for length := 1; count < n; length++ {
		start := 1
		for i := 1; i < (length+1)/2; i++ {
			start *= 10
		}
		end := start * 10
		for half := start; half < end && count < n; half++ {
			// build palindrome
			var pal int64
			if length%2 == 0 {
				pal = int64(half)
				x := half
				for x > 0 {
					pal = pal*10 + int64(x%10)
					x /= 10
				}
			} else {
				pal = int64(half)
				x := half / 10
				for x > 0 {
					pal = pal*10 + int64(x%10)
					x /= 10
				}
			}
			if isPalBase(pal, k) {
				ans += pal
				count++
			}
		}
	}
	return ans
}
