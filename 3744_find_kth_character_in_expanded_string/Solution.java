// LeetCode 3744 - Find Kth Character in Expanded String
// https://leetcode.com/problems/find-kth-character-in-expanded-string/

class Solution {
    public char kthCharacter(String s, long k) {
        String[] words = s.trim().split("\s+");
        for (String w : words) {
            long m = (1 + (long)w.length()) * (long)w.length() / 2;
            if (k == m) return ' ';
            if (k > m) {
                k -= m + 1;
            } else {
                long cur = 0;
                for (int i = 0; ; i++) {
                    cur += i + 1;
                    if (k < cur) return w.charAt(i);
                }
            }
        }
        return ' ';
    }
}
