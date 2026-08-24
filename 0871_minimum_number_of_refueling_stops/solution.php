<?php
// LeetCode 0871 - Minimum Number of Refueling Stops
// https://leetcode.com/problems/minimum-number-of-refueling-stops/

class Solution {
    /**
     * @param Integer $target
     * @param Integer $startFuel
     * @param Integer[][] $stations
     * @return Integer
     */
    function minRefuelStops($target, $startFuel, $stations) {
        $pq = [];
        $push = function($gas) use (&$pq) {
            $pq[] = $gas;
            $i = count($pq) - 1;
            while ($i > 0) {
                $p = ($i - 1) >> 1;
                if ($pq[$i] <= $pq[$p]) break;
                $tmp = $pq[$i];
                $pq[$i] = $pq[$p];
                $pq[$p] = $tmp;
                $i = $p;
            }
        };
        $pop = function() use (&$pq) {
            $top = $pq[0];
            $last = array_pop($pq);
            if (count($pq)) {
                $pq[0] = $last;
                $i = 0;
                while (true) {
                    $largest = $i;
                    $l = $i * 2 + 1;
                    $r = $i * 2 + 2;
                    if ($l < count($pq) && $pq[$l] > $pq[$largest]) $largest = $l;
                    if ($r < count($pq) && $pq[$r] > $pq[$largest]) $largest = $r;
                    if ($largest === $i) break;
                    $tmp = $pq[$i];
                    $pq[$i] = $pq[$largest];
                    $pq[$largest] = $tmp;
                    $i = $largest;
                }
            }
            return $top;
        };
        $all = $stations;
        $all[] = [$target, 0];
        $ans = 0;
        $prev = 0;
        $fuel = $startFuel;
        foreach ($all as $st) {
            $pos = $st[0];
            $gas = $st[1];
            $fuel -= $pos - $prev;
            while (count($pq) && $fuel < 0) {
                $fuel += $pop();
                $ans++;
            }
            if ($fuel < 0) return -1;
            $push($gas);
            $prev = $pos;
        }
        return $ans;
    }
}
