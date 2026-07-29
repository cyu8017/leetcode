// LeetCode 1007 - Minimum Domino Rotations For Equal Row
// https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/

class Solution {
    func minDominoRotations(_ tops: [Int], _ bottoms: [Int]) -> Int {
        func check(_ target: Int) -> Int {
            var rotTop = 0, rotBot = 0
            for i in 0..<tops.count {
                if tops[i] != target && bottoms[i] != target { return Int.max }
                if tops[i] != target { rotTop += 1 }
                if bottoms[i] != target { rotBot += 1 }
            }
            return min(rotTop, rotBot)
        }
        let ans = min(check(tops[0]), check(bottoms[0]))
        return ans == Int.max ? -1 : ans
    }
}
