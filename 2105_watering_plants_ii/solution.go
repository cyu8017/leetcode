// LeetCode 2105 - Watering Plants II
// https://leetcode.com/problems/watering-plants-ii/

func minimumRefill(plants []int, capacityA int, capacityB int) int {
	i, j := 0, len(plants)-1
	a, b := capacityA, capacityB
	ans := 0
	for i < j {
		if a < plants[i] {
			ans++
			a = capacityA
		}
		a -= plants[i]
		i++
		if b < plants[j] {
			ans++
			b = capacityB
		}
		b -= plants[j]
		j--
	}
	if i == j {
		if a >= b {
			if a < plants[i] {
				ans++
			}
		} else if b < plants[i] {
			ans++
		}
	}
	return ans
}
