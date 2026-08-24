<?php
// LeetCode 3759 - Count Elements With At Least K Greater Values
// https://leetcode.com/problems/count-elements-with-at-least-k-greater-values/

class Solution {
    function countElements($nums, $k) {
        $n = count($nums);
        if ($k === 0) return $n;
        $a = $nums;
        sort($a);
        $ans = 0;
        for ($i = 0; $i < $n - $k; $i++) {
            if ($a[$n - $k] > $a[$i]) $ans++;
        }
        return $ans;
    }
}
