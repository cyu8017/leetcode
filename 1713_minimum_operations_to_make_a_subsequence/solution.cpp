// LeetCode 1713 - Minimum Operations to Make a Subsequence
// https://leetcode.com/problems/minimum-operations-to-make-a-subsequence/

#include <algorithm>
#include <unordered_map>
#include <vector>

class Solution {
public:
    int minOperations(std::vector<int>& target, std::vector<int>& arr) {
        std::unordered_map<int, int> pos;
        for (int i = 0; i < (int)target.size(); i++) {
            pos[target[i]] = i;
        }
        std::vector<int> lis;
        for (int value : arr) {
            auto it = pos.find(value);
            if (it == pos.end()) {
                continue;
            }
            int idx = it->second;
            auto place = std::lower_bound(lis.begin(), lis.end(), idx);
            if (place == lis.end()) {
                lis.push_back(idx);
            } else {
                *place = idx;
            }
        }
        return (int)target.size() - (int)lis.size();
    }
};
