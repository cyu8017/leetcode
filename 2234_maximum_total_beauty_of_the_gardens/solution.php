<?php
// LeetCode 2234 - Maximum Total Beauty of the Gardens
// https://leetcode.com/problems/maximum-total-beauty-of-the-gardens/

class Solution {
    function maximumBeauty($flowers, $newFlowers, $target, $full, $partial) {
        $n = count($flowers);
        for ($i = 0; $i < $n; $i++) if ($flowers[$i] > $target) $flowers[$i] = $target;
        sort($flowers);
        $sum = 0;
        foreach ($flowers as $f) $sum += $f;
        if ($target * $n - $sum <= $newFlowers) {
            $allFull = $n * $full;
            $leaveOne = $n > 0 ? ($n - 1) * $full + ($target - 1) * $partial : 0;
            return max($allFull, $leaveOne);
        }
        $pref = array_fill(0, $n + 1, 0);
        for ($i = 0; $i < $n; $i++) $pref[$i + 1] = $pref[$i] + $flowers[$i];
        $ans = 0;
        $j = $n - 1;
        $remain = $newFlowers;
        for ($complete = 0; $complete <= $n; $complete++) {
            if ($complete > 0) {
                $need = $target - $flowers[$n - $complete];
                if ($remain < $need) break;
                $remain -= $need;
            }
            while ($j >= $n - $complete || ($j >= 0 && $flowers[$j] * ($j + 1) - $pref[$j + 1] > $remain)) $j--;
            $partialVal = 0;
            if ($j >= 0) {
                $extra = intdiv($remain - ($flowers[$j] * ($j + 1) - $pref[$j + 1]), $j + 1);
                $partialVal = $flowers[$j] + $extra;
                if ($partialVal >= $target) $partialVal = $target - 1;
            }
            $ans = max($ans, $complete * $full + $partialVal * $partial);
        }
        return $ans;
    }
}
