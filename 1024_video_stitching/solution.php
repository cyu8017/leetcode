<?php
// LeetCode 1024 - Video Stitching
// https://leetcode.com/problems/video-stitching/

class Solution {
    /**
     * @param Integer[][] $clips
     * @param Integer $time
     * @return Integer
     */
    function videoStitching($clips, $time) {
        $furthest = array_fill(0, $time + 1, 0);
        foreach ($clips as $clip) {
            $start = $clip[0];
            $end = $clip[1];
            if ($start <= $time) {
                $furthest[$start] = max($furthest[$start], $end);
            }
        }
        $ans = $reach = $nextReach = 0;
        for ($i = 0; $i < $time; $i++) {
            $nextReach = max($nextReach, $furthest[$i]);
            if ($i === $reach) {
                if ($nextReach <= $i) {
                    return -1;
                }
                $ans++;
                $reach = $nextReach;
            }
        }
        return $ans;
    }
}
