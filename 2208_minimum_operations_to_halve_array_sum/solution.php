<?php
// LeetCode 2208 - Minimum Operations to Halve Array Sum
// https://leetcode.com/problems/minimum-operations-to-halve-array-sum/

class Solution {
    function halveArray($nums) {
        $pq = new SplPriorityQueue();
        $sum = 0.0;
        foreach ($nums as $x) {
            $pq->insert((float)$x, (float)$x);
            $sum += $x;
        }
        $target = $sum / 2.0;
        $ans = 0;
        while ($sum > $target) {
            $top = $pq->extract();
            $x = $top / 2.0;
            $sum -= $x;
            $pq->insert($x, $x);
            $ans++;
        }
        return $ans;
    }
}
