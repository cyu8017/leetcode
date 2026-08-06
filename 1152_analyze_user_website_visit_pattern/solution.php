<?php
// LeetCode 1152 - Analyze User Website Visit Pattern
// https://leetcode.com/problems/analyze-user-website-visit-pattern/

class Solution {
    /**
     * @param String[] $username
     * @param Integer[] $timestamp
     * @param String[] $website
     * @return String[]
     */
    function mostVisitedPattern($username, $timestamp, $website) {
        $visits = [];
        $n = count($username);
        for ($i = 0; $i < $n; $i++) {
            $visits[$username[$i]][] = [$timestamp[$i], $website[$i]];
        }
        $scores = [];
        foreach ($visits as $user => $list) {
            usort($list, fn($a, $b) => $a[0] <=> $b[0]);
            $sites = array_map(fn($x) => $x[1], $list);
            $patterns = [];
            $m = count($sites);
            for ($i = 0; $i < $m; $i++) {
                for ($j = $i + 1; $j < $m; $j++) {
                    for ($k = $j + 1; $k < $m; $k++) {
                        $key = $sites[$i] . "\0" . $sites[$j] . "\0" . $sites[$k];
                        $patterns[$key] = [$sites[$i], $sites[$j], $sites[$k]];
                    }
                }
            }
            foreach ($patterns as $key => $pattern) {
                $scores[$key] = ($scores[$key] ?? [0, $pattern]);
                $scores[$key][0]++;
            }
        }
        $bestCount = -1;
        $best = null;
        foreach ($scores as [$count, $pattern]) {
            if ($count > $bestCount || ($count === $bestCount && ($best === null || $pattern < $best))) {
                $bestCount = $count;
                $best = $pattern;
            }
        }
        return $best;
    }
}
