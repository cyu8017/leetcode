<?php
// LeetCode 1257 - Smallest Common Region
// https://leetcode.com/problems/smallest-common-region/

class Solution {
    /**
     * @param String[][] $regions
     * @param String $region1
     * @param String $region2
     * @return String
     */
    function findSmallestRegion($regions, $region1, $region2) {
        $parent = [];
        foreach ($regions as $group) {
            for ($i = 1; $i < count($group); $i++) {
                $parent[$group[$i]] = $group[0];
            }
        }
        $ancestors = [];
        while ($region1) {
            $ancestors[$region1] = true;
            $region1 = $parent[$region1] ?? null;
        }
        while (!isset($ancestors[$region2])) {
            $region2 = $parent[$region2];
        }
        return $region2;
    }
}
