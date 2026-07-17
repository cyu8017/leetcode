<?php
// LeetCode 1792 - Maximum Average Pass Ratio
// https://leetcode.com/problems/maximum-average-pass-ratio/

class Solution {
    /**
     * @param Integer[][] $classes
     * @param Integer $extraStudents
     * @return Float
     */
    function maxAverageRatio($classes, $extraStudents) {
        $gain = function ($p, $t) {
            return ($p + 1) / ($t + 1) - $p / $t;
        };

        $heap = new SplPriorityQueue();
        $heap->setExtractFlags(SplPriorityQueue::EXTR_DATA);
        foreach ($classes as $cls) {
            $p = $cls[0];
            $t = $cls[1];
            $heap->insert([$p, $t], $gain($p, $t));
        }
        for ($i = 0; $i < $extraStudents; $i++) {
            list($p, $t) = $heap->extract();
            $p += 1;
            $t += 1;
            $heap->insert([$p, $t], $gain($p, $t));
        }
        $total = 0.0;
        $count = count($classes);
        while (!$heap->isEmpty()) {
            list($p, $t) = $heap->extract();
            $total += $p / $t;
        }
        return $total / $count;
    }
}
