<?php
// LeetCode 2061 - Number of Spaces Cleaning Robot Cleaned
// https://leetcode.com/problems/number-of-spaces-cleaning-robot-cleaned/

class Solution {
    /**
     * @param Integer[][] $room
     * @return Integer
     */
    function numberOfCleanRooms($room) {
        $m = count($room);
        $n = count($room[0]);
        $dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]];
        $vis = [];
        $cleaned = ["0,0" => true];
        $r = 0;
        $c = 0;
        $d = 0;
        while (true) {
            $state = $r * 10000 + $c * 10 + $d;
            if (isset($vis[$state])) break;
            $vis[$state] = true;
            $nr = $r + $dirs[$d][0];
            $nc = $c + $dirs[$d][1];
            if ($nr >= 0 && $nr < $m && $nc >= 0 && $nc < $n && $room[$nr][$nc] === 0) {
                $r = $nr;
                $c = $nc;
                $cleaned[$r . "," . $c] = true;
            } else $d = ($d + 1) % 4;
        }
        return count($cleaned);
    }
}
