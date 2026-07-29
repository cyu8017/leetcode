// LeetCode 1955 - Count Number of Special Subsequences
#include <vector>

class Solution {
public:
    int countSpecialSubsequences(std::vector<int>& nums) {
        const int MOD = 1000000007;
        long long a = 0, b = 0, c = 0;
        for (int x : nums) {
            if (x == 0) a = (a * 2 + 1) % MOD;
            else if (x == 1) b = (b * 2 + a) % MOD;
            else c = (c * 2 + b) % MOD;
        }
        return (int)c;
    }
};
