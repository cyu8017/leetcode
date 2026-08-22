// LeetCode 3480 - Maximize Subarrays After Removing One Conflicting Pair
// https://leetcode.com/problems/maximize-subarrays-after-removing-one-conflicting-pair/

func maxSubarrays(n int, conflictingPairs [][]int) int64 {
	m := len(conflictingPairs)
	var best int64
	for skip := 0; skip < m; skip++ {
		banned := [][2]int{}
		for i, p := range conflictingPairs {
			if i == skip {
				continue
			}
			a, b := p[0], p[1]
			if a > b {
				a, b = b, a
			}
			banned = append(banned, [2]int{a, b})
		}
		// count valid subarrays: for each r, max l such that no banned inside
		rightLimit := make([]int, n+2)
		for i := range rightLimit {
			rightLimit[i] = n + 1
		}
		for _, b := range banned {
			if b[1] < rightLimit[b[0]] {
				rightLimit[b[0]] = b[1]
			}
		}
		minRight := n + 1
		var cnt int64
		for l := n; l >= 1; l-- {
			if rightLimit[l] < minRight {
				minRight = rightLimit[l]
			}
			cnt += int64(minRight - l)
		}
		if cnt > best {
			best = cnt
		}
	}
	return best
}
