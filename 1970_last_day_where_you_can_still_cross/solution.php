<?php
// LeetCode 1970 - Last Day Where You Can Still Cross
// https://leetcode.com/problems/last-day-where-you-can-still-cross/

class Solution {
    /**
     * @param Integer $row
     * @param Integer $col
     * @param Integer[][] $cells
     * @return Integer
     */
    function latestDayToCross($row, $col, $cells) {
        $lo = 1;
        $hi = count($cells);
        $ans = 0;
        while ($lo <= $hi) {
            $mid = intdiv($lo + $hi, 2);
            if ($this->can($row, $col, $cells, $mid)) {
                $ans = $mid;
                $lo = $mid + 1;
            } else {
                $hi = $mid - 1;
            }
        }
        return $ans;
    }

    private function can($row, $col, $cells, $day) {
        $blocked = [];
        for ($i = 0; $i < $day; $i++) {
            $blocked[($cells[$i][0] - 1) . ',' . ($cells[$i][1] - 1)] = true;
        }
        $stack = [];
        $seen = [];
        for ($c = 0; $c < $col; $c++) {
            $key = "0,$c";
            if (!isset($blocked[$key])) {
                $stack[] = [0, $c];
                $seen[$key] = true;
            }
        }
        $dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]];
        while (!empty($stack)) {
            [$r, $c] = array_pop($stack);
            if ($r === $row - 1) {
                return true;
            }
            foreach ($dirs as $d) {
                $nr = $r + $d[0];
                $nc = $c + $d[1];
                $nkey = "$nr,$nc";
                if ($nr >= 0 && $nr < $row && $nc >= 0 && $nc < $col
                    && !isset($blocked[$nkey]) && !isset($seen[$nkey])) {
                    $seen[$nkey] = true;
                    $stack[] = [$nr, $nc];
                }
            }
        }
        return false;
    }
}
