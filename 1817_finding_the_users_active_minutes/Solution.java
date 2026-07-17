// LeetCode 1817 - Finding the Users Active Minutes
// https://leetcode.com/problems/finding-the-users-active-minutes/

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

class Solution {
    public int[] findingUsersActiveMinutes(int[][] logs, int k) {
        Map<Integer, Set<Integer>> userMinutes = new HashMap<>();
        for (int[] log : logs) {
            userMinutes.computeIfAbsent(log[0], ignored -> new HashSet<>()).add(log[1]);
        }

        int[] answer = new int[k];
        for (Set<Integer> minutes : userMinutes.values()) {
            int uam = minutes.size();
            if (uam <= k) {
                answer[uam - 1]++;
            }
        }
        return answer;
    }
}
