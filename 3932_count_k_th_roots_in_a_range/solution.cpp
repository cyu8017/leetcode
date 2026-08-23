// LeetCode 3932 - Count K Th Roots In A Range
// https://leetcode.com/problems/count-k-th-roots-in-a-range/

class Solution {
public:
    int countKthRoots(int l, int r, int k) {
        if (k == 1) return r - l + 1;
        int ans = 0;
        for (long long x = 0;; x++) {
            long long y = 1;
            bool tooBig = false;
            for (int i = 0; i < k; i++) {
                if (x != 0 && y > (long long)r / x) {
                    tooBig = true;
                    break;
                }
                y *= x;
                if (y > r) break;
            }
            if (tooBig || y > r) break;
            if (l <= y && y <= r) ans++;
        }
        return ans;
    }
};
