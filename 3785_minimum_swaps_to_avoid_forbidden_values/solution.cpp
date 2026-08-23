// LeetCode 3785 - Minimum Swaps to Avoid Forbidden Values
// https://leetcode.com/problems/minimum-swaps-to-avoid-forbidden-values/

#include <unordered_map>
#include <vector>

class Solution {
public:
    int minSwaps(std::vector<int>& nums, std::vector<int>& forbidden) {
        int n = (int)nums.size();
        std::unordered_map<int, int> freq;
        for (int x : nums) freq[x]++;
        for (int x : forbidden) freq[x]++;
        for (auto& [_, c] : freq) {
            if (c > n) return -1;
        }
        std::unordered_map<int, int> bad;
        int total = 0, largest = 0;
        for (int i = 0; i < n; i++) {
            if (nums[i] == forbidden[i]) {
                bad[nums[i]]++;
                total++;
                if (bad[nums[i]] > largest) largest = bad[nums[i]];
            }
        }
        if ((total + 1) / 2 > largest) return (total + 1) / 2;
        return largest;
    }
};
