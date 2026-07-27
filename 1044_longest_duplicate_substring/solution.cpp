// LeetCode 1044 - Longest Duplicate Substring
// https://leetcode.com/problems/longest-duplicate-substring/

#include <string>
#include <unordered_map>
#include <vector>

class Solution {
public:
    std::string longestDupSubstring(std::string s) {
        const unsigned long long BASE = 911382323ULL;
        int n = static_cast<int>(s.size());

        auto search = [&](int length) -> int {
            if (length == 0) return 0;
            unsigned long long h = 0, power = 1;
            for (int i = 0; i < length; ++i) {
                h = h * BASE + static_cast<unsigned char>(s[i]);
                if (i) power *= BASE;
            }
            std::unordered_map<unsigned long long, std::vector<int>> seen;
            seen[h].push_back(0);
            for (int i = 1; i + length - 1 < n; ++i) {
                h = h - static_cast<unsigned char>(s[i - 1]) * power;
                h = h * BASE + static_cast<unsigned char>(s[i + length - 1]);
                auto it = seen.find(h);
                if (it != seen.end()) {
                    for (int j : it->second) {
                        if (s.compare(j, length, s, i, length) == 0) return i;
                    }
                }
                seen[h].push_back(i);
            }
            return -1;
        };

        int lo = 0, hi = n - 1, start = -1, bestLen = 0;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            int pos = search(mid);
            if (pos >= 0) {
                start = pos;
                bestLen = mid;
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return start >= 0 ? s.substr(start, bestLen) : "";
    }
};

