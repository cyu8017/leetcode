// LeetCode 1987 - Number of Unique Good Subsequences
#include <string>

class Solution {
public:
    int numberOfUniqueGoodSubsequences(std::string binary) {
        const int MOD = 1000000007;
        long long ends0 = 0, ends1 = 0;
        bool has0 = false;
        for (char ch : binary) {
            if (ch == '0') {
                has0 = true;
                ends0 = (ends0 + ends1) % MOD;
            } else {
                ends1 = (ends0 + ends1 + 1) % MOD;
            }
        }
        return (int)((ends0 + ends1 + (has0 ? 1 : 0)) % MOD);
    }
};
