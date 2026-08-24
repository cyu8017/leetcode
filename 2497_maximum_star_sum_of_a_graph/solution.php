<?php
// LeetCode 2497 - Maximum Star Sum of a Graph
// https://leetcode.com/problems/maximum-star-sum-of-a-graph/

class Solution {
    function maxStarSum($vals, $edges, $k) {
        $n = count($vals);
        $g = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $g[$e[0]][] = $e[1];
            $g[$e[1]][] = $e[0];
        }
        $ans = $vals[0];
        for ($i = 0; $i < $n; $i++) {
            $neigh = [];
            foreach ($g[$i] as $v) {
                if ($vals[$v] > 0) $neigh[] = $vals[$v];
            }
            rsort($neigh);
            $sum = $vals[$i];
            for ($j = 0; $j < count($neigh) && $j < $k; $j++) $sum += $neigh[$j];
            if ($sum > $ans) $ans = $sum;
        }
        return $ans;
    }
}
