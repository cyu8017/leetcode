<?php
// LeetCode 0537 - Complex Number Multiplication
// https://leetcode.com/problems/complex-number-multiplication/

class Solution {
    /**
     * @param String $num1
     * @param String $num2
     * @return String
     */
    function complexNumberMultiply($num1, $num2) {
        return $this->complex_number_multiply($num1, $num2);
    }

    /**
     * @param String $num1
     * @param String $num2
     * @return String
     */
    function complex_number_multiply($num1, $num2) {
        list($a, $b) = $this->parse($num1);
        list($c, $d) = $this->parse($num2);
        $real = $a * $c - $b * $d;
        $imag = $a * $d + $b * $c;
        return $real . "+" . $imag . "i";
    }

    /**
     * @param String $num
     * @return int[]
     */
    private function parse($num) {
        $parts = explode("+", $num);
        $real = (int)$parts[0];
        $imag = (int)substr($parts[1], 0, -1);
        return [$real, $imag];
    }
}
