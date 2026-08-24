<?php
// LeetCode 3181 - Maximum Total Reward Using Operations II
// https://leetcode.com/problems/maximum-total-reward-using-operations-ii/

class Solution {
    function maxTotalReward($rewardValues) {
        sort($rewardValues);
        $uniq = [];
        foreach ($rewardValues as $x) {
            if (empty($uniq) || $x !== $uniq[count($uniq) - 1]) $uniq[] = $x;
        }
        $W = 31;
        $MASK = 0x7FFFFFFF;
        $maxBit = 100001;
        $nw = intdiv($maxBit + $W - 1, $W) + 40;
        $f = array_fill(0, $nw, 0);
        $f[0] = 1;
        foreach ($uniq as $v) {
            $maskWords = intdiv($v, $W);
            $maskRem = $v % $W;
            $shifted = array_fill(0, $nw, 0);
            $srcWords = $maskWords + ($maskRem ? 1 : 0);
            for ($i = 0; $i < $srcWords && $i < $nw; $i++) {
                $word = $f[$i];
                if ($i === $maskWords && $maskRem) $word &= (1 << $maskRem) - 1;
                $dest = $i + $maskWords;
                if ($dest < $nw) $shifted[$dest] |= (($word << $maskRem) & $MASK);
                if ($maskRem && $dest + 1 < $nw) $shifted[$dest + 1] |= ($word >> ($W - $maskRem));
            }
            for ($i = 0; $i < $nw; $i++) $f[$i] |= $shifted[$i];
        }
        for ($i = 100000; $i >= 0; $i--) {
            $wi = intdiv($i, $W);
            $bi = $i % $W;
            if (($f[$wi] >> $bi) & 1) return $i;
        }
        return 0;
    }
}
