// LeetCode 1888 - Minimum Number of Flips to Make the Binary String Alternating
// https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/

class Solution {
    public int minFlips(String s) {
        int n = s.length();
        char[] doubled = (s + s).toCharArray();
        int alt0 = 0;
        int alt1 = 0;

        for (int i = 0; i < n; i++) {
            if (doubled[i] != (i % 2 == 0 ? '0' : '1')) {
                alt0++;
            }
            if (doubled[i] != (i % 2 == 0 ? '1' : '0')) {
                alt1++;
            }
        }

        int answer = Math.min(alt0, alt1);
        for (int i = 0; i < n; i++) {
            if (doubled[i] != (i % 2 == 0 ? '0' : '1')) {
                alt0--;
            }
            if (doubled[i + n] != ((i + n) % 2 == 0 ? '0' : '1')) {
                alt0++;
            }

            if (doubled[i] != (i % 2 == 0 ? '1' : '0')) {
                alt1--;
            }
            if (doubled[i + n] != ((i + n) % 2 == 0 ? '1' : '0')) {
                alt1++;
            }

            answer = Math.min(answer, Math.min(alt0, alt1));
        }
        return answer;
    }
}
