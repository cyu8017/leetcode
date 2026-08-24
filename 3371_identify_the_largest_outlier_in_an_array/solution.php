<?php
// LeetCode 3371 - Identify the Largest Outlier in an Array
// https://leetcode.com/problems/identify-the-largest-outlier-in-an-array/

class Solution {
    function getLargestOutlier($nums) {
        $sum = 0;
        $freq = [];
        foreach ($nums as $x) {
            $sum += $x;
            $freq[$x] = ($freq[$x] ?? 0) + 1;
        }
        $ans = -2147483648;
        foreach ($nums as $x) {
            $freq[$x]--;
            $rem = $sum - $x;
            if ($rem % 2 === 0) {
                $cand = intdiv($rem, 2);
                if (($freq[$cand] ?? 0) > 0 && $x > $ans) $ans = $x;
            }
            $freq[$x]++;
        }
        return $ans;
    }
}
