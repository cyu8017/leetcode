<?php
// LeetCode 2155 - All Divisions With the Highest Score of a Binary Array
// https://leetcode.com/problems/all-divisions-with-the-highest-score-of-a-binary-array/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function maxScoreIndices($nums) {
        $n = count($nums);
        $total1 = 0;
        foreach ($nums as $x) $total1 += $x;
        $best = $total1;
        $left0 = 0;
        $right1 = $total1;
        $ans = [0];
        for ($i = 0; $i < $n; $i++) {
            if ($nums[$i] === 0) $left0++;
            else $right1--;
            $score = $left0 + $right1;
            if ($score > $best) { $best = $score; $ans = [$i + 1]; }
            else if ($score === $best) $ans[] = $i + 1;
        }
        return $ans;
    }
}
