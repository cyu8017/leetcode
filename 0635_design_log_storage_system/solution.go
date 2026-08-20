// LeetCode 0635 - Design Log Storage System
// https://leetcode.com/problems/design-log-storage-system/

import "sort"

type logEntry struct {
	id        int
	timestamp string
}

type LogSystem struct {
	logs []logEntry
}

func Constructor() LogSystem {
	return LogSystem{}
}

func (ls *LogSystem) Put(id int, timestamp string) {
	ls.logs = append(ls.logs, logEntry{id, timestamp})
}

func (ls *LogSystem) Retrieve(start string, end string, granularity string) []int {
	indexMap := map[string]int{
		"Year": 4, "Month": 7, "Day": 10, "Hour": 13, "Minute": 16, "Second": 19,
	}
	index := indexMap[granularity]
	startKey := start[:index]
	endKey := end[:index]
	type pair struct {
		ts string
		id int
	}
	matched := []pair{}
	for _, log := range ls.logs {
		key := log.timestamp[:index]
		if startKey <= key && key <= endKey {
			matched = append(matched, pair{log.timestamp, log.id})
		}
	}
	sort.Slice(matched, func(i, j int) bool {
		if matched[i].ts == matched[j].ts {
			return matched[i].id < matched[j].id
		}
		return matched[i].ts < matched[j].ts
	})
	out := make([]int, len(matched))
	for i, p := range matched {
		out[i] = p.id
	}
	return out
}
