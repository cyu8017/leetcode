// LeetCode 0057 - Insert Interval
// https://leetcode.com/problems/insert-interval/

func insert(intervals [][]int, newInterval []int) [][]int {
	result := make([][]int, 0, len(intervals)+1)
	i := 0

	for i < len(intervals) && intervals[i][1] < newInterval[0] {
		result = append(result, intervals[i])
		i++
	}

	for i < len(intervals) && intervals[i][0] <= newInterval[1] {
		if intervals[i][0] < newInterval[0] {
			newInterval[0] = intervals[i][0]
		}
		if intervals[i][1] > newInterval[1] {
			newInterval[1] = intervals[i][1]
		}
		i++
	}

	result = append(result, newInterval)

	for i < len(intervals) {
		result = append(result, intervals[i])
		i++
	}

	return result
}
