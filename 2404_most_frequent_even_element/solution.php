<?php
// LeetCode 2404 - Most Frequent Even Element
// https://leetcode.com/problems/most-frequent-even-element/

class Solution {
    function mostFrequentEven($nums) {
        $cnt = [];
        $ans = -1;
        $best = 0;
        foreach ($nums as $x) {
            if ($x % 2 !== 0) continue;
            $c = ($cnt[$x] ?? 0) + 1;
            $cnt[$x] = $c;
            if ($c > $best || ($c === $best && ($ans === -1 || $x < $ans))) {
                $best = $c;
                $ans = $x;
            }
        }
        return $ans;
    }
}
