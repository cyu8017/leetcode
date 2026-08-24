<?php
// LeetCode 3490 - Count Beautiful Numbers
// https://leetcode.com/problems/count-beautiful-numbers/

class Solution {
    private function countBeautiful($n) {
        if ($n <= 0) return 0;
        $s = strval($n);
        $dfs = null;
        $dfs = function($pos, $tight, $sum, $prod, $started) use (&$dfs, $s) {
            if ($pos === strlen($s)) {
                if (!$started) return 0;
                return ($sum > 0 && $prod % $sum === 0) ? 1 : 0;
            }
            $up = $tight ? (ord($s[$pos]) - 48) : 9;
            $ans = 0;
            for ($d = 0; $d <= $up; $d++) {
                $nt = $tight && $d === $up;
                if (!$started && $d === 0) $ans += $dfs($pos + 1, $nt, 0, 1, false);
                else {
                    $ns = $sum + $d;
                    $np = !$started ? $d : $prod * $d;
                    $ans += $dfs($pos + 1, $nt, $ns, $np, true);
                }
            }
            return $ans;
        };
        return $dfs(0, true, 0, 1, false);
    }

    function beautifulNumbers($l, $r) {
        return $this->countBeautiful($r) - $this->countBeautiful($l - 1);
    }
}
