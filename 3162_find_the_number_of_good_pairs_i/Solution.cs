// LeetCode 3162 - Find the Number of Good Pairs I
// https://leetcode.com/problems/find-the-number-of-good-pairs-i/

public class Solution {
    public int NumberOfPairs(int[] nums1, int[] nums2, int k) {
        int ans = 0;
        foreach (int x in nums1)
            foreach (int y in nums2)
                if (x % (y * k) == 0) ans++;
        return ans;
    }
}
