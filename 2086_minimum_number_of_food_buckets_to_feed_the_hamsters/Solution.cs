// LeetCode 2086 - Minimum Number of Food Buckets to Feed the Hamsters
// https://leetcode.com/problems/minimum-number-of-food-buckets-to-feed-the-hamsters/

public class Solution {
    public int MinimumBuckets(string hamsters) {
        char[] b = hamsters.ToCharArray();
        int ans = 0;
        for (int i = 0; i < b.Length; i++) {
            if (b[i] != 'H') continue;
            if (i > 0 && b[i - 1] == 'B') continue;
            if (i + 1 < b.Length && b[i + 1] == '.') { b[i + 1] = 'B'; ans++; }
            else if (i > 0 && b[i - 1] == '.') { b[i - 1] = 'B'; ans++; }
            else return -1;
        }
        return ans;
    }
}
