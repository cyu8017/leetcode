// LeetCode 2600 - K Items With the Maximum Sum
// https://leetcode.com/problems/k-items-with-the-maximum-sum/

using System;

public class Solution {
    public int KItemsWithMaximumSum(int numOnes, int numZeros, int numNegOnes, int k) {
        int ans = 0;
        int take = Math.Min(numOnes, k);
        ans += take;
        k -= take;
        take = Math.Min(numZeros, k);
        k -= take;
        take = Math.Min(numNegOnes, k);
        ans -= take;
        return ans;
    }
}
