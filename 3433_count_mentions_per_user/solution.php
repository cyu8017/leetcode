<?php
// LeetCode 3433 - Count Mentions Per User
// https://leetcode.com/problems/count-mentions-per-user/

class Solution {
    function countMentions($numberOfUsers, $events) {
        usort($events, function($a, $b) {
            $ti = intval($a[1]);
            $tj = intval($b[1]);
            if ($ti !== $tj) return $ti <=> $tj;
            return strcmp($b[0], $a[0]);
        });
        $online = array_fill(0, $numberOfUsers, true);
        $offlineUntil = array_fill(0, $numberOfUsers, 0);
        $ans = array_fill(0, $numberOfUsers, 0);
        foreach ($events as $e) {
            $t = intval($e[1]);
            for ($i = 0; $i < $numberOfUsers; $i++) {
                if (!$online[$i] && $offlineUntil[$i] <= $t) $online[$i] = true;
            }
            if ($e[0] === "OFFLINE") {
                $id = intval($e[2]);
                $online[$id] = false;
                $offlineUntil[$id] = $t + 60;
            } else {
                $msg = $e[2];
                if ($msg === "ALL") {
                    for ($i = 0; $i < $numberOfUsers; $i++) $ans[$i]++;
                } else if ($msg === "HERE") {
                    for ($i = 0; $i < $numberOfUsers; $i++) if ($online[$i]) $ans[$i]++;
                } else {
                    foreach (explode(" ", $msg) as $part) {
                        $id = intval(substr($part, 2));
                        $ans[$id]++;
                    }
                }
            }
        }
        return $ans;
    }
}
