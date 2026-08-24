<?php
// LeetCode 2456 - Most Popular Video Creator
// https://leetcode.com/problems/most-popular-video-creator/

class Solution {
    function mostPopularCreator($creators, $ids, $views) {
        $mp = [];
        $maxTotal = 0;
        $n = count($creators);
        for ($i = 0; $i < $n; $i++) {
            $c = $creators[$i];
            if (!isset($mp[$c])) {
                $mp[$c] = ["total" => $views[$i], "bestID" => $ids[$i], "bestViews" => $views[$i]];
            } else {
                $mp[$c]["total"] += $views[$i];
                if ($views[$i] > $mp[$c]["bestViews"] ||
                    ($views[$i] === $mp[$c]["bestViews"] && $ids[$i] < $mp[$c]["bestID"])) {
                    $mp[$c]["bestViews"] = $views[$i];
                    $mp[$c]["bestID"] = $ids[$i];
                }
            }
            if ($mp[$c]["total"] > $maxTotal) $maxTotal = $mp[$c]["total"];
        }
        $ans = [];
        foreach ($mp as $creator => $info) {
            if ($info["total"] === $maxTotal) $ans[] = [$creator, $info["bestID"]];
        }
        return $ans;
    }
}
