<?php
// LeetCode 0893 - Groups of Special-Equivalent Strings
// https://leetcode.com/problems/groups-of-special-equivalent-strings/

class Solution {
    function numSpecialEquivGroups($words) {
        $groups = [];
        foreach ($words as $w) {
            $even = [];
            $odd = [];
            $n = strlen($w);
            for ($i = 0; $i < $n; $i++) {
                if ($i % 2 === 0) $even[] = $w[$i];
                else $odd[] = $w[$i];
            }
            sort($even);
            sort($odd);
            $groups[implode("", $even) . "|" . implode("", $odd)] = true;
        }
        return count($groups);
    }
}
