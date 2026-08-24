<?php
// LeetCode 0645 - Set Mismatch
// https://leetcode.com/problems/set-mismatch/

class Solution {
    function findErrorNums($nums) {
        $n = count($nums);
        $seen = array_fill(0, $n + 1, 0);
        $duplicate = -1;
        $missing = -1;
        foreach ($nums as $value) ++$seen[$value];
        for ($value = 1; $value <= $n; ++$value) {
            if ($seen[$value] === 2) $duplicate = $value;
            elseif ($seen[$value] === 0) $missing = $value;
        }
        return [$duplicate, $missing];
    }
}
