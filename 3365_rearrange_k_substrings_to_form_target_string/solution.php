<?php
// LeetCode 3365 - Rearrange K Substrings to Form Target String
// https://leetcode.com/problems/rearrange-k-substrings-to-form-target-string/

class Solution {
    function isPossibleToRearrange($s, $t, $k) {
        $n = strlen($s);
        $sz = intdiv($n, $k);
        $cnt = [];
        for ($i = 0; $i < $n; $i += $sz) {
            $a = substr($s, $i, $sz);
            $b = substr($t, $i, $sz);
            $cnt[$a] = ($cnt[$a] ?? 0) + 1;
            $cnt[$b] = ($cnt[$b] ?? 0) - 1;
        }
        foreach ($cnt as $v) if ($v !== 0) return false;
        return true;
    }
}
