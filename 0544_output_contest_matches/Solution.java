// LeetCode 0544 - Output Contest Matches
// https://leetcode.com/problems/output-contest-matches/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public String findContestMatch(int n) {
        List<String> teams = new ArrayList<>();
        for (int i = 1; i <= n; i++) {
            teams.add(String.valueOf(i));
        }

        while (teams.size() > 1) {
            List<String> nextRound = new ArrayList<>();
            for (int i = 0; i < teams.size() / 2; i++) {
                nextRound.add("(" + teams.get(i) + "," + teams.get(teams.size() - 1 - i) + ")");
            }
            teams = nextRound;
        }

        return teams.get(0);
    }
}
