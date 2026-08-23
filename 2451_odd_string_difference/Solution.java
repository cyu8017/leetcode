// LeetCode 2451 - Odd String Difference
// https://leetcode.com/problems/odd-string-difference/

class Solution {
    public String oddString(String[] words) {
        String diff(String w) {
            var b = new StringBuilder();
            for (int i = 1; i < w.length(); i++) {
                int d = w.charAt(i) - w.charAt(i - 1);
                b.append((char)(d + 128));
                b.append(',');
            }
            return b.toString();
        }
        String d0 = Diff(words[0]), d1 = Diff(words[1]);
        if (d0 == d1) {
            for (int i = 2; i < words.length; i++) {
                if (Diff(words[i]) != d0) return words[i];
            }
        }
        if (Diff(words[2]) == d0) return words[1];
        return words[0];
    }
}
