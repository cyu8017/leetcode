// LeetCode 2910 - Minimum Number of Groups to Create a Valid Assignment
// https://leetcode.com/problems/minimum-number-of-groups-to-create-a-valid-assignment/

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    public int minGroupsForValidAssignment(int[] balls) {
        Map<Integer, Integer> freq = new HashMap<>();
        for (int b : balls) freq.merge(b, 1, Integer::sum);
        List<Integer> counts = new ArrayList<>();
        int minF = 1 << 30;
        for (int f : freq.values()) {
            counts.add(f);
            if (f < minF) minF = f;
        }
        for (int size = minF; size >= 1; size--) {
            boolean ok = true;
            int groups = 0;
            for (int c : counts) {
                int rem = c % (size + 1);
                int g2 = c / (size + 1);
                if (rem == 0) groups += g2;
                else if (size - rem <= g2) groups += g2 + 1;
                else {
                    ok = false;
                    break;
                }
            }
            if (ok) return groups;
        }
        return balls.length;
    }
}
