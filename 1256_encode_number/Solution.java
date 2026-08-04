// LeetCode 1256 - Encode Number
// https://leetcode.com/problems/encode-number/

class Solution {
    public String encode(int num) {
        return Integer.toBinaryString(num + 1).substring(1);
    }
}

