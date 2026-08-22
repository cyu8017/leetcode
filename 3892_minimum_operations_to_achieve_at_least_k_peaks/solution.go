// LeetCode 3892 - Minimum Operations to Achieve At Least K Peaks
// https://leetcode.com/problems/minimum-operations-to-achieve-at-least-k-peaks/

func minOperations(nums []int, k int) int64 {
	n := len(nums)
	if k == 0 {
		return 0
	}
	if k > n/2 {
		return -1
	}
	cost := make([]int64, n)
	for i, value := range nums {
		left, right := nums[(i+n-1)%n], nums[(i+1)%n]
		need := left
		if right > need {
			need = right
		}
		if need >= value {
			cost[i] = int64(need - value + 1)
		}
	}
	const inf int64 = 1 << 60
	line := func(left, right, choose int) int64 {
		if choose == 0 {
			return 0
		}
		if left > right || choose > (right-left+2)/2 {
			return inf
		}
		prev2 := make([]int64, choose+1)
		prev1 := make([]int64, choose+1)
		for j := 1; j <= choose; j++ {
			prev2[j], prev1[j] = inf, inf
		}
		for i := left; i <= right; i++ {
			current := append([]int64(nil), prev1...)
			for j := 1; j <= choose; j++ {
				if prev2[j-1] != inf && prev2[j-1]+cost[i] < current[j] {
					current[j] = prev2[j-1] + cost[i]
				}
			}
			prev2, prev1 = prev1, current
		}
		return prev1[choose]
	}
	answer := line(1, n-1, k)
	withFirst := line(2, n-2, k-1)
	if withFirst != inf {
		withFirst += cost[0]
		if withFirst < answer {
			answer = withFirst
		}
	}
	if answer == inf {
		return -1
	}
	return answer
}