<?php
// LeetCode 1962 - Remove Stones to Minimize the Total
// https://leetcode.com/problems/remove-stones-to-minimize-the-total/

class Solution {
    /**
     * @param Integer[] $piles
     * @param Integer $k
     * @return Integer
     */
    function minStoneSum($piles, $k) {
        $heap = new SplMaxHeap();
        foreach ($piles as $p) {
            $heap->insert($p);
        }
        for ($i = 0; $i < $k; $i++) {
            $x = $heap->extract();
            $heap->insert($x - intdiv($x, 2));
        }
        $sum = 0;
        while (!$heap->isEmpty()) {
            $sum += $heap->extract();
        }
        return $sum;
    }
}
