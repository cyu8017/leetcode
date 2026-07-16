// LeetCode 0458 - Poor Pigs
// https://leetcode.com/problems/poor-pigs/

func poorPigs(buckets int, minutesToDie int, minutesToTest int) int {
	states := minutesToTest/minutesToDie + 1
	pigs := 0
	capacity := 1
	for capacity < buckets {
		pigs++
		capacity *= states
	}
	return pigs
}
