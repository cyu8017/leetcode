// LeetCode 0263 - Ugly Number
// https://leetcode.com/problems/ugly-number/

class Solution {
    /**
     * @param Integer $n
     * @return Boolean
     */
    function isUgly($n) {
        if ($n <= 0) {
            return false;
        }
        foreach ([2, 3, 5] as $factor) {
            while ($n % $factor === 0) {
                $n = intdiv($n, $factor);
            }
        }
        return $n === 1;
    }
}
