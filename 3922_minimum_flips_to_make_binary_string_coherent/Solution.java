// LeetCode 3922 - Minimum Flips to Make Binary String Coherent
// https://leetcode.com/problems/minimum-flips-to-make-binary-string-coherent/

class Solution {
    public int minFlips(String s) {
        int ones = 0;
        for (char c : s.toCharArray()) if (c == '1') ones++;
        int answer = ones;
        if (ones > 0) answer = ones - 1;
        int zeros = s.length() - ones;
        answer = Math.min(answer, zeros);
        if (s.length() >= 2) {
            int cost = 0;
            for (int i = 0; i < s.length(); i++) {
                char want = (i == 0 || i == s.length() - 1) ? '1' : '0';
                if (s.charAt(i) != want) cost++;
            }
            answer = Math.min(answer, cost);
        }
        return answer;
    }
}
