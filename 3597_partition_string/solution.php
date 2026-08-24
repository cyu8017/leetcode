<?php
// LeetCode 3597 - Partition String
// https://leetcode.com/problems/partition-string/

class Solution {
    function partitionString($s) {
        $vis = [];
        $ans = [];
        $t = '';
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $t .= $s[$i];
            if (!isset($vis[$t])) {
                $vis[$t] = true;
                $ans[] = $t;
                $t = '';
            }
        }
        return $ans;
    }
}
