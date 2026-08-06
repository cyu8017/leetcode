<?php
class Solution {
    /**
     * @param Integer[] $tasks
     * @param Integer $sessionTime
     * @return Integer
     */
    function minSessions($tasks, $sessionTime) {
        $n = count($tasks);
        $full = 1 << $n;
        $infSessions = $n + 1;
        $dp = array_fill(0, $full, [$infSessions, 0]);
        $dp[0] = [1, 0];
        for ($mask = 0; $mask < $full; $mask++) {
            [$sessions, $used] = $dp[$mask];
            if ($sessions > $n) {
                continue;
            }
            for ($i = 0; $i < $n; $i++) {
                if ($mask & (1 << $i)) {
                    continue;
                }
                $t = $tasks[$i];
                $nmask = $mask | (1 << $i);
                if ($used + $t <= $sessionTime) {
                    $cand = [$sessions, $used + $t];
                } else {
                    $cand = [$sessions + 1, $t];
                }
                if ($cand[0] < $dp[$nmask][0] ||
                    ($cand[0] === $dp[$nmask][0] && $cand[1] < $dp[$nmask][1])) {
                    $dp[$nmask] = $cand;
                }
            }
        }
        return $dp[$full - 1][0];
    }
}
