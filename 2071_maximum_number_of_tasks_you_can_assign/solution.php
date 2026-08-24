<?php
// LeetCode 2071 - Maximum Number of Tasks You Can Assign
// https://leetcode.com/problems/maximum-number-of-tasks-you-can-assign/

class Solution {
    /**
     * @param Integer[] $tasks
     * @param Integer[] $workers
     * @param Integer $pills
     * @param Integer $strength
     * @return Integer
     */
    function maxTaskAssign($tasks, $workers, $pills, $strength) {
        sort($tasks);
        sort($workers);
        $remove = function (&$ws, $x) {
            $ws[$x]--;
            if ($ws[$x] === 0) unset($ws[$x]);
        };
        $can = function ($k) use ($tasks, $workers, $pills, $strength, $remove) {
            if ($k === 0) return true;
            $ws = [];
            $wn = count($workers);
            for ($i = $wn - $k; $i < $wn; $i++)
                $ws[$workers[$i]] = ($ws[$workers[$i]] ?? 0) + 1;
            $p = $pills;
            for ($i = $k - 1; $i >= 0; $i--) {
                $task = $tasks[$i];
                $ks = array_keys($ws);
                sort($ks);
                $strongest = $ks[count($ks) - 1];
                if ($strongest >= $task) {
                    $remove($ws, $strongest);
                    continue;
                }
                if ($p === 0) return false;
                $need = $task - $strength;
                $found = null;
                foreach ($ks as $key) if ($key >= $need) { $found = $key; break; }
                if ($found === null) return false;
                $remove($ws, $found);
                $p--;
            }
            return true;
        };
        $lo = 0;
        $hi = min(count($tasks), count($workers));
        while ($lo < $hi) {
            $mid = ($lo + $hi + 1) >> 1;
            if ($can($mid)) $lo = $mid;
            else $hi = $mid - 1;
        }
        return $lo;
    }
}
