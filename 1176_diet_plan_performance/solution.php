<?php
// LeetCode 1176 - Diet Plan Performance
// https://leetcode.com/problems/diet-plan-performance/

class Solution {
    /**
     * @param Integer[] $calories
     * @param Integer $k
     * @param Integer $lower
     * @param Integer $upper
     * @return Integer
     */
    function dietPlanPerformance($calories, $k, $lower, $upper) {
        $window = array_sum(array_slice($calories, 0, $k));
        $ans = 0;
        if ($window < $lower) $ans--;
        elseif ($window > $upper) $ans++;
        $n = count($calories);
        for ($i = $k; $i < $n; $i++) {
            $window += $calories[$i] - $calories[$i - $k];
            if ($window < $lower) $ans--;
            elseif ($window > $upper) $ans++;
        }
        return $ans;
    }
}
