// LeetCode 2398 - Maximum Number of Robots Within Budget
// https://leetcode.com/problems/maximum-number-of-robots-within-budget/

func maximumRobots(chargeTimes []int, runningCosts []int, budget int64) int {
	n := len(chargeTimes)
	left := 0
	var sum int64
	dq := []int{}
	ans := 0
	for right := 0; right < n; right++ {
		for len(dq) > 0 && chargeTimes[dq[len(dq)-1]] <= chargeTimes[right] {
			dq = dq[:len(dq)-1]
		}
		dq = append(dq, right)
		sum += int64(runningCosts[right])
		for left <= right && int64(chargeTimes[dq[0]])+int64(right-left+1)*sum > budget {
			if dq[0] == left {
				dq = dq[1:]
			}
			sum -= int64(runningCosts[left])
			left++
		}
		if right-left+1 > ans {
			ans = right - left + 1
		}
	}
	return ans
}
