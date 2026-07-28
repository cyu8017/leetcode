// LeetCode 1024 - Video Stitching
// https://leetcode.com/problems/video-stitching/

/**
 * @param {number[][]} clips
 * @param {number} time
 * @return {number}
 */
var videoStitching = function(clips, time) {
    const furthest = new Array(time + 1).fill(0);
    for (const [start, end] of clips) {
        if (start <= time) furthest[start] = Math.max(furthest[start], end);
    }
    let ans = 0, reach = 0, nextReach = 0;
    for (let i = 0; i < time; i++) {
        nextReach = Math.max(nextReach, furthest[i]);
        if (i === reach) {
            if (nextReach <= i) return -1;
            ans++;
            reach = nextReach;
        }
    }
    return ans;
};
