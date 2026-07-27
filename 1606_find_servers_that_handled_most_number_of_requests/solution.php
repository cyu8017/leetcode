<?php
// LeetCode 1606 - Find Servers That Handled Most Number of Requests
// https://leetcode.com/problems/find-servers-that-handled-most-number-of-requests/

class Solution {
    /**
     * @param Integer $k
     * @param Integer[] $arrival
     * @param Integer[] $load
     * @return Integer[]
     */
    function busiestServers($k, $arrival, $load) {
        $free = new SplMinHeap();
        for ($i = 0; $i < $k; $i++) {
            $free->insert($i);
        }
        $busy = new SplMinHeap();
        $count = array_fill(0, $k, 0);
        $n = count($arrival);
        for ($i = 0; $i < $n; $i++) {
            $t = $arrival[$i];
            $length = $load[$i];
            while (!$busy->isEmpty() && $busy->top()[0] <= $t) {
                $server = $busy->extract()[1];
                $free->insert($i + (($server - $i) % $k + $k) % $k);
            }
            if ($free->isEmpty()) {
                continue;
            }
            $server = $free->extract() % $k;
            $count[$server]++;
            $busy->insert([$t + $length, $server]);
        }
        $best = max($count);
        $ans = [];
        for ($i = 0; $i < $k; $i++) {
            if ($count[$i] === $best) {
                $ans[] = $i;
            }
        }
        return $ans;
    }
}
