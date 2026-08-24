<?php
// LeetCode 2171 - Removing Minimum Number of Magic Beans
// https://leetcode.com/problems/removing-minimum-number-of-magic-beans/

class Solution {
    /**
     * @param Integer[] $beans
     * @return Integer
     */
    function minimumRemoval($beans) {
        sort($beans);
        $n = count($beans);
        $sum = 0;
        foreach ($beans as $b) $sum += $b;
        $ans = $sum;
        for ($i = 0; $i < $n; $i++) {
            $remain = ($n - $i) * $beans[$i];
            $ans = min($ans, $sum - $remain);
        }
        return $ans;
    }
}
