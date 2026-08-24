<?php
// LeetCode 3075 - Maximize Happiness of Selected Children
// https://leetcode.com/problems/maximize-happiness-of-selected-children/

class Solution {
    function maximumHappinessSum($happiness, $k) {
        sort($happiness);
        $ans = 0;
        $n = count($happiness);
        for ($i = 0; $i < $k; $i++) {
            $x = $happiness[$n - $i - 1] - $i;
            $ans += max($x, 0);
        }
        return $ans;
    }
}
