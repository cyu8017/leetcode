<?php
// LeetCode 2747 - Count Zero Request Servers
// https://leetcode.com/problems/count-zero-request-servers/

class Solution {
    function countServers($n, $logs, $x, $queries) {
        usort($logs, function($a, $b) { return $a[1] <=> $b[1]; });
        $qs = [];
        foreach ($queries as $i => $t) $qs[] = [$t, $i];
        usort($qs, function($a, $b) { return $a[0] <=> $b[0]; });
        $ans = array_fill(0, count($queries), 0);
        $cnt = [];
        $active = 0;
        $l = 0;
        $r = 0;
        $m = count($logs);
        foreach ($qs as $q) {
            $t = $q[0];
            $qi = $q[1];
            while ($r < $m && $logs[$r][1] <= $t) {
                $id = $logs[$r][0];
                $c = $cnt[$id] ?? 0;
                if ($c === 0) $active++;
                $cnt[$id] = $c + 1;
                $r++;
            }
            while ($l < $r && $logs[$l][1] < $t - $x) {
                $id = $logs[$l][0];
                $c = $cnt[$id] - 1;
                $cnt[$id] = $c;
                if ($c === 0) $active--;
                $l++;
            }
            $ans[$qi] = $n - $active;
        }
        return $ans;
    }
}
