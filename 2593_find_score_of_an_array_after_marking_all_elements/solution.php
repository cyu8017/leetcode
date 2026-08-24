<?php
// LeetCode 2593 - Find Score of an Array After Marking All Elements
// https://leetcode.com/problems/find-score-of-an-array-after-marking-all-elements/

class Solution {
    function findScore($nums) {
        $n = count($nums);
        $idx = range(0, $n - 1);
        usort($idx, function($a, $b) use ($nums) {
            if ($nums[$a] !== $nums[$b]) return $nums[$a] <=> $nums[$b];
            return $a <=> $b;
        });
        $marked = array_fill(0, $n, false);
        $ans = 0;
        foreach ($idx as $i) {
            if ($marked[$i]) continue;
            $ans += $nums[$i];
            $marked[$i] = true;
            if ($i - 1 >= 0) $marked[$i - 1] = true;
            if ($i + 1 < $n) $marked[$i + 1] = true;
        }
        return $ans;
    }
}
