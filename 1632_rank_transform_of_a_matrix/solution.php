<?php
// LeetCode 1632 - Rank Transform of a Matrix
// https://leetcode.com/problems/rank-transform-of-a-matrix/

class Solution {
    /**
     * @param Integer[][] $matrix
     * @return Integer[][]
     */
    function matrixRankTransform($matrix) {
        $m = count($matrix);
        $n = count($matrix[0]);
        $groups = [];
        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                $groups[$matrix[$i][$j]][] = [$i, $j];
            }
        }
        ksort($groups, SORT_NUMERIC);
        $rank = array_fill(0, $m + $n, 0);
        $ans = array_fill(0, $m, array_fill(0, $n, 0));
        foreach ($groups as $cells) {
            $parent = [];
            $find = function ($x) use (&$parent, &$find) {
                if (!isset($parent[$x])) {
                    $parent[$x] = $x;
                }
                if ($parent[$x] !== $x) {
                    $parent[$x] = $find($parent[$x]);
                }
                return $parent[$x];
            };
            foreach ($cells as [$i, $j]) {
                $a = $find($i);
                $b = $find($m + $j);
                $parent[$a] = $b;
            }
            $best = [];
            foreach ($cells as [$i, $j]) {
                $r = $find($i);
                $best[$r] = max($best[$r] ?? 0, $rank[$i], $rank[$m + $j]);
            }
            foreach ($cells as [$i, $j]) {
                $ans[$i][$j] = $best[$find($i)] + 1;
            }
            foreach ($cells as [$i, $j]) {
                $rank[$i] = max($rank[$i], $ans[$i][$j]);
                $rank[$m + $j] = max($rank[$m + $j], $ans[$i][$j]);
            }
        }
        return $ans;
    }
}
