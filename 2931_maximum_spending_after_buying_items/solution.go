// LeetCode 2931 - Maximum Spending After Buying Items
// https://leetcode.com/problems/maximum-spending-after-buying-items/

func maxSpending(values [][]int) int64 {
	m := len(values)
	n := len(values[0])
	idx := make([]int, m)
	for i := range idx {
		idx[i] = n - 1
	}
	var ans int64
	day := int64(1)
	total := m * n
	for t := 0; t < total; t++ {
		bestI := -1
		bestV := 1 << 60
		for i := 0; i < m; i++ {
			if idx[i] >= 0 && values[i][idx[i]] < bestV {
				bestV = values[i][idx[i]]
				bestI = i
			}
		}
		ans += int64(bestV) * day
		idx[bestI]--
		day++
	}
	return ans
}
