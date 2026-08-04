// LeetCode 1599 - Maximum Profit of Operating a Centennial Wheel
// https://leetcode.com/problems/maximum-profit-of-operating-a-centennial-wheel/

func minOperationsMaxProfit(customers []int, boardingCost int, runningCost int) int {
	waiting, profit, best, answer, rotation := 0, 0, 0, 0, 0
	i := 0
	for i < len(customers) || waiting > 0 {
		if i < len(customers) {
			waiting += customers[i]
		}
		boarded := 4
		if waiting < boarded {
			boarded = waiting
		}
		waiting -= boarded
		rotation++
		profit += boarded*boardingCost - runningCost
		if profit > best {
			best = profit
			answer = rotation
		}
		i++
	}
	if best > 0 {
		return answer
	}
	return -1
}
