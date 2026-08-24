<?php
// LeetCode 0857 - Minimum Cost to Hire K Workers
// https://leetcode.com/problems/minimum-cost-to-hire-k-workers/

class Solution {
    /**
     * @param Integer[] $quality
     * @param Integer[] $wage
     * @param Integer $k
     * @return Float
     */
    function mincostToHireWorkers($quality, $wage, $k) {
        $n = count($quality);
        $workers = [];
        for ($i = 0; $i < $n; $i++) $workers[] = [$wage[$i] / $quality[$i], $quality[$i]];
        usort($workers, function($a, $b) { return $a[0] <=> $b[0]; });
        $heap = [];
        $push = function($q) use (&$heap) {
            $heap[] = $q;
            $i = count($heap) - 1;
            while ($i > 0) {
                $p = ($i - 1) >> 1;
                if ($heap[$i] <= $heap[$p]) break;
                $tmp = $heap[$i];
                $heap[$i] = $heap[$p];
                $heap[$p] = $tmp;
                $i = $p;
            }
        };
        $pop = function() use (&$heap) {
            $top = $heap[0];
            $last = array_pop($heap);
            if (count($heap)) {
                $heap[0] = $last;
                $i = 0;
                while (true) {
                    $largest = $i;
                    $l = $i * 2 + 1;
                    $r = $i * 2 + 2;
                    if ($l < count($heap) && $heap[$l] > $heap[$largest]) $largest = $l;
                    if ($r < count($heap) && $heap[$r] > $heap[$largest]) $largest = $r;
                    if ($largest === $i) break;
                    $tmp = $heap[$i];
                    $heap[$i] = $heap[$largest];
                    $heap[$largest] = $tmp;
                    $i = $largest;
                }
            }
            return $top;
        };
        $totalQ = 0;
        $ans = INF;
        foreach ($workers as $w) {
            $ratio = $w[0];
            $q = $w[1];
            $push($q);
            $totalQ += $q;
            if (count($heap) > $k) $totalQ -= $pop();
            if (count($heap) === $k) $ans = min($ans, $totalQ * $ratio);
        }
        return $ans;
    }
}
