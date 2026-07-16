// LeetCode 0089 - Gray Code
// https://leetcode.com/problems/gray-code/

#include <vector>

class Solution {
public:
    std::vector<int> grayCode(int n) {
        std::vector<int> result;
        int size = 1 << n;
        result.reserve(size);
        for (int i = 0; i < size; i++) {
            result.push_back(i ^ (i >> 1));
        }
        return result;
    }
};
