// LeetCode 0326 - Power of Three
// https://leetcode.com/problems/power-of-three/

class Solution {
    /**
     * @param Integer $n
     * @return Boolean
     */
    function isPowerOfThree($n) {
        if ($n <= 0) {
            return false;
        }
        while ($n % 3 === 0) {
            $n = intdiv($n, 3);
        }
        return $n === 1;
    }
}
