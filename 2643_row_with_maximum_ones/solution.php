<?php
// LeetCode 2643 - Row With Maximum Ones
// https://leetcode.com/problems/row-with-maximum-ones/

class Solution {
    function rowAndMaximumOnes($mat) {
        $bestRow = 0;
        $bestCnt = -1;
        for ($i = 0; $i < count($mat); $i++) {
            $cnt = 0;
            foreach ($mat[$i] as $v) $cnt += $v;
            if ($cnt > $bestCnt) { $bestCnt = $cnt; $bestRow = $i; }
        }
        return [$bestRow, $bestCnt];
    }
}
