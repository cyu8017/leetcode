#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
SOLUTIONS = {}

def add(folder, body):
    SOLUTIONS[folder] = body

add("3957_maximum_sum_of_m_non_overlapping_subarrays_ii", r'''<?php
// LeetCode 3957 - Maximum Sum of M Non-Overlapping Subarrays II
// https://leetcode.com/problems/maximum-sum-of-m-non-overlapping-subarrays-ii/

class Solution {
    function maxSum($nums, $m, $l, $r) {
        $n = count($nums);
        $prefix = array_fill(0, $n + 1, 0);
        for ($i = 0; $i < $n; $i++) $prefix[$i + 1] = $prefix[$i] + $nums[$i];
        $unconstrained = $this->run($prefix, $n, $l, $r, 0);
        if ($unconstrained[1] > 0 && $unconstrained[1] <= $m) return $unconstrained[0];
        if ($unconstrained[1] > $m) {
            $bound = 0;
            foreach ($nums as $value) $bound += $value >= 0 ? $value : -$value;
            $low = 0;
            $high = $bound + 1;
            while ($low < $high) {
                $mid = $low + intdiv($high - $low + 1, 2);
                if ($this->run($prefix, $n, $l, $r, $mid)[1] >= $m) $low = $mid;
                else $high = $mid - 1;
            }
            $state = $this->run($prefix, $n, $l, $r, $low);
            return $state[0] + $low * $m;
        }
        $infinity = 1 << 60;
        $bestSingle = -$infinity;
        $deque = [];
        for ($end = 1; $end <= $n; $end++) {
            $addIndex = $end - $l;
            if ($addIndex >= 0) {
                while (count($deque) > 0 && $prefix[$deque[count($deque) - 1]] >= $prefix[$addIndex]) array_pop($deque);
                $deque[] = $addIndex;
            }
            $minIndex = $end - $r;
            while (count($deque) > 0 && $deque[0] < $minIndex) array_shift($deque);
            if (count($deque) > 0) {
                $sum = $prefix[$end] - $prefix[$deque[0]];
                if ($sum > $bestSingle) $bestSingle = $sum;
            }
        }
        return $bestSingle;
    }

    private function better($a, $b) {
        return $a[0] > $b[0] || ($a[0] === $b[0] && $a[1] > $b[1]);
    }

    private function run($prefix, $n, $l, $r, $penalty) {
        $dp = array_fill(0, $n + 1, [0, 0]);
        $deque = [];
        for ($end = 1; $end <= $n; $end++) {
            $addIndex = $end - $l;
            if ($addIndex >= 0) {
                while (count($deque) > 0) {
                    $last = $deque[count($deque) - 1];
                    $left = [$dp[$addIndex][0] - $prefix[$addIndex], $dp[$addIndex][1]];
                    $right = [$dp[$last][0] - $prefix[$last], $dp[$last][1]];
                    if (!$this->better($left, $right)) break;
                    array_pop($deque);
                }
                $deque[] = $addIndex;
            }
            $minIndex = $end - $r;
            while (count($deque) > 0 && $deque[0] < $minIndex) array_shift($deque);
            $dp[$end] = [$dp[$end - 1][0], $dp[$end - 1][1]];
            if (count($deque) > 0) {
                $start = $deque[0];
                $take = [$dp[$start][0] + $prefix[$end] - $prefix[$start] - $penalty, $dp[$start][1] + 1];
                if ($this->better($take, $dp[$end])) $dp[$end] = $take;
            }
        }
        return $dp[$n];
    }
}
''')

add("3971_maximum_total_value", r'''<?php
// LeetCode 3971 - Maximum Total Value
// https://leetcode.com/problems/maximum-total-value/

class Solution {
    function maximumTotalValue($value, $decay, $m) {
        $mod = 1000000007;
        if ($this->countAtLeast($value, $decay, 1) <= $m) {
            $sum = 0;
            for ($i = 0; $i < count($value); $i++) {
                $terms = intdiv($value[$i] - 1, $decay[$i]) + 1;
                $sum = ($sum + $terms * $value[$i] - $decay[$i] * $terms * ($terms - 1) / 2) % $mod;
            }
            return $sum;
        }
        $high = 0;
        foreach ($value as $v) if ($v > $high) $high = $v;
        $low = 1;
        while ($low < $high) {
            $mid = intdiv($low + $high + 1, 2);
            if ($this->countAtLeast($value, $decay, $mid) >= $m) $low = $mid;
            else $high = $mid - 1;
        }
        $threshold = $low;
        $count = 0;
        $sum = 0;
        for ($i = 0; $i < count($value); $i++) {
            if ($value[$i] < $threshold) continue;
            $terms = intdiv($value[$i] - $threshold, $decay[$i]) + 1;
            $count += $terms;
            $sum = ($sum + ($terms * $value[$i] - $decay[$i] * $terms * ($terms - 1) / 2) % $mod) % $mod;
        }
        $sum = ($sum - (($count - $m) % $mod) * ($threshold % $mod)) % $mod;
        if ($sum < 0) $sum += $mod;
        return $sum;
    }

    private function countAtLeast($value, $decay, $threshold) {
        $count = 0;
        for ($i = 0; $i < count($value); $i++) {
            if ($value[$i] >= $threshold) $count += intdiv($value[$i] - $threshold, $decay[$i]) + 1;
        }
        return $count;
    }
}
''')

add("3972_valid_subarrays_with_matching_sum_digits_ii", r'''<?php
// LeetCode 3972 - Valid Subarrays With Matching Sum Digits II
// https://leetcode.com/problems/valid-subarrays-with-matching-sum-digits-ii/

class Solution {
    function countValidSubarrays($nums, $x) {
        $byRemainder = array_fill(0, 10, []);
        $byRemainder[0][] = 0;
        $prefix = 0;
        $answer = 0;
        foreach ($nums as $value) {
            $prefix += $value;
            $required = (($prefix - $x) % 10 + 10) % 10;
            $values = $byRemainder[$required];
            for ($power = 1; $x * $power <= $prefix; $power *= 10) {
                $low = $x * $power;
                $high = ($x + 1) * $power - 1;
                $minPrefix = $prefix - $high;
                $maxPrefix = $prefix - $low;
                $left = $this->lowerBound($values, $minPrefix);
                $right = $this->upperBound($values, $maxPrefix);
                $answer += $right - $left;
                if ($power > intdiv($prefix, 10)) break;
            }
            $byRemainder[$prefix % 10][] = $prefix;
        }
        return $answer;
    }

    private function lowerBound($a, $x) {
        $lo = 0;
        $hi = count($a);
        while ($lo < $hi) {
            $mid = intdiv($lo + $hi, 2);
            if ($a[$mid] < $x) $lo = $mid + 1;
            else $hi = $mid;
        }
        return $lo;
    }

    private function upperBound($a, $x) {
        $lo = 0;
        $hi = count($a);
        while ($lo < $hi) {
            $mid = intdiv($lo + $hi, 2);
            if ($a[$mid] <= $x) $lo = $mid + 1;
            else $hi = $mid;
        }
        return $lo;
    }
}
''')

add("3977_minimum_time_to_reach_target_with_limited_power", r'''<?php
// LeetCode 3977 - Minimum Time to Reach Target With Limited Power
// https://leetcode.com/problems/minimum-time-to-reach-target-with-limited-power/

class Solution {
    function minTimeMaxPower($n, $edges, $power, $cost, $source, $target) {
        $INF = PHP_INT_MAX / 4;
        $g = array_fill(0, $n, []);
        foreach ($edges as $e) $g[$e[0]][] = [$e[1], $e[2]];
        $dist = array_fill(0, $n, array_fill(0, $power + 1, $INF));
        $dist[$source][$power] = 0;
        $pq = new SplPriorityQueue();
        $pq->setExtractFlags(SplPriorityQueue::EXTR_DATA);
        $pq->insert([0, $power, $source], 0);
        while (!$pq->isEmpty()) {
            $cur = $pq->extract();
            $d = $cur[0];
            $p = $cur[1];
            $u = $cur[2];
            if ($u === $target) return [$d, $p];
            if ($d > $dist[$u][$p] || $p < $cost[$u]) continue;
            $p -= $cost[$u];
            foreach ($g[$u] as $e) {
                $v = $e[0];
                $t = $e[1];
                $nd = $d + $t;
                if ($nd < $dist[$v][$p]) {
                    $dist[$v][$p] = $nd;
                    $pq->insert([$nd, $p, $v], -$nd);
                }
            }
        }
        return [-1, -1];
    }
}
''')

add("3984_divisible_game", r'''<?php
// LeetCode 3984 - Divisible Game
// https://leetcode.com/problems/divisible-game/

class Solution {
    function divisibleGame($nums) {
        $candidates = [2 => true];
        foreach ($nums as $value) {
            for ($divisor = 2; $divisor * $divisor <= $value; $divisor++) {
                if ($value % $divisor != 0) continue;
                $candidates[$divisor] = true;
                $candidates[intdiv($value, $divisor)] = true;
            }
            if ($value > 1) $candidates[$value] = true;
        }
        $bestScore = -(1 << 62);
        $bestK = 0;
        foreach ($candidates as $k => $_) {
            $ending = 0;
            $score = 0;
            for ($i = 0; $i < count($nums); $i++) {
                $value = $nums[$i];
                $contribution = -$value;
                if ($value % $k == 0) $contribution = $value;
                if ($i == 0 || $ending + $contribution < $contribution) $ending = $contribution;
                else $ending += $contribution;
                if ($i == 0 || $ending > $score) $score = $ending;
            }
            if ($score > $bestScore || ($score == $bestScore && $k < $bestK)) {
                $bestScore = $score;
                $bestK = $k;
            }
        }
        $mod = 1000000007;
        $answer = (($bestScore % $mod) * $bestK) % $mod;
        if ($answer < 0) $answer += $mod;
        return $answer;
    }
}
''')

add("3999_minimum_number_of_string_groups_through_transformations", r'''<?php
// LeetCode 3999 - Minimum Number of String Groups Through Transformations
// https://leetcode.com/problems/minimum-number-of-string-groups-through-transformations/

class Solution {
    function minimumGroups($words) {
        $keys = [];
        foreach ($words as $w) {
            $n = strlen($w);
            $even = '';
            $odd = '';
            for ($i = 0; $i < $n; $i++) {
                if ($i % 2 === 0) $even .= $w[$i];
                else $odd .= $w[$i];
            }
            $keys[] = $this->canonicalRotate($even) . '#' . $this->canonicalRotate($odd);
        }
        sort($keys);
        $groups = 0;
        for ($i = 0; $i < count($keys); $i++) {
            if ($i === 0 || $keys[$i] !== $keys[$i - 1]) $groups++;
        }
        return $groups;
    }

    private function leastRotation($s) {
        $n = strlen($s);
        $i = 0;
        $j = 1;
        $k = 0;
        while ($i < $n && $j < $n && $k < $n) {
            $a = $s[($i + $k) % $n];
            $b = $s[($j + $k) % $n];
            if ($a === $b) $k++;
            else {
                if ($a > $b) $i += $k + 1;
                else $j += $k + 1;
                if ($i === $j) $j++;
                $k = 0;
            }
        }
        return $i < $j ? $i : $j;
    }

    private function canonicalRotate($s) {
        $n = strlen($s);
        if ($n <= 1) return $s;
        $r = $this->leastRotation($s);
        if ($r === 0) return $s;
        return substr($s, $r) . substr($s, 0, $r);
    }
}
''')

add("4008_minimum_initial_strength_to_defeat_all_monsters", r'''<?php
// LeetCode 4008 - Minimum Initial Strength to Defeat All Monsters
// https://leetcode.com/problems/minimum-initial-strength-to-defeat-all-monsters/

class Solution {
    function minInitialStrength($monsters, $boosts) {
        $n = count($monsters);
        $d = array_fill(0, $n + 1, 0);
        foreach ($boosts as $b) {
            $d[$b[0]] += $b[2];
            $d[$b[1] + 1] -= $b[2];
        }
        $left = 0;
        $right = 1000000000000000;
        while ($left < $right) {
            $mid = intdiv($left + $right, 2);
            if ($this->check($mid, $monsters, $d)) $right = $mid;
            else $left = $mid + 1;
        }
        return $left;
    }

    private function check($v, $monsters, $d) {
        $bonus = 0;
        for ($i = 0; $i < count($monsters); $i++) {
            $bonus += $d[$i];
            if ($v + $bonus < $monsters[$i]) return false;
            $v -= $monsters[$i];
            if ($v < 0) $v = 0;
        }
        return true;
    }
}
''')

add("4012_count_of_unfinished_tasks_after_each_shift", r'''<?php
// LeetCode 4012 - Count of Unfinished Tasks After Each Shift
// https://leetcode.com/problems/count-of-unfinished-tasks-after-each-shift/

class Solution {
    function countTasks($tasks, $shifts) {
        $m = count($tasks);
        $n = count($shifts);
        $s = array_fill(0, $m + 1, 0);
        for ($i = 0; $i < $m; $i++) $s[$i + 1] = $s[$i] + $tasks[$i];
        $ans = array_fill(0, $n, 0);
        $iIdx = 0;
        $cur = 0;
        for ($j = 0; $j < $n; $j++) {
            if ($shifts[$j] < $tasks[$iIdx] - $cur) {
                $cur += $shifts[$j];
                $ans[$j] = $m - $iIdx;
            } else {
                $t = $shifts[$j] - ($tasks[$iIdx] - $cur);
                if ($t >= $s[$m] - $s[$iIdx + 1]) {
                    $iIdx = 0;
                    $cur = 0;
                } else {
                    $l = $iIdx + 1;
                    $r = $m;
                    while ($l < $r) {
                        $mid = ($l + $r) >> 1;
                        if ($t < $s[$mid + 1] - $s[$iIdx + 1]) $r = $mid;
                        else $l = $mid + 1;
                    }
                    $cur = $t - ($s[$l] - $s[$iIdx + 1]);
                    $iIdx = $l;
                    $ans[$j] = $m - $iIdx;
                }
            }
        }
        return $ans;
    }
}
''')

add("4013_count_subarrays_with_even_odd_ratio_ii", r'''<?php
// LeetCode 4013 - Count Subarrays With Even Odd Ratio II
// https://leetcode.com/problems/count-subarrays-with-even-odd-ratio-ii/

class Solution {
    function countRatioSubarrays($nums, $a, $b) {
        $n = count($nums);
        $s = array_fill(0, $n + 1, 0);
        for ($i = 0; $i < $n; $i++) {
            if ($nums[$i] % 2 === 1) $s[$i + 1] = $s[$i] + $a;
            else $s[$i + 1] = $s[$i] - $b;
        }
        $st = $s;
        sort($st);
        $uniq = [];
        foreach ($st as $v) {
            if (empty($uniq) || $v !== $uniq[count($uniq) - 1]) $uniq[] = $v;
        }
        $st = $uniq;
        $bit = array_fill(0, count($st) + 2, 0);
        $ans = 0;
        foreach ($s as $v) {
            $x = $this->lowerBound($st, $v) + 1;
            $ans += $this->query($bit, $x);
            $this->update($bit, $x, 1);
        }
        return $ans;
    }

    private function update(&$c, $x, $delta) {
        $n = count($c) - 1;
        for (; $x <= $n; $x += $x & -$x) $c[$x] += $delta;
    }

    private function query($c, $x) {
        $sum = 0;
        for (; $x > 0; $x -= $x & -$x) $sum += $c[$x];
        return $sum;
    }

    private function lowerBound($a, $x) {
        $lo = 0;
        $hi = count($a);
        while ($lo < $hi) {
            $mid = intdiv($lo + $hi, 2);
            if ($a[$mid] < $x) $lo = $mid + 1;
            else $hi = $mid;
        }
        return $lo;
    }
}
''')

n = 0
for folder, body in SOLUTIONS.items():
    path = ROOT / folder / "solution.php"
    path.write_text(body)
    n += 1
    print("wrote", folder)
print("total", n)
