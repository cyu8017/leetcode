<?php
// LeetCode 3905 - Multi Source Flood Fill
// https://leetcode.com/problems/multi-source-flood-fill/

class Solution {
    function colorGrid($n, $m, $sources) {
        $ans = [];
        for ($i = 0; $i < $n; $i++) $ans[$i] = array_fill(0, $m, 0);
        $q = [];
        foreach ($sources as $s) $q[] = [$s[0], $s[1], $s[2]];
        $dirs = [-1, 0, 1, 0, -1];
        foreach ($q as $s) $ans[$s[0]][$s[1]] = $s[2];
        while (count($q)) {
            $vis = [];
            foreach ($q as $curr) {
                $r = $curr[0];
                $c = $curr[1];
                $color = $curr[2];
                for ($i = 0; $i < 4; $i++) {
                    $x = $r + $dirs[$i];
                    $y = $c + $dirs[$i + 1];
                    if ($x >= 0 && $x < $n && $y >= 0 && $y < $m && $ans[$x][$y] === 0) {
                        $key = $x . ',' . $y;
                        if (!isset($vis[$key]) || $color > $vis[$key]) $vis[$key] = $color;
                    }
                }
            }
            $q = [];
            foreach ($vis as $key => $color) {
                $parts = explode(',', $key);
                $x = intval($parts[0]);
                $y = intval($parts[1]);
                $ans[$x][$y] = $color;
                $q[] = [$x, $y, $color];
            }
        }
        return $ans;
    }
}
