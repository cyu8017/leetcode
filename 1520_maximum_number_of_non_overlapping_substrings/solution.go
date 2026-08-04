// LeetCode 1520 - Maximum Number of Non-Overlapping Substrings
// https://leetcode.com/problems/maximum-number-of-non-overlapping-substrings/

import "sort"

func maxNumOfSubstrings(s string) []string {
	first := map[byte]int{}
	last := map[byte]int{}
	for i := len(s) - 1; i >= 0; i-- {
		first[s[i]] = i
	}
	for i := 0; i < len(s); i++ {
		last[s[i]] = i
	}
	type interval struct{ end, start int }
	intervals := []interval{}
	for i := 0; i < len(s); i++ {
		ch := s[i]
		if first[ch] != i {
			continue
		}
		end := last[ch]
		j := i
		valid := true
		for j <= end {
			if first[s[j]] < i {
				valid = false
				break
			}
			if last[s[j]] > end {
				end = last[s[j]]
			}
			j++
		}
		if valid {
			intervals = append(intervals, interval{end, i})
		}
	}
	sort.Slice(intervals, func(i, j int) bool {
		return intervals[i].end < intervals[j].end
	})
	answer := []string{}
	previousEnd := -1
	for _, iv := range intervals {
		if iv.start > previousEnd {
			answer = append(answer, s[iv.start:iv.end+1])
			previousEnd = iv.end
		}
	}
	sort.Slice(answer, func(i, j int) bool {
		return len(answer[i]) < len(answer[j])
	})
	return answer
}
