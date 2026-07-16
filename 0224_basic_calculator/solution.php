// LeetCode 0224 - Basic Calculator
// https://leetcode.com/problems/basic-calculator/

class Solution {
    /**
     * @param String $s
     * @return Integer
     */
    function calculate($s) {
        $stack = [];
        $result = 0;
        $number = 0;
        $sign = 1;
        $length = strlen($s);
        for ($i = 0; $i < $length; $i++) {
            $char = $s[$i];
            if ($char >= '0' && $char <= '9') {
                $number = $number * 10 + (ord($char) - 48);
            } elseif ($char === '+' || $char === '-') {
                $result += $sign * $number;
                $number = 0;
                $sign = $char === '+' ? 1 : -1;
            } elseif ($char === '(') {
                $stack[] = $result;
                $stack[] = $sign;
                $result = 0;
                $sign = 1;
            } elseif ($char === ')') {
                $result += $sign * $number;
                $number = 0;
                $result *= array_pop($stack);
                $result += array_pop($stack);
            }
        }
        $result += $sign * $number;
        return $result;
    }
}
