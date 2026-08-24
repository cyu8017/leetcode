<?php
// LeetCode 3964 - Minimum Lights To Illuminate A Road
// https://leetcode.com/problems/minimum-lights-to-illuminate-a-road/

class Solution {
    function minLights($lights) {
        $n = count($lights);
        $d = array_fill(0, $n, 0);
        for ($i = 0; $i < $n; $i++) {
            $v = $lights[$i];
            if ($v > 0) {
                $l = max(0, $i - $v);
                $r = min($n - 1, $i + $v);
                $d[$l]++;
                if ($r + 1 < $n) $d[$r + 1]--;
            }
        }
        $s = 0;
        $cnt = 0;
        $ans = 0;
        foreach ($d as $x) {
            $s += $x;
            if ($s == 0) $cnt++;
            else {
                $ans += intdiv($cnt + 2, 3);
                $cnt = 0;
            }
        }
        $ans += intdiv($cnt + 2, 3);
        return $ans;
    }
}
