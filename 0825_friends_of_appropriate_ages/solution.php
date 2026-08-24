<?php
// LeetCode 0825 - Friends Of Appropriate Ages
// https://leetcode.com/problems/friends-of-appropriate-ages/

class Solution {
    /**
     * @param Integer[] $ages
     * @return Integer
     */
    function numFriendRequests($ages) {
        $count = array_fill(0, 121, 0);
        foreach ($ages as $age) $count[$age]++;
        $ans = 0;
        for ($a = 1; $a <= 120; $a++) {
            if (!$count[$a]) continue;
            for ($b = 1; $b <= 120; $b++) {
                if (!$count[$b]) continue;
                if ($b <= 0.5 * $a + 7) continue;
                if ($b > $a) continue;
                if ($b > 100 && $a < 100) continue;
                $ans += $count[$a] * $count[$b];
                if ($a === $b) $ans -= $count[$a];
            }
        }
        return $ans;
    }
}
