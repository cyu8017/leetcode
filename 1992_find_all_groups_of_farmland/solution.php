<?php
// LeetCode 1992 - Find All Groups of Farmland
// https://leetcode.com/problems/find-all-groups-of-farmland/

class Solution {
    /**
     * @param Integer[][] $land
     * @return Integer[][]
     */
    function findFarmland($land) {
        $m = count($land);
        $n = count($land[0]);
        $ans = [];
        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                if ($land[$i][$j] === 1
                    && ($i === 0 || $land[$i - 1][$j] === 0)
                    && ($j === 0 || $land[$i][$j - 1] === 0)
                ) {
                    $r = $i;
                    $c = $j;
                    while ($r + 1 < $m && $land[$r + 1][$j] === 1) {
                        $r++;
                    }
                    while ($c + 1 < $n && $land[$i][$c + 1] === 1) {
                        $c++;
                    }
                    $ans[] = [$i, $j, $r, $c];
                }
            }
        }
        return $ans;
    }
}
