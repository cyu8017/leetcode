// LeetCode 2106 - Maximum Fruits Harvested After at Most K Steps
// https://leetcode.com/problems/maximum-fruits-harvested-after-at-most-k-steps/

func maxTotalFruits(fruits [][]int, startPos int, k int) int {
	n := len(fruits)
	pref := make([]int, n+1)
	pos := make([]int, n)
	for i, f := range fruits {
		pos[i] = f[0]
		pref[i+1] = pref[i] + f[1]
	}
	ans := 0
	// left then right, and right then left
	j := 0
	for i := 0; i < n; i++ {
		for j < n && minSteps2106(pos[i], pos[j], startPos) > k {
			j++
		}
		if j <= i {
			sum := pref[i+1] - pref[j]
			if sum > ans {
				ans = sum
			}
		}
	}
	j = 0
	for i := 0; i < n; i++ {
		for j <= i && minSteps2106(pos[j], pos[i], startPos) > k {
			j++
		}
		sum := pref[i+1] - pref[j]
		if sum > ans {
			ans = sum
		}
	}
	return ans
}

func minSteps2106(left, right, start int) int {
	// cover [left,right] starting at start
	if right <= start {
		return start - left
	}
	if left >= start {
		return right - start
	}
	a := (start - left) + (right - left)
	b := (right - start) + (right - left)
	if a < b {
		return a
	}
	return b
}
