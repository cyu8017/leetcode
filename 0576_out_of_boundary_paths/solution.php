<?php
// LeetCode 0576 - Out of Boundary Paths
// https://leetcode.com/problems/out-of-boundary-paths/

class Solution {
    function findPaths($m, $n, $maxMove, $startRow, $startColumn) {
        $MOD = 1000000007;
        $dp = [];
        for ($i = 0; $i < $m; ++$i) $dp[$i] = array_fill(0, $n, 0);
        $dp[$startRow][$startColumn] = 1;
        $result = 0;
        $dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]];
        for ($move = 0; $move < $maxMove; ++$move) {
            $nxt = [];
            for ($i = 0; $i < $m; ++$i) $nxt[$i] = array_fill(0, $n, 0);
            for ($row = 0; $row < $m; ++$row) {
                for ($col = 0; $col < $n; ++$col) {
                    $ways = $dp[$row][$col];
                    if ($ways === 0) continue;
                    foreach ($dirs as $d) {
                        $nr = $row + $d[0];
                        $nc = $col + $d[1];
                        if ($nr >= 0 && $nr < $m && $nc >= 0 && $nc < $n) {
                            $nxt[$nr][$nc] = ($nxt[$nr][$nc] + $ways) % $MOD;
                        } else {
                            $result = ($result + $ways) % $MOD;
                        }
                    }
                }
            }
            $dp = $nxt;
        }
        return $result;
    }
}
