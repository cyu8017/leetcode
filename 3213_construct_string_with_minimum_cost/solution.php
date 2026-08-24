<?php
// LeetCode 3213 - Construct String with Minimum Cost
// https://leetcode.com/problems/construct-string-with-minimum-cost/

class Solution {
    function minimumCost($target, $words, $costs) {
        $bas = 13331;
        $mod = 998244353;
        $inf = intdiv(PHP_INT_MAX, 2);
        $n = strlen($target);
        $p = array_fill(0, $n + 1, 0);
        $h = array_fill(0, $n + 1, 0);
        $p[0] = 1;
        $h[0] = 0;
        for ($i = 1; $i <= $n; $i++) {
            $p[$i] = ($p[$i - 1] * $bas) % $mod;
            $h[$i] = ($h[$i - 1] * $bas + ord($target[$i - 1])) % $mod;
        }
        $f = array_fill(0, $n + 1, $inf);
        $f[0] = 0;
        $ss = [];
        foreach ($words as $w) $ss[strlen($w)] = true;
        $lengths = array_keys($ss);
        sort($lengths);
        $d = [];
        for ($i = 0; $i < count($words); $i++) {
            $x = 0;
            $len = strlen($words[$i]);
            for ($c = 0; $c < $len; $c++) $x = ($x * $bas + ord($words[$i][$c])) % $mod;
            if (!isset($d[$x]) || $costs[$i] < $d[$x]) $d[$x] = $costs[$i];
        }
        for ($i = 1; $i <= $n; $i++) {
            foreach ($lengths as $j) {
                if ($j > $i) break;
                $x = ($h[$i] - ($h[$i - $j] * $p[$j]) % $mod + $mod) % $mod;
                if (isset($d[$x])) $f[$i] = min($f[$i], $f[$i - $j] + $d[$x]);
            }
        }
        return $f[$n] >= $inf ? -1 : $f[$n];
    }
}
