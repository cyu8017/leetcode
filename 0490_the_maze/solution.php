<?php
// LeetCode 0490 - The Maze
// https://leetcode.com/problems/the-maze/

class Solution {
    /**
     * @param int[][] $maze
     * @param int[] $start
     * @param int[] $destination
     * @return bool
     */
    function hasPath($maze, $start, $destination) {
        return $this->has_path($maze, $start, $destination);
    }

    /**
     * @param int[][] $maze
     * @param int[] $start
     * @param int[] $destination
     * @return bool
     */
    function has_path($maze, $start, $destination) {
        $rows = count($maze);
        $cols = count($maze[0]);
        $directions = [[-1, 0], [1, 0], [0, -1], [0, 1]];
        $visited = [];
        $stack = [[$start[0], $start[1]]];

        while (count($stack) > 0) {
            [$row, $col] = array_pop($stack);
            $key = "{$row},{$col}";
            if (isset($visited[$key])) {
                continue;
            }
            $visited[$key] = true;
            if ($row === $destination[0] && $col === $destination[1]) {
                return true;
            }
            foreach ($directions as [$dr, $dc]) {
                $nr = $row;
                $nc = $col;
                while ($nr + $dr >= 0 && $nr + $dr < $rows && $nc + $dc >= 0 && $nc + $dc < $cols && $maze[$nr + $dr][$nc + $dc] === 0) {
                    $nr += $dr;
                    $nc += $dc;
                }
                $nextKey = "{$nr},{$nc}";
                if (!isset($visited[$nextKey])) {
                    $stack[] = [$nr, $nc];
                }
            }
        }
        return false;
    }
}
