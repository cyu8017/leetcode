// LeetCode 0781 - Rabbits in Forest
// https://leetcode.com/problems/rabbits-in-forest/

import java.util.*;

class Solution {
    public int numRabbits(int[] answers) {
        Map<Integer, Integer> counts = new HashMap<>();
        for (int answer : answers) counts.merge(answer, 1, Integer::sum);
        int total = 0;
        for (Map.Entry<Integer, Integer> e : counts.entrySet()) {
            int group = e.getKey() + 1;
            int groups = (e.getValue() + group - 1) / group;
            total += groups * group;
        }
        return total;
    }
}
