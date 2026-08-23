// LeetCode 3440 - Reschedule Meetings for Maximum Free Time II
// https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-ii/

#include <vector>

class Solution {
public:
    int maxFreeTime(int eventTime, std::vector<int>& startTime, std::vector<int>& endTime) {
        int n = (int)startTime.size();
        std::vector<int> gaps(n + 1);
        gaps[0] = startTime[0];
        for (int i = 1; i < n; i++) gaps[i] = startTime[i] - endTime[i - 1];
        gaps[n] = eventTime - endTime[n - 1];
        int ans = 0;
        for (int g : gaps) if (g > ans) ans = g;
        std::vector<int> leftMax(n + 1), rightMax(n + 1);
        for (int i = 0; i <= n; i++) {
            leftMax[i] = gaps[i];
            if (i > 0 && leftMax[i - 1] > leftMax[i]) leftMax[i] = leftMax[i - 1];
        }
        for (int i = n; i >= 0; i--) {
            rightMax[i] = gaps[i];
            if (i < n && rightMax[i + 1] > rightMax[i]) rightMax[i] = rightMax[i + 1];
        }
        for (int i = 0; i < n; i++) {
            int dur = endTime[i] - startTime[i];
            int merged = gaps[i] + gaps[i + 1];
            int bestOther = 0;
            if (i > 0 && leftMax[i - 1] > bestOther) bestOther = leftMax[i - 1];
            if (i + 2 <= n && rightMax[i + 2] > bestOther) bestOther = rightMax[i + 2];
            int cand = merged;
            if (bestOther >= dur) cand = merged + dur;
            if (cand > ans) ans = cand;
        }
        return ans;
    }
};
