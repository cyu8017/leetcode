<?php
// LeetCode 0791 - Custom Sort String
// https://leetcode.com/problems/custom-sort-string/

class Solution {
    /**
     * @param String $order
     * @param String $s
     * @return String
     */
    function customSortString($order, $s) {
        $count = array_fill(0, 26, 0);
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) $count[ord($s[$i]) - 97]++;
        $sb = "";
        $on = strlen($order);
        for ($i = 0; $i < $on; $i++) {
            $ch = $order[$i];
            $idx = ord($ch) - 97;
            while ($count[$idx]-- > 0) $sb .= $ch;
        }
        for ($i = 0; $i < 26; $i++) {
            while ($count[$i]-- > 0) $sb .= chr(97 + $i);
        }
        return $sb;
    }
}
