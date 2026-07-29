// LeetCode 1238 - Circular Permutation in Binary Representation
// https://leetcode.com/problems/circular-permutation-in-binary-representation/

#include <vector>

class Solution {
public:
    std::vector<int> circularPermutation(int n, int start) {
        std::vector<int> answer;
        const int total = 1 << n;
        answer.reserve(total);
        for (int i = 0; i < total; ++i) {
            answer.push_back(start ^ i ^ (i >> 1));
        }
        return answer;
    }
};
