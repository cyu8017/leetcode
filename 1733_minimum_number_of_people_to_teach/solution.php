<?php
// LeetCode 1733 - Minimum Number of People to Teach
// https://leetcode.com/problems/minimum-number-of-people-to-teach/

class Solution {
    /**
     * @param Integer $n
     * @param Integer[][] $languages
     * @param Integer[][] $friendships
     * @return Integer
     */
    function minimumTeachings($n, $languages, $friendships) {
        $known = [];
        foreach ($languages as $user => $items) {
            $known[$user] = array_fill_keys($items, true);
        }
        $need = [];
        foreach ($friendships as [$u, $v]) {
            $shares = false;
            foreach ($known[$u - 1] as $lang => $unused) {
                if (isset($known[$v - 1][$lang])) {
                    $shares = true;
                    break;
                }
            }
            if (!$shares) {
                $need[$u - 1] = true;
                $need[$v - 1] = true;
            }
        }
        if (count($need) === 0) {
            return 0;
        }
        $best = PHP_INT_MAX;
        for ($lang = 1; $lang <= $n; $lang++) {
            $teach = 0;
            foreach ($need as $user => $unused) {
                if (!isset($known[$user][$lang])) {
                    $teach++;
                }
            }
            $best = min($best, $teach);
        }
        return $best;
    }
}
