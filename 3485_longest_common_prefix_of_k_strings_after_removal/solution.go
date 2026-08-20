// LeetCode 3485 - Longest Common Prefix of K Strings After Removal
// https://leetcode.com/problems/longest-common-prefix-of-k-strings-after-removal/

func longestCommonPrefix(words []string, k int) []int {
	n := len(words)
	ans := make([]int, n)
	for i := 0; i < n; i++ {
		// remove words[i], find max LCP among any k of remaining
		rest := []string{}
		for j, w := range words {
			if j != i {
				rest = append(rest, w)
			}
		}
		if len(rest) < k {
			ans[i] = 0
			continue
		}
		best := 0
		// brute combinations too heavy; sort and check windows of k
		sortStrings(rest)
		for j := 0; j+k-1 < len(rest); j++ {
			lcp := lcpOf(rest[j : j+k])
			if lcp > best {
				best = lcp
			}
		}
		ans[i] = best
	}
	return ans
}

func sortStrings(a []string) {
	for i := 0; i < len(a); i++ {
		for j := i + 1; j < len(a); j++ {
			if a[j] < a[i] {
				a[i], a[j] = a[j], a[i]
			}
		}
	}
}

func lcpOf(a []string) int {
	if len(a) == 0 {
		return 0
	}
	pref := a[0]
	for _, s := range a[1:] {
		i := 0
		for i < len(pref) && i < len(s) && pref[i] == s[i] {
			i++
		}
		pref = pref[:i]
		if len(pref) == 0 {
			return 0
		}
	}
	return len(pref)
}
