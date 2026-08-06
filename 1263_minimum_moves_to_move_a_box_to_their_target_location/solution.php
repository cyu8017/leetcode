<?php
// LeetCode 1263 - Minimum Moves to Move a Box to Their Target Location
// https://leetcode.com/problems/minimum-moves-to-move-a-box-to-their-target-location/

class Solution {
    /**
     * @param String[][] $grid
     * @return Integer
     */
    function minPushBox($grid) {
        $m = count($grid);
        $n = count($grid[0]);
        $box = $player = $target = null;
        for ($r = 0; $r < $m; $r++) {
            for ($c = 0; $c < $n; $c++) {
                if ($grid[$r][$c] === 'B') $box = [$r, $c];
                elseif ($grid[$r][$c] === 'S') $player = [$r, $c];
                elseif ($grid[$r][$c] === 'T') $target = [$r, $c];
            }
        }
        $reachable = function ($start, $blocked) use ($grid, $m, $n) {
            $seen = [$start[0] . ',' . $start[1] => true];
            $stack = [$start];
            while (!empty($stack)) {
                [$r, $c] = array_pop($stack);
                foreach ([[1,0],[-1,0],[0,1],[0,-1]] as [$dr, $dc]) {
                    $nr = $r + $dr; $nc = $c + $dc;
                    $key = "$nr,$nc";
                    if ($nr >= 0 && $nr < $m && $nc >= 0 && $nc < $n
                        && $grid[$nr][$nc] !== '#'
                        && !($nr === $blocked[0] && $nc === $blocked[1])
                        && !isset($seen[$key])) {
                        $seen[$key] = true;
                        $stack[] = [$nr, $nc];
                    }
                }
            }
            return $seen;
        };
        $queue = [[$box, $player, 0]];
        $seen = [$box[0] . ',' . $box[1] . ',' . $player[0] . ',' . $player[1] => true];
        $head = 0;
        while ($head < count($queue)) {
            [$b, $p, $pushes] = $queue[$head++];
            if ($b[0] === $target[0] && $b[1] === $target[1]) return $pushes;
            $canReach = $reachable($p, $b);
            foreach ([[1,0],[-1,0],[0,1],[0,-1]] as [$dr, $dc]) {
                $stand = [$b[0] - $dr, $b[1] - $dc];
                $nb = [$b[0] + $dr, $b[1] + $dc];
                $standKey = $stand[0] . ',' . $stand[1];
                if (isset($canReach[$standKey])
                    && $nb[0] >= 0 && $nb[0] < $m && $nb[1] >= 0 && $nb[1] < $n
                    && $grid[$nb[0]][$nb[1]] !== '#') {
                    $state = $nb[0] . ',' . $nb[1] . ',' . $b[0] . ',' . $b[1];
                    if (!isset($seen[$state])) {
                        $seen[$state] = true;
                        $queue[] = [$nb, $b, $pushes + 1];
                    }
                }
            }
        }
        return -1;
    }
}
