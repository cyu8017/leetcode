<?php
// LeetCode 2597 - The Number of Beautiful Subsets
// https://leetcode.com/problems/the-number-of-beautiful-subsets/

class Solution {
    function beautifulSubsets($nums, $k) {
        $freq = [];
        foreach ($nums as $x) $freq[$x] = ($freq[$x] ?? 0) + 1;
        $groups = [];
        foreach ($freq as $key => $_) {
            $rem = $key % $k;
            if (!isset($groups[$rem])) $groups[$rem] = [];
            $groups[$rem][] = $key;
        }
        $ans = 1;
        foreach ($groups as $vals) {
            sort($vals);
            $prevTake = 0;
            $prevSkip = 1;
            $prevVal = -PHP_INT_MAX;
            foreach ($vals as $v) {
                $ways = 1;
                for ($i = 0; $i < $freq[$v]; $i++) $ways *= 2;
                $ways--;
                $skip = $prevTake + $prevSkip;
                $take = $ways * $prevSkip;
                if ($prevVal + $k !== $v) $take += $ways * $prevTake;
                $prevTake = $take;
                $prevSkip = $skip;
                $prevVal = $v;
            }
            $ans *= $prevTake + $prevSkip;
        }
        return $ans - 1;
    }
}
