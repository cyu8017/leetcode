// LeetCode 3100 - Water Bottles II
// https://leetcode.com/problems/water-bottles-ii/

func maxBottlesDrunk(numBottles int, numExchange int) int {
	ans := numBottles
	for numBottles >= numExchange {
		numBottles -= numExchange
		numExchange++
		ans++
		numBottles++
	}
	return ans
}
