<?php
// LeetCode 1882 - Process Tasks Using Servers
// https://leetcode.com/problems/process-tasks-using-servers/

class AvailableServerHeap extends SplMinHeap {
    public function compare($value1, $value2): int {
        if ($value1[0] !== $value2[0]) {
            return $value2[0] <=> $value1[0];
        }
        return $value2[1] <=> $value1[1];
    }
}

class BusyServerHeap extends SplMinHeap {
    public function compare($value1, $value2): int {
        if ($value1[0] !== $value2[0]) {
            return $value2[0] <=> $value1[0];
        }
        if ($value1[1] !== $value2[1]) {
            return $value2[1] <=> $value1[1];
        }
        return $value2[2] <=> $value1[2];
    }
}

class Solution {
    /**
     * @param Integer[] $servers
     * @param Integer[] $tasks
     * @return Integer[]
     */
    function assignTasks($servers, $tasks) {
        $available = new AvailableServerHeap();
        foreach ($servers as $index => $weight) {
            $available->insert([$weight, $index]);
        }

        $busy = new BusyServerHeap();
        $answer = [];
        $time = 0;

        foreach ($tasks as $moment => $task) {
            $time = max($time, $moment);
            while (!$busy->isEmpty() && $busy->top()[0] <= $time) {
                [, $weight, $index] = $busy->extract();
                $available->insert([$weight, $index]);
            }

            while ($available->isEmpty()) {
                $time = $busy->top()[0];
                while (!$busy->isEmpty() && $busy->top()[0] <= $time) {
                    [, $weight, $index] = $busy->extract();
                    $available->insert([$weight, $index]);
                }
            }

            [$weight, $index] = $available->extract();
            $busy->insert([$time + $task, $weight, $index]);
            $answer[] = $index;
        }

        return $answer;
    }
}
