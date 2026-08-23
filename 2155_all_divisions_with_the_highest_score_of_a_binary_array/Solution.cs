// LeetCode 2155 - All Divisions With the Highest Score of a Binary Array
// https://leetcode.com/problems/all-divisions-with-the-highest-score-of-a-binary-array/

public class Solution {
    public IList<int> MaxScoreIndices(int[] nums) {
        int n = nums.Length;
        int total1 = 0;
        foreach (int x in nums) total1 += x;
        int best = total1, left0 = 0, right1 = total1;
        var ans = new List<int> { 0 };
        for (int i = 0; i < n; i++) {
            if (nums[i] == 0) left0++;
            else right1--;
            int score = left0 + right1;
            if (score > best) { best = score; ans = new List<int> { i + 1 }; }
            else if (score == best) ans.Add(i + 1);
        }
        return ans;
    }
}
