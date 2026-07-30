// LeetCode 1256 - Encode Number
// https://leetcode.com/problems/encode-number/

public class Solution {
    public string Encode(int num) {
        return Convert.ToString(num + 1, 2)[1..];
    }
}
