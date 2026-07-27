// LeetCode 1013 - Partition Array Into Three Parts With Equal Sum
// https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/

#include <numeric>
#include <vector>

class Solution {
public:
    bool canThreePartsEqualSum(std::vector<int>& arr) {
        int total = std::accumulate(arr.begin(), arr.end(), 0);
        if (total % 3 != 0) return false;
        int target = total / 3;
        int parts = 0, cur = 0;
        for (int x : arr) {
            cur += x;
            if (cur == target) {
                ++parts;
                cur = 0;
            }
        }
        return parts >= 3;
    }
};

