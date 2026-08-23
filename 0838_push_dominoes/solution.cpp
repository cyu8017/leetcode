// LeetCode 0838 - Push Dominoes
// https://leetcode.com/problems/push-dominoes/

#include <algorithm>
#include <string>
#include <vector>

class Solution {
public:
    std::string pushDominoes(std::string dominoes) {
        int n = static_cast<int>(dominoes.size());
        std::vector<int> force(n, 0);
        int f = 0;
        for (int i = 0; i < n; ++i) {
            if (dominoes[i] == 'R') {
                f = n;
            } else if (dominoes[i] == 'L') {
                f = 0;
            } else {
                f = std::max(f - 1, 0);
            }
            force[i] += f;
        }
        f = 0;
        for (int i = n - 1; i >= 0; --i) {
            if (dominoes[i] == 'L') {
                f = n;
            } else if (dominoes[i] == 'R') {
                f = 0;
            } else {
                f = std::max(f - 1, 0);
            }
            force[i] -= f;
        }
        for (int i = 0; i < n; ++i) {
            if (force[i] > 0) {
                dominoes[i] = 'R';
            } else if (force[i] < 0) {
                dominoes[i] = 'L';
            } else {
                dominoes[i] = '.';
            }
        }
        return dominoes;
    }
};
