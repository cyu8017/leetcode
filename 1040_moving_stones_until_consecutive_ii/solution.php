<?php
// LeetCode 1040 - Moving Stones Until Consecutive II
// https://leetcode.com/problems/moving-stones-until-consecutive-ii/

class Solution {
    /**
     * @param Integer[] $stones
     * @return Integer[]
     */
    function numMovesStonesII($stones) {
        sort($stones);
        $n = count($stones);
        $maxMoves = max(
            $stones[$n - 1] - $stones[1] - $n + 2,
            $stones[$n - 2] - $stones[0] - $n + 2
        );
        $minMoves = $maxMoves;
        $i = 0;
        for ($j = 0; $j < $n; $j++) {
            while ($stones[$j] - $stones[$i] + 1 > $n) {
                $i++;
            }
            $inside = $j - $i + 1;
            if ($inside === $n - 1 && $stones[$j] - $stones[$i] + 1 === $n - 1) {
                $minMoves = min($minMoves, 2);
            } else {
                $minMoves = min($minMoves, $n - $inside);
            }
        }
        return [$minMoves, $maxMoves];
    }
}
