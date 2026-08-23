// LeetCode 2355 - Maximum Number of Books You Can Take
// https://leetcode.com/problems/maximum-number-of-books-you-can-take/

#include <vector>

class Solution {
public:
    long long maximumBooks(std::vector<int>& books) {
        int n = (int)books.size();
        std::vector<long long> dp(n);
        std::vector<int> stack;
        long long ans = 0;
        auto sum = [](int l, int r, int h) -> long long {
            int width = r - l + 1;
            if (h >= width) return 1LL * width * (2LL * h - width + 1) / 2;
            return 1LL * h * (h + 1) / 2;
        };
        for (int i = 0; i < n; i++) {
            while (!stack.empty() && books[stack.back()] >= books[i] - (i - stack.back())) {
                stack.pop_back();
            }
            if (stack.empty()) {
                dp[i] = sum(0, i, books[i]);
            } else {
                int j = stack.back();
                dp[i] = dp[j] + sum(j + 1, i, books[i]);
            }
            if (dp[i] > ans) ans = dp[i];
            stack.push_back(i);
        }
        return ans;
    }
};
