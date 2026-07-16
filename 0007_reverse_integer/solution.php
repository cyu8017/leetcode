// LeetCode 0007 - Reverse Integer
// https://leetcode.com/problems/reverse-integer/

class Solution {
    /**
     * @param Integer $x
     * @return Integer
     */
    function reverse($x) {
        $result = 0;

        while ($x !== 0) {
            $pop = $x % 10;
            $x = intdiv($x, 10);

            if ($result > intdiv(PHP_INT_MAX, 10) || ($result === intdiv(PHP_INT_MAX, 10) && $pop > 7)) {
                return 0;
            }
            if ($result < intdiv(PHP_INT_MIN, 10) || ($result === intdiv(PHP_INT_MIN, 10) && $pop < -8)) {
                return 0;
            }

            $result = $result * 10 + $pop;
        }

        return $result;
    }
}
