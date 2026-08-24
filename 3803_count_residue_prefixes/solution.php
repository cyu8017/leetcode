<?php
// LeetCode 3803 - Count Residue Prefixes
// https://leetcode.com/problems/count-residue-prefixes/

class Solution {
    function residuePrefixes($s) {
        $st = [];
        $ans = 0;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $st[$s[$i]] = true;
            if (count($st) === ($i + 1) % 3) $ans++;
        }
        return $ans;
    }
}
