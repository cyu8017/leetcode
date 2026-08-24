# LeetCode 3433 - Count Mentions Per User
# https://leetcode.com/problems/count-mentions-per-user/

from typing import List


class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        events = sorted(events, key=lambda e: (int(e[1]), 0 if e[0] == "OFFLINE" else 1))
        online = [True] * numberOfUsers
        offline_until = [0] * numberOfUsers
        ans = [0] * numberOfUsers
        for e in events:
            t = int(e[1])
            for i in range(numberOfUsers):
                if not online[i] and offline_until[i] <= t:
                    online[i] = True
            if e[0] == "OFFLINE":
                uid = int(e[2])
                online[uid] = False
                offline_until[uid] = t + 60
            else:
                msg = e[2]
                if msg == "ALL":
                    for i in range(numberOfUsers):
                        ans[i] += 1
                elif msg == "HERE":
                    for i in range(numberOfUsers):
                        if online[i]:
                            ans[i] += 1
                else:
                    for part in msg.split(" "):
                        uid = int(part[2:])
                        ans[uid] += 1
        return ans
