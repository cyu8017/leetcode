// LeetCode 1024 - Video Stitching
// https://leetcode.com/problems/video-stitching/

class Solution {
    fun videoStitching(clips: Array<IntArray>, time: Int): Int {
        val furthest = IntArray(time + 1)
        for (clip in clips) {
            val start = clip[0]; val end = clip[1]
            if (start <= time) furthest[start] = maxOf(furthest[start], end)
        }
        var ans = 0; var reach = 0; var nextReach = 0
        for (i in 0 until time) {
            nextReach = maxOf(nextReach, furthest[i])
            if (i == reach) {
                if (nextReach <= i) return -1
                ans++
                reach = nextReach
            }
        }
        return ans
    }
}
