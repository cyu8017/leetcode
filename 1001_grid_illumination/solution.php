<?php
// LeetCode 1001 - Grid Illumination
// https://leetcode.com/problems/grid-illumination/

class Solution {
    /**
     * @param Integer $n
     * @param Integer[][] $lamps
     * @param Integer[][] $queries
     * @return Integer[]
     */
    function gridIllumination($n, $lamps, $queries) {
        $rows = [];
        $cols = [];
        $diag1 = [];
        $diag2 = [];
        $lit = [];
        foreach ($lamps as $lamp) {
            $r = $lamp[0];
            $c = $lamp[1];
            $key = $r . ',' . $c;
            if (isset($lit[$key])) {
                continue;
            }
            $lit[$key] = true;
            $rows[$r] = ($rows[$r] ?? 0) + 1;
            $cols[$c] = ($cols[$c] ?? 0) + 1;
            $diag1[$r - $c] = ($diag1[$r - $c] ?? 0) + 1;
            $diag2[$r + $c] = ($diag2[$r + $c] ?? 0) + 1;
        }
        $ans = [];
        foreach ($queries as $q) {
            $r = $q[0];
            $c = $q[1];
            $ans[] = (($rows[$r] ?? 0) || ($cols[$c] ?? 0) || ($diag1[$r - $c] ?? 0) || ($diag2[$r + $c] ?? 0)) ? 1 : 0;
            for ($i = $r - 1; $i <= $r + 1; $i++) {
                for ($j = $c - 1; $j <= $c + 1; $j++) {
                    $key = $i . ',' . $j;
                    if (isset($lit[$key])) {
                        unset($lit[$key]);
                        $rows[$i]--;
                        $cols[$j]--;
                        $diag1[$i - $j]--;
                        $diag2[$i + $j]--;
                    }
                }
            }
        }
        return $ans;
    }
}
