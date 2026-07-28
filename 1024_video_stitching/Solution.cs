// LeetCode 1024 - Video Stitching
// https://leetcode.com/problems/video-stitching/

public class Solution {
    public int VideoStitching(int[][] clips, int time) {
        var furthest = new int[time + 1];
        foreach (var clip in clips) {
            int start = clip[0], end = clip[1];
            if (start <= time) furthest[start] = Math.Max(furthest[start], end);
        }
        int ans = 0, reach = 0, nextReach = 0;
        for (int i = 0; i < time; i++) {
            nextReach = Math.Max(nextReach, furthest[i]);
            if (i == reach) {
                if (nextReach <= i) return -1;
                ans++;
                reach = nextReach;
            }
        }
        return ans;
    }
}
