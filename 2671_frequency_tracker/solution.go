// LeetCode 2671 - Frequency Tracker
// https://leetcode.com/problems/frequency-tracker/


type FrequencyTracker struct {
	freq  map[int]int
	count map[int]int
}

func Constructor() FrequencyTracker {
	return FrequencyTracker{freq: map[int]int{}, count: map[int]int{}}
}

func (f *FrequencyTracker) Add(number int) {
	old := f.freq[number]
	if old > 0 {
		f.count[old]--
	}
	f.freq[number] = old + 1
	f.count[old+1]++
}

func (f *FrequencyTracker) DeleteOne(number int) {
	old := f.freq[number]
	if old == 0 {
		return
	}
	f.count[old]--
	f.freq[number] = old - 1
	if old-1 > 0 {
		f.count[old-1]++
	}
}

func (f *FrequencyTracker) HasFrequency(frequency int) bool {
	return f.count[frequency] > 0
}
