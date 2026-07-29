// LeetCode 0673 - Number of Longest Increasing Subsequence
// https://leetcode.com/problems/number-of-longest-increasing-subsequence/

#include <algorithm>
#include <vector>

class Solution {
public:
    int findNumberOfLIS(std::vector<int>& nums) {
        const int n = static_cast<int>(nums.size());
        std::vector<int> lengths(n, 1);
        std::vector<int> counts(n, 1);
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < i; ++j) {
                if (nums[j] >= nums[i]) {
                    continue;
                }
                if (lengths[j] + 1 > lengths[i]) {
                    lengths[i] = lengths[j] + 1;
                    counts[i] = counts[j];
                } else if (lengths[j] + 1 == lengths[i]) {
                    counts[i] += counts[j];
                }
            }
        }
        const int longest = *std::max_element(lengths.begin(), lengths.end());
        int answer = 0;
        for (int i = 0; i < n; ++i) {
            if (lengths[i] == longest) {
                answer += counts[i];
            }
        }
        return answer;
    }
};
