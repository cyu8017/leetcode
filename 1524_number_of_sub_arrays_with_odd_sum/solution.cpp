// LeetCode 1524 - Number of Sub-arrays With Odd Sum
// https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/

#include <vector>

class Solution {
public:
    int numOfSubarrays(std::vector<int>& arr) {
        int counts[2] = {1, 0};
        int parity = 0;
        long long answer = 0;
        for (int value : arr) {
            parity ^= value & 1;
            answer += counts[parity ^ 1];
            counts[parity] += 1;
        }
        return static_cast<int>(answer % 1000000007);
    }
};
