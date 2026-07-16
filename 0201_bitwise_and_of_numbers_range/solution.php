// LeetCode 0201 - Bitwise AND of Numbers Range
// https://leetcode.com/problems/bitwise-and-of-numbers-range/

class Solution {
    function rangeBitwiseAnd($left, $right) {
        $shift = 0;
        while ($left < $right) {
            $left >>= 1;
            $right >>= 1;
            $shift++;
        }
        return $left << $shift;
    }
}