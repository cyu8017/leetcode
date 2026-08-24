<?php
// LeetCode 3193 - Count the Number of Inversions
// https://leetcode.com/problems/count-the-number-of-inversions/

class Solution {
    function numberOfPermutations($n, $requirements) {
        $req = array_fill(0, $n, -1);
        foreach ($requirements as $r) $req[$r[0]] = $r[1];
        if ($req[0] > 0) return 0;
        $req[0] = 0;
        $m = 0;
        foreach ($req as $v) $m = max($m, $v);
        $mod = 1000000007;
        $f = [];
        for ($i = 0; $i < $n; $i++) $f[$i] = array_fill(0, $m + 1, 0);
        $f[0][0] = 1;
        for ($i = 1; $i < $n; $i++) {
            $l = 0;
            $r = $m;
            if ($req[$i] >= 0) { $l = $req[$i]; $r = $req[$i]; }
            for ($j = $l; $j <= $r; $j++) {
                for ($k = 0; $k <= min($i, $j); $k++) {
                    $f[$i][$j] = ($f[$i][$j] + $f[$i - 1][$j - $k]) % $mod;
                }
            }
        }
        return $f[$n - 1][$req[$n - 1]];
    }
}
