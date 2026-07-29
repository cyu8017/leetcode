<?php
// LeetCode 1046 - Last Stone Weight
// https://leetcode.com/problems/last-stone-weight/

class Solution {
    /**
     * @param Integer[] $stones
     * @return Integer
     */
    function lastStoneWeight($stones) {
        $heap = new SplMaxHeap();
        foreach ($stones as $stone) {
            $heap->insert($stone);
        }
        while ($heap->count() > 1) {
            $a = $heap->extract();
            $b = $heap->extract();
            if ($a !== $b) {
                $heap->insert($a - $b);
            }
        }
        return $heap->isEmpty() ? 0 : $heap->top();
    }
}
