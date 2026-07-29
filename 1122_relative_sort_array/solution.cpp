// LeetCode 1122 - Relative Sort Array
// https://leetcode.com/problems/relative-sort-array/

#include <map>
#include <unordered_map>
#include <vector>

class Solution {
public:
    std::vector<int> relativeSortArray(std::vector<int>& arr1, std::vector<int>& arr2) {
        std::unordered_map<int, int> count;
        for (int x : arr1) {
            ++count[x];
        }
        std::vector<int> ans;
        for (int x : arr2) {
            while (count[x]-- > 0) {
                ans.push_back(x);
            }
            count.erase(x);
        }
        std::map<int, int> remaining(count.begin(), count.end());
        for (const auto& [x, c] : remaining) {
            for (int i = 0; i < c; ++i) {
                ans.push_back(x);
            }
        }
        return ans;
    }
};
