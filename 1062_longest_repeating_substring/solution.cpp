// LeetCode 1062 - Longest Repeating Substring
// https://leetcode.com/problems/longest-repeating-substring/

#include <string>
#include <unordered_set>

class Solution {
public:
    int longestRepeatingSubstring(std::string s) {
        int n = static_cast<int>(s.size());
        auto hasDup = [&](int length) {
            std::unordered_set<std::string> seen;
            for (int i = 0; i <= n - length; ++i) {
                std::string sub = s.substr(i, length);
                if (seen.count(sub)) {
                    return true;
                }
                seen.insert(sub);
            }
            return false;
        };

        int lo = 1;
        int hi = n - 1;
        int ans = 0;
        while (lo <= hi) {
            int mid = (lo + hi) / 2;
            if (hasDup(mid)) {
                ans = mid;
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return ans;
    }
};
