<?php
// LeetCode 1834 - Single-Threaded CPU
// https://leetcode.com/problems/single-threaded-cpu/

class TaskHeap extends SplMinHeap {
    public function compare($value1, $value2): int {
        if ($value1[0] !== $value2[0]) {
            return $value2[0] <=> $value1[0];
        }
        return $value2[1] <=> $value1[1];
    }
}

class Solution {
    /**
     * @param Integer[][] $tasks
     * @return Integer[]
     */
    function getOrder($tasks) {
        $indexed = [];
        foreach ($tasks as $idx => $task) {
            $indexed[] = [$idx, $task];
        }
        usort($indexed, function ($a, $b) {
            if ($a[1][0] !== $b[1][0]) {
                return $a[1][0] <=> $b[1][0];
            }
            return $a[0] <=> $b[0];
        });

        $i = 0;
        $n = count($tasks);
        $heap = new TaskHeap();
        $time = 0;
        $order = [];

        while ($i < $n || !$heap->isEmpty()) {
            if ($i < $n && $heap->isEmpty()) {
                $time = max($time, $indexed[$i][1][0]);
            }

            while ($i < $n && $indexed[$i][1][0] <= $time) {
                $idx = $indexed[$i][0];
                $task = $indexed[$i][1];
                $heap->insert([$task[1], $idx]);
                $i++;
            }

            [$duration, $idx] = $heap->extract();
            $time += $duration;
            $order[] = $idx;
        }

        return $order;
    }
}
