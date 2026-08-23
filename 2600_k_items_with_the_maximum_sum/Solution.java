// LeetCode 2600 - K Items With the Maximum Sum
// https://leetcode.com/problems/k-items-with-the-maximum-sum/

class Solution {
    public int kItemsWithMaximumSum(int numOnes, int numZeros, int numNegOnes, int k) {
        int ans = 0;
        int take = Math.min(numOnes, k);
        ans += take;
        k -= take;
        take = Math.min(numZeros, k);
        k -= take;
        take = Math.min(numNegOnes, k);
        ans -= take;
        return ans;
    }
}
