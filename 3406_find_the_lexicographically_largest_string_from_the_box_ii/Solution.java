// LeetCode 3406 - Find the Lexicographically Largest String From the Box II
// https://leetcode.com/problems/find-the-lexicographically-largest-string-from-the-box-ii/

class Solution {
    public String answerString(String word, int numFriends) {
        if (numFriends == 1) return word;
        int n = word.length();
        int maxLen = n - (numFriends - 1);
        String ans = "";
        for (int i = 0; i < n; i++) {
            int end = i + maxLen;
            if (end > n) end = n;
            String cand = word.substring(i, end);
            if (cand.compareTo(ans) > 0) ans = cand;
        }
        return ans;
    }
}
