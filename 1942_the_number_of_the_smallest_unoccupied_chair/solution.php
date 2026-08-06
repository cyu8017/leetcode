<?php

class Solution {
    /**
     * @param Integer[][] $times
     * @param Integer $targetFriend
     * @return Integer
     */
    function smallestChair($times, $targetFriend) {
        $n = count($times);
        $order = range(0, $n - 1);
        usort($order, function ($a, $b) use ($times) {
            return $times[$a][0] <=> $times[$b][0];
        });

        $free = new SplMinHeap();
        $nextChair = 0;
        $leaving = new SplMinHeap();

        foreach ($order as $i) {
            $arr = $times[$i][0];
            $leave = $times[$i][1];
            while (!$leaving->isEmpty() && $leaving->top()[0] <= $arr) {
                $free->insert($leaving->extract()[1]);
            }
            if (!$free->isEmpty()) {
                $chair = $free->extract();
            } else {
                $chair = $nextChair;
                $nextChair++;
            }
            if ($i === $targetFriend) {
                return $chair;
            }
            $leaving->insert([$leave, $chair]);
        }
        return -1;
    }
}
