// LeetCode 0815 - Bus Routes
// https://leetcode.com/problems/bus-routes/

func numBusesToDestination(routes [][]int, source int, target int) int {
	if source == target {
		return 0
	}
	stopToBuses := map[int][]int{}
	for bus, stops := range routes {
		for _, stop := range stops {
			stopToBuses[stop] = append(stopToBuses[stop], bus)
		}
	}
	type item struct{ stop, buses int }
	queue := []item{{source, 0}}
	seenStops := map[int]bool{source: true}
	seenBuses := map[int]bool{}
	for len(queue) > 0 {
		cur := queue[0]
		queue = queue[1:]
		for _, bus := range stopToBuses[cur.stop] {
			if seenBuses[bus] {
				continue
			}
			seenBuses[bus] = true
			for _, nxt := range routes[bus] {
				if nxt == target {
					return cur.buses + 1
				}
				if !seenStops[nxt] {
					seenStops[nxt] = true
					queue = append(queue, item{nxt, cur.buses + 1})
				}
			}
		}
	}
	return -1
}
