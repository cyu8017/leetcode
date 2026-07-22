// LeetCode 1640 - Check Array Formation Through Concatenation
// https://leetcode.com/problems/check-array-formation-through-concatenation/

#include <unordered_map>
#include <vector>

class Solution {
public:
    bool canFormArray(std::vector<int>& arr, std::vector<std::vector<int>>& pieces) {
        std::unordered_map<int, std::vector<int>*> by_first;
        for (auto& p : pieces) {
            by_first[p[0]] = &p;
        }
        int i = 0;
        while (i < static_cast<int>(arr.size())) {
            if (!by_first.count(arr[i])) {
                return false;
            }
            const auto& p = *by_first[arr[i]];
            for (int x : p) {
                if (i >= static_cast<int>(arr.size()) || arr[i] != x) {
                    return false;
                }
                ++i;
            }
        }
        return true;
    }
};
