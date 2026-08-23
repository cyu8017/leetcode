// LeetCode 3752 - Lexicographically Smallest Negated Permutation that Sums to Target
// https://leetcode.com/problems/lexicographically-smallest-negated-permutation-that-sums-to-target/

#include <vector>

class Solution {
public:
    std::vector<int> lexicographicallySmallest(int n, long long target) {
        long long total = 1LL * n * (n + 1) / 2;
        if (target < -total || target > total || (total - target) % 2 != 0) return {};
        long long remaining = (total - target) / 2;
        std::vector<bool> negative(n + 1, false);
        for (int value = n; value >= 1; value--) {
            if (value <= remaining) {
                negative[value] = true;
                remaining -= value;
            }
        }
        std::vector<int> answer;
        for (int value = n; value >= 1; value--) {
            if (negative[value]) answer.push_back(-value);
        }
        for (int value = 1; value <= n; value++) {
            if (!negative[value]) answer.push_back(value);
        }
        return answer;
    }
};
