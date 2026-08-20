// LeetCode 2808 - Minimum Seconds to Equalize a Circular Array
// https://leetcode.com/problems/minimum-seconds-to-equalize-a-circular-array/

func minimumSeconds(nums []int) int {
	n := len(nums)
	pos := map[int][]int{}
	for i, v := range nums {
		pos[v] = append(pos[v], i)
	}
	ans := n
	for _, p := range pos {
		maxGap := 0
		for i := 0; i < len(p); i++ {
			gap := 0
			if i+1 < len(p) {
				gap = p[i+1] - p[i]
			} else {
				gap = p[0] + n - p[i]
			}
			if gap/2 > maxGap {
				maxGap = gap / 2
			}
		}
		if maxGap < ans {
			ans = maxGap
		}
	}
	return ans
}
