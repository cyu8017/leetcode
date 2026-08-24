<?php
// LeetCode 0397 - Integer Replacement
// https://leetcode.com/problems/integer-replacement/

class Solution {
    /**
     * @param Integer $n
     * @return Integer
     */
    function integerReplacement($n) {
        return $this->integer_replacement($n);
    }

    /**
     * @param Integer $n
     * @return Integer
     */
    function integer_replacement($n) {
        $steps = 0;
        while ($n !== 1) {
            if ($n % 2 === 0) {
                $n = intdiv($n, 2);
            } elseif ($n === 3 || $n % 4 === 1) {
                $n--;
            } else {
                $n++;
            }
            $steps++;
        }
        return $steps;
    }
}
