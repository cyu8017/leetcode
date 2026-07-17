<?php
// LeetCode 1759 - Count Number of Homogenous Substrings
// https://leetcode.com/problems/count-number-of-homogenous-substrings/

class Solution {
    /**
     * @param String $s
     * @return Integer
     */
    function countHomogenous($s) {
        $mod = 1000000007;
        $n = strlen($s);
        $ans = 0;
        $i = 0;
        while ($i < $n) {
            $j = $i;
            while ($j < $n && $s[$j] === $s[$i]) {
                $j++;
            }
            $length = $j - $i;
            $ans = ($ans + intdiv($length * ($length + 1), 2)) % $mod;
            $i = $j;
        }
        return $ans;
    }
}
