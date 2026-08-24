<?php
// LeetCode 3354 - Make Array Elements Equal to Zero
// https://leetcode.com/problems/make-array-elements-equal-to-zero/

class Solution {
    function countValidSelections($nums) {
        $n = count($nums);
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            if ($nums[$i] !== 0) continue;
            foreach ([-1, 1] as $dir) {
                $a = $nums;
                $cur = $i;
                $d = $dir;
                while ($cur >= 0 && $cur < $n) {
                    if ($a[$cur] === 0) $cur += $d;
                    else {
                        $a[$cur]--;
                        $d = -$d;
                        $cur += $d;
                    }
                }
                $ok = true;
                foreach ($a as $v) if ($v !== 0) { $ok = false; break; }
                if ($ok) $ans++;
            }
        }
        return $ans;
    }
}
