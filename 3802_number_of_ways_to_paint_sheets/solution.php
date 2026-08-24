<?php
// LeetCode 3802 - Number of Ways to Paint Sheets
// https://leetcode.com/problems/number-of-ways-to-paint-sheets/

class Solution {
    function numberOfWays($n, $limit) {
        $MOD = 1000000007;
        sort($limit);
        $points = [1, $n];
        foreach ($limit as $x) {
            if ($x + 1 > 1 && $x + 1 < $n) $points[] = $x + 1;
            if ($n - $x > 1 && $n - $x < $n) $points[] = $n - $x;
        }
        sort($points);
        $u = 0;
        for ($i = 0; $i < count($points); $i++) {
            if ($u === 0 || $points[$i] !== $points[$u - 1]) $points[$u++] = $points[$i];
        }
        $points = array_slice($points, 0, $u);
        $countGE = function($lim, $x) {
            $lo = 0;
            $hi = count($lim);
            while ($lo < $hi) {
                $mid = ($lo + $hi) >> 1;
                if ($lim[$mid] < $x) $lo = $mid + 1;
                else $hi = $mid;
            }
            return count($lim) - $lo;
        };
        $ans = 0;
        for ($i = 0; $i + 1 < count($points); $i++) {
            $x = $points[$i];
            $a = $countGE($limit, $x);
            $b = $countGE($limit, $n - $x);
            $same = $countGE($limit, max($x, $n - $x));
            $ways = ($a * $b - $same) % $MOD;
            $length = $points[$i + 1] - $x;
            $ans = ($ans + $ways * $length) % $MOD;
        }
        if ($ans < 0) $ans += $MOD;
        return $ans;
    }
}
