<?php
// LeetCode 0943 - Find the Shortest Superstring
// https://leetcode.com/problems/find-the-shortest-superstring/

class Solution {
    function shortestSuperstring($words) {
        $n = count($words);
        $overlap = [];
        for ($i = 0; $i < $n; $i++) {
            $overlap[$i] = array_fill(0, $n, 0);
            for ($j = 0; $j < $n; $j++) {
                if ($i === $j) continue;
                $a = $words[$i];
                $b = $words[$j];
                for ($k = min(strlen($a), strlen($b)); $k > 0; $k--) {
                    if (substr($a, -$k) === substr($b, 0, $k)) {
                        $overlap[$i][$j] = $k;
                        break;
                    }
                }
            }
        }
        $N = 1 << $n;
        $dp = [];
        for ($mask = 0; $mask < $N; $mask++) $dp[$mask] = array_fill(0, $n, null);
        for ($i = 0; $i < $n; $i++) $dp[1 << $i][$i] = $words[$i];
        for ($mask = 0; $mask < $N; $mask++) {
            for ($last = 0; $last < $n; $last++) {
                if (($mask & (1 << $last)) === 0 || $dp[$mask][$last] === null) continue;
                for ($nxt = 0; $nxt < $n; $nxt++) {
                    if (($mask & (1 << $nxt)) !== 0) continue;
                    $cand = $dp[$mask][$last] . substr($words[$nxt], $overlap[$last][$nxt]);
                    $nmask = $mask | (1 << $nxt);
                    if ($dp[$nmask][$nxt] === null || strlen($cand) < strlen($dp[$nmask][$nxt]))
                        $dp[$nmask][$nxt] = $cand;
                }
            }
        }
        $full = $N - 1;
        $best = null;
        for ($i = 0; $i < $n; $i++) {
            if ($dp[$full][$i] !== null && ($best === null || strlen($dp[$full][$i]) < strlen($best)))
                $best = $dp[$full][$i];
        }
        return $best;
    }
}
