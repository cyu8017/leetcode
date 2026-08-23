// LeetCode 3316 - Find Maximum Removals From Source String
// https://leetcode.com/problems/find-maximum-removals-from-source-string/

#include <string>
#include <vector>

class Solution {
public:
    int maxRemovals(std::string source, std::string pattern, std::vector<int>& targetIndices) {
        int n = (int)source.size();
        auto ok = [&](int removeFirst) {
            std::vector<char> mark(n, 0);
            for (int i = 0; i < removeFirst; i++) mark[targetIndices[i]] = 1;
            int j = 0;
            for (int i = 0; i < n && j < (int)pattern.size(); i++) {
                if (mark[i]) continue;
                if (source[i] == pattern[j]) j++;
            }
            return j == (int)pattern.size();
        };
        int lo = 0, hi = (int)targetIndices.size();
        while (lo < hi) {
            int mid = (lo + hi + 1) / 2;
            if (ok(mid)) lo = mid;
            else hi = mid - 1;
        }
        return lo;
    }
};
