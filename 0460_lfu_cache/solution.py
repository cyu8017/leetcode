# LeetCode 0460 - LFU Cache
# https://leetcode.com/problems/lfu-cache/

from collections import defaultdict


class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 0
        self.key_values: dict[int, int] = {}
        self.key_freqs: dict[int, int] = {}
        self.freq_keys: dict[int, list[int]] = defaultdict(list)

    def _touch(self, key: int) -> None:
        freq = self.key_freqs[key]
        bucket = self.freq_keys[freq]
        bucket.remove(key)
        if not bucket and freq == self.min_freq:
            self.min_freq += 1
        self.key_freqs[key] = freq + 1
        self.freq_keys[freq + 1].append(key)

    def get(self, key: int) -> int:
        if key not in self.key_values:
            return -1
        self._touch(key)
        return self.key_values[key]

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if key in self.key_values:
            self.key_values[key] = value
            self._touch(key)
            return

        if len(self.key_values) >= self.capacity:
            evict = self.freq_keys[self.min_freq].pop(0)
            del self.key_values[evict]
            del self.key_freqs[evict]

        self.key_values[key] = value
        self.key_freqs[key] = 1
        self.freq_keys[1].append(key)
        self.min_freq = 1
