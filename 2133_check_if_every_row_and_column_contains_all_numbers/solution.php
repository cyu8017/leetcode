<?php
// LeetCode 2133 - Check if Every Row and Column Contains All Numbers
// https://leetcode.com/problems/check-if-every-row-and-column-contains-all-numbers/

class Solution {
    /**
     * @param Integer[][] $matrix
     * @return Boolean
     */
    function checkValid($matrix) {
        $n = count($matrix);
        for ($i = 0; $i < $n; $i++) {
            $row = array_fill(0, $n + 1, false);
            $col = array_fill(0, $n + 1, false);
            for ($j = 0; $j < $n; $j++) {
                if ($row[$matrix[$i][$j]] || $col[$matrix[$j][$i]]) return false;
                $row[$matrix[$i][$j]] = true;
                $col[$matrix[$j][$i]] = true;
            }
        }
        return true;
    }
}
