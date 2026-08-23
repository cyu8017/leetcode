// LeetCode 3022 - Minimize OR of Remaining Elements Using Operations
// https://leetcode.com/problems/minimize-or-of-remaining-elements-using-operations/

public class Solution {
    public int MinOrAfterOperations(int[] nums, int k) {
        int ans = 0, rans = 0;
        for (int i = 29; i >= 0; i--) {
            int test = ans + (1 << i);
            int cnt = 0, val = 0;
            foreach (int num in nums) {
                if (val == 0) val = test & num;
                else val &= test & num;
                if (val != 0) cnt++;
            }
            if (cnt > k) rans += (1 << i);
            else ans += (1 << i);
        }
        return rans;
    }
}
