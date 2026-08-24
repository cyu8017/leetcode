<?php
// LeetCode 2325 - Decode the Message
// https://leetcode.com/problems/decode-the-message/

class Solution {
    function decodeMessage($key, $message) {
        $mp = array_fill(0, 26, 0);
        $next = 97;
        $kn = strlen($key);
        for ($i = 0; $i < $kn; $i++) {
            $c = $key[$i];
            if ($c === ' ' || $mp[ord($c) - 97] !== 0) continue;
            $mp[ord($c) - 97] = $next++;
        }
        $out = $message;
        $n = strlen($out);
        for ($i = 0; $i < $n; $i++) {
            if ($out[$i] !== ' ') $out[$i] = chr($mp[ord($out[$i]) - 97]);
        }
        return $out;
    }
}
