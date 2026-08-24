<?php
// LeetCode 3595 - Once Twice
// https://leetcode.com/problems/once-twice/

class Solution {
    function onceTwice($nums) {
        $freq = [];
        foreach ($nums as $x) $freq[$x] = ($freq[$x] ?? 0) + 1;
        $a = 0;
        $b = 0;
        foreach ($freq as $k => $v) {
            if ($v === 1) $a = $k;
            else if ($v === 2) $b = $k;
        }
        return [$a, $b];
    }
}
