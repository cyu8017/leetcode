<?php
// LeetCode 0850 - Rectangle Area II
// https://leetcode.com/problems/rectangle-area-ii/

class Solution {
    /**
     * @param Integer[][] $rectangles
     * @return Integer
     */
    function rectangleArea($rectangles) {
        $MOD = 1000000007;
        $events = [];
        foreach ($rectangles as $r) {
            $events[] = [$r[0], 1, $r[1], $r[3]];
            $events[] = [$r[2], -1, $r[1], $r[3]];
        }
        usort($events, function($a, $b) { return $a[0] <=> $b[0]; });
        $coveredLength = function($active) {
            if (!count($active)) return 0;
            $sorted = $active;
            usort($sorted, function($a, $b) { return $a[0] <=> $b[0]; });
            $total = 0;
            $curStart = $sorted[0][0];
            $curEnd = $sorted[0][1];
            $len = count($sorted);
            for ($i = 1; $i < $len; $i++) {
                $start = $sorted[$i][0];
                $end = $sorted[$i][1];
                if ($start > $curEnd) {
                    $total += $curEnd - $curStart;
                    $curStart = $start;
                    $curEnd = $end;
                } else {
                    $curEnd = max($curEnd, $end);
                }
            }
            $total += $curEnd - $curStart;
            return $total;
        };
        $active = [];
        $area = 0;
        $prevX = $events[0][0];
        foreach ($events as $e) {
            $x = $e[0];
            $typ = $e[1];
            $y1 = $e[2];
            $y2 = $e[3];
            $area += $coveredLength($active) * ($x - $prevX);
            if ($typ === 1) $active[] = [$y1, $y2];
            else {
                $len = count($active);
                for ($i = 0; $i < $len; $i++) {
                    if ($active[$i][0] === $y1 && $active[$i][1] === $y2) {
                        array_splice($active, $i, 1);
                        break;
                    }
                }
            }
            $prevX = $x;
        }
        return $area % $MOD;
    }
}
