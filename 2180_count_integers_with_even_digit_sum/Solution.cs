// LeetCode 2180 - Count Integers With Even Digit Sum
// https://leetcode.com/problems/count-integers-with-even-digit-sum/

public class Solution {
    public int CountEven(int num) {
        int ans = 0;
        for (int x = 1; x <= num; x++) {
            int s = 0, y = x;
            while (y > 0) { s += y % 10; y /= 10; }
            if (s % 2 == 0) ans++;
        }
        return ans;
    }
}
