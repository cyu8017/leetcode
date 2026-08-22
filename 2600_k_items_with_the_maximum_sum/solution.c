// LeetCode 2600 - K Items With the Maximum Sum
// https://leetcode.com/problems/k-items-with-the-maximum-sum/

int kItemsWithMaximumSum(int numOnes, int numZeros, int numNegOnes, int k) {
    int ans = 0;
    int take = numOnes < k ? numOnes : k;
    ans += take; k -= take;
    take = numZeros < k ? numZeros : k;
    k -= take;
    take = numNegOnes < k ? numNegOnes : k;
    ans -= take;
    return ans;
}
