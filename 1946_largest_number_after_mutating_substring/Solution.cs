// LeetCode 1946 - Largest Number After Mutating Substring
// https://leetcode.com/problems/largest-number-after-mutating-substring/

public class Solution {
    public string MaximumNumber(string num, int[] change) {
        var chars = num.ToCharArray();
        bool started = false;
        for (int i = 0; i < chars.Length; i++) {
            int d = chars[i] - '0';
            int mapped = change[d];
            if (mapped > d) {
                chars[i] = (char)('0' + mapped);
                started = true;
            } else if (mapped < d && started) break;
        }
        return new string(chars);
    }
}