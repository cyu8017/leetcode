<?php
// LeetCode 3858 - Minimum Bitwise OR From Grid
// https://leetcode.com/problems/minimum-bitwise-or-from-grid/

class Solution {
    function bitLen($x) {
        if ($x === 0) return 0;
        $n = 0;
        while ($x > 0) { $n++; $x >>= 1; }
        return $n;
    }
    function minimumOR($grid) {
        $mx = 0;
        foreach ($grid as $row) foreach ($row as $x) $mx = max($mx, $x);
        $m = $this->bitLen($mx);
        $ans = 0;
        for ($i = $m - 1; $i >= 0; $i--) {
            $mask = $ans | ((1 << $i) - 1);
            foreach ($grid as $row) {
                $found = false;
                foreach ($row as $x) {
                    if (($x | $mask) === $mask) { $found = true; break; }
                }
                if (!$found) {
                    $ans |= 1 << $i;
                    break;
                }
            }
        }
        return $ans;
    }
}
