// LeetCode 1701 - Average Waiting Time
// https://leetcode.com/problems/average-waiting-time/

func averageWaitingTime(customers [][]int) float64 {
	current := 0
	total := 0
	for _, customer := range customers {
		if customer[0] > current {
			current = customer[0]
		}
		current += customer[1]
		total += current - customer[0]
	}
	return float64(total) / float64(len(customers))
}
