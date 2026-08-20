// LeetCode 2753 - Count Houses in a Circular Street II
// https://leetcode.com/problems/count-houses-in-a-circular-street-ii/

func houseCount(street []int, k int) int {
	n := len(street)
	if n == 0 {
		return 0
	}
	start := -1
	for i, v := range street {
		if v == 1 {
			start = i
			break
		}
	}
	if start < 0 {
		return 0
	}
	count := 1
	moves := 0
	i := start
	for moves < k {
		i = (i + 1) % n
		moves++
		if i == start {
			break
		}
		if street[i] == 1 {
			count++
		}
	}
	return count
}
