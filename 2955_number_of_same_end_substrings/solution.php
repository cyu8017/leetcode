<?php
// LeetCode 2955 - Number of Same-End Substrings
// https://leetcode.com/problems/number-of-same-end-substrings/

class Solution {
    function sameEndSubstringCount($s, $queries) {
        $n = strlen($s);
        $pref = [];
        $pref[0] = array_fill(0, 26, 0);
        for ($i = 0; $i < $n; $i++) {
            $pref[$i + 1] = $pref[$i];
            $pref[$i + 1][ord($s[$i]) - 97]++;
        }
        $ans = array_fill(0, count($queries), 0);
        for ($qi = 0; $qi < count($queries); $qi++) {
            $l = $queries[$qi][0];
            $r = $queries[$qi][1];
            $total = 0;
            for ($c = 0; $c < 26; $c++) {
                $cnt = $pref[$r + 1][$c] - $pref[$l][$c];
                $total += intdiv($cnt * ($cnt + 1), 2);
            }
            $ans[$qi] = $total;
        }
        return $ans;
    }
}
