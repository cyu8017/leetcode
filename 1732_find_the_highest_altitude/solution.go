// LeetCode 1732 - Find the Highest Altitude
// https://leetcode.com/problems/find-the-highest-altitude/

func largestAltitude(gain []int) int {
	altitude := 0
	best := 0
	for _, change := range gain {
		altitude += change
		if altitude > best {
			best = altitude
		}
	}
	return best
}
