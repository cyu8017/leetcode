// LeetCode 2249 - Count Lattice Points Inside a Circle
// https://leetcode.com/problems/count-lattice-points-inside-a-circle/

import java.util.HashSet;
import java.util.Set;

class Solution {
    public int countLatticePoints(int[][] circles) {
        Set<Long> seen = new HashSet<>();
        for (int[] c : circles) {
            int x = c[0], y = c[1], r = c[2];
            for (int i = x - r; i <= x + r; i++)
                for (int j = y - r; j <= y + r; j++)
                    if ((i - x) * (i - x) + (j - y) * (j - y) <= r * r)
                        seen.add(((long) i << 32) | (j & 0xffffffffL));
        }
        return seen.size();
    }
}
