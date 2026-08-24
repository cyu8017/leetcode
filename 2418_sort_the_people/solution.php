<?php
// LeetCode 2418 - Sort the People
// https://leetcode.com/problems/sort-the-people/

class Solution {
    function sortPeople($names, $heights) {
        $n = count($names);
        $idx = range(0, $n - 1);
        usort($idx, function ($a, $b) use ($heights) {
            return $heights[$b] <=> $heights[$a];
        });
        $ans = [];
        foreach ($idx as $i) $ans[] = $names[$i];
        return $ans;
    }
}
