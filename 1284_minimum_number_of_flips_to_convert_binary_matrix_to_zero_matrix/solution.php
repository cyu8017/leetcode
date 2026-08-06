<?php
// LeetCode 1284 - Minimum Number of Flips to Convert Binary Matrix to Zero Matrix
// https://leetcode.com/problems/minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix/

class Solution {
    /**
     * @param Integer[][] $mat
     * @return Integer
     */
    function minFlips($mat) {
        $m = count($mat);
        $n = count($mat[0]);
        $start = 0;
        for ($r = 0; $r < $m; $r++) {
            for ($c = 0; $c < $n; $c++) {
                $start |= $mat[$r][$c] << ($r * $n + $c);
            }
        }
        $masks = [];
        for ($r = 0; $r < $m; $r++) {
            for ($c = 0; $c < $n; $c++) {
                $mask = 0;
                foreach ([[0,0],[1,0],[-1,0],[0,1],[0,-1]] as [$dr, $dc]) {
                    $nr = $r + $dr; $nc = $c + $dc;
                    if ($nr >= 0 && $nr < $m && $nc >= 0 && $nc < $n) {
                        $mask ^= 1 << ($nr * $n + $nc);
                    }
                }
                $masks[] = $mask;
            }
        }
        $queue = [[$start, 0]];
        $seen = [$start => true];
        $head = 0;
        while ($head < count($queue)) {
            [$state, $distance] = $queue[$head++];
            if ($state === 0) return $distance;
            foreach ($masks as $mask) {
                $nxt = $state ^ $mask;
                if (!isset($seen[$nxt])) {
                    $seen[$nxt] = true;
                    $queue[] = [$nxt, $distance + 1];
                }
            }
        }
        return -1;
    }
}
