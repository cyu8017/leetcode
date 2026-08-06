<?php
// LeetCode 1196 - How Many Apples Can You Put into the Basket
// https://leetcode.com/problems/how-many-apples-can-you-put-into-the-basket/

class Solution {
    /**
     * @param Integer[] $weight
     * @return Integer
     */
    function maxNumberOfApples($weight) {
        sort($weight);
        $total = 0;
        foreach ($weight as $i => $w) {
            $total += $w;
            if ($total > 5000) return $i;
        }
        return count($weight);
    }
}
