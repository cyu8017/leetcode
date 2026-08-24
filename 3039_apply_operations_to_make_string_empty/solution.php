<?php
// LeetCode 3039 - Apply Operations to Make String Empty
// https://leetcode.com/problems/apply-operations-to-make-string-empty/

class Solution {
    function lastNonEmptyString($s) {
        $cnt = array_fill(0, 26, 0);
        $last = array_fill(0, 26, 0);
        $mx = 0;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $c = ord($s[$i]) - 97;
            $cnt[$c]++;
            $last[$c] = $i;
            $mx = max($mx, $cnt[$c]);
        }
        $ans = '';
        for ($i = 0; $i < $n; $i++) {
            $c = ord($s[$i]) - 97;
            if ($cnt[$c] === $mx && $last[$c] === $i) $ans .= $s[$i];
        }
        return $ans;
    }
}
