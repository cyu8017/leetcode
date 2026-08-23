// LeetCode 2813 - Maximum Elegance of a K-Length Subsequence
// https://leetcode.com/problems/maximum-elegance-of-a-k-length-subsequence/

#include <algorithm>
#include <unordered_set>
#include <vector>

class Solution {
public:
    long long findMaximumElegance(std::vector<std::vector<int>>& items, int k) {
        std::sort(items.begin(), items.end(), [](auto& a, auto& b) { return a[0] > b[0]; });
        std::unordered_set<int> seen;
        long long total = 0;
        std::vector<int> dup;
        for (int i = 0; i < k; i++) {
            total += items[i][0];
            int c = items[i][1];
            if (seen.count(c)) dup.push_back(items[i][0]);
            else seen.insert(c);
        }
        long long ans = total + 1LL * (long long)seen.size() * (long long)seen.size();
        for (int i = k; i < (int)items.size(); i++) {
            int c = items[i][1];
            if (seen.count(c) || dup.empty()) continue;
            total += items[i][0] - dup.back();
            dup.pop_back();
            seen.insert(c);
            ans = std::max(ans, total + 1LL * (long long)seen.size() * (long long)seen.size());
        }
        return ans;
    }
};
