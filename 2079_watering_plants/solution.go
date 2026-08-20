// LeetCode 2079 - Watering Plants
// https://leetcode.com/problems/watering-plants/

func wateringPlants(plants []int, capacity int) int {
	ans, cur := 0, capacity
	for i, p := range plants {
		if cur < p {
			ans += i * 2
			cur = capacity
		}
		cur -= p
		ans++
	}
	return ans
}
