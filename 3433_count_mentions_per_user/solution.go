// LeetCode 3433 - Count Mentions Per User
// https://leetcode.com/problems/count-mentions-per-user/

import "sort"
import "strconv"
import "strings"

func countMentions(numberOfUsers int, events [][]string) []int {
	sort.SliceStable(events, func(i, j int) bool {
		ti, _ := strconv.Atoi(events[i][1])
		tj, _ := strconv.Atoi(events[j][1])
		if ti != tj {
			return ti < tj
		}
		// OFFLINE before MESSAGE at same time
		return events[i][0] > events[j][0]
	})
	online := make([]bool, numberOfUsers)
	offlineUntil := make([]int, numberOfUsers)
	for i := range online {
		online[i] = true
	}
	ans := make([]int, numberOfUsers)
	for _, e := range events {
		t, _ := strconv.Atoi(e[1])
		for i := 0; i < numberOfUsers; i++ {
			if !online[i] && offlineUntil[i] <= t {
				online[i] = true
			}
		}
		if e[0] == "OFFLINE" {
			id, _ := strconv.Atoi(e[2])
			online[id] = false
			offlineUntil[id] = t + 60
		} else {
			msg := e[2]
			if msg == "ALL" {
				for i := 0; i < numberOfUsers; i++ {
					ans[i]++
				}
			} else if msg == "HERE" {
				for i := 0; i < numberOfUsers; i++ {
					if online[i] {
						ans[i]++
					}
				}
			} else {
				for _, part := range strings.Fields(msg) {
					id, _ := strconv.Atoi(part[2:])
					ans[id]++
				}
			}
		}
	}
	return ans
}
