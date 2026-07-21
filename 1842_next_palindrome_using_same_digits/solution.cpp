// LeetCode 1842 - Next Palindrome Using Same Digits
// https://leetcode.com/problems/next-palindrome-using-same-digits/

#include <algorithm>
#include <string>
#include <vector>

class Solution {
public:
    std::string nextPalindrome(std::string num) {
        std::vector<char> nums(num.begin(), num.end());
        if (!nextPermutation(nums)) {
            return "";
        }
        int n = static_cast<int>(nums.size());
        for (int i = 0; i < n / 2; ++i) {
            nums[n - i - 1] = nums[i];
        }
        return std::string(nums.begin(), nums.end());
    }

private:
    bool nextPermutation(std::vector<char>& nums) {
        int n = static_cast<int>(nums.size()) / 2;
        int i = n - 2;
        while (i >= 0 && nums[i] >= nums[i + 1]) {
            --i;
        }
        if (i < 0) {
            return false;
        }
        int j = n - 1;
        while (nums[j] <= nums[i]) {
            --j;
        }
        std::swap(nums[i], nums[j]);
        std::reverse(nums.begin() + i + 1, nums.begin() + n);
        return true;
    }
};
