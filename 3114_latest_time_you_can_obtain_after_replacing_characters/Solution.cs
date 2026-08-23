// LeetCode 3114 - Latest Time You Can Obtain After Replacing Characters
// https://leetcode.com/problems/latest-time-you-can-obtain-after-replacing-characters/

public class Solution {
    public string FindLatestTime(string s) {
        for (int h = 11; ; h--) {
            for (int m = 59; m >= 0; m--) {
                string t = $"{h:D2}:{m:D2}";
                bool ok = true;
                for (int i = 0; i < 5; i++) {
                    if (s[i] != '?' && s[i] != t[i]) {
                        ok = false;
                        break;
                    }
                }
                if (ok) return t;
            }
        }
    }
}
