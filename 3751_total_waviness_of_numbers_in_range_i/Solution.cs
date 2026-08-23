// LeetCode 3751 - Total Waviness Of Numbers In Range I
// https://leetcode.com/problems/total-waviness-of-numbers-in-range-i/

using System.Collections.Generic;

public class Solution {
    int F(int x) {
        var nums = new List<int>();
        while (x > 0) {
            nums.Add(x % 10);
            x /= 10;
        }
        int m = nums.Count;
        if (m < 3) return 0;
        int s = 0;
        for (int i = 1; i < m - 1; i++) {
            if ((nums[i] > nums[i - 1] && nums[i] > nums[i + 1]) ||
                (nums[i] < nums[i - 1] && nums[i] < nums[i + 1])) s++;
        }
        return s;
    }

    public int TotalWaviness(int num1, int num2) {
        int ans = 0;
        for (int x = num1; x <= num2; x++) ans += F(x);
        return ans;
    }
}
