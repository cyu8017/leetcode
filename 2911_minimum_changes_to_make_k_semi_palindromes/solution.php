<?php
// LeetCode 2911 - Minimum Changes to Make K Semi-palindromes
// https://leetcode.com/problems/minimum-changes-to-make-k-semi-palindromes/

class Solution {
    function minimumChanges($s, $k) {
        $n = strlen($s);
        $INF = 1 << 20;
        $cost = [];
        for ($i = 0; $i < $n; $i++) $cost[$i] = array_fill(0, $n, $INF);
        for ($i = 0; $i < $n; $i++)
            for ($j = $i + 1; $j < $n; $j++)
                $cost[$i][$j] = $this->semiCost($s, $i, $j, $INF);
        $dp = [];
        for ($p = 0; $p <= $k; $p++) $dp[$p] = array_fill(0, $n + 1, $INF);
        $dp[0][0] = 0;
        for ($p = 1; $p <= $k; $p++)
            for ($i = 1; $i <= $n; $i++)
                for ($t = 0; $t < $i - 1; $t++) {
                    $cand = $dp[$p - 1][$t] + $cost[$t][$i - 1];
                    if ($cand < $dp[$p][$i]) $dp[$p][$i] = $cand;
                }
        return $dp[$k][$n];
    }

    private function semiCost($s, $l, $r, $INF) {
        $length = $r - $l + 1;
        $best = $INF;
        for ($d = 1; $d < $length; $d++) {
            if ($length % $d !== 0) continue;
            $chg = 0;
            for ($start = 0; $start < $d; $start++) {
                $chars = [];
                for ($i = $l + $start; $i <= $r; $i += $d) $chars[] = $s[$i];
                $i = 0;
                $j = count($chars) - 1;
                while ($i < $j) {
                    if ($chars[$i] !== $chars[$j]) $chg++;
                    $i++;
                    $j--;
                }
            }
            if ($chg < $best) $best = $chg;
        }
        return $best;
    }
}
