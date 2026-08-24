// LeetCode 2139 - Minimum Moves to Reach Target Score
// https://leetcode.com/problems/minimum-moves-to-reach-target-score/

class Solution {
    fun minMoves(target: Int, maxDoubles: Int): Int {
        var ans: Int = 0
        while (target > 1 && maxDoubles > 0) {
            if (target % 2 != 0) { target--; ans++; }
            else { target /= 2; maxDoubles--; ans++; }
        }
        return ans + target - 1
    }
}
