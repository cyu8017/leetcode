// LeetCode 2534 - Time Taken to Cross the Door
// https://leetcode.com/problems/time-taken-to-cross-the-door/

func timeTaken(arrival []int, state []int) []int {
	n := len(arrival)
	ans := make([]int, n)
	enter, exit := []int{}, []int{}
	i, t := 0, 0
	prev := 1 // last used for exit preferred initially
	for i < n || len(enter) > 0 || len(exit) > 0 {
		for i < n && arrival[i] <= t {
			if state[i] == 0 {
				enter = append(enter, i)
			} else {
				exit = append(exit, i)
			}
			i++
		}
		if len(enter) == 0 && len(exit) == 0 {
			if i < n {
				t = arrival[i]
				prev = 1
			}
			continue
		}
		if prev == 1 {
			if len(exit) > 0 {
				ans[exit[0]] = t
				exit = exit[1:]
				prev = 1
			} else {
				ans[enter[0]] = t
				enter = enter[1:]
				prev = 0
			}
		} else {
			if len(enter) > 0 {
				ans[enter[0]] = t
				enter = enter[1:]
				prev = 0
			} else {
				ans[exit[0]] = t
				exit = exit[1:]
				prev = 1
			}
		}
		t++
	}
	return ans
}
