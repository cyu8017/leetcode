// LeetCode 1217 - Minimum Cost to Move Chips to The Same Position
// https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/

using System.Linq;

public class Solution {
    public int MinCostToMoveChips(int[] position) {
        int odd = position.Count(x => (x & 1) == 1);
        return System.Math.Min(odd, position.Length - odd);
    }
}
