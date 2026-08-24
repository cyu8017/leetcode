<?php
// LeetCode 0864 - Shortest Path to Get All Keys
// https://leetcode.com/problems/shortest-path-to-get-all-keys/

class Solution {
    /**
     * @param String[] $grid
     * @return Integer
     */
    function shortestPathAllKeys($grid) {
        $m = count($grid);
        $n = strlen($grid[0]);
        $allKeys = 0;
        $sr = 0;
        $sc = 0;
        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                $ch = $grid[$i][$j];
                if ($ch === '@') { $sr = $i; $sc = $j; }
                elseif ($ch >= 'a' && $ch <= 'f') $allKeys |= 1 << (ord($ch) - 97);
            }
        }
        $encode = function($r, $c, $mask) {
            return ($r << 20) | ($c << 10) | $mask;
        };
        $queue = [[$sr, $sc, 0, 0]];
        $seen = [$encode($sr, $sc, 0) => true];
        $dr = [1, -1, 0, 0];
        $dc = [0, 0, 1, -1];
        $qi = 0;
        while ($qi < count($queue)) {
            $r = $queue[$qi][0];
            $c = $queue[$qi][1];
            $mask = $queue[$qi][2];
            $dist = $queue[$qi][3];
            $qi++;
            if ($mask === $allKeys) return $dist;
            for ($k = 0; $k < 4; $k++) {
                $nr = $r + $dr[$k];
                $nc = $c + $dc[$k];
                if ($nr < 0 || $nr >= $m || $nc < 0 || $nc >= $n || $grid[$nr][$nc] === '#') continue;
                $cell = $grid[$nr][$nc];
                $nmask = $mask;
                if ($cell >= 'a' && $cell <= 'f') $nmask |= 1 << (ord($cell) - 97);
                if ($cell >= 'A' && $cell <= 'F' && ($mask & (1 << (ord($cell) - 65))) === 0) continue;
                $key = $encode($nr, $nc, $nmask);
                if (!isset($seen[$key])) {
                    $seen[$key] = true;
                    $queue[] = [$nr, $nc, $nmask, $dist + 1];
                }
            }
        }
        return -1;
    }
}
