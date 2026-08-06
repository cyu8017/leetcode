<?php
// LeetCode 1239 - Maximum Length of a Concatenated String with Unique Characters
// https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/

class Solution {
    /**
     * @param String[] $arr
     * @return Integer
     */
    function maxLength($arr) {
        $masks = [[0, 0]];
        foreach ($arr as $word) {
            $mask = 0;
            $len = strlen($word);
            $ok = true;
            for ($i = 0; $i < $len; $i++) {
                $bit = 1 << (ord($word[$i]) - 97);
                if ($mask & $bit) { $ok = false; break; }
                $mask |= $bit;
            }
            if (!$ok || substr_count(decbin($mask), '1') !== $len) continue;
            $extra = [];
            foreach ($masks as [$used, $length]) {
                if (($used & $mask) === 0) $extra[] = [$used | $mask, $length + $len];
            }
            foreach ($extra as $e) $masks[] = $e;
        }
        $best = 0;
        foreach ($masks as [, $length]) $best = max($best, $length);
        return $best;
    }
}
