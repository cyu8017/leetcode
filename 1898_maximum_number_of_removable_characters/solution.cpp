// LeetCode 1898 - Maximum Number of Removable Characters
// https://leetcode.com/problems/maximum-number-of-removable-characters/

#include <string>
#include <unordered_set>
#include <vector>

class Solution {
public:
    int maximumRemovals(std::string s, std::string p, std::vector<int>& removable) {
        auto stillSubsequence = [&](int k) {
            std::unordered_set<int> removed(removable.begin(), removable.begin() + k);
            int index = 0;
            for (int position = 0; position < static_cast<int>(s.size()); position++) {
                if (removed.count(position)) continue;
                if (index < static_cast<int>(p.size()) && s[position] == p[index]) {
                    index++;
                }
            }
            return index == static_cast<int>(p.size());
        };

        int lo = 0;
        int hi = static_cast<int>(removable.size());
        while (lo < hi) {
            int mid = lo + (hi - lo + 1) / 2;
            if (stillSubsequence(mid)) {
                lo = mid;
            } else {
                hi = mid - 1;
            }
        }
        return lo;
    }
};
