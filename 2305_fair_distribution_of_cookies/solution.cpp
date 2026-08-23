// LeetCode 2305 - Fair Distribution of Cookies
// https://leetcode.com/problems/fair-distribution-of-cookies/

#include <vector>
#include <unordered_set>
#include <climits>
#include <algorithm>
#include <functional>

class Solution {
public:
    int distributeCookies(std::vector<int>& cookies, int k) {
        int n = (int)cookies.size();
        std::vector<int> bags(k);
        int ans = INT_MAX;
        std::function<void(int)> dfs = [&](int i) {
            if (i == n) {
                ans = std::min(ans, *std::max_element(bags.begin(), bags.end()));
                return;
            }
            std::unordered_set<int> seen;
            for (int j = 0; j < k; ++j) {
                if (seen.count(bags[j])) continue;
                seen.insert(bags[j]);
                bags[j] += cookies[i];
                if (bags[j] < ans) dfs(i + 1);
                bags[j] -= cookies[i];
                if (bags[j] == 0) break;
            }
        };
        dfs(0);
        return ans;
    }
};
