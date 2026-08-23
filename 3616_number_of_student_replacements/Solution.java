// LeetCode 3616 - Number of Student Replacements
// https://leetcode.com/problems/number-of-student-replacements/

class Solution {
    public int totalReplacements(int[] ranks) {
        int ans = 0, cur = ranks[0];
        for (int x : ranks) {
            if (x < cur) {
                cur = x;
                ans++;
            }
        }
        return ans;
    }
}
