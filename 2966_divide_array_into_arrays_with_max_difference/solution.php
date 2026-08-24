<?php
// LeetCode 2966 - Divide Array Into Arrays With Max Difference
// https://leetcode.com/problems/divide-array-into-arrays-with-max-difference/

class Solution {
    function divideArray($nums, $k) {
        sort($nums);
        $ans = [];
        for ($i = 0; $i < count($nums); $i += 3) {
            if ($nums[$i + 2] - $nums[$i] > $k) return [];
            $ans[] = [$nums[$i], $nums[$i + 1], $nums[$i + 2]];
        }
        return $ans;
    }
}
