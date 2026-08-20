// LeetCode 2121 - Intervals Between Identical Elements
// https://leetcode.com/problems/intervals-between-identical-elements/

func getDistances(arr []int) []int64 {
	n := len(arr)
	pos := map[int][]int{}
	for i, v := range arr {
		pos[v] = append(pos[v], i)
	}
	ans := make([]int64, n)
	for _, idxs := range pos {
		m := len(idxs)
		pref := make([]int64, m+1)
		for i, idx := range idxs {
			pref[i+1] = pref[i] + int64(idx)
		}
		for i, idx := range idxs {
			left := int64(i)*int64(idx) - pref[i]
			right := (pref[m] - pref[i+1]) - int64(m-i-1)*int64(idx)
			ans[idx] = left + right
		}
	}
	return ans
}
