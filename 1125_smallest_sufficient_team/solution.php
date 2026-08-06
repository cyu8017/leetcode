<?php
// LeetCode 1125 - Smallest Sufficient Team
// https://leetcode.com/problems/smallest-sufficient-team/

class Solution {
    /**
     * @param String[] $req_skills
     * @param String[][] $people
     * @return Integer[]
     */
    function smallestSufficientTeam($req_skills, $people) {
        $n = count($req_skills);
        $skillId = array_flip($req_skills);
        $m = 1 << $n;
        $dp = array_fill(0, $m, null);
        $dp[0] = [];
        foreach ($people as $i => $skills) {
            $mask = 0;
            foreach ($skills as $s) {
                if (isset($skillId[$s])) $mask |= 1 << $skillId[$s];
            }
            if ($mask === 0) continue;
            for ($prev = 0; $prev < $m; $prev++) {
                if ($dp[$prev] === null) continue;
                $comb = $prev | $mask;
                if ($dp[$comb] === null || count($dp[$comb]) > count($dp[$prev]) + 1) {
                    $dp[$comb] = array_merge($dp[$prev], [$i]);
                }
            }
        }
        return $dp[$m - 1];
    }
}
