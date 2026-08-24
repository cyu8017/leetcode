<?php
// LeetCode 3843 - First Element With Unique Frequency
// https://leetcode.com/problems/first-element-with-unique-frequency/

class Solution {
    function firstUniqueFreq($nums) {
        $cnt = [];
        foreach ($nums as $x) $cnt[$x] = ($cnt[$x] ?? 0) + 1;
        $freq = [];
        foreach ($cnt as $v) $freq[$v] = ($freq[$v] ?? 0) + 1;
        foreach ($nums as $x) {
            if ($freq[$cnt[$x]] === 1) return $x;
        }
        return -1;
    }
}
