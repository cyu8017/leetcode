<?php
// LeetCode 3644 - Maximum K to Sort a Permutation
// https://leetcode.com/problems/maximum-k-to-sort-a-permutation/

class Solution {
    function sortPermutation($nums) {
        $ans = -1;
        $n = count($nums);
        for ($i = 0; $i < $n; $i++)
            if ($i !== $nums[$i]) $ans &= $nums[$i];
        return max($ans, 0);
    }
}
