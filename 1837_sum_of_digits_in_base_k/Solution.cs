// LeetCode 1837 - Sum of Digits in Base K
// https://leetcode.com/problems/sum-of-digits-in-base-k/

public class Solution {
    public int SumBase(int n, int k) {
        int total = 0;
        while (n > 0) {
            total += n % k;
            n /= k;
        }
        return total;
    }
}
