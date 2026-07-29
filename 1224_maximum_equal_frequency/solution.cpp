// LeetCode 1224 - Maximum Equal Frequency
// https://leetcode.com/problems/maximum-equal-frequency/

#include <algorithm>
#include <unordered_map>
#include <vector>

class Solution {
public:
    int maxEqualFreq(std::vector<int>& nums) {
        std::unordered_map<int, int> count;
        std::unordered_map<int, int> frequencies;
        int answer = 0;
        for (int i = 0; i < static_cast<int>(nums.size()); ++i) {
            int x = nums[i];
            int old = count[x];
            if (old) {
                --frequencies[old];
                if (frequencies[old] == 0) {
                    frequencies.erase(old);
                }
            }
            ++count[x];
            ++frequencies[old + 1];
            int high = 0;
            for (const auto& [f, _] : frequencies) {
                high = std::max(high, f);
            }
            int idx = i + 1;
            if (high == 1 || frequencies[high] * high + 1 == idx ||
                (frequencies[high] == 1 && frequencies[high - 1] * (high - 1) + high == idx)) {
                answer = idx;
            }
        }
        return answer;
    }
};
