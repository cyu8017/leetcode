// LeetCode 1425 - Constrained Subsequence Sum
// https://leetcode.com/problems/constrained-subsequence-sum/

func constrainedSubsetSum(nums []int, k int) int {
	best := append([]int(nil), nums...)
	queue := []int{}
	for i, value := range nums {
		for len(queue) > 0 && queue[0] < i-k {
			queue = queue[1:]
		}
		if len(queue) > 0 && best[queue[0]] > 0 {
			best[i] = value + best[queue[0]]
		} else {
			best[i] = value
		}
		for len(queue) > 0 && best[queue[len(queue)-1]] <= best[i] {
			queue = queue[:len(queue)-1]
		}
		queue = append(queue, i)
	}
	ans := best[0]
	for _, v := range best {
		if v > ans {
			ans = v
		}
	}
	return ans
}
