// LeetCode 0332 - Reconstruct Itinerary
// https://leetcode.com/problems/reconstruct-itinerary/

import (
	"sort"
)

func findItinerary(tickets [][]string) []string {
	targets := make(map[string][]string)
	sortedTickets := append([][]string(nil), tickets...)
	sort.Slice(sortedTickets, func(i, j int) bool {
		if sortedTickets[i][0] == sortedTickets[j][0] {
			return sortedTickets[i][1] < sortedTickets[j][1]
		}
		return sortedTickets[i][0] < sortedTickets[j][0]
	})
	for index := len(sortedTickets) - 1; index >= 0; index-- {
		source := sortedTickets[index][0]
		targets[source] = append(targets[source], sortedTickets[index][1])
	}

	route := make([]string, 0)
	var visit func(airport string)
	visit = func(airport string) {
		for len(targets[airport]) > 0 {
			next := targets[airport][len(targets[airport])-1]
			targets[airport] = targets[airport][:len(targets[airport])-1]
			visit(next)
		}
		route = append(route, airport)
	}

	visit("JFK")
	for left, right := 0, len(route)-1; left < right; left, right = left+1, right-1 {
		route[left], route[right] = route[right], route[left]
	}
	return route
}
