// LeetCode 2866 - Beautiful Towers II
// https://leetcode.com/problems/beautiful-towers-ii/

func maximumSumOfHeights(maxHeights []int) int64 {
	n := len(maxHeights)
	left := make([]int64, n)
	st := []int{-1}
	var sum int64
	for i := 0; i < n; i++ {
		for len(st) > 1 && maxHeights[st[len(st)-1]] >= maxHeights[i] {
			j := st[len(st)-1]
			st = st[:len(st)-1]
			sum -= int64(maxHeights[j]) * int64(j-st[len(st)-1])
		}
		sum += int64(maxHeights[i]) * int64(i-st[len(st)-1])
		left[i] = sum
		st = append(st, i)
	}
	right := make([]int64, n)
	st = []int{n}
	sum = 0
	for i := n - 1; i >= 0; i-- {
		for len(st) > 1 && maxHeights[st[len(st)-1]] >= maxHeights[i] {
			j := st[len(st)-1]
			st = st[:len(st)-1]
			sum -= int64(maxHeights[j]) * int64(st[len(st)-1]-j)
		}
		sum += int64(maxHeights[i]) * int64(st[len(st)-1]-i)
		right[i] = sum
		st = append(st, i)
	}
	var ans int64
	for i := 0; i < n; i++ {
		cand := left[i] + right[i] - int64(maxHeights[i])
		if cand > ans {
			ans = cand
		}
	}
	return ans
}
