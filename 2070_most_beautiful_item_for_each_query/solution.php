<?php
// LeetCode 2070 - Most Beautiful Item for Each Query
// https://leetcode.com/problems/most-beautiful-item-for-each-query/

class Solution {
    /**
     * @param Integer[][] $items
     * @param Integer[] $queries
     * @return Integer[]
     */
    function maximumBeauty($items, $queries) {
        usort($items, fn($a, $b) => $a[0] <=> $b[0]);
        $maxB = 0;
        foreach ($items as &$it) {
            $maxB = max($maxB, $it[1]);
            $it[1] = $maxB;
        }
        unset($it);
        $ans = [];
        $n = count($items);
        foreach ($queries as $i => $q) {
            $lo = 0;
            $hi = $n;
            while ($lo < $hi) {
                $mid = ($lo + $hi) >> 1;
                if ($items[$mid][0] <= $q) $lo = $mid + 1;
                else $hi = $mid;
            }
            $ans[$i] = $lo === 0 ? 0 : $items[$lo - 1][1];
        }
        return $ans;
    }
}
