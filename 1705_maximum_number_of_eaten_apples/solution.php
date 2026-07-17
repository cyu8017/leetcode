<?php
// LeetCode 1705 - Maximum Number of Eaten Apples
// https://leetcode.com/problems/maximum-number-of-eaten-apples/

class Solution {
    /**
     * @param Integer[] $apples
     * @param Integer[] $days
     * @return Integer
     */
    function eatenApples($apples, $days) {
        $heap = new SplPriorityQueue();
        $heap->setExtractFlags(SplPriorityQueue::EXTR_DATA);
        $n = count($apples);
        $day = 0;
        $eaten = 0;
        while ($day < $n || !$heap->isEmpty()) {
            if ($day < $n && $apples[$day] > 0) {
                $expire = $day + $days[$day];
                $heap->insert([$expire, $apples[$day]], -$expire);
            }
            while (!$heap->isEmpty() && $heap->top()[0] <= $day) {
                $heap->extract();
            }
            if (!$heap->isEmpty()) {
                [$expire, $count] = $heap->extract();
                $eaten++;
                if ($count > 1) {
                    $heap->insert([$expire, $count - 1], -$expire);
                }
            }
            $day++;
        }
        return $eaten;
    }
}
