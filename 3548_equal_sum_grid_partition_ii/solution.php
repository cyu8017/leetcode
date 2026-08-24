<?php
// LeetCode 3548 - Equal Sum Grid Partition II
// https://leetcode.com/problems/equal-sum-grid-partition-ii/

class Solution {
    private function rotate($grid) {
        $m = count($grid);
        $n = count($grid[0]);
        $t = [];
        for ($j = 0; $j < $n; $j++) $t[$j] = array_fill(0, $m, 0);
        for ($i = 0; $i < $m; $i++) for ($j = 0; $j < $n; $j++) $t[$j][$i] = $grid[$i][$j];
        return $t;
    }

    private function check($g) {
        $m = count($g);
        $n = count($g[0]);
        $s1 = 0;
        $s2 = 0;
        $cnt1 = [];
        $cnt2 = [];
        foreach ($g as $row) foreach ($row as $x) {
            $s2 += $x;
            $cnt2[$x] = ($cnt2[$x] ?? 0) + 1;
        }
        for ($i = 0; $i < $m - 1; $i++) {
            foreach ($g[$i] as $x) {
                $s1 += $x;
                $s2 -= $x;
                $cnt1[$x] = ($cnt1[$x] ?? 0) + 1;
                $cnt2[$x] = $cnt2[$x] - 1;
            }
            if ($s1 === $s2) return true;
            if ($s1 < $s2) {
                $diff = $s2 - $s1;
                if (($cnt2[$diff] ?? 0) > 0) {
                    if (($m - $i - 1 > 1 && $n > 1) ||
                        ($i === $m - 2 && ($g[$i + 1][0] === $diff || $g[$i + 1][$n - 1] === $diff)) ||
                        ($n === 1 && ($g[$i + 1][0] === $diff || $g[$m - 1][0] === $diff)))
                        return true;
                }
            } else {
                $diff = $s1 - $s2;
                if (($cnt1[$diff] ?? 0) > 0) {
                    if (($i + 1 > 1 && $n > 1) ||
                        ($i === 0 && ($g[0][0] === $diff || $g[0][$n - 1] === $diff)) ||
                        ($n === 1 && ($g[0][0] === $diff || $g[$i][0] === $diff)))
                        return true;
                }
            }
        }
        return false;
    }

    function canPartitionGrid($grid) {
        return $this->check($grid) || $this->check($this->rotate($grid));
    }
}
