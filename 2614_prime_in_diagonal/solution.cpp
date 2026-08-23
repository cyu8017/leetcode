// LeetCode 2614 - Prime In Diagonal
// https://leetcode.com/problems/prime-in-diagonal/

#include <vector>

class Solution {
public:
    int diagonalPrime(std::vector<std::vector<int>>& nums) {
        auto isPrime = [](int x) {
            if (x < 2) return false;
            for (int i = 2; i * i <= x; ++i) if (x % i == 0) return false;
            return true;
        };
        int n = (int)nums.size();
        int best = 0;
        for (int i = 0; i < n; ++i) {
            for (int v : {nums[i][i], nums[i][n - 1 - i]}) {
                if (isPrime(v) && v > best) best = v;
            }
        }
        return best;
    }
};
