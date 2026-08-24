<?php
// LeetCode 3078 - Match Alphanumerical Pattern in Matrix I
// https://leetcode.com/problems/match-alphanumerical-pattern-in-matrix-i/

class Solution {
    public $board;
    public $pattern;
    public $r;
    public $c;
    function findPattern($board, $pattern) {
        $this->board = $board;
        $this->pattern = $pattern;
        $m = count($board);
        $n = count($board[0]);
        $this->r = count($pattern);
        $this->c = strlen($pattern[0]);
        for ($i = 0; $i < $m - $this->r + 1; $i++) {
            for ($j = 0; $j < $n - $this->c + 1; $j++) {
                if ($this->check($i, $j)) return [$i, $j];
            }
        }
        return [-1, -1];
    }
    function check($i, $j) {
        $d1 = array_fill(0, 26, 0);
        $d2 = array_fill(0, 10, 0);
        for ($a = 0; $a < $this->r; $a++) {
            for ($b = 0; $b < $this->c; $b++) {
                $x = $i + $a;
                $y = $j + $b;
                $ch = $this->pattern[$a][$b];
                if ($ch >= "0" && $ch <= "9") {
                    if (ord($ch) - 48 !== $this->board[$x][$y]) return false;
                } else {
                    $v = ord($ch) - 97;
                    if ($d1[$v] > 0 && $d1[$v] - 1 !== $this->board[$x][$y]) return false;
                    if ($d2[$this->board[$x][$y]] > 0 && $d2[$this->board[$x][$y]] - 1 !== $v) return false;
                    $d1[$v] = $this->board[$x][$y] + 1;
                    $d2[$this->board[$x][$y]] = $v + 1;
                }
            }
        }
        return true;
    }
}
