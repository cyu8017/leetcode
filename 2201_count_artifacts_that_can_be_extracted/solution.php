<?php
// LeetCode 2201 - Count Artifacts That Can Be Extracted
// https://leetcode.com/problems/count-artifacts-that-can-be-extracted/

class Solution {
    function digArtifacts($n, $artifacts, $dig) {
        $dug = [];
        foreach ($dig as $d) $dug[$d[0] . ',' . $d[1]] = true;
        $ans = 0;
        foreach ($artifacts as $a) {
            $ok = true;
            for ($r = $a[0]; $r <= $a[2] && $ok; $r++) {
                for ($c = $a[1]; $c <= $a[3]; $c++) {
                    if (!isset($dug[$r . ',' . $c])) { $ok = false; break; }
                }
            }
            if ($ok) $ans++;
        }
        return $ans;
    }
}
