<?php
// LeetCode 2805 - Custom Interval
// https://leetcode.com/problems/custom-interval/

class Solution {
    public $nextId = 1;
    public $cancelled = [];
    function customInterval($fn, $delay = null, $period = null) {
        if (!is_callable($fn)) {
            $cancelTime = $period;
            $period = $delay;
            $delay = $fn;
            $times = [];
            $count = 0;
            $t = 0;
            while (true) {
                $t += $delay + $period * $count;
                if ($cancelTime !== null && $t >= $cancelTime) break;
                $times[] = $t;
                $count++;
                if ($count > 100000) break;
            }
            return $times;
        }
        $id = $this->nextId++;
        $this->cancelled[$id] = false;
        return $id;
    }
    function customClearInterval($id) {
        $this->cancelled[$id] = true;
    }
}
