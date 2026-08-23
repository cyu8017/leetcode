// LeetCode 2582 - Pass the Pillow
// https://leetcode.com/problems/pass-the-pillow/

public class Solution {
    public int PassThePillow(int n, int time) {
        int cycle = 2 * (n - 1);
        int t = time % cycle;
        if (t < n) return 1 + t;
        return n - (t - (n - 1));
    }
}
