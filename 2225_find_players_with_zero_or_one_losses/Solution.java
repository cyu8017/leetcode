// LeetCode 2225 - Find Players With Zero or One Losses
// https://leetcode.com/problems/find-players-with-zero-or-one-losses/

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

class Solution {
    public List<List<Integer>> findWinners(int[][] matches) {
        Map<Integer, Integer> lose = new HashMap<>();
        Set<Integer> seen = new HashSet<>();
        for (int[] m : matches) {
            seen.add(m[0]);
            seen.add(m[1]);
            lose.put(m[1], lose.getOrDefault(m[1], 0) + 1);
        }
        List<Integer> zero = new ArrayList<>();
        List<Integer> one = new ArrayList<>();
        for (int p : seen) {
            int L = lose.getOrDefault(p, 0);
            if (L == 0) zero.add(p);
            else if (L == 1) one.add(p);
        }
        Collections.sort(zero);
        Collections.sort(one);
        List<List<Integer>> ans = new ArrayList<>();
        ans.add(zero);
        ans.add(one);
        return ans;
    }
}
