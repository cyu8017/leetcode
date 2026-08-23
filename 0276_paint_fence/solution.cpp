// LeetCode 0276 - Paint Fence
// https://leetcode.com/problems/paint-fence/

class Solution {
public:
    int numWays(int n, int k) {
        if (n == 0) {
            return 0;
        }
        if (n == 1) {
            return k;
        }
        if (n == 2) {
            return k * k;
        }
        int prev2 = k;
        int prev1 = k * k;
        for (int i = 3; i <= n; i++) {
            int next = (prev1 + prev2) * (k - 1);
            prev2 = prev1;
            prev1 = next;
        }
        return prev1;
    }
};
