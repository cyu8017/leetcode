// LeetCode 1419 - Minimum Number of Frogs Croaking
// https://leetcode.com/problems/minimum-number-of-frogs-croaking/

func minNumberOfFrogs(croakOfFrogs string) int {
	order := map[byte]int{'c': 0, 'r': 1, 'o': 2, 'a': 3, 'k': 4}
	counts := [5]int{}
	active, answer := 0, 0
	for i := 0; i < len(croakOfFrogs); i++ {
		idx, ok := order[croakOfFrogs[i]]
		if !ok || (idx > 0 && counts[idx-1] == 0) {
			return -1
		}
		if idx > 0 {
			counts[idx-1]--
		}
		counts[idx]++
		if idx == 0 {
			active++
			if active > answer {
				answer = active
			}
		} else if idx == 4 {
			counts[4]--
			active--
		}
	}
	if active == 0 {
		return answer
	}
	return -1
}
