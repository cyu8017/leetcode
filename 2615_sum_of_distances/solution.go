// LeetCode 2615 - Sum of Distances
// https://leetcode.com/problems/sum-of-distances/


func distance(nums []int) []int64 {
	n := len(nums)
	ans := make([]int64, n)
	pos := map[int][]int{}
	for i, x := range nums {
		pos[x] = append(pos[x], i)
	}
	for _, idxs := range pos {
		m := len(idxs)
		pref := make([]int64, m+1)
		for i, idx := range idxs {
			pref[i+1] = pref[i] + int64(idx)
		}
		for j, idx := range idxs {
			left := int64(j)*int64(idx) - pref[j]
			right := pref[m] - pref[j+1] - int64(m-1-j)*int64(idx)
			ans[idx] = left + right
		}
	}
	return ans
}
