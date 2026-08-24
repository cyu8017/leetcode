<?php
// LeetCode 2194 - Cells in a Range on an Excel Sheet
// https://leetcode.com/problems/cells-in-a-range-on-an-excel-sheet/

class Solution {
    /**
     * @param String $s
     * @return String[]
     */
    function cellsInRange($s) {
        $ans = [];
        for ($c = ord($s[0]); $c <= ord($s[3]); $c++)
            for ($r = ord($s[1]); $r <= ord($s[4]); $r++)
                $ans[] = chr($c) . chr($r);
        return $ans;
    }
}
