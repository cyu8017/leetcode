<?php
// LeetCode 2402 - Meeting Rooms III
// https://leetcode.com/problems/meeting-rooms-iii/

class Solution {
    function mostBooked($n, $meetings) {
        usort($meetings, function($a, $b) { return $a[0] - $b[0]; });
        $free = new SplPriorityQueue();
        $free->setExtractFlags(SplPriorityQueue::EXTR_DATA);
        $busy = new SplPriorityQueue();
        $busy->setExtractFlags(SplPriorityQueue::EXTR_DATA);
        for ($i = 0; $i < $n; $i++) $free->insert($i, -$i);
        $cnt = array_fill(0, $n, 0);
        foreach ($meetings as $m) {
            $start = $m[0];
            $end = $m[1];
            while (!$busy->isEmpty()) {
                $top = $busy->top();
                if ($top[0] > $start) break;
                $busy->extract();
                $free->insert($top[1], -$top[1]);
            }
            $dur = $end - $start;
            if (!$free->isEmpty()) {
                $room = $free->extract();
                $begin = $start;
            } else {
                $top = $busy->extract();
                $begin = $top[0];
                $room = $top[1];
            }
            $finish = $begin + $dur;
            $busy->insert([$finish, $room], -($finish * ($n + 1) + $room));
            $cnt[$room]++;
        }
        $ans = 0;
        for ($i = 1; $i < $n; $i++) if ($cnt[$i] > $cnt[$ans]) $ans = $i;
        return $ans;
    }
}
