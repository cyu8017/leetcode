<?php
// LeetCode 0505 - The Maze II
// https://leetcode.com/problems/the-maze-ii/

class Solution {
    /**
     * @param int[][] $maze
     * @param int[] $start
     * @param int[] $destination
     * @return int
     */
    function shortestDistance($maze, $start, $destination) {
        return $this->shortest_distance($maze, $start, $destination);
    }

    /**
     * @param int[][] $maze
     * @param int[] $start
     * @param int[] $destination
     * @return int
     */
    function shortest_distance($maze, $start, $destination) {
        $rows = count($maze);
        $cols = count($maze[0]);
        $target = [$destination[0], $destination[1]];
        $directions = [[-1, 0], [1, 0], [0, -1], [0, 1]];
        $best = [];
        $heap = new SplMinHeap();
        $heap->insert([0, $start[0], $start[1]]);

        while (!$heap->isEmpty()) {
            [$dist, $row, $col] = $heap->extract();
            if ($row === $target[0] && $col === $target[1]) {
                return $dist;
            }
            $key = "{$row},{$col}";
            if (($best[$key] ?? PHP_INT_MAX) <= $dist) {
                continue;
            }
            $best[$key] = $dist;

            foreach ($directions as [$dr, $dc]) {
                $nextRow = $row;
                $nextCol = $col;
                $traveled = 0;
                while ($nextRow + $dr >= 0 && $nextRow + $dr < $rows &&
                       $nextCol + $dc >= 0 && $nextCol + $dc < $cols &&
                       $maze[$nextRow + $dr][$nextCol + $dc] === 0) {
                    $nextRow += $dr;
                    $nextCol += $dc;
                    $traveled++;
                }
                if ($nextRow === $row && $nextCol === $col) {
                    continue;
                }
                $newDist = $dist + $traveled;
                $nextKey = "{$nextRow},{$nextCol}";
                if ($newDist < ($best[$nextKey] ?? PHP_INT_MAX)) {
                    $heap->insert([$newDist, $nextRow, $nextCol]);
                }
            }
        }
        return -1;
    }
}
