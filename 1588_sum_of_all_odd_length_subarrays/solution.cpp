// LeetCode 1588 - Sum of All Odd Length Subarrays
// https://leetcode.com/problems/sum-of-all-odd-length-subarrays/

#include <vector>

class Solution {
public:
    int sumOddLengthSubarrays(std::vector<int>& arr) {
        const int n = static_cast<int>(arr.size());
        int answer = 0;
        for (int i = 0; i < n; ++i) {
            answer += arr[i] * (((i + 1) * (n - i) + 1) / 2);
        }
        return answer;
    }
};
