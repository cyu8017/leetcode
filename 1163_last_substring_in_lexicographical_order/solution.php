<?php
// LeetCode 1163 - Last Substring in Lexicographical Order
// https://leetcode.com/problems/last-substring-in-lexicographical-order/

class Solution {
    /**
     * @param String $s
     * @return String
     */
    function lastSubstring($s) {
        $i = 0; $j = 1; $k = 0;
        $n = strlen($s);
        while ($j + $k < $n) {
            if ($s[$i + $k] === $s[$j + $k]) {
                $k++;
                continue;
            }
            if ($s[$i + $k] > $s[$j + $k]) {
                $j = $j + $k + 1;
            } else {
                $i = max($i + $k + 1, $j);
                $j = $i + 1;
            }
            $k = 0;
        }
        return substr($s, $i);
    }
}
