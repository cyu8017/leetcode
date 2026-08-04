// LeetCode 1271 - Hexspeak
// https://leetcode.com/problems/hexspeak/

import java.math.BigInteger;

class Solution {
    public String toHexspeak(String num) {
        BigInteger value = new BigInteger(num);
        String digits = "0123456789ABCDEF";
        StringBuilder out = new StringBuilder();
        while (value.signum() > 0) {
            int rem = value.mod(BigInteger.valueOf(16)).intValue();
            if (rem >= 2 && rem <= 9) return "ERROR";
            out.insert(0, digits.charAt(rem));
            value = value.divide(BigInteger.valueOf(16));
        }
        String result = out.length() == 0 ? "0" : out.toString();
        return result.replace('0', 'O').replace('1', 'I');
    }
}
