// LeetCode 1854 - Maximum Population Year
// https://leetcode.com/problems/maximum-population-year/

func maximumPopulation(logs [][]int) int {
	diff := make([]int, 101)

	for _, log := range logs {
		birth, death := log[0], log[1]
		diff[birth-1950]++
		diff[death-1950]--
	}

	bestYear := 1950
	bestPopulation := 0
	population := 0

	for offset := 0; offset < 101; offset++ {
		population += diff[offset]
		if population > bestPopulation {
			bestPopulation = population
			bestYear = 1950 + offset
		}
	}

	return bestYear
}
