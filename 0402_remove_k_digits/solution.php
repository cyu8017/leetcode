<?php
// LeetCode 0402 - Remove K Digits
// https://leetcode.com/problems/remove-k-digits/

class Solution {
    /**
     * @param String $num
     * @param Integer $k
     * @return String
     */
    function removeKdigits($num, $k) {
        return $this->remove_kdigits($num, $k);
    }

    /**
     * @param String $num
     * @param Integer $k
     * @return String
     */
    function remove_kdigits($num, $k) {
        $stack = [];
        $length = strlen($num);
        for ($index = 0; $index < $length; $index++) {
            $digit = $num[$index];
            while ($k > 0 && count($stack) > 0 && $stack[count($stack) - 1] > $digit) {
                array_pop($stack);
                $k--;
            }
            $stack[] = $digit;
        }

        if ($k > 0) {
            $stack = array_slice($stack, 0, count($stack) - $k);
        }

        $result = ltrim(implode("", $stack), "0");
        return $result === "" ? "0" : $result;
    }
}
