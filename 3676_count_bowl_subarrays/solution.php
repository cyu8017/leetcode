<?php
// LeetCode 3676 - Count Bowl Subarrays
// https://leetcode.com/problems/count-bowl-subarrays/

class Solution {
    function bowlSubarrays($nums) {
        $n = count($nums);
        $ans = 0;
        $ngr = array_fill(0, $n, -1);
        $ngl = array_fill(0, $n, -1);
        $stack = [];
        for ($i = $n - 1; $i >= 0; $i--) {
            while ($stack && $nums[$stack[count($stack) - 1]] < $nums[$i]) array_pop($stack);
            if ($stack) $ngr[$i] = $stack[count($stack) - 1];
            $stack[] = $i;
        }
        $stack = [];
        for ($i = 0; $i < $n; $i++) {
            while ($stack && $nums[$stack[count($stack) - 1]] < $nums[$i]) array_pop($stack);
            if ($stack) $ngl[$i] = $stack[count($stack) - 1];
            $stack[] = $i;
        }
        for ($i = 0; $i < $n; $i++) {
            if ($ngr[$i] !== -1 && $ngr[$i] - $i >= 2) $ans++;
            if ($ngl[$i] !== -1 && $i - $ngl[$i] >= 2) $ans++;
        }
        return $ans;
    }
}
