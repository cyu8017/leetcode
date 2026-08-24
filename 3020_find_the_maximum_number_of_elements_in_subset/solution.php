<?php
// LeetCode 3020 - Find the Maximum Number of Elements in Subset
// https://leetcode.com/problems/find-the-maximum-number-of-elements-in-subset/

class Solution {
    function maximumLength($nums) {
        $cnt = [];
        foreach ($nums as $x) $cnt[$x] = ($cnt[$x] ?? 0) + 1;
        $ones = $cnt[1] ?? 0;
        $ans = $ones - (($ones % 2) ^ 1);
        unset($cnt[1]);
        foreach (array_keys($cnt) as $start) {
            $x = $start;
            $t = 0;
            while (($cnt[$x] ?? 0) > 1) {
                $x = $x * $x;
                $t += 2;
            }
            if (($cnt[$x] ?? 0) > 0) $t += 1;
            else $t -= 1;
            $ans = max($ans, $t);
        }
        return $ans;
    }
}
