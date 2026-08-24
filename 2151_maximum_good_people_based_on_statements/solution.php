<?php
// LeetCode 2151 - Maximum Good People Based on Statements
// https://leetcode.com/problems/maximum-good-people-based-on-statements/

class Solution {
    /**
     * @param Integer[][] $statements
     * @return Integer
     */
    function maximumGood($statements) {
        $n = count($statements);
        $ans = 0;
        for ($mask = 0; $mask < (1 << $n); $mask++) {
            $ok = true;
            for ($i = 0; $i < $n && $ok; $i++) {
                if (($mask & (1 << $i)) === 0) continue;
                for ($j = 0; $j < $n; $j++) {
                    $s = $statements[$i][$j];
                    if ($s === 2) continue;
                    $goodJ = ($mask & (1 << $j)) !== 0;
                    if (($s === 1 && !$goodJ) || ($s === 0 && $goodJ)) { $ok = false; break; }
                }
            }
            if ($ok) {
                $bc = 0;
                $x = $mask;
                while ($x) { $bc += $x & 1; $x >>= 1; }
                $ans = max($ans, $bc);
            }
        }
        return $ans;
    }
}
