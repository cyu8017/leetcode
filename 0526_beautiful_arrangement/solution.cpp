// LeetCode 0526 - Beautiful Arrangement
// https://leetcode.com/problems/beautiful-arrangement/

#include <vector>

class Solution {
    int count_ = 0;

    void backtrack(int index, int n, std::vector<bool>& used) {
        if (index == n + 1) {
            ++count_;
            return;
        }
        for (int num = 1; num <= n; ++num) {
            if (used[num]) {
                continue;
            }
            if (index % num == 0 || num % index == 0) {
                used[num] = true;
                backtrack(index + 1, n, used);
                used[num] = false;
            }
        }
    }

public:
    int countArrangement(int n) {
        count_ = 0;
        std::vector<bool> used(n + 1, false);
        backtrack(1, n, used);
        return count_;
    }
};
