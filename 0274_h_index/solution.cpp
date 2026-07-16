// LeetCode 0274 - H-Index
// https://leetcode.com/problems/h-index/

#include <algorithm>
#include <vector>

class Solution {
public:
    int hIndex(std::vector<int>& citations) {
        std::vector<int> buckets(citations.size() + 1, 0);
        for (int citation : citations) {
            buckets[std::min(citation, static_cast<int>(citations.size()))]++;
        }
        int total = 0;
        for (int h = static_cast<int>(buckets.size()) - 1; h >= 0; h--) {
            total += buckets[h];
            if (total >= h) {
                return h;
            }
        }
        return 0;
    }
};
