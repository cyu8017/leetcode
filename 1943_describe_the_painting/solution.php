<?php

class Solution {
    /**
     * @param Integer[][] $segments
     * @return Integer[][]
     */
    function splitPainting($segments) {
        $diff = [];
        foreach ($segments as $seg) {
            $s = $seg[0];
            $e = $seg[1];
            $c = $seg[2];
            $diff[$s] = ($diff[$s] ?? 0) + $c;
            $diff[$e] = ($diff[$e] ?? 0) - $c;
        }
        $points = array_keys($diff);
        sort($points);
        $ans = [];
        $cur = 0;
        $len = count($points);
        for ($i = 0; $i < $len - 1; $i++) {
            $cur += $diff[$points[$i]];
            if ($cur !== 0) {
                $ans[] = [$points[$i], $points[$i + 1], $cur];
            }
        }
        return $ans;
    }
}
