// LeetCode 3178 - Find the Child Who Has the Ball After K Seconds
// https://leetcode.com/problems/find-the-child-who-has-the-ball-after-k-seconds/

public class Solution {
    public int NumberOfChild(int n, int k) {
        int mod = k % (n - 1);
        k /= (n - 1);
        if (k % 2 == 1) return n - mod - 1;
        return mod;
    }
}
