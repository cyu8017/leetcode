// LeetCode 1333 - Filter Restaurants by Vegan-Friendly, Price and Distance
// https://leetcode.com/problems/filter-restaurants-by-vegan-friendly-price-and-distance/

import "sort"

func filterRestaurants(restaurants [][]int, veganFriendly int, maxPrice int, maxDistance int) []int {
	var valid [][]int
	for _, row := range restaurants {
		if (veganFriendly == 0 || row[2] == 1) && row[3] <= maxPrice && row[4] <= maxDistance {
			valid = append(valid, row)
		}
	}
	sort.Slice(valid, func(i, j int) bool {
		if valid[i][1] != valid[j][1] {
			return valid[i][1] > valid[j][1]
		}
		return valid[i][0] > valid[j][0]
	})
	answer := make([]int, len(valid))
	for i, row := range valid {
		answer[i] = row[0]
	}
	return answer
}
