// LeetCode 3168 - Minimum Number of Chairs in a Waiting Room
// https://leetcode.com/problems/minimum-number-of-chairs-in-a-waiting-room/

func minimumChairs(s string) int {
	cnt, left := 0, 0
	for _, c := range s {
		if c == 'E' {
			if left > 0 {
				left--
			} else {
				cnt++
			}
		} else {
			left++
		}
	}
	return cnt
}
