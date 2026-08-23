// LeetCode 3158 - Find the XOR of Numbers Which Appear Twice
// https://leetcode.com/problems/find-the-xor-of-numbers-which-appear-twice/

public class Solution {
    public int DuplicateNumbersXOR(int[] nums) {
        int[] cnt = new int[51];
        int ans = 0;
        foreach (int x in nums) {
            if (++cnt[x] == 2) ans ^= x;
        }
        return ans;
    }
}
