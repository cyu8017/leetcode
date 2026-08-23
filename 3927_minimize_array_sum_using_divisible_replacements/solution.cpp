// LeetCode 3927 - Minimize Array Sum Using Divisible Replacements
// https://leetcode.com/problems/minimize-array-sum-using-divisible-replacements/

#include <vector>

class Solution {
public:
    long long minArraySum(std::vector<int>& nums) {
        int maximum = 0;
        std::vector<bool> present(100001, false);
        for (int value : nums) {
            present[value] = true;
            if (value > maximum) maximum = value;
        }
        std::vector<int> best(maximum + 1, 0);
        for (int divisor = 1; divisor <= maximum; divisor++) {
            if (!present[divisor]) continue;
            for (int multiple = divisor; multiple <= maximum; multiple += divisor) {
                if (best[multiple] == 0) best[multiple] = divisor;
            }
        }
        long long answer = 0;
        for (int value : nums) answer += best[value];
        return answer;
    }
};
