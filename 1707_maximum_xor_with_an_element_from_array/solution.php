<?php
// LeetCode 1707 - Maximum XOR With an Element From Array
// https://leetcode.com/problems/maximum-xor-with-an-element-from-array/

class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer[][] $queries
     * @return Integer[]
     */
    function maximizeXor($nums, $queries) {
        sort($nums);
        $order = range(0, count($queries) - 1);
        usort($order, function ($a, $b) use ($queries) {
            return $queries[$a][1] <=> $queries[$b][1];
        });

        $children = [[-1, -1]];

        $insert = function ($num) use (&$children) {
            $node = 0;
            for ($bit = 31; $bit >= 0; $bit--) {
                $b = ($num >> $bit) & 1;
                if ($children[$node][$b] === -1) {
                    $children[$node][$b] = count($children);
                    $children[] = [-1, -1];
                }
                $node = $children[$node][$b];
            }
        };

        $ans = array_fill(0, count($queries), -1);
        $added = 0;
        $n = count($nums);
        foreach ($order as $qi) {
            $x = $queries[$qi][0];
            $limit = $queries[$qi][1];
            while ($added < $n && $nums[$added] <= $limit) {
                $insert($nums[$added]);
                $added++;
            }
            if ($added === 0) {
                continue;
            }
            $node = 0;
            $value = 0;
            for ($bit = 31; $bit >= 0; $bit--) {
                $b = ($x >> $bit) & 1;
                $want = $b ^ 1;
                if ($children[$node][$want] !== -1) {
                    $value |= 1 << $bit;
                    $node = $children[$node][$want];
                } else {
                    $node = $children[$node][$b];
                }
            }
            $ans[$qi] = $value;
        }
        return $ans;
    }
}
