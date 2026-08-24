<?php
// LeetCode 3471 - Find the Largest Almost Missing Integer
// https://leetcode.com/problems/find-the-largest-almost-missing-integer/

class Solution {
    function largestInteger($nums, $k) {
        $n = count($nums);
        $cnt = [];
        for ($i = 0; $i + $k <= $n; $i++) {
            $seen = [];
            for ($j = $i; $j < $i + $k; $j++) $seen[$nums[$j]] = true;
            foreach ($seen as $x => $_) $cnt[$x] = ($cnt[$x] ?? 0) + 1;
        }
        $ans = -1;
        foreach ($cnt as $key => $value) {
            if ($value === 1 && $key > $ans) $ans = $key;
        }
        return $ans;
    }
}
