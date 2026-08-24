<?php
// LeetCode 3756 - Concatenate Non Zero Digits And Multiply By Sum II
// https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-ii/

class Solution {
    function sumAndMultiply($s, $queries) {
        $MX = 100001;
        $MOD = 1000000007;
        $PW = array_fill(0, $MX, 0);
        $PW[0] = 1;
        for ($i = 1; $i < $MX; $i++) $PW[$i] = ($PW[$i - 1] * 10) % $MOD;
        $n = strlen($s);
        $sumD = array_fill(0, $n + 1, 0);
        $cntN0 = array_fill(0, $n + 1, 0);
        $p = array_fill(0, $n + 1, 0);
        for ($i = 1; $i <= $n; $i++) {
            $d = ord($s[$i - 1]) - 48;
            $sumD[$i] = $sumD[$i - 1] + $d;
            $cntN0[$i] = $cntN0[$i - 1];
            if ($d > 0) {
                $cntN0[$i]++;
                $p[$i] = ($p[$i - 1] * 10 + $d) % $MOD;
            } else $p[$i] = $p[$i - 1];
        }
        $ans = array_fill(0, count($queries), 0);
        for ($i = 0; $i < count($queries); $i++) {
            $l = $queries[$i][0];
            $r = $queries[$i][1];
            $n0 = $cntN0[$r + 1] - $cntN0[$l];
            $sd = $sumD[$r + 1] - $sumD[$l];
            $x = ($p[$r + 1] - ($p[$l] * $PW[$n0]) % $MOD + $MOD) % $MOD;
            $ans[$i] = ($x * $sd) % $MOD;
        }
        return $ans;
    }
}
