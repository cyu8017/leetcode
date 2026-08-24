<?php
// LeetCode 2326 - Spiral Matrix IV
// https://leetcode.com/problems/spiral-matrix-iv/

class ListNode {
    public $val = 0;
    public $next = null;
    function __construct($val = 0, $next = null) {
        $this->val = $val;
        $this->next = $next;
    }
}

class Solution {
    function spiralMatrix($m, $n, $head) {
        $ans = array_fill(0, $m, array_fill(0, $n, -1));
        $dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]];
        $r = 0;
        $c = 0;
        $d = 0;
        while ($head !== null) {
            $ans[$r][$c] = $head->val;
            $head = $head->next;
            $nr = $r + $dirs[$d][0];
            $nc = $c + $dirs[$d][1];
            if ($nr < 0 || $nr >= $m || $nc < 0 || $nc >= $n || $ans[$nr][$nc] !== -1) {
                $d = ($d + 1) % 4;
                $nr = $r + $dirs[$d][0];
                $nc = $c + $dirs[$d][1];
            }
            $r = $nr;
            $c = $nc;
        }
        return $ans;
    }
}
