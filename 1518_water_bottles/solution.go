// LeetCode 1518 - Water Bottles
// https://leetcode.com/problems/water-bottles/

func numWaterBottles(numBottles int, numExchange int) int {
	total := numBottles
	for numBottles >= numExchange {
		newBottles := numBottles / numExchange
		remainder := numBottles % numExchange
		total += newBottles
		numBottles = newBottles + remainder
	}
	return total
}
