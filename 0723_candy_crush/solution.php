<?php
// LeetCode 0723 - Candy Crush
// https://leetcode.com/problems/candy-crush/

class Solution {
    function candyCrush($board) {
        $m = count($board);
        $n = count($board[0]);
        $stable = false;
        while (!$stable) {
            $stable = true;
            for ($i = 0; $i < $m; $i++) {
                for ($j = 0; $j < $n - 2; $j++) {
                    $value = abs($board[$i][$j]);
                    if ($value !== 0 && $value === abs($board[$i][$j + 1]) && $value === abs($board[$i][$j + 2])) {
                        $board[$i][$j] = $board[$i][$j + 1] = $board[$i][$j + 2] = -$value;
                        $stable = false;
                    }
                }
            }
            for ($j = 0; $j < $n; $j++) {
                for ($i = 0; $i < $m - 2; $i++) {
                    $value = abs($board[$i][$j]);
                    if ($value !== 0 && $value === abs($board[$i + 1][$j]) && $value === abs($board[$i + 2][$j])) {
                        $board[$i][$j] = $board[$i + 1][$j] = $board[$i + 2][$j] = -$value;
                        $stable = false;
                    }
                }
            }
            for ($j = 0; $j < $n; $j++) {
                $write = $m - 1;
                for ($i = $m - 1; $i >= 0; $i--) {
                    if ($board[$i][$j] > 0) $board[$write--][$j] = $board[$i][$j];
                }
                for ($i = $write; $i >= 0; $i--) $board[$i][$j] = 0;
            }
        }
        return $board;
    }
}
