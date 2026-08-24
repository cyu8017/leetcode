<?php
// LeetCode 3450 - Maximum Students on a Single Bench
// https://leetcode.com/problems/maximum-students-on-a-single-bench/

class Solution {
    function maxStudentsOnBench($students) {
        $bench = [];
        foreach ($students as $s) {
            if (!isset($bench[$s[1]])) $bench[$s[1]] = [];
            $bench[$s[1]][$s[0]] = true;
        }
        $ans = 0;
        foreach ($bench as $set) {
            $sz = count($set);
            if ($sz > $ans) $ans = $sz;
        }
        return $ans;
    }
}
