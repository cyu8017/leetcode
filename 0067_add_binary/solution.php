<?php
// LeetCode 0067 - Add Binary
// https://leetcode.com/problems/add-binary/

class Solution {
    /**
     * @param String $a
     * @param String $b
     * @return String
     */
    function addBinary($a, $b) {
        $i = strlen($a) - 1;
        $j = strlen($b) - 1;
        $carry = 0;
        $result = [];

        while ($i >= 0 || $j >= 0 || $carry) {
            $total = $carry;
            if ($i >= 0) {
                $total += (int)$a[$i];
                $i--;
            }
            if ($j >= 0) {
                $total += (int)$b[$j];
                $j--;
            }
            $result[] = (string)($total % 2);
            $carry = intdiv($total, 2);
        }

        return implode('', array_reverse($result));
    }
}
