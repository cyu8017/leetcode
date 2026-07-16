// LeetCode 0029 - Divide Two Integers
// https://leetcode.com/problems/divide-two-integers/

class Solution {
    /**
     * @param Integer $dividend
     * @param Integer $divisor
     * @return Integer
     */
    function divide($dividend, $divisor) {
        if ($dividend === -2147483648 && $divisor === -1) {
            return 2147483647;
        }

        $negative = ($dividend < 0) xor ($divisor < 0);
        $a = abs($dividend);
        $b = abs($divisor);
        $quotient = 0;

        for ($i = 31; $i >= 0; $i--) {
            if (($a >> $i) >= $b) {
                $quotient += 1 << $i;
                $a -= $b << $i;
            }
        }

        return $negative ? -$quotient : $quotient;
    }
}
