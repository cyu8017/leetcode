// LeetCode 3295 - Report Spam Message
// https://leetcode.com/problems/report-spam-message/

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

class Solution {
    public boolean reportSpam(String[] message, String[] bannedWords) {
        Set<String> ban = new HashSet<>(Arrays.asList(bannedWords));
        int cnt = 0;
        for (String w : message) {
            if (ban.contains(w)) {
                cnt++;
                if (cnt >= 2) return true;
            }
        }
        return false;
    }
}
