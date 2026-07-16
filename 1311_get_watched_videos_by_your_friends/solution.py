# LeetCode 1311 - Get Watched Videos By Your Friends

from collections import Counter, deque
from typing import List

class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        queue, seen = deque([(id, 0)]), {id}
        people = []
        while queue:
            person, distance = queue.popleft()
            if distance == level:
                people.append(person)
                continue
            for friend in friends[person]:
                if friend not in seen:
                    seen.add(friend); queue.append((friend, distance + 1))
        counts = Counter(video for person in people for video in watchedVideos[person])
        return sorted(counts, key=lambda video: (counts[video], video))
