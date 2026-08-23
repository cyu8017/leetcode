// LeetCode 3952 - Maximum Total Value of Covered Indices
// https://leetcode.com/problems/maximum-total-value-of-covered-indices/

#include <string>
#include <vector>

class Solution {
public:
    int maxTotalValue(std::vector<int>& nums, std::string s) {
        int answer = 0;
        for (int i = 0; i < (int)s.size();) {
            if (s[i] == '0') {
                i++;
                continue;
            }
            int start = i;
            while (i < (int)s.size() && s[i] == '1') i++;
            int end = i - 1;
            if (start == 0) {
                for (int index = start; index <= end; index++) answer += nums[index];
                continue;
            }
            int minimum = nums[start - 1];
            int total = 0;
            for (int index = start - 1; index <= end; index++) {
                total += nums[index];
                if (nums[index] < minimum) minimum = nums[index];
            }
            answer += total - minimum;
        }
        return answer;
    }
};
