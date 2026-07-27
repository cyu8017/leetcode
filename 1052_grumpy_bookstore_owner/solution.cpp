// LeetCode 1052 - Grumpy Bookstore Owner
// https://leetcode.com/problems/grumpy-bookstore-owner/

#include <algorithm>
#include <vector>

class Solution {
public:
    int maxSatisfied(std::vector<int>& customers, std::vector<int>& grumpy, int minutes) {
        int base = 0;
        for (size_t i = 0; i < customers.size(); ++i) {
            if (grumpy[i] == 0) {
                base += customers[i];
            }
        }
        int gain = 0;
        int best = 0;
        for (size_t i = 0; i < customers.size(); ++i) {
            if (grumpy[i]) {
                gain += customers[i];
            }
            if (static_cast<int>(i) >= minutes && grumpy[i - minutes]) {
                gain -= customers[i - minutes];
            }
            best = std::max(best, gain);
        }
        return base + best;
    }
};
