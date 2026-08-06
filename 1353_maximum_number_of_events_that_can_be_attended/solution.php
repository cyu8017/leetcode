<?php
class Solution {
    function maxEvents($events) {
        usort($events, function($a, $b) { return $a[0] <=> $b[0]; });
        $h = new SplMinHeap();
        $i = 0;
        $ans = 0;
        $day = 0;
        $n = count($events);
        while ($i < $n || !$h->isEmpty()) {
            if ($h->isEmpty()) $day = max($day, $events[$i][0]);
            while ($i < $n && $events[$i][0] <= $day) {
                $h->insert($events[$i][1]);
                $i++;
            }
            while (!$h->isEmpty() && $h->top() < $day) $h->extract();
            if (!$h->isEmpty()) {
                $h->extract();
                $ans++;
                $day++;
            }
        }
        return $ans;
    }
}
