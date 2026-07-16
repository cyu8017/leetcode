import heapq
from collections import defaultdict

class FileSharing:
    def __init__(self, m: int):
        self.owners = defaultdict(set)
        self.chunks = {}
        self.free = []
        self.next_id = 1

    def join(self, ownedChunks: list[int]) -> int:
        user = heapq.heappop(self.free) if self.free else self.next_id
        if user == self.next_id:
            self.next_id += 1
        self.chunks[user] = set(ownedChunks)
        for chunk in ownedChunks:
            self.owners[chunk].add(user)
        return user

    def leave(self, userID: int) -> None:
        for chunk in self.chunks.pop(userID, ()):
            self.owners[chunk].discard(userID)
        heapq.heappush(self.free, userID)

    def request(self, userID: int, chunkID: int) -> list[int]:
        users = sorted(self.owners[chunkID])
        if users:
            self.chunks[userID].add(chunkID)
            self.owners[chunkID].add(userID)
        return users
