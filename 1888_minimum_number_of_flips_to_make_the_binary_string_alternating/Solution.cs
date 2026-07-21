// LeetCode 1888 - Minimum Number of Flips to Make the Binary String Alternating
// https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/

public class Solution {
    public int MinFlips(string s) {
        int n = s.Length;
        string doubled = s + s;
        int alt0 = 0;
        int alt1 = 0;
        for (int i = 0; i < n; i++) {
            char expect0 = i % 2 == 0 ? '0' : '1';
            char expect1 = i % 2 == 0 ? '1' : '0';
            if (doubled[i] != expect0) {
                alt0++;
            }
            if (doubled[i] != expect1) {
                alt1++;
            }
        }
        int answer = Math.Min(alt0, alt1);
        for (int i = 0; i < n; i++) {
            char expect0i = i % 2 == 0 ? '0' : '1';
            char expect0n = (i + n) % 2 == 0 ? '0' : '1';
            if (doubled[i] != expect0i) {
                alt0--;
            }
            if (doubled[i + n] != expect0n) {
                alt0++;
            }

            char expect1i = i % 2 == 0 ? '1' : '0';
            char expect1n = (i + n) % 2 == 0 ? '1' : '0';
            if (doubled[i] != expect1i) {
                alt1--;
            }
            if (doubled[i + n] != expect1n) {
                alt1++;
            }

            answer = Math.Min(answer, Math.Min(alt0, alt1));
        }
        return answer;
    }
}
