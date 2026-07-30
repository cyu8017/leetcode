// LeetCode 1250 - Check If It Is a Good Array
// https://leetcode.com/problems/check-if-it-is-a-good-array/

public class Solution {
    public bool IsGoodArray(int[] nums) {
        int g = nums[0];
        for (int i = 1; i < nums.Length; i++) g = Gcd(g, nums[i]);
        return g == 1;
    }

    private static int Gcd(int a, int b) {
        while (b != 0) (a, b) = (b, a % b);
        return a;
    }
}
