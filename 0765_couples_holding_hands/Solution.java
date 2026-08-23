// LeetCode 0765 - Couples Holding Hands
// https://leetcode.com/problems/couples-holding-hands/

import java.util.*;

class Solution {
    public int minSwapsCouples(int[] row) {
        Map<Integer, Integer> pos = new HashMap<>();
        for (int i = 0; i < row.length; i++) pos.put(row[i], i);
        int swaps = 0;
        for (int i = 0; i < row.length; i += 2) {
            int partner = row[i] ^ 1;
            if (row[i + 1] == partner) continue;
            int j = pos.get(partner);
            pos.put(row[i + 1], j);
            row[j] = row[i + 1];
            row[i + 1] = partner;
            pos.put(partner, i + 1);
            swaps++;
        }
        return swaps;
    }
}
