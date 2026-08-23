// LeetCode 3751 - Total Waviness Of Numbers In Range I
// https://leetcode.com/problems/total-waviness-of-numbers-in-range-i/

#include <vector>

class Solution {
    int f(int x) {
        std::vector<int> nums;
        while (x > 0) {
            nums.push_back(x % 10);
            x /= 10;
        }
        int m = (int)nums.size();
        if (m < 3) return 0;
        int s = 0;
        for (int i = 1; i < m - 1; i++) {
            if ((nums[i] > nums[i - 1] && nums[i] > nums[i + 1]) ||
                (nums[i] < nums[i - 1] && nums[i] < nums[i + 1])) s++;
        }
        return s;
    }

public:
    int totalWaviness(int num1, int num2) {
        int ans = 0;
        for (int x = num1; x <= num2; x++) ans += f(x);
        return ans;
    }
};
