<?php
// LeetCode 3680 - Generate Schedule
// https://leetcode.com/problems/generate-schedule/

class Solution {
    function generateSchedule($n) {
        if ($n < 5) return [];
        $matches = [];
        for ($i = 0; $i < $n; $i++)
            for ($j = 0; $j < $n; $j++)
                if ($i !== $j) $matches[] = [$i, $j];
        $used = array_fill(0, count($matches), false);
        $sched = [];
        $last0 = -1;
        $last1 = -1;
        $dfs = function() use (&$dfs, &$matches, &$used, &$sched, &$last0, &$last1) {
            if (count($sched) === count($matches)) return true;
            $mn = count($matches);
            for ($i = 0; $i < $mn; $i++) {
                if ($used[$i]) continue;
                $m = $matches[$i];
                if ($m[0] === $last0 || $m[0] === $last1 || $m[1] === $last0 || $m[1] === $last1) continue;
                $used[$i] = true;
                $sched[] = $m;
                $p0 = $last0;
                $p1 = $last1;
                $last0 = $m[0];
                $last1 = $m[1];
                if ($dfs()) return true;
                $last0 = $p0;
                $last1 = $p1;
                array_pop($sched);
                $used[$i] = false;
            }
            return false;
        };
        if ($dfs()) return $sched;
        return [];
    }
}
