// LeetCode 0969 - Pancake Sorting
// https://leetcode.com/problems/pancake-sorting/

#include <algorithm>
#include <vector>

class Solution {
public:
    std::vector<int> pancakeSort(std::vector<int>& arr) {
        std::vector<int> a = arr, ans;
        for (int size = (int)a.size(); size > 1; size--) {
            int i = (int)(std::find(a.begin(), a.end(), size) - a.begin());
            if (i == size - 1) continue;
            if (i) {
                ans.push_back(i + 1);
                std::reverse(a.begin(), a.begin() + i + 1);
            }
            ans.push_back(size);
            std::reverse(a.begin(), a.begin() + size);
        }
        return ans;
    }
};
