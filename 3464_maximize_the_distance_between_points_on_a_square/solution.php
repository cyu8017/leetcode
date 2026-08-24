<?php
// LeetCode 3464 - Maximize the Distance Between Points on a Square
// https://leetcode.com/problems/maximize-the-distance-between-points-on-a-square/

class Solution {
    private function canPlace($arr, $perim, $mid, $k) {
        $n = count($arr);
        for ($s = 0; $s < $n; $s++) {
            $cnt = 1;
            $last = $arr[$s];
            $idx = $s;
            for (; $cnt < $k; ) {
                $target = $last + $mid;
                $found = false;
                for ($step = 1; $step < $n; $step++) {
                    $ni = ($idx + $step) % $n;
                    $val = $arr[$ni];
                    $add = $ni <= $idx ? $perim : 0;
                    if ($val + $add >= $target) {
                        $last = $val + $add;
                        $idx = $ni;
                        $cnt++;
                        $found = true;
                        break;
                    }
                }
                if (!$found) break;
            }
            if ($cnt === $k && $last - $arr[$s] <= $perim - $mid) return true;
        }
        return false;
    }

    function maxDistance($side, $points, $k) {
        $arr = array_fill(0, count($points), 0);
        for ($i = 0; $i < count($points); $i++) {
            $x = $points[$i][0];
            $y = $points[$i][1];
            if ($y === 0) $d = $x;
            else if ($x === $side) $d = $side + $y;
            else if ($y === $side) $d = 2 * $side + ($side - $x);
            else $d = 3 * $side + ($side - $y);
            $arr[$i] = $d;
        }
        sort($arr);
        $perim = 4 * $side;
        $lo = 0;
        $hi = 2 * $side;
        while ($lo < $hi) {
            $mid = intdiv($lo + $hi + 1, 2);
            if ($this->canPlace($arr, $perim, $mid, $k)) $lo = $mid;
            else $hi = $mid - 1;
        }
        return $lo;
    }
}
