// LeetCode 2350 - Shortest Impossible Sequence of Rolls
// https://leetcode.com/problems/shortest-impossible-sequence-of-rolls/

import java.util.HashSet;
import java.util.Set;

class Solution {
    public int shortestSequence(int[] rolls, int k) {
        var seen = new HashSet<>();
        int ans = 1;
        for (int r : rolls) {
            seen.add(r);
            if (seen.size() == k) {
                ans++;
                seen.clear();
            }
        }
        return ans;
    }
}
