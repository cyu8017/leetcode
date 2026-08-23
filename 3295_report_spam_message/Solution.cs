// LeetCode 3295 - Report Spam Message
// https://leetcode.com/problems/report-spam-message/

using System.Collections.Generic;

public class Solution {
    public bool ReportSpam(string[] message, string[] bannedWords) {
        var ban = new HashSet<string>(bannedWords);
        int cnt = 0;
        foreach (string w in message) {
            if (ban.Contains(w)) {
                cnt++;
                if (cnt >= 2) return true;
            }
        }
        return false;
    }
}
