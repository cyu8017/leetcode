// LeetCode 1024 - Video Stitching
// https://leetcode.com/problems/video-stitching/

#include <algorithm>
#include <vector>

class Solution {
public:
    int videoStitching(std::vector<std::vector<int>>& clips, int time) {
        std::vector<int> furthest(time + 1, 0);
        for (auto& clip : clips) {
            int start = clip[0], end = clip[1];
            if (start <= time) furthest[start] = std::max(furthest[start], end);
        }
        int ans = 0, reach = 0, nextReach = 0;
        for (int i = 0; i < time; ++i) {
            nextReach = std::max(nextReach, furthest[i]);
            if (i == reach) {
                if (nextReach <= i) return -1;
                ++ans;
                reach = nextReach;
            }
        }
        return ans;
    }
};

