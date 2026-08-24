<?php
// LeetCode 3387 - Maximize Amount After Two Days of Conversions
// https://leetcode.com/problems/maximize-amount-after-two-days-of-conversions/

class Solution {
    function buildRateGraph($pairs, $rates) {
        $g = [];
        for ($i = 0; $i < count($pairs); $i++) {
            $a = $pairs[$i][0];
            $b = $pairs[$i][1];
            if (!isset($g[$a])) $g[$a] = [];
            if (!isset($g[$b])) $g[$b] = [];
            $g[$a][$b] = $rates[$i];
            $g[$b][$a] = 1.0 / $rates[$i];
        }
        return $g;
    }

    function bellman($start, $pairs, $rates) {
        $g = $this->buildRateGraph($pairs, $rates);
        $dist = [];
        $dist[$start] = 1.0;
        for ($it = 0; $it < 100; $it++) {
            $updated = false;
            foreach ($g as $from => $tos) {
                if (!isset($dist[$from]) || $dist[$from] === 0) continue;
                foreach ($tos as $to => $rate) {
                    $nv = $dist[$from] * $rate;
                    if (!isset($dist[$to]) || $nv > $dist[$to]) {
                        $dist[$to] = $nv;
                        $updated = true;
                    }
                }
            }
            if (!$updated) break;
        }
        return $dist;
    }

    function maxAmount($initialCurrency, $pairs1, $rates1, $pairs2, $rates2) {
        $amt1 = $this->bellman($initialCurrency, $pairs1, $rates1);
        $ans = 1.0;
        $g2 = $this->buildRateGraph($pairs2, $rates2);
        foreach ($amt1 as $c => $a) {
            if ($a <= 0) continue;
            $dist = [];
            $dist[$c] = $a;
            $updated = true;
            for ($it = 0; $it < 100 && $updated; $it++) {
                $updated = false;
                foreach ($g2 as $from => $tos) {
                    if (!isset($dist[$from]) || $dist[$from] === 0) continue;
                    foreach ($tos as $to => $rate) {
                        $nv = $dist[$from] * $rate;
                        if (!isset($dist[$to]) || $nv > $dist[$to]) {
                            $dist[$to] = $nv;
                            $updated = true;
                        }
                    }
                }
            }
            if (isset($dist[$initialCurrency]) && $dist[$initialCurrency] > $ans) {
                $ans = $dist[$initialCurrency];
            }
        }
        return $ans;
    }
}
