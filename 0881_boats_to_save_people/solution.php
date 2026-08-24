<?php
// LeetCode 0881 - Boats to Save People
// https://leetcode.com/problems/boats-to-save-people/

class Solution {
    function numRescueBoats($people, $limit) {
        sort($people);
        $i = 0;
        $j = count($people) - 1;
        $boats = 0;
        while ($i <= $j) {
            if ($people[$i] + $people[$j] <= $limit) $i++;
            $j--;
            $boats++;
        }
        return $boats;
    }
}
