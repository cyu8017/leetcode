<?php
// LeetCode 2120 - Execution of All Suffix Instructions Staying in a Grid
// https://leetcode.com/problems/execution-of-all-suffix-instructions-staying-in-a-grid/

class Solution {
    /**
     * @param Integer $n
     * @param Integer[] $startPos
     * @param String $s
     * @return Integer[]
     */
    function executeInstructions($n, $startPos, $s) {
        $m = strlen($s);
        $ans = array_fill(0, $m, 0);
        for ($i = 0; $i < $m; $i++) {
            $r = $startPos[0];
            $c = $startPos[1];
            $cnt = 0;
            for ($j = $i; $j < $m; $j++) {
                $ch = $s[$j];
                if ($ch === 'L') $c--;
                else if ($ch === 'R') $c++;
                else if ($ch === 'U') $r--;
                else $r++;
                if ($r < 0 || $r >= $n || $c < 0 || $c >= $n) break;
                $cnt++;
            }
            $ans[$i] = $cnt;
        }
        return $ans;
    }
}
