<?php

// LeetCode 0198 - House Robber
class Solution {
    function rob($nums) {
        $prev2 = 0;
        $prev1 = 0;
        foreach ($nums as $num) {
            $current = max($prev1, $prev2 + $num);
            $prev2 = $prev1;
            $prev1 = $current;
        }
        return $prev1;
    }
}