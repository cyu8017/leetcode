// LeetCode 2761 - Prime Pairs With Target Sum
// https://leetcode.com/problems/prime-pairs-with-target-sum/

#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> findPrimePairs(int n) {
        std::vector<bool> isPrime(n + 1, false);
        for (int i = 2; i <= n; i++) isPrime[i] = true;
        for (int i = 2; i * i <= n; i++) {
            if (isPrime[i]) {
                for (int j = i * i; j <= n; j += i) isPrime[j] = false;
            }
        }
        std::vector<std::vector<int>> ans;
        for (int x = 2; x <= n / 2; x++) {
            int y = n - x;
            if (isPrime[x] && isPrime[y]) ans.push_back({x, y});
        }
        return ans;
    }
};
