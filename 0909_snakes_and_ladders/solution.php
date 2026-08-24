<?php
// LeetCode 0909 - Snakes and Ladders
// https://leetcode.com/problems/snakes-and-ladders/

class Solution {
    function snakesAndLadders($board) {
        $n = count($board);
        $target = $n * $n;
        $pos = function ($square) use ($n) {
            $square--;
            $row = intdiv($square, $n);
            $rem = $square % $n;
            $r = $n - 1 - $row;
            $c = $row % 2 === 0 ? $rem : $n - 1 - $rem;
            return [$r, $c];
        };
        $q = [1];
        $seen = array_fill(0, $target + 1, false);
        $seen[1] = true;
        $moves = 0;
        while ($q) {
            $sz = count($q);
            for ($s = 0; $s < $sz; $s++) {
                $cur = array_shift($q);
                if ($cur === $target) return $moves;
                $lim = min($cur + 6, $target);
                for ($nxt = $cur + 1; $nxt <= $lim; $nxt++) {
                    [$r, $c] = $pos($nxt);
                    $dest = $board[$r][$c] !== -1 ? $board[$r][$c] : $nxt;
                    if (!$seen[$dest]) {
                        $seen[$dest] = true;
                        $q[] = $dest;
                    }
                }
            }
            $moves++;
        }
        return -1;
    }
}
