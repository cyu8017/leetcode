// LeetCode 1887 - Reduction Operations to Make the Array Elements Equal
// https://leetcode.com/problems/reduction-operations-to-make-the-array-elements-equal/

#include <algorithm>
#include <vector>

class Solution {
public:
    int reductionOperations(std::vector<int>& nums) {
        std::sort(nums.begin(), nums.end());
        int answer = 0;
        int rank = 0;
        for (int i = 1; i < static_cast<int>(nums.size()); i++) {
            if (nums[i] != nums[i - 1]) {
                rank++;
            }
            answer += rank;
        }
        return answer;
    }
};
