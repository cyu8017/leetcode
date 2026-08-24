// LeetCode 2139 - Minimum Moves to Reach Target Score
// https://leetcode.com/problems/minimum-moves-to-reach-target-score/

class Solution {
    func minMoves(_ target: Int, _ maxDoubles: Int) -> Int {
        var target = target, maxDoubles = maxDoubles, ans = 0
        while target > 1 && maxDoubles > 0 {
            if target % 2 != 0 { target -= 1; ans += 1 }
            else { target /= 2; maxDoubles -= 1; ans += 1 }
        }
        return ans + target - 1
    }
}
