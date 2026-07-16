// LeetCode 0050 - Pow(x, n)
// https://leetcode.com/problems/powx-n/

class Solution {
    /**
     * @param Float $x
     * @param Integer $n
     * @return Float
     */
    function myPow($x, $n) {
        if ($n == 0) {
            return 1.0;
        }

        $baseValue = $x;
        $exponent = $n;
        if ($exponent < 0) {
            $baseValue = 1.0 / $baseValue;
            $exponent = -$exponent;
        }

        $result = 1.0;
        $current = $baseValue;

        while ($exponent != 0) {
            if ($exponent & 1) {
                $result *= $current;
            }
            $current *= $current;
            $exponent >>= 1;
        }

        return $result;
    }
}
