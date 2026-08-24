<?php
// LeetCode 2977 - Minimum Cost to Convert String II
// https://leetcode.com/problems/minimum-cost-to-convert-string-ii/

class Solution {
    function minimumCost($source, $target, $original, $changed, $cost) {
        $INF = PHP_INT_MAX / 4;
        $ids = [];
        $id = 0;
        for ($i = 0; $i < count($original); $i++) {
            if (!isset($ids[$original[$i]])) $ids[$original[$i]] = $id++;
            if (!isset($ids[$changed[$i]])) $ids[$changed[$i]] = $id++;
        }
        $m = count($ids);
        $dist = [];
        for ($i = 0; $i < $m; $i++) {
            $dist[$i] = array_fill(0, $m, $INF);
            $dist[$i][$i] = 0;
        }
        for ($i = 0; $i < count($original); $i++) {
            $u = $ids[$original[$i]];
            $v = $ids[$changed[$i]];
            $ww = $cost[$i];
            if ($ww < $dist[$u][$v]) $dist[$u][$v] = $ww;
        }
        for ($k = 0; $k < $m; $k++) {
            for ($i = 0; $i < $m; $i++) {
                for ($j = 0; $j < $m; $j++) {
                    if ($dist[$i][$k] + $dist[$k][$j] < $dist[$i][$j]) {
                        $dist[$i][$j] = $dist[$i][$k] + $dist[$k][$j];
                    }
                }
            }
        }
        $n = strlen($source);
        $dp = array_fill(0, $n + 1, $INF);
        $dp[0] = 0;
        $lens = [];
        foreach ($ids as $key => $_) $lens[strlen($key)] = true;
        for ($i = 0; $i < $n; $i++) {
            if ($dp[$i] >= $INF / 2) continue;
            if ($source[$i] === $target[$i] && $dp[$i] < $dp[$i + 1]) $dp[$i + 1] = $dp[$i];
            foreach ($lens as $L => $_) {
                if ($i + $L > $n) continue;
                $ss = substr($source, $i, $L);
                $tt = substr($target, $i, $L);
                if (!isset($ids[$ss]) || !isset($ids[$tt])) continue;
                $iu = $ids[$ss];
                $iv = $ids[$tt];
                if ($dist[$iu][$iv] < $INF / 2) {
                    $cand = $dp[$i] + $dist[$iu][$iv];
                    if ($cand < $dp[$i + $L]) $dp[$i + $L] = $cand;
                }
            }
        }
        if ($dp[$n] >= $INF / 2) return -1;
        return $dp[$n];
    }
}
