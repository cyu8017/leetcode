// LeetCode 0981 - Time Based Key-Value Store
// https://leetcode.com/problems/time-based-key-value-store/

import "sort"

type pair struct {
	ts  int
	val string
}

type TimeMap struct {
	store map[string][]pair
}

func Constructor() TimeMap {
	return TimeMap{store: map[string][]pair{}}
}

func (this *TimeMap) Set(key string, value string, timestamp int) {
	this.store[key] = append(this.store[key], pair{timestamp, value})
}

func (this *TimeMap) Get(key string, timestamp int) string {
	arr := this.store[key]
	i := sort.Search(len(arr), func(i int) bool {
		return arr[i].ts > timestamp
	}) - 1
	if i >= 0 {
		return arr[i].val
	}
	return ""
}
