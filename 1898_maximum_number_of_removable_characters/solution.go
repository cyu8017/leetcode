// LeetCode 1898 - Maximum Number of Removable Characters
// https://leetcode.com/problems/maximum-number-of-removable-characters/

func maximumRemovals(s string, p string, removable []int) int {
	stillSubsequence := func(k int) bool {
		removed := make(map[int]bool, k)
		for i := 0; i < k; i++ {
			removed[removable[i]] = true
		}
		index := 0
		for position := 0; position < len(s); position++ {
			if removed[position] {
				continue
			}
			if index < len(p) && s[position] == p[index] {
				index++
			}
		}
		return index == len(p)
	}

	lo, hi := 0, len(removable)
	for lo < hi {
		mid := (lo + hi + 1) / 2
		if stillSubsequence(mid) {
			lo = mid
		} else {
			hi = mid - 1
		}
	}
	return lo
}
