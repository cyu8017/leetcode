// LeetCode 0849 - Maximize Distance to Closest Person
// https://leetcode.com/problems/maximize-distance-to-closest-person/

func maxDistToClosest(seats []int) int {
	n := len(seats)
	prev, ans := -1, 0
	for i, occupied := range seats {
		if occupied == 1 {
			if prev == -1 {
				ans = i
			} else if (i-prev)/2 > ans {
				ans = (i - prev) / 2
			}
			prev = i
		}
	}
	if n-1-prev > ans {
		ans = n - 1 - prev
	}
	return ans
}
