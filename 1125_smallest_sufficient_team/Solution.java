// LeetCode 1125 - Smallest Sufficient Team
// https://leetcode.com/problems/smallest-sufficient-team/

import java.util.*;

class Solution {
    public int[] smallestSufficientTeam(String[] req_skills, List<List<String>> people) {
        Map<String, Integer> skillId = new HashMap<>();
        for (int i = 0; i < req_skills.length; i++) skillId.put(req_skills[i], i);
        int n = people.size();
        int[] personMasks = new int[n];
        for (int i = 0; i < n; i++) {
            int mask = 0;
            for (String skill : people.get(i)) mask |= 1 << skillId.get(skill);
            personMasks[i] = mask;
        }
        int target = (1 << req_skills.length) - 1;
        int[] teamMask = new int[1 << req_skills.length];
        int[] teamSize = new int[1 << req_skills.length];
        Arrays.fill(teamSize, Integer.MAX_VALUE);
        teamSize[0] = 0;
        for (int state = 0; state <= target; state++) {
            if (teamSize[state] == Integer.MAX_VALUE) continue;
            for (int i = 0; i < n; i++) {
                int next = state | personMasks[i];
                if (teamSize[next] > teamSize[state] + 1) {
                    teamSize[next] = teamSize[state] + 1;
                    teamMask[next] = teamMask[state] | (1 << i);
                }
            }
        }
        List<Integer> team = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            if (((teamMask[target] >> i) & 1) == 1) team.add(i);
        }
        int[] ans = new int[team.size()];
        for (int i = 0; i < team.size(); i++) ans[i] = team.get(i);
        return ans;
    }
}
