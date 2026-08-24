<?php
// LeetCode 2018 - Check if Word Can Be Placed In Crossword
// https://leetcode.com/problems/check-if-word-can-be-placed-in-crossword/

class Solution {
    /**
     * @param String[][] $board
     * @param String $word
     * @return Boolean
     */
    function placeWordInCrossword($board, $word) {
        $m = count($board);
        $n = count($board[0]);
        $L = strlen($word);
        $match = function ($cells) use ($word, $L) {
            if (strlen($cells) !== $L) return false;
            $ok1 = true;
            $ok2 = true;
            for ($i = 0; $i < $L; $i++) {
                if ($cells[$i] !== ' ' && $cells[$i] !== $word[$i]) $ok1 = false;
                if ($cells[$i] !== ' ' && $cells[$i] !== $word[$L - 1 - $i]) $ok2 = false;
            }
            return $ok1 || $ok2;
        };
        for ($r = 0; $r < $m; $r++) {
            $c = 0;
            while ($c < $n) {
                while ($c < $n && $board[$r][$c] === '#') $c++;
                $start = $c;
                while ($c < $n && $board[$r][$c] !== '#') $c++;
                if ($c - $start === $L) {
                    $sb = "";
                    for ($i = $start; $i < $c; $i++) $sb .= $board[$r][$i];
                    if ($match($sb)) return true;
                }
            }
        }
        for ($c = 0; $c < $n; $c++) {
            $r = 0;
            while ($r < $m) {
                while ($r < $m && $board[$r][$c] === '#') $r++;
                $start = $r;
                while ($r < $m && $board[$r][$c] !== '#') $r++;
                if ($r - $start === $L) {
                    $sb = "";
                    for ($i = 0; $i < $L; $i++) $sb .= $board[$start + $i][$c];
                    if ($match($sb)) return true;
                }
            }
        }
        return false;
    }
}
