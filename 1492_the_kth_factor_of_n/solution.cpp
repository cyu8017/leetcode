class Solution {
public:
    int kthFactor(int n, int k) {
        for (int x = 1; x <= n; ++x) {
            if (n % x == 0) {
                if (--k == 0) return x;
            }
        }
        return -1;
    }
};
