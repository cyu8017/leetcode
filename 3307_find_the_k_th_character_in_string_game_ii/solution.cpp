// LeetCode 3307 - Find the K-th Character in String Game II
// https://leetcode.com/problems/find-the-k-th-character-in-string-game-ii/

#include <cstdint>
#include <vector>

class Solution {
public:
    char kthCharacter(long long k, std::vector<int>& operations) {
        int shift = 0;
        std::vector<int> ops = operations;
        while (!ops.empty()) {
            int op = ops.back();
            ops.pop_back();
            long long half = 1LL << (int)ops.size();
            if (k > half) {
                k -= half;
                if (op == 1) shift++;
            }
        }
        return char('a' + shift % 26);
    }
};
