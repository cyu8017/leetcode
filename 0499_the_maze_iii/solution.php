<?php
// LeetCode 0499 - The Maze III
// https://leetcode.com/problems/the-maze-iii/

class Solution {
    /**
     * @param Integer[][] $maze
     * @param Integer[] $ball
     * @param Integer[] $hole
     * @return String
     */
    function findShortestWay($maze, $ball, $hole) {
        return $this->find_shortest_way($maze, $ball, $hole);
    }

    /**
     * @param Integer[][] $maze
     * @param Integer[] $ball
     * @param Integer[] $hole
     * @return String
     */
    function find_shortest_way($maze, $ball, $hole) {
        $rows = count($maze);
        $cols = count($maze[0]);
        $holeRow = $hole[0];
        $holeCol = $hole[1];
        $directions = [
            'd' => [1, 0],
            'l' => [0, -1],
            'r' => [0, 1],
            'u' => [-1, 0],
        ];

        $roll = function ($row, $col, $dr, $dc) use ($maze, $rows, $cols, $holeRow, $holeCol) {
            $distance = 0;
            while ($row + $dr >= 0 && $row + $dr < $rows && $col + $dc >= 0 && $col + $dc < $cols && $maze[$row + $dr][$col + $dc] === 0) {
                $row += $dr;
                $col += $dc;
                $distance++;
                if ($row === $holeRow && $col === $holeCol) {
                    break;
                }
            }
            return [$row, $col, $distance];
        };

        $best = [];
        $heap = [[0, '', $ball[0], $ball[1]]];

        while ($heap !== []) {
            usort($heap, function ($left, $right) {
                if ($left[0] !== $right[0]) {
                    return $left[0] <=> $right[0];
                }
                return strcmp($left[1], $right[1]);
            });
            [$dist, $path, $row, $col] = array_shift($heap);
            $state = "{$row},{$col}";
            if (isset($best[$state])) {
                [$bestDist, $bestPath] = $best[$state];
                if ($bestDist < $dist || ($bestDist === $dist && $bestPath <= $path)) {
                    continue;
                }
            }
            $best[$state] = [$dist, $path];
            if ($row === $holeRow && $col === $holeCol) {
                return $path;
            }

            foreach ($directions as $direction => [$dr, $dc]) {
                [$nextRow, $nextCol, $traveled] = $roll($row, $col, $dr, $dc);
                if ($nextRow === $row && $nextCol === $col) {
                    continue;
                }
                $newDist = $dist + $traveled;
                $newPath = $path . $direction;
                $target = "{$nextRow},{$nextCol}";
                if (!isset($best[$target])) {
                    $heap[] = [$newDist, $newPath, $nextRow, $nextCol];
                    continue;
                }
                [$existingDist, $existingPath] = $best[$target];
                if ($newDist < $existingDist || ($newDist === $existingDist && $newPath < $existingPath)) {
                    $heap[] = [$newDist, $newPath, $nextRow, $nextCol];
                }
            }
        }

        return 'impossible';
    }
}
