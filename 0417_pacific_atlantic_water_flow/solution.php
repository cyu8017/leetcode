<?php
// LeetCode 0417 - Pacific Atlantic Water Flow
// https://leetcode.com/problems/pacific-atlantic-water-flow/

class Solution {
    /**
     * @param Integer[][] $heights
     * @return Integer[][]
     */
    function pacificAtlantic($heights) {
        return $this->pacific_atlantic($heights);
    }

    /**
     * @param Integer[][] $heights
     * @return Integer[][]
     */
    function pacific_atlantic($heights) {
        if (!$heights || !$heights[0]) {
            return [];
        }

        $rows = count($heights);
        $cols = count($heights[0]);
        $pacific = [];
        $atlantic = [];

        for ($row = 0; $row < $rows; $row++) {
            $this->dfs($heights, $row, 0, $pacific, $heights[$row][0]);
            $this->dfs($heights, $row, $cols - 1, $atlantic, $heights[$row][$cols - 1]);
        }
        for ($col = 0; $col < $cols; $col++) {
            $this->dfs($heights, 0, $col, $pacific, $heights[0][$col]);
            $this->dfs($heights, $rows - 1, $col, $atlantic, $heights[$rows - 1][$col]);
        }

        $result = [];
        foreach ($pacific as $key => $_) {
            if (isset($atlantic[$key])) {
                [$row, $col] = array_map("intval", explode(",", $key));
                $result[] = [$row, $col];
            }
        }
        return $result;
    }

    /**
     * @param Integer[][] $heights
     * @param int $row
     * @param int $col
     * @param array<string, bool> $visited
     * @param int $previous
     * @return void
     */
    private function dfs($heights, $row, $col, &$visited, $previous) {
        $key = $row . "," . $col;
        if (isset($visited[$key])) {
            return;
        }
        if ($row < 0 || $row >= count($heights) || $col < 0 || $col >= count($heights[0])) {
            return;
        }
        if ($heights[$row][$col] < $previous) {
            return;
        }

        $visited[$key] = true;
        $height = $heights[$row][$col];
        $this->dfs($heights, $row + 1, $col, $visited, $height);
        $this->dfs($heights, $row - 1, $col, $visited, $height);
        $this->dfs($heights, $row, $col + 1, $visited, $height);
        $this->dfs($heights, $row, $col - 1, $visited, $height);
    }
}
