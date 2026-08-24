<?php
// LeetCode 2610 - Convert an Array Into a 2D Array With Conditions
// https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/

class Solution {
    function findMatrix($nums) {
        $freq = [];
        $ans = [];
        foreach ($nums as $x) {
            $f = $freq[$x] ?? 0;
            if ($f === count($ans)) $ans[] = [];
            $ans[$f][] = $x;
            $freq[$x] = $f + 1;
        }
        return $ans;
    }
}
