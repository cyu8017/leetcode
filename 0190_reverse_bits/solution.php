// LeetCode 0190 - Reverse Bits
// https://leetcode.com/problems/reverse-bits/

class Solution {
    /**
     * @param Integer $n
     * @return Integer
     */
    function reverseBits($n) {
        $result = 0;
        for ($index = 0; $index < 32; $index++) {
            $result = ($result << 1) | ($n & 1);
            $n >>= 1;
        }
        return $result;
    }
}