// LeetCode 0765 - Couples Holding Hands
// https://leetcode.com/problems/couples-holding-hands/

using System.Collections.Generic;

public class Solution {
    public int MinSwapsCouples(int[] row) {
        var pos = new Dictionary<int, int>();
        for (int i = 0; i < row.Length; i++) pos[row[i]] = i;
        int swaps = 0;
        for (int i = 0; i < row.Length; i += 2) {
            int partner = row[i] ^ 1;
            if (row[i + 1] == partner) continue;
            int j = pos[partner];
            pos[row[i + 1]] = j;
            row[j] = row[i + 1];
            row[i + 1] = partner;
            pos[partner] = i + 1;
            swaps++;
        }
        return swaps;
    }
}
