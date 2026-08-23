// LeetCode 2757 - Generate Circular Array Values
// https://leetcode.com/problems/generate-circular-array-values/
// JS generator stand-in.

#include <functional>
#include <vector>

class Solution {
public:
    std::function<int()> cyclicGenerator(std::vector<int>& arr, int startIndex) {
        int i = startIndex;
        int n = (int)arr.size();
        return [arr, i, n]() mutable {
            int v = arr[i];
            i = (i + 1) % n;
            return v;
        };
    }
};
