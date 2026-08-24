<?php
// LeetCode 3625 - Count Number of Trapezoids II
// https://leetcode.com/problems/count-number-of-trapezoids-ii/

class Solution {
    function countTrapezoids($points) {
        $n = count($points);
        $cnt1 = [];
        $cnt2 = [];
        $fkey = function($x) {
            return is_int($x) || (is_float($x) && $x == (int)$x) ? (string)(int)$x : sprintf('%.12g', $x);
        };
        for ($i = 0; $i < $n; $i++) {
            $x1 = $points[$i][0];
            $y1 = $points[$i][1];
            for ($j = 0; $j < $i; $j++) {
                $x2 = $points[$j][0];
                $y2 = $points[$j][1];
                $dx = $x2 - $x1;
                $dy = $y2 - $y1;
                if ($dx === 0) {
                    $k = 1e9;
                    $b = $x1;
                } else {
                    $k = $dy / $dx;
                    $b = ($y1 * $dx - $x1 * $dy) / $dx;
                }
                $sk = $fkey($k);
                $sb = $fkey($b);
                if (!isset($cnt1[$sk])) $cnt1[$sk] = [];
                if (!isset($cnt1[$sk][$sb])) $cnt1[$sk][$sb] = 0;
                $cnt1[$sk][$sb]++;
                $p = ($x1 + $x2 + 2000) * 4000 + ($y1 + $y2 + 2000);
                if (!isset($cnt2[$p])) $cnt2[$p] = [];
                if (!isset($cnt2[$p][$sk])) $cnt2[$p][$sk] = 0;
                $cnt2[$p][$sk]++;
            }
        }
        $ans = 0;
        foreach ($cnt1 as $e) {
            $s = 0;
            foreach ($e as $t) {
                $ans += $s * $t;
                $s += $t;
            }
        }
        foreach ($cnt2 as $e) {
            $s = 0;
            foreach ($e as $t) {
                $ans -= $s * $t;
                $s += $t;
            }
        }
        return $ans;
    }
}
