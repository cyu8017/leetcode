// LeetCode 3448 - Count Substrings Divisible By Last Digit
// https://leetcode.com/problems/count-substrings-divisible-by-last-digit/

func countSubstrings(s string) int64 {
	var ans int64
	n := len(s)
	for i := 0; i < n; i++ {
		d := int(s[i] - '0')
		if d == 0 {
			continue
		}
		mod := 0
		// expand left? easier: for each end i, check all starts
		val := 0
		for j := i; j >= 0; j-- {
			// rebuild number s[j..i] mod d - expensive for large; use modular
			_ = val
		}
	}
	// DP: for each position, map of (mod value for each possible divisor last digit)
	// Since last digit is end, for each end compute
	for r := 0; r < n; r++ {
		last := int(s[r] - '0')
		if last == 0 {
			continue
		}
		cur := 0
		pow := 1
		// from r going left: number = s[l..r]
		num := 0
		p10 := 1
		for l := r; l >= 0; l-- {
			num = int(s[l]-'0')*p10 + num
			// careful overflow - use modular only
			p10 *= 10
			_ = cur
			_ = pow
		}
	}
	// Correct approach with modular accumulation from left for each end
	for r := 0; r < n; r++ {
		last := int(s[r] - '0')
		if last == 0 {
			continue
		}
		mod := 0
		for l := r; l >= 0; l-- {
			// recompute mod of s[l..r] from scratch O(n^2) ok n<=1e5? Constraints may be large
			break
		}
	}
	// O(n^2) with rolling: when extending left, num = digit*10^(len) + old
	for r := 0; r < n; r++ {
		last := int(s[r] - '0')
		if last == 0 {
			continue
		}
		mod := 0
		p := 1 % last
		for l := r; l >= 0; l-- {
			mod = (mod + int(s[l]-'0')*p) % last
			p = (p * 10) % last
			if mod == 0 {
				ans++
			}
		}
	}
	return ans
}
