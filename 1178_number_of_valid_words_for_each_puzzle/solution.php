<?php
// LeetCode 1178 - Number of Valid Words for Each Puzzle
// https://leetcode.com/problems/number-of-valid-words-for-each-puzzle/

class Solution {
    /**
     * @param String[] $words
     * @param String[] $puzzles
     * @return Integer[]
     */
    function findNumOfValidWords($words, $puzzles) {
        $maskOf = function ($s) {
            $mask = 0;
            $n = strlen($s);
            for ($i = 0; $i < $n; $i++) $mask |= 1 << (ord($s[$i]) - 97);
            return $mask;
        };
        $freq = [];
        foreach ($words as $w) {
            $m = $maskOf($w);
            $freq[$m] = ($freq[$m] ?? 0) + 1;
        }
        $ans = [];
        foreach ($puzzles as $puzzle) {
            $first = 1 << (ord($puzzle[0]) - 97);
            $full = $maskOf($puzzle);
            $sub = $full;
            $total = 0;
            while (true) {
                if ($sub & $first) $total += $freq[$sub] ?? 0;
                if ($sub === 0) break;
                $sub = ($sub - 1) & $full;
            }
            $ans[] = $total;
        }
        return $ans;
    }
}
