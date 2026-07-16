// LeetCode 0227 - Basic Calculator II
// https://leetcode.com/problems/basic-calculator-ii/

class Solution {
    /**
     * @param String $s
     * @return Integer
     */
    function calculate($s) {
        $stack = [];
        $number = 0;
        $operator = "+";

        $length = strlen($s);
        for ($index = 0; $index < $length; $index++) {
            $char = $s[$index];
            if (ctype_digit($char)) {
                $number = $number * 10 + (int)$char;
            }
            if ($char === "+" || $char === "-" || $char === "*" || $char === "/" || $index === $length - 1) {
                if ($operator === "+") {
                    $stack[] = $number;
                } elseif ($operator === "-") {
                    $stack[] = -$number;
                } elseif ($operator === "*") {
                    $stack[count($stack) - 1] = array_pop($stack) * $number;
                } elseif ($operator === "/") {
                    $stack[count($stack) - 1] = intdiv(array_pop($stack), $number);
                }
                $operator = $char;
                $number = 0;
            }
        }

        return array_sum($stack);
    }
}
