// LeetCode 0259 - 3Sum Smaller
// https://leetcode.com/problems/3sum-smaller/

#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
    int threeSumSmaller(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());
        int count = 0;
        for (int index = 0; index + 2 < (int)nums.size(); index++) {
            int left = index + 1;
            int right = (int)nums.size() - 1;
            while (left < right) {
                int total = nums[index] + nums[left] + nums[right];
                if (total < target) {
                    count += right - left;
                    left++;
                } else {
                    right--;
                }
            }
        }
        return count;
    }
};
