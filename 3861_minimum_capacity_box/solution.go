// LeetCode 3861 - Minimum Capacity Box
// https://leetcode.com/problems/minimum-capacity-box/

func minimumIndex(capacity []int, itemSize int) int {
	ans := -1
	for i, x := range capacity {
		if x >= itemSize && (ans == -1 || x < capacity[ans]) {
			ans = i
		}
	}
	return ans
}
