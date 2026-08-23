// LeetCode 3507 - Minimum Pair Removal to Sort Array I
// https://leetcode.com/problems/minimum-pair-removal-to-sort-array-i/

#include <vector>

class Solution {
    bool isNonDecreasing(const std::vector<int>& a) {
        for (int i = 1; i < (int)a.size(); i++) if (a[i] < a[i - 1]) return false;
        return true;
    }
public:
    int minimumPairRemoval(std::vector<int>& nums) {
        std::vector<int> arr = nums;
        int ans = 0;
        while (!isNonDecreasing(arr)) {
            int k = 0, s = arr[0] + arr[1];
            for (int i = 1; i + 1 < (int)arr.size(); i++) {
                int t = arr[i] + arr[i + 1];
                if (s > t) { s = t; k = i; }
            }
            arr[k] = s;
            arr.erase(arr.begin() + k + 1);
            ans++;
        }
        return ans;
    }
};
