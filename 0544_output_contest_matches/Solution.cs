// LeetCode 0544 - Output Contest Matches
// https://leetcode.com/problems/output-contest-matches/

using System.Collections.Generic;

public class Solution {
    public string FindContestMatch(int n) {
        List<string> teams = new List<string>();
        for (int i = 1; i <= n; i++) {
            teams.Add(i.ToString());
        }

        while (teams.Count > 1) {
            List<string> nextRound = new List<string>();
            for (int i = 0; i < teams.Count / 2; i++) {
                nextRound.Add("(" + teams[i] + "," + teams[teams.Count - 1 - i] + ")");
            }
            teams = nextRound;
        }

        return teams[0];
    }
}
