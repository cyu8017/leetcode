// LeetCode 3272 - Find the Count of Good Integers
// https://leetcode.com/problems/find-the-count-of-good-integers/

import "sort"

func countGoodIntegers(n int, k int) int64 {
	half := (n + 1) / 2
	start := 1
	for i := 1; i < half; i++ {
		start *= 10
	}
	end := start * 10
	seen := map[string]bool{}
	var ans int64
	fact := make([]int64, n+1)
	fact[0] = 1
	for i := 1; i <= n; i++ {
		fact[i] = fact[i-1] * int64(i)
	}
	for h := start; h < end; h++ {
		s := itoa3272(h)
		pal := s
		revStart := len(s) - 1
		if n%2 == 1 {
			revStart--
		}
		for i := revStart; i >= 0; i-- {
			pal += string(s[i])
		}
		if atoi3272(pal)%k != 0 {
			continue
		}
		chars := []byte(pal)
		sort.Slice(chars, func(i, j int) bool { return chars[i] < chars[j] })
		key := string(chars)
		if seen[key] {
			continue
		}
		seen[key] = true
		cnt := [10]int{}
		for _, c := range chars {
			cnt[c-'0']++
		}
		// permutations without leading zero
		total := fact[n]
		for _, c := range cnt {
			total /= fact[c]
		}
		if cnt[0] > 0 {
			bad := fact[n-1]
			cnt[0]--
			for _, c := range cnt {
				bad /= fact[c]
			}
			cnt[0]++
			total -= bad
		}
		ans += total
	}
	return ans
}

func itoa3272(x int) string {
	if x == 0 {
		return "0"
	}
	var b []byte
	for x > 0 {
		b = append([]byte{byte('0' + x%10)}, b...)
		x /= 10
	}
	return string(b)
}
func atoi3272(s string) int {
	v := 0
	for _, c := range s {
		v = v*10 + int(c-'0')
	}
	return v
}
