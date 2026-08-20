// LeetCode 3259 - Maximum Energy Boost From Two Drinks
// https://leetcode.com/problems/maximum-energy-boost-from-two-drinks/

func maxEnergyBoost(energyDrinkA []int, energyDrinkB []int) int64 {
	n := len(energyDrinkA)
	dpA := make([]int64, n)
	dpB := make([]int64, n)
	dpA[0] = int64(energyDrinkA[0])
	dpB[0] = int64(energyDrinkB[0])
	if n == 1 {
		if dpA[0] > dpB[0] {
			return dpA[0]
		}
		return dpB[0]
	}
	dpA[1] = int64(energyDrinkA[1]) + dpA[0]
	dpB[1] = int64(energyDrinkB[1]) + dpB[0]
	for i := 2; i < n; i++ {
		x := dpA[i-1]
		if dpB[i-2] > x {
			x = dpB[i-2]
		}
		dpA[i] = int64(energyDrinkA[i]) + x
		y := dpB[i-1]
		if dpA[i-2] > y {
			y = dpA[i-2]
		}
		dpB[i] = int64(energyDrinkB[i]) + y
	}
	if dpA[n-1] > dpB[n-1] {
		return dpA[n-1]
	}
	return dpB[n-1]
}
