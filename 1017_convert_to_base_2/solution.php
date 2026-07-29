<?php
// LeetCode 1017 - Convert to Base -2
// https://leetcode.com/problems/convert-to-base-2/

class Solution {
    /**
     * @param Integer $n
     * @return String
     */
    function baseNeg2($n) {
        if ($n === 0) {
            return '0';
        }
        $ans = [];
        while ($n !== 0) {
            $rem = $n % -2;
            $n = intdiv($n, -2);
            if ($rem < 0) {
                $n++;
                $rem += 2;
            }
            $ans[] = strval($rem);
        }
        return implode('', array_reverse($ans));
    }
}
