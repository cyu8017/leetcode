<?php
// LeetCode 3621 - Number of Integers With Popcount Depth Equal to K I
// https://leetcode.com/problems/number-of-integers-with-popcount-depth-equal-to-k-i/

class Solution {
    function popcountDepth($n, $k) {
        if ($k === 0) return $n >= 1 ? 1 : 0;
        $bitCount = function($x) {
            $c = 0;
            while ($x) { $c += $x & 1; $x >>= 1; }
            return $c;
        };
        $depth = function($x) use ($bitCount) {
            if ($x <= 0) return 100;
            $d = 0;
            while ($x > 1) {
                $x = $bitCount($x);
                $d++;
            }
            return $d;
        };
        $s = '';
        for ($x = $n; $x > 0; $x = intdiv($x, 2)) $s .= (string)($x & 1);
        $s = strrev($s);
        if (strlen($s) === 0) $s = '0';
        $memo = [];
        $dfs = function($pos, $tight, $started, $pc) use (&$dfs, &$memo, $s, $k, $depth) {
            if ($pos === strlen($s)) {
                if ($started === 0) return 0;
                if ($pc === 1) return $k === 1 ? 1 : 0;
                return $depth($pc) === $k - 1 ? 1 : 0;
            }
            $key = $pos . ',' . $tight . ',' . $started . ',' . $pc;
            if (isset($memo[$key])) return $memo[$key];
            $up = $tight === 1 ? (int)$s[$pos] : 1;
            $res = 0;
            for ($dig = 0; $dig <= $up; $dig++) {
                $nt = ($tight === 1 && $dig === $up) ? 1 : 0;
                if ($started === 0 && $dig === 0) $res += $dfs($pos + 1, $nt, 0, 0);
                else $res += $dfs($pos + 1, $nt, 1, $pc + $dig);
            }
            $memo[$key] = $res;
            return $res;
        };
        $ans = $dfs(0, 1, 0, 0);
        // popcount==1 includes 1, whose depth is 0 not 1
        if ($k === 1) $ans -= 1;
        return $ans;
    }
}
