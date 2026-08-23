// LeetCode 3114 - Latest Time You Can Obtain After Replacing Characters
// https://leetcode.com/problems/latest-time-you-can-obtain-after-replacing-characters/

class Solution {
    public String findLatestTime(String s) {
        for (int h = 11; ; h--) {
            for (int m = 59; m >= 0; m--) {
                String t = String.format("%02d:%02d", h, m);
                boolean ok = true;
                for (int i = 0; i < 5; i++) {
                    if (s.charAt(i) != '?' && s.charAt(i) != t.charAt(i)) {
                        ok = false;
                        break;
                    }
                }
                if (ok) return t;
            }
        }
    }
}
