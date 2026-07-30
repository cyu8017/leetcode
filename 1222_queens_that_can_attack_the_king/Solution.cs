// LeetCode 1222 - Queens That Can Attack the King
// https://leetcode.com/problems/queens-that-can-attack-the-king/

using System.Collections.Generic;

public class Solution {
    public IList<IList<int>> QueensAttacktheKing(int[][] queens, int[] king) {
        var occupied = new HashSet<(int, int)>();
        foreach (var q in queens) occupied.Add((q[0], q[1]));
        var answer = new List<IList<int>>();
        int[] dirs = { -1, 0, 1 };
        foreach (int dr in dirs) {
            foreach (int dc in dirs) {
                if (dr == 0 && dc == 0) continue;
                int r = king[0] + dr, c = king[1] + dc;
                while (r >= 0 && r < 8 && c >= 0 && c < 8) {
                    if (occupied.Contains((r, c))) {
                        answer.Add(new int[] { r, c });
                        break;
                    }
                    r += dr;
                    c += dc;
                }
            }
        }
        return answer;
    }
}
