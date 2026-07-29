// LeetCode 1248 - Count Number of Nice Subarrays
// https://leetcode.com/problems/count-number-of-nice-subarrays/

#include <unordered_map>
#include <vector>

class Solution {
public:
    int numberOfSubarrays(std::vector<int>& nums, int k) {
        std::unordered_map<int, int> frequency{{0, 1}};
        int odd = 0, answer = 0;
        for (int x : nums) {
            odd += x & 1;
            answer += frequency[odd - k];
            ++frequency[odd];
        }
        return answer;
    }
};
