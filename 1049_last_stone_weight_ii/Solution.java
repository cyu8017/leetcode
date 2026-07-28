// LeetCode 1049 - Last Stone Weight II
// https://leetcode.com/problems/last-stone-weight-ii/

import java.util.HashSet;
import java.util.Set;

class Solution {
    public int lastStoneWeightII(int[] stones) {
        int total = 0;
        for (int s : stones) total += s;
        Set<Integer> reachable = new HashSet<>();
        reachable.add(0);
        for (int stone : stones) {
            Set<Integer> next = new HashSet<>();
            for (int s : reachable) {
                next.add(s);
                next.add(s + stone);
            }
            reachable = next;
        }
        int best = total;
        for (int s : reachable) best = Math.min(best, Math.abs(total - 2 * s));
        return best;
    }
}
