# LeetCode 2456 - Most Popular Video Creator
# https://leetcode.com/problems/most-popular-video-creator/

from typing import List


class Solution:
    def mostPopularCreator(
        self, creators: List[str], ids: List[str], views: List[int]
    ) -> List[List[str]]:
        mp = {}
        max_total = 0
        for i in range(len(creators)):
            info = mp.get(creators[i])
            if not info:
                info = {"total": views[i], "bestID": ids[i], "bestViews": views[i]}
                mp[creators[i]] = info
            else:
                info["total"] += views[i]
                if views[i] > info["bestViews"] or (
                    views[i] == info["bestViews"] and ids[i] < info["bestID"]
                ):
                    info["bestViews"] = views[i]
                    info["bestID"] = ids[i]
            max_total = max(max_total, mp[creators[i]]["total"])
        ans = []
        for creator, info in mp.items():
            if info["total"] == max_total:
                ans.append([creator, info["bestID"]])
        return ans
