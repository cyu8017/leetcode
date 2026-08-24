<?php
// LeetCode 2122 - Recover the Original Array
// https://leetcode.com/problems/recover-the-original-array/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function recoverArray($nums) {
        sort($nums);
        $n = count($nums);
        for ($i = 1; $i < $n; $i++) {
            $diff = $nums[$i] - $nums[0];
            if ($diff === 0 || $diff % 2 !== 0) continue;
            $k = intdiv($diff, 2);
            $used = array_fill(0, $n, false);
            $used[0] = true;
            $used[$i] = true;
            $ans = [intdiv($nums[0] + $nums[$i], 2)];
            $l = 0;
            $r = $i;
            $ok = true;
            while (count($ans) < intdiv($n, 2)) {
                while ($l < $n && $used[$l]) $l++;
                if ($l === $n) { $ok = false; break; }
                $need = $nums[$l] + 2 * $k;
                while ($r < $n && ($used[$r] || $nums[$r] < $need)) $r++;
                if ($r === $n || $nums[$r] !== $need) { $ok = false; break; }
                $used[$l] = true;
                $used[$r] = true;
                $ans[] = $nums[$l] + $k;
            }
            if ($ok) return $ans;
        }
        return [];
    }
}
