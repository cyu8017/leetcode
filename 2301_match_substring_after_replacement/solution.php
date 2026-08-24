<?php
// LeetCode 2301 - Match Substring After Replacement
// https://leetcode.com/problems/match-substring-after-replacement/

class Solution {
    function matchReplacement($s, $sub, $mappings) {
        $allow = [];
        foreach ($mappings as $m) $allow[(ord($m[0]) << 8) | ord($m[1])] = true;
        $n = strlen($s);
        $mlen = strlen($sub);
        for ($i = 0; $i + $mlen <= $n; $i++) {
            $ok = true;
            for ($j = 0; $j < $mlen; $j++) {
                $a = $s[$i + $j];
                $b = $sub[$j];
                if ($a === $b || isset($allow[(ord($b) << 8) | ord($a)])) continue;
                $ok = false;
                break;
            }
            if ($ok) return true;
        }
        return false;
    }
}
