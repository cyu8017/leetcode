// LeetCode 1234 - Replace the Substring for Balanced String
// https://leetcode.com/problems/replace-the-substring-for-balanced-string/

class Solution {
    public int balancedString(String s) {
        int[] count = new int[128];
        for (char ch : s.toCharArray()) count[ch]++;
        int limit = s.length() / 4;
        int n = s.length(), left = 0, answer = n;
        for (int right = 0; right < n; right++) {
            count[s.charAt(right)]--;
            while (left < n && count['Q'] <= limit && count['W'] <= limit
                    && count['E'] <= limit && count['R'] <= limit) {
                answer = Math.min(answer, right - left + 1);
                count[s.charAt(left)]++;
                left++;
            }
        }
        return answer;
    }
}

