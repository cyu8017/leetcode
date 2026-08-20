// LeetCode 2158 - Amount of New Area Painted Each Day
// https://leetcode.com/problems/amount-of-new-area-painted-each-day/

func amountPainted(paint [][]int) []int {
	ans := make([]int, len(paint))
	line := make([]int, 50001)
	for i, p := range paint {
		start, end := p[0], p[1]
		j := start
		for j < end {
			if line[j] == 0 {
				ans[i]++
				line[j] = end
				j++
			} else {
				next := line[j]
				line[j] = end
				if next > end {
					line[j] = next
				}
				j = next
			}
		}
	}
	return ans
}
