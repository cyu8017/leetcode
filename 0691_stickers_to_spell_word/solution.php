<?php
// LeetCode 0691 - Stickers to Spell Word
// https://leetcode.com/problems/stickers-to-spell-word/

class Solution {
    function minStickers($stickers, $target) {
        $need = array_fill(0, 26, 0);
        $len = strlen($target);
        for ($i = 0; $i < $len; $i++) $need[ord($target[$i]) - 97]++;
        $chars = [];
        for ($i = 0; $i < 26; $i++) if ($need[$i] > 0) $chars[] = chr(97 + $i);
        $sticks = [];
        foreach ($stickers as $sticker) {
            $counts = array_fill(0, 26, 0);
            $slen = strlen($sticker);
            for ($i = 0; $i < $slen; $i++) $counts[ord($sticker[$i]) - 97]++;
            $useful = false;
            foreach ($chars as $ch) if ($counts[ord($ch) - 97] > 0) { $useful = true; break; }
            if ($useful) $sticks[] = $counts;
        }
        $memo = [];
        $dfs = function ($state) use (&$dfs, &$memo, &$chars, &$sticks) {
            $k = implode(',', $state);
            if (isset($memo[$k])) return $memo[$k];
            $i = 0;
            while ($i < count($state) && $state[$i] === 0) $i++;
            if ($i === count($state)) {
                $memo[$k] = 0;
                return 0;
            }
            $first = $chars[$i];
            $best = 1000000000;
            foreach ($sticks as $stick) {
                if ($stick[ord($first) - 97] === 0) continue;
                $nxt = $state;
                for ($j = 0; $j < count($chars); $j++) {
                    $nxt[$j] = max(0, $nxt[$j] - $stick[ord($chars[$j]) - 97]);
                }
                $best = min($best, 1 + $dfs($nxt));
            }
            $memo[$k] = $best;
            return $best;
        };
        $state = [];
        foreach ($chars as $ch) $state[] = $need[ord($ch) - 97];
        $result = $dfs($state);
        return $result >= 1000000000 ? -1 : $result;
    }
}
