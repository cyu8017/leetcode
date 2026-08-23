// LeetCode 2910 - Minimum Number of Groups to Create a Valid Assignment
// https://leetcode.com/problems/minimum-number-of-groups-to-create-a-valid-assignment/

using System.Collections.Generic;

public class Solution {
    public int MinGroupsForValidAssignment(int[] balls) {
        var freq = new Dictionary<int, int>();
        foreach (int b in balls) {
            if (!freq.ContainsKey(b)) freq[b] = 0;
            freq[b]++;
        }
        var counts = new List<int>();
        int minF = 1 << 30;
        foreach (var f in freq.Values) {
            counts.Add(f);
            if (f < minF) minF = f;
        }
        for (int size = minF; size >= 1; size--) {
            bool ok = true;
            int groups = 0;
            foreach (int c in counts) {
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
        return balls.Length;
    }
}
