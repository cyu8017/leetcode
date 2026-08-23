// LeetCode 2429 - Minimize XOR
// https://leetcode.com/problems/minimize-xor/

public class Solution {
    public int MinimizeXor(int num1, int num2) {
        int bits = 0;
        for (int x = num2; x != 0; x &= x - 1) bits++;
        int ans = 0;
        for (int i = 31; i >= 0 && bits > 0; i--) {
            if (((num1 >> i) & 1) != 0) {
                ans |= 1 << i;
                bits--;
            }
        }
        for (int i = 0; i < 32 && bits > 0; i++) {
            if (((ans >> i) & 1) == 0) {
                ans |= 1 << i;
                bits--;
            }
        }
        return ans;
    }
}
