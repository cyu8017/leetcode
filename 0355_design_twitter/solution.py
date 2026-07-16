# LeetCode 0355 - Design Twitter
# https://leetcode.com/problems/design-twitter/

import heapq
from collections import defaultdict
from typing import List


class Twitter:
    def __init__(self):
        self.time = 0
        self.tweets: dict[int, list[tuple[int, int]]] = defaultdict(list)
        self.following: dict[int, set[int]] = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        heap: list[tuple[int, int]] = []
        users = self.following[userId] | {userId}

        for uid in users:
            for timestamp, tweet_id in self.tweets[uid][-10:]:
                heapq.heappush(heap, (-timestamp, tweet_id))

        feed: list[int] = []
        while heap and len(feed) < 10:
            feed.append(heapq.heappop(heap)[1])

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
