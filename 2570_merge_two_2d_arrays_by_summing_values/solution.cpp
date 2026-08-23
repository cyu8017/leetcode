// LeetCode 2570 - Merge Two 2D Arrays by Summing Values
// https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/

#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> mergeArrays(std::vector<std::vector<int>>& nums1, std::vector<std::vector<int>>& nums2) {
        int i = 0, j = 0;
        std::vector<std::vector<int>> ans;
        while (i < (int)nums1.size() && j < (int)nums2.size()) {
            if (nums1[i][0] == nums2[j][0]) {
                ans.push_back({nums1[i][0], nums1[i][1] + nums2[j][1]});
                i++; j++;
            } else if (nums1[i][0] < nums2[j][0]) {
                ans.push_back({nums1[i][0], nums1[i][1]});
                i++;
            } else {
                ans.push_back({nums2[j][0], nums2[j][1]});
                j++;
            }
        }
        while (i < (int)nums1.size()) {
            ans.push_back({nums1[i][0], nums1[i][1]});
            i++;
        }
        while (j < (int)nums2.size()) {
            ans.push_back({nums2[j][0], nums2[j][1]});
            j++;
        }
        return ans;
    }
};
