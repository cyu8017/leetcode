<?php
// LeetCode 2948 - Make Lexicographically Smallest Array by Swapping Elements
// https://leetcode.com/problems/make-lexicographically-smallest-array-by-swapping-elements/

class Solution {
    function lexicographicallySmallestArray($nums, $limit) {
        $n = count($nums);
        $idx = range(0, $n - 1);
        usort($idx, function($a, $b) use ($nums) {
            return $nums[$a] <=> $nums[$b];
        });
        $ans = array_fill(0, $n, 0);
        for ($i = 0; $i < $n; ) {
            $j = $i + 1;
            while ($j < $n && $nums[$idx[$j]] - $nums[$idx[$j - 1]] <= $limit) $j++;
            $groupIdx = [];
            for ($t = 0; $t < $j - $i; $t++) $groupIdx[] = $idx[$i + $t];
            sort($groupIdx);
            for ($t = 0; $t < $j - $i; $t++) $ans[$groupIdx[$t]] = $nums[$idx[$i + $t]];
            $i = $j;
        }
        return $ans;
    }
}
