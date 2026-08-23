// LeetCode 3751 - Total Waviness Of Numbers In Range I
// https://leetcode.com/problems/total-waviness-of-numbers-in-range-i/

import java.util.ArrayList;
import java.util.List;

class Solution {
    int F(int x) {
        var nums = new ArrayList<Integer>();
        while (x > 0) {
            nums.add(x % 10);
            x /= 10;
        }
        int m = nums.size();
        if (m < 3) return 0;
        int s = 0;
        for (int i = 1; i < m - 1; i++) {
            if ((nums.get(i) > nums.get(i - 1) && nums.get(i) > nums.get(i + 1)) ||
                (nums.get(i) < nums.get(i - 1) && nums.get(i) < nums.get(i + 1))) s++;
        }
        return s;
    }

    public int totalWaviness(int num1, int num2) {
        int ans = 0;
        for (int x = num1; x <= num2; x++) ans += F(x);
        return ans;
    }
}
