// LeetCode 1094 - Car Pooling
// https://leetcode.com/problems/car-pooling/

func carPooling(trips [][]int, capacity int) bool {
	diff := make([]int, 1001)
	for _, t := range trips {
		diff[t[1]] += t[0]
		diff[t[2]] -= t[0]
	}
	cur := 0
	for _, x := range diff {
		cur += x
		if cur > capacity {
			return false
		}
	}
	return true
}
