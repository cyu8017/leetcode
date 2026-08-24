<?php
// LeetCode 3839 - Number of Prefix Connected Groups
// https://leetcode.com/problems/number-of-prefix-connected-groups/

class Solution {
    function prefixConnected($words, $k) {
        $cnt = [];
        foreach ($words as $w) {
            if (strlen($w) >= $k) {
                $p = substr($w, 0, $k);
                $cnt[$p] = ($cnt[$p] ?? 0) + 1;
            }
        }
        $ans = 0;
        foreach ($cnt as $v) if ($v > 1) $ans++;
        return $ans;
    }
}
