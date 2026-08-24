<?php
// LeetCode 3382 - Maximum Area Rectangle With Point Constraints II
// https://leetcode.com/problems/maximum-area-rectangle-with-point-constraints-ii/

class Solution {
    function pack($x, $y) {
        return $x . ',' . $y;
    }

    function maxRectangleArea($xCoord, $yCoord) {
        $n = count($xCoord);
        $points = [];
        for ($i = 0; $i < $n; $i++) $points[] = [$xCoord[$i], $yCoord[$i]];
        $set = [];
        foreach ($points as $p) $set[$this->pack($p[0], $p[1])] = true;
        $ans = -1;
        for ($i = 0; $i < $n; $i++) {
            for ($j = $i + 1; $j < $n; $j++) {
                $x1 = $points[$i][0];
                $y1 = $points[$i][1];
                $x2 = $points[$j][0];
                $y2 = $points[$j][1];
                if ($x1 === $x2 || $y1 === $y2) continue;
                if (!isset($set[$this->pack($x1, $y2)]) || !isset($set[$this->pack($x2, $y1)])) continue;
                $minX = min($x1, $x2);
                $maxX = max($x1, $x2);
                $minY = min($y1, $y2);
                $maxY = max($y1, $y2);
                $ok = true;
                foreach ($points as $p) {
                    $x = $p[0];
                    $y = $p[1];
                    if ($x > $minX && $x < $maxX && $y > $minY && $y < $maxY) { $ok = false; break; }
                    $onBorder = (($x === $minX || $x === $maxX) && $y >= $minY && $y <= $maxY) ||
                            (($y === $minY || $y === $maxY) && $x >= $minX && $x <= $maxX);
                    if ($onBorder) {
                        $isCorner = ($x === $minX || $x === $maxX) && ($y === $minY || $y === $maxY);
                        if (!$isCorner) { $ok = false; break; }
                    }
                }
                if ($ok) {
                    $area = ($maxX - $minX) * ($maxY - $minY);
                    if ($area > $ans) $ans = $area;
                }
            }
        }
        return $ans;
    }
}
