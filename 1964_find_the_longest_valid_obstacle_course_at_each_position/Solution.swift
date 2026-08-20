// LeetCode 1964 - Find the Longest Valid Obstacle Course at Each Position
// https://leetcode.com/problems/find-the-longest-valid-obstacle-course-at-each-position/

class Solution {
    func longestObstacleCourseAtEachPosition(_ obstacles: [Int]) -> [Int] {
        var tails: [Int] = []
        var ans: [Int] = []
        for x in obstacles {
            var lo = 0, hi = tails.count
            while lo < hi {
                let mid = (lo + hi) / 2
                if tails[mid] <= x { lo = mid + 1 } else { hi = mid }
            }
            if lo == tails.count {
                tails.append(x)
            } else {
                tails[lo] = x
            }
            ans.append(lo + 1)
        }
        return ans
    }
}
