// LeetCode 1960 - Maximum Product of the Length of Two Palindromic Substrings
#include <algorithm>
#include <string>
#include <vector>

class Solution {
public:
    long long maxProduct(std::string s) {
        int n = (int)s.size();
        std::vector<int> radius(n, 0);
        int center = 0, right = 0;
        for (int i = 0; i < n; i++) {
            if (i < right) radius[i] = std::min(right - i, radius[2 * center - i]);
            while (i - radius[i] - 1 >= 0 && i + radius[i] + 1 < n &&
                   s[i - radius[i] - 1] == s[i + radius[i] + 1]) radius[i]++;
            if (i + radius[i] > right) { center = i; right = i + radius[i]; }
        }
        std::vector<int> end(n, 1), start(n, 1);
        for (int i = 0; i < n; i++) {
            int r = radius[i];
            end[i + r] = std::max(end[i + r], 2 * r + 1);
            start[i - r] = std::max(start[i - r], 2 * r + 1);
        }
        for (int i = n - 2; i >= 0; i--) end[i] = std::max(end[i], end[i + 1] - 2);
        for (int i = 1; i < n; i++) start[i] = std::max(start[i], start[i - 1] - 2);
        std::vector<int> pre(n), suf(n);
        pre[0] = end[0];
        for (int i = 1; i < n; i++) pre[i] = std::max(pre[i - 1], end[i]);
        suf[n - 1] = start[n - 1];
        for (int i = n - 2; i >= 0; i--) suf[i] = std::max(suf[i + 1], start[i]);
        long long ans = 0;
        for (int i = 0; i + 1 < n; i++) ans = std::max(ans, 1LL * pre[i] * suf[i + 1]);
        return ans;
    }
};
