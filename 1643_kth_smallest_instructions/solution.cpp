// LeetCode 1643 - Kth Smallest Instructions
// https://leetcode.com/problems/kth-smallest-instructions/

#include <string>
#include <vector>

class Solution {
    static long long comb(int n, int k) {
        if (k < 0 || k > n) {
            return 0;
        }
        long long r = 1;
        for (int i = 1; i <= k; ++i) {
            r = r * (n - k + i) / i;
        }
        return r;
    }

public:
    std::string kthSmallestPath(std::vector<int>& destination, int k) {
        int v = destination[0], h = destination[1];
        std::string ans;
        while (h + v) {
            if (h) {
                const long long count = comb(h + v - 1, v);
                if (k <= count) {
                    ans.push_back('H');
                    --h;
                    continue;
                }
                k -= static_cast<int>(count);
            }
            ans.push_back('V');
            --v;
        }
        return ans;
    }
};
