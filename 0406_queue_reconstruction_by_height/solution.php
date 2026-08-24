<?php
// LeetCode 0406 - Queue Reconstruction by Height
// https://leetcode.com/problems/queue-reconstruction-by-height/

class Solution {
    /**
     * @param Integer[][] $people
     * @return Integer[][]
     */
    function reconstructQueue($people) {
        return $this->reconstruct_queue($people);
    }

    /**
     * @param Integer[][] $people
     * @return Integer[][]
     */
    function reconstruct_queue($people) {
        usort($people, function ($left, $right) {
            if ($left[0] === $right[0]) {
                return $left[1] <=> $right[1];
            }
            return $right[0] <=> $left[0];
        });

        $queue = [];
        foreach ($people as $person) {
            array_splice($queue, $person[1], 0, [$person]);
        }

        return $queue;
    }
}
