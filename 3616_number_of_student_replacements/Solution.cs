// LeetCode 3616 - Number of Student Replacements
// https://leetcode.com/problems/number-of-student-replacements/

public class Solution {
    public int TotalReplacements(int[] ranks) {
        int ans = 0, cur = ranks[0];
        foreach (int x in ranks) {
            if (x < cur) {
                cur = x;
                ans++;
            }
        }
        return ans;
    }
}
