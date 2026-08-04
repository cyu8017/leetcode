// LeetCode 1348 - Tweet Counts Per Frequency
// https://leetcode.com/problems/tweet-counts-per-frequency/

import "sort"

type TweetCounts struct {
	times map[string][]int
}

func Constructor() TweetCounts {
	return TweetCounts{times: map[string][]int{}}
}

func (this *TweetCounts) RecordTweet(tweetName string, time int) {
	this.times[tweetName] = append(this.times[tweetName], time)
}

func (this *TweetCounts) GetTweetCountsPerFrequency(freq string, tweetName string, startTime int, endTime int) []int {
	delta := 60
	if freq == "hour" {
		delta = 3600
	} else if freq == "day" {
		delta = 86400
	}
	n := (endTime-startTime)/delta + 1
	answer := make([]int, n)
	arr := this.times[tweetName]
	sort.Ints(arr)
	for _, t := range arr {
		if t < startTime || t > endTime {
			continue
		}
		answer[(t-startTime)/delta]++
	}
	return answer
}
