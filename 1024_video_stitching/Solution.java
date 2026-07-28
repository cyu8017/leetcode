// LeetCode 1024 - Video Stitching
// https://leetcode.com/problems/video-stitching/

class Solution {
    public int videoStitching(int[][] clips, int time) {
        int[] furthest = new int[time + 1];
        for (int[] clip : clips) {
            int start = clip[0], end = clip[1];
            if (start <= time) furthest[start] = Math.max(furthest[start], end);
        }
        int ans = 0, reach = 0, nextReach = 0;
        for (int i = 0; i < time; i++) {
            nextReach = Math.max(nextReach, furthest[i]);
            if (i == reach) {
                if (nextReach <= i) return -1;
                ans++;
                reach = nextReach;
            }
        }
        return ans;
    }
}
