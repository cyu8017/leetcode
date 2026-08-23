// LeetCode 2086 - Minimum Number of Food Buckets to Feed the Hamsters
// https://leetcode.com/problems/minimum-number-of-food-buckets-to-feed-the-hamsters/

class Solution {
    public int minimumBuckets(String hamsters) {
        char[] b = hamsters.toCharArray();
        int ans = 0;
        for (int i = 0; i < b.length; i++) {
            if (b[i] != 'H') continue;
            if (i > 0 && b[i - 1] == 'B') continue;
            if (i + 1 < b.length && b[i + 1] == '.') { b[i + 1] = 'B'; ans++; }
            else if (i > 0 && b[i - 1] == '.') { b[i - 1] = 'B'; ans++; }
            else return -1;
        }
        return ans;
    }
}
