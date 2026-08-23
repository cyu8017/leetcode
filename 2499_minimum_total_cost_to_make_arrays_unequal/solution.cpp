// LeetCode 2499 - Minimum Total Cost to Make Arrays Unequal
// https://leetcode.com/problems/minimum-total-cost-to-make-arrays-unequal/

#include <unordered_map>
#include <vector>

class Solution {
public:
    long long minimumTotalCost(std::vector<int>& nums1, std::vector<int>& nums2) {
        int n = (int)nums1.size();
        std::unordered_map<int, int> freq;
        long long ans = 0;
        int same = 0;
        for (int i = 0; i < n; i++) {
            if (nums1[i] == nums2[i]) {
                same++;
                freq[nums1[i]]++;
                ans += i;
            }
        }
        int maxFreq = 0, maxVal = 0;
        for (auto& [v, c] : freq) {
            if (c > maxFreq) {
                maxFreq = c;
                maxVal = v;
            }
        }
        int need = maxFreq * 2 - same;
        if (need <= 0) return ans;
        for (int i = 0; i < n && need > 0; i++) {
            if (nums1[i] != nums2[i] && nums1[i] != maxVal && nums2[i] != maxVal) {
                ans += i;
                need--;
            }
        }
        return need > 0 ? -1 : ans;
    }
};
