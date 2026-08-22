// LeetCode 3518 - Smallest Palindromic Rearrangement II
// https://leetcode.com/problems/smallest-palindromic-rearrangement-ii/

func smallestPalindrome(s string, k int) string {
	const MAX = 1_000_000 + 1
	cnt := make([]int, 26)
	for i := 0; i < len(s); i++ {
		cnt[s[i]-'a']++
	}
	odd := 0
	for _, c := range cnt {
		if c%2 == 1 {
			odd++
		}
	}
	if odd > 1 {
		return ""
	}
	half := make([]int, 26)
	mid := byte(0)
	for i := 0; i < 26; i++ {
		half[i] = cnt[i] / 2
		if cnt[i]%2 == 1 {
			mid = byte('a' + i)
		}
	}
	nCk := func(n, kk int) int {
		if kk < 0 || kk > n {
			return 0
		}
		res := 1
		if kk > n-kk {
			kk = n - kk
		}
		for i := 1; i <= kk; i++ {
			res = res * (n - i + 1) / i
			if res >= MAX {
				return MAX
			}
		}
		return res
	}
	countArr := func(h []int) int {
		total := 0
		for _, f := range h {
			total += f
		}
		res := 1
		for _, f := range h {
			res *= nCk(total, f)
			if res >= MAX {
				return MAX
			}
			total -= f
		}
		return res
	}
	if countArr(half) < k {
		return ""
	}
	halfLen := 0
	for _, f := range half {
		halfLen += f
	}
	left := make([]byte, 0, halfLen)
	for t := 0; t < halfLen; t++ {
		for i := 0; i < 26; i++ {
			if half[i] == 0 {
				continue
			}
			half[i]--
			arr := countArr(half)
			if arr >= k {
				left = append(left, byte('a'+i))
				break
			}
			k -= arr
			half[i]++
		}
	}
	res := string(left)
	if mid != 0 {
		res += string(mid)
	}
	for i := len(left) - 1; i >= 0; i-- {
		res += string(left[i])
	}
	return res
}
