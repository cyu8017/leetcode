// LeetCode 2582 - Pass the Pillow
// https://leetcode.com/problems/pass-the-pillow/

class Solution {
public:
    int passThePillow(int n, int time) {
        int cycle = 2 * (n - 1);
        int t = time % cycle;
        if (t < n) return 1 + t;
        return n - (t - (n - 1));
    }
};
