<?php
// LeetCode 2086 - Minimum Number of Food Buckets to Feed the Hamsters
// https://leetcode.com/problems/minimum-number-of-food-buckets-to-feed-the-hamsters/

class Solution {
    /**
     * @param String $hamsters
     * @return Integer
     */
    function minimumBuckets($hamsters) {
        $b = str_split($hamsters);
        $ans = 0;
        $n = count($b);
        for ($i = 0; $i < $n; $i++) {
            if ($b[$i] !== 'H') continue;
            if ($i > 0 && $b[$i - 1] === 'B') continue;
            if ($i + 1 < $n && $b[$i + 1] === '.') { $b[$i + 1] = 'B'; $ans++; }
            else if ($i > 0 && $b[$i - 1] === '.') { $b[$i - 1] = 'B'; $ans++; }
            else return -1;
        }
        return $ans;
    }
}
