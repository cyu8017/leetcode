// LeetCode 1983 - Widest Pair of Indices With Equal Range Sum
#include <algorithm>
#include <unordered_map>
#include <vector>

class Solution {
public:
    int widestPairOfIndices(std::vector<int>& nums1, std::vector<int>& nums2) {
        std::unordered_map<int, int> first;
        first[0] = -1;
        int ans = 0, s = 0;
        for (int i = 0; i < (int)nums1.size(); i++) {
            s += nums1[i] - nums2[i];
            if (first.count(s)) ans = std::max(ans, i - first[s]);
            else first[s] = i;
        }
        return ans;
    }
};
