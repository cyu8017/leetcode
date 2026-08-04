// LeetCode 1217 - Minimum Cost to Move Chips to The Same Position
// https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/

class Solution {
    public int minCostToMoveChips(int[] position) {
        int odd = 0;
        for (int x : position) {
            if ((x & 1) == 1) odd++;
        }
        return Math.min(odd, position.length - odd);
    }
}
