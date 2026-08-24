# LeetCode 2254 - Design Video Sharing Platform
# https://leetcode.com/problems/design-video-sharing-platform/

import heapq
from typing import List


class VideoSharingPlatform:
    def __init__(self):
        self.nextID = 0
        self.free = []
        self.videos = {}
        self.views = {}
        self.likes = {}
        self.dislikes = {}

    def upload(self, video: str) -> int:
        if self.free:
            vid = heapq.heappop(self.free)
        else:
            vid = self.nextID
            self.nextID += 1
        self.videos[vid] = video
        self.views[vid] = 0
        self.likes[vid] = 0
        self.dislikes[vid] = 0
        return vid

    def remove(self, videoId: int) -> None:
        if videoId not in self.videos:
            return
        del self.videos[videoId]
        del self.views[videoId]
        del self.likes[videoId]
        del self.dislikes[videoId]
        heapq.heappush(self.free, videoId)

    def watch(self, videoId: int, startMinute: int, endMinute: int) -> str:
        v = self.videos.get(videoId)
        if v is None:
            return "-1"
        self.views[videoId] += 1
        if startMinute >= len(v):
            return ""
        endMinute = min(endMinute, len(v) - 1)
        return v[startMinute : endMinute + 1]

    def like(self, videoId: int) -> None:
        if videoId in self.videos:
            self.likes[videoId] += 1

    def dislike(self, videoId: int) -> None:
        if videoId in self.videos:
            self.dislikes[videoId] += 1

    def getLikesAndDislikes(self, videoId: int) -> List[int]:
        if videoId not in self.videos:
            return [-1]
        return [self.likes[videoId], self.dislikes[videoId]]

    def getViews(self, videoId: int) -> int:
        if videoId not in self.videos:
            return -1
        return self.views[videoId]
