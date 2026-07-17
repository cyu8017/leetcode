<?php
// LeetCode 1773 - Count Items Matching a Rule
// https://leetcode.com/problems/count-items-matching-a-rule/

class Solution {
    /**
     * @param String[][] $items
     * @param String $ruleKey
     * @param String $ruleValue
     * @return Integer
     */
    function countMatches($items, $ruleKey, $ruleValue) {
        $idx = ['type' => 0, 'color' => 1, 'name' => 2][$ruleKey];
        $count = 0;
        foreach ($items as $item) {
            if ($item[$idx] === $ruleValue) {
                $count++;
            }
        }
        return $count;
    }
}
