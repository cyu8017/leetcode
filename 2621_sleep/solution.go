// LeetCode 2621 - Sleep
// https://leetcode.com/problems/sleep/


import "time"

func sleep(millis int) {
	time.Sleep(time.Duration(millis) * time.Millisecond)
}
