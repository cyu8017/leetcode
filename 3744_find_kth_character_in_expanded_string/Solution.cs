// LeetCode 3744 - Find Kth Character in Expanded String
// https://leetcode.com/problems/find-kth-character-in-expanded-string/

public class Solution {
    public char KthCharacter(string s, long k) {
        string[] words = s.Split(new[] { ' ' }, System.StringSplitOptions.RemoveEmptyEntries);
        foreach (string w in words) {
            long m = (1 + (long)w.Length) * (long)w.Length / 2;
            if (k == m) return ' ';
            if (k > m) {
                k -= m + 1;
            } else {
                long cur = 0;
                for (int i = 0; ; i++) {
                    cur += i + 1;
                    if (k < cur) return w[i];
                }
            }
        }
        return ' ';
    }
}
