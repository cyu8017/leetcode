// LeetCode 0069 - Sqrt(x)
// https://leetcode.com/problems/sqrtx/

class Solution {
    /**
     * @param Integer $x
     * @return Integer
     */
    function mySqrt($x) {
        if ($x < 2) {
            return $x;
        }

        $left = 2;
        $right = intdiv($x, 2);

        while ($left <= $right) {
            $mid = intdiv($left + $right, 2);
            $square = $mid * $mid;
            if ($square === $x) {
                return $mid;
            }
            if ($square < $x) {
                $left = $mid + 1;
            } else {
                $right = $mid - 1;
            }
        }

        return $right;
    }
}
