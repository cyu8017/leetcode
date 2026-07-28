// LeetCode 1044 - Longest Duplicate Substring
// https://leetcode.com/problems/longest-duplicate-substring/

func longestDupSubstring(s string) string {
	const mod = (1 << 61) - 1
	const base = 256
	n := len(s)
	nums := make([]int, n)
	for i := 0; i < n; i++ {
		nums[i] = int(s[i])
	}
	modMul := func(a, b int) int {
		return int((uint64(a) * uint64(b)) % mod)
	}
	search := func(length int) int {
		if length == 0 {
			return 0
		}
		h := 0
		for i := 0; i < length; i++ {
			h = (modMul(h, base) + nums[i]) % mod
		}
		seen := map[int][]int{h: {0}}
		power := 1
		for i := 0; i < length; i++ {
			power = modMul(power, base)
		}
		for i := 1; i+length-1 < n; i++ {
			h = (modMul(h, base) - modMul(nums[i-1], power) + nums[i+length-1]) % mod
			if h < 0 {
				h += mod
			}
			cur := s[i : i+length]
			if idxs, ok := seen[h]; ok {
				for _, j := range idxs {
					if s[j:j+length] == cur {
						return i
					}
				}
				seen[h] = append(seen[h], i)
			} else {
				seen[h] = []int{i}
			}
		}
		return -1
	}
	lo, hi := 0, n-1
	start, bestLen := -1, 0
	for lo <= hi {
		mid := (lo + hi) / 2
		pos := search(mid)
		if pos >= 0 {
			start = pos
			bestLen = mid
			lo = mid + 1
		} else {
			hi = mid - 1
		}
	}
	if start < 0 {
		return ""
	}
	return s[start : start+bestLen]
}
