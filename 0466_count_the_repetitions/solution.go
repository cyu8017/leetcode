// LeetCode 0466 - Count The Repetitions
// https://leetcode.com/problems/count-the-repetitions/

func getMaxRepetitions(s1 string, n1 int, s2 string, n2 int) int {
	if len(s2) == 0 {
		return 0
	}

	index := 0
	s2Count := 0
	record := make(map[int][2]int)

repeatLoop:
	for repeat := 0; repeat < n1; repeat++ {
		for _, char := range s1 {
			if byte(char) == s2[index] {
				index++
				if index == len(s2) {
					index = 0
					s2Count++
				}
			}
		}
		if previous, ok := record[index]; ok {
			previousRepeat, previousCount := previous[0], previous[1]
			cycle := repeat - previousRepeat
			countCycle := s2Count - previousCount
			remaining := n1 - repeat - 1
			s2Count += (remaining / cycle) * countCycle
			if repeat+(remaining/cycle)*cycle >= n1-1 {
				break repeatLoop
			}
		}
		record[index] = [2]int{repeat, s2Count}
	}

	return s2Count / n2
}
