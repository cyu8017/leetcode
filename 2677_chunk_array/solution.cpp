// LeetCode 2677 - Chunk Array
// https://leetcode.com/problems/chunk-array/

#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> chunk(std::vector<int>& arr, int size) {
        std::vector<std::vector<int>> ans;
        for (int i = 0; i < (int)arr.size(); i += size) {
            std::vector<int> part;
            for (int j = i; j < (int)arr.size() && j < i + size; j++) part.push_back(arr[j]);
            ans.push_back(part);
        }
        return ans;
    }
};
