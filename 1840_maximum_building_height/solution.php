<?php
// LeetCode 1840 - Maximum Building Height
// https://leetcode.com/problems/maximum-building-height/

class Solution {
    /**
     * @param Integer $n
     * @param Integer[][] $restrictions
     * @return Integer
     */
    function maxBuilding($n, $restrictions) {
        $points = array_merge([[1, 0]], $restrictions);
        usort($points, function ($a, $b) {
            return $a[0] <=> $b[0];
        });
        if ($points[count($points) - 1][0] !== $n) {
            $points[] = [$n, $n - 1];
        }

        for ($i = 1; $i < count($points); $i++) {
            [$prevId, $prevHeight] = $points[$i - 1];
            [$currId, $currHeight] = $points[$i];
            $points[$i][1] = min($currHeight, $prevHeight + $currId - $prevId);
        }

        for ($i = count($points) - 2; $i >= 0; $i--) {
            [$nextId, $nextHeight] = $points[$i + 1];
            [$currId, $currHeight] = $points[$i];
            $points[$i][1] = min($currHeight, $nextHeight + $nextId - $currId);
        }

        $best = 0;
        foreach ($points as [, $height]) {
            $best = max($best, $height);
        }
        for ($i = 0; $i < count($points) - 1; $i++) {
            [$id1, $h1] = $points[$i];
            [$id2, $h2] = $points[$i + 1];
            $best = max($best, intdiv($h1 + $h2 + $id2 - $id1, 2));
        }

        return $best;
    }
}
