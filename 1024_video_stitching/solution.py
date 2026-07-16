# LeetCode 1024 - Video Stitching
# https://leetcode.com/problems/video-stitching/

class Solution:
    def videoStitching(self, clips: list[list[int]], time: int) -> int:
        furthest = [0] * (time + 1)
        for start, end in clips:
            if start <= time:
                furthest[start] = max(furthest[start], end)
        ans = reach = next_reach = 0
        for i in range(time):
            next_reach = max(next_reach, furthest[i])
            if i == reach:
                if next_reach <= i:
                    return -1
                ans += 1
                reach = next_reach
        return ans
