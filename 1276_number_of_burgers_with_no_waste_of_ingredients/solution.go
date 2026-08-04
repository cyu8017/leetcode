// LeetCode 1276 - Number of Burgers with No Waste of Ingredients
// https://leetcode.com/problems/number-of-burgers-with-no-waste-of-ingredients/

func numOfBurgers(tomatoSlices int, cheeseSlices int) []int {
	if tomatoSlices%2 != 0 {
		return []int{}
	}
	jumbo := tomatoSlices/2 - cheeseSlices
	small := cheeseSlices - jumbo
	if jumbo >= 0 && small >= 0 {
		return []int{jumbo, small}
	}
	return []int{}
}
