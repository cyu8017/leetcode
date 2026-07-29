<?php
// LeetCode 1036 - Escape a Large Maze
// https://leetcode.com/problems/escape-a-large-maze/

class Solution {
    /**
     * @param Integer[][] $blocked
     * @param Integer[] $source
     * @param Integer[] $target
     * @return Boolean
     */
    function isEscapePossible($blocked, $source, $target) {
        $blockedSet = [];
        foreach ($blocked as $b) {
            $blockedSet[$b[0] . ',' . $b[1]] = true;
        }
        $bCount = count($blocked);
        $limit = intdiv($bCount * ($bCount - 1), 2);

        $bfs = function ($start, $goal) use ($blockedSet, $limit) {
            $queue = [$start];
            $seen = [$start[0] . ',' . $start[1] => true];
            $qi = 0;
            while ($qi < count($queue)) {
                if (count($seen) > $limit) {
                    return true;
                }
                [$r, $c] = $queue[$qi++];
                if ($r === $goal[0] && $c === $goal[1]) {
                    return true;
                }
                foreach ([[$r + 1, $c], [$r - 1, $c], [$r, $c + 1], [$r, $c - 1]] as $nb) {
                    $nr = $nb[0];
                    $nc = $nb[1];
                    $key = $nr . ',' . $nc;
                    if ($nr >= 0 && $nr < 1000000 && $nc >= 0 && $nc < 1000000
                        && !isset($blockedSet[$key]) && !isset($seen[$key])) {
                        $seen[$key] = true;
                        $queue[] = [$nr, $nc];
                    }
                }
            }
            return false;
        };

        return $bfs($source, $target) && $bfs($target, $source);
    }
}
