// LeetCode 0355 - Design Twitter
// https://leetcode.com/problems/design-twitter/

import "sort"

type Twitter struct {
	time      int
	tweets    map[int][][2]int
	following map[int]map[int]bool
}

func Constructor() Twitter {
	return Twitter{
		tweets:    make(map[int][][2]int),
		following: make(map[int]map[int]bool),
	}
}

func (this *Twitter) PostTweet(userId int, tweetId int) {
	this.time++
	this.tweets[userId] = append(this.tweets[userId], [2]int{this.time, tweetId})
}

func (this *Twitter) GetNewsFeed(userId int) []int {
	type item struct {
		timestamp int
		tweetId   int
	}

	items := make([]item, 0)
	users := map[int]bool{userId: true}
	for followee := range this.following[userId] {
		users[followee] = true
	}

	for uid := range users {
		timeline := this.tweets[uid]
		start := len(timeline) - 10
		if start < 0 {
			start = 0
		}
		for _, entry := range timeline[start:] {
			items = append(items, item{timestamp: entry[0], tweetId: entry[1]})
		}
	}

	sort.Slice(items, func(i, j int) bool {
		if items[i].timestamp != items[j].timestamp {
			return items[i].timestamp > items[j].timestamp
		}
		return items[i].tweetId < items[j].tweetId
	})

	feed := make([]int, 0, 10)
	for _, entry := range items {
		if len(feed) == 10 {
			break
		}
		feed = append(feed, entry.tweetId)
	}
	return feed
}

func (this *Twitter) Follow(followerId int, followeeId int) {
	if this.following[followerId] == nil {
		this.following[followerId] = make(map[int]bool)
	}
	this.following[followerId][followeeId] = true
}

func (this *Twitter) Unfollow(followerId int, followeeId int) {
	delete(this.following[followerId], followeeId)
}
