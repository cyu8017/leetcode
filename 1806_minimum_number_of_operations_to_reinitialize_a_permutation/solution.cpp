// LeetCode 1806 - Minimum Number of Operations to Reinitialize a Permutation
// https://leetcode.com/problems/minimum-number-of-operations-to-reinitialize-a-permutation/

#include <vector>

class Solution {
public:
    int reinitializePermutation(int n) {
        std::vector<int> perm(n);
        for (int i = 0; i < n; ++i) {
            perm[i] = i;
        }
        std::vector<int> target = perm;
        int operations = 0;
        while (true) {
            std::vector<int> newPerm(n);
            for (int i = 0; i < n; ++i) {
                if (i % 2 == 0) {
                    newPerm[i] = perm[i / 2];
                } else {
                    newPerm[i] = perm[n / 2 + (i - 1) / 2];
                }
            }
            perm = std::move(newPerm);
            ++operations;
            if (perm == target) {
                return operations;
            }
        }
    }
};
