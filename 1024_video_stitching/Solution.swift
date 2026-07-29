// LeetCode 1024 - Video Stitching
// https://leetcode.com/problems/video-stitching/

class Solution {
    func videoStitching(_ clips: [[Int]], _ time: Int) -> Int {
        var furthest = Array(repeating: 0, count: time + 1)
        for clip in clips {
            let start = clip[0], end = clip[1]
            if start <= time {
                furthest[start] = max(furthest[start], end)
            }
        }
        var ans = 0, reach = 0, nextReach = 0
        for i in 0..<time {
            nextReach = max(nextReach, furthest[i])
            if i == reach {
                if nextReach <= i { return -1 }
                ans += 1
                reach = nextReach
            }
        }
        return ans
    }
}
