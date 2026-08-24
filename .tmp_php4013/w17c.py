#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")

def w(folder, body):
    (ROOT / folder / "solution.php").write_text(body if body.endswith("\n") else body + "\n", encoding="utf-8")
    print("wrote", folder)

w("3429_paint_house_iv", r'''<?php
// LeetCode 3429 - Paint House IV
// https://leetcode.com/problems/paint-house-iv/

class Solution {
    function minCost($n, $cost) {
        $inf = intdiv(PHP_INT_MAX, 4);
        $m = intdiv($n, 2);
        $dp = [];
        for ($a = 0; $a < 3; $a++) {
            $dp[$a] = [];
            for ($b = 0; $b < 3; $b++) {
                $dp[$a][$b] = ($a === $b) ? $inf : $cost[0][$a] + $cost[$n - 1][$b];
            }
        }
        for ($i = 1; $i < $m; $i++) {
            $ndp = [];
            for ($a = 0; $a < 3; $a++) $ndp[$a] = array_fill(0, 3, $inf);
            for ($pa = 0; $pa < 3; $pa++) {
                for ($pb = 0; $pb < 3; $pb++) {
                    if ($dp[$pa][$pb] >= $inf) continue;
                    for ($a = 0; $a < 3; $a++) {
                        if ($a === $pa) continue;
                        for ($b = 0; $b < 3; $b++) {
                            if ($b === $pb || $a === $b) continue;
                            $v = $dp[$pa][$pb] + $cost[$i][$a] + $cost[$n - 1 - $i][$b];
                            if ($v < $ndp[$a][$b]) $ndp[$a][$b] = $v;
                        }
                    }
                }
            }
            $dp = $ndp;
        }
        $ans = $inf;
        for ($a = 0; $a < 3; $a++)
            for ($b = 0; $b < 3; $b++)
                if ($dp[$a][$b] < $ans) $ans = $dp[$a][$b];
        return $ans;
    }
}
''')

w("3430_maximum_and_minimum_sums_of_at_most_size_k_subarrays", r'''<?php
// LeetCode 3430 - Maximum and Minimum Sums of at Most Size K Subarrays
// https://leetcode.com/problems/maximum-and-minimum-sums-of-at-most-size-k-subarrays/

class Solution {
    function minMaxSubarraySum($nums, $k) {
        $n = count($nums);
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            $mn = $nums[$i];
            $mx = $nums[$i];
            for ($j = $i; $j < $n && $j - $i + 1 <= $k; $j++) {
                if ($nums[$j] < $mn) $mn = $nums[$j];
                if ($nums[$j] > $mx) $mx = $nums[$j];
                $ans += $mn + $mx;
            }
        }
        return $ans;
    }
}
''')

w("3431_minimum_unlocked_indices_to_sort_nums", r'''<?php
// LeetCode 3431 - Minimum Unlocked Indices to Sort Nums
// https://leetcode.com/problems/minimum-unlocked-indices-to-sort-nums/

class Solution {
    function minUnlockedIndices($nums, $locked) {
        $n = count($nums);
        $need = false;
        for ($i = 1; $i < $n; $i++) {
            if ($nums[$i] < $nums[$i - 1]) { $need = true; break; }
        }
        if (!$need) return 0;
        $left = $n;
        $right = -1;
        for ($i = 0; $i < $n; $i++) {
            for ($j = $i + 1; $j < $n; $j++) {
                if ($nums[$i] > $nums[$j]) {
                    if ($i < $left) $left = $i;
                    if ($j > $right) $right = $j;
                }
            }
        }
        if ($right < $left) return 0;
        $ans = 0;
        for ($i = $left; $i <= $right; $i++) if ($locked[$i] === 1) $ans++;
        $tmp = $nums;
        $lock = $locked;
        for ($i = $left; $i <= $right; $i++) $lock[$i] = 0;
        $changed = true;
        while ($changed) {
            $changed = false;
            for ($i = 0; $i + 1 < $n; $i++) {
                if ($lock[$i] === 0 && $lock[$i + 1] === 0 && $tmp[$i] > $tmp[$i + 1]) {
                    $t = $tmp[$i]; $tmp[$i] = $tmp[$i + 1]; $tmp[$i + 1] = $t;
                    $changed = true;
                }
            }
        }
        for ($i = 1; $i < $n; $i++) if ($tmp[$i] < $tmp[$i - 1]) return -1;
        return $ans;
    }
}
''')

w("3432_count_partitions_with_even_sum_difference", r'''<?php
// LeetCode 3432 - Count Partitions with Even Sum Difference
// https://leetcode.com/problems/count-partitions-with-even-sum-difference/

class Solution {
    function countPartitions($nums) {
        $total = 0;
        foreach ($nums as $x) $total += $x;
        $ans = 0;
        $left = 0;
        for ($i = 0; $i < count($nums) - 1; $i++) {
            $left += $nums[$i];
            if (($left - ($total - $left)) % 2 === 0) $ans++;
        }
        return $ans;
    }
}
''')

w("3433_count_mentions_per_user", r'''<?php
// LeetCode 3433 - Count Mentions Per User
// https://leetcode.com/problems/count-mentions-per-user/

class Solution {
    function countMentions($numberOfUsers, $events) {
        usort($events, function($a, $b) {
            $ti = intval($a[1]);
            $tj = intval($b[1]);
            if ($ti !== $tj) return $ti <=> $tj;
            return strcmp($b[0], $a[0]);
        });
        $online = array_fill(0, $numberOfUsers, true);
        $offlineUntil = array_fill(0, $numberOfUsers, 0);
        $ans = array_fill(0, $numberOfUsers, 0);
        foreach ($events as $e) {
            $t = intval($e[1]);
            for ($i = 0; $i < $numberOfUsers; $i++) {
                if (!$online[$i] && $offlineUntil[$i] <= $t) $online[$i] = true;
            }
            if ($e[0] === "OFFLINE") {
                $id = intval($e[2]);
                $online[$id] = false;
                $offlineUntil[$id] = $t + 60;
            } else {
                $msg = $e[2];
                if ($msg === "ALL") {
                    for ($i = 0; $i < $numberOfUsers; $i++) $ans[$i]++;
                } else if ($msg === "HERE") {
                    for ($i = 0; $i < $numberOfUsers; $i++) if ($online[$i]) $ans[$i]++;
                } else {
                    foreach (explode(" ", $msg) as $part) {
                        $id = intval(substr($part, 2));
                        $ans[$id]++;
                    }
                }
            }
        }
        return $ans;
    }
}
''')

w("3434_maximum_frequency_after_subarray_operation", r'''<?php
// LeetCode 3434 - Maximum Frequency After Subarray Operation
// https://leetcode.com/problems/maximum-frequency-after-subarray-operation/

class Solution {
    function maxFrequency($nums, $k) {
        $base = 0;
        foreach ($nums as $x) if ($x === $k) $base++;
        $ans = $base;
        $uniq = [];
        foreach ($nums as $x) $uniq[$x] = true;
        foreach ($uniq as $v => $_) {
            if ($v === $k) continue;
            $best = 0;
            $cur = 0;
            foreach ($nums as $x) {
                $delta = 0;
                if ($x === $v) $delta = 1;
                else if ($x === $k) $delta = -1;
                $cur += $delta;
                if ($cur < 0) $cur = 0;
                if ($cur > $best) $best = $cur;
            }
            if ($base + $best > $ans) $ans = $base + $best;
        }
        return $ans;
    }
}
''')

w("3435_frequencies_of_shortest_supersequences", r'''<?php
// LeetCode 3435 - Frequencies of Shortest Supersequences
// https://leetcode.com/problems/frequencies-of-shortest-supersequences/

class Solution {
    function supersequences($words) {
        $used = array_fill(0, 26, false);
        foreach ($words as $w) {
            $used[ord($w[0]) - 97] = true;
            $used[ord($w[1]) - 97] = true;
        }
        $letters = [];
        for ($i = 0; $i < 26; $i++) if ($used[$i]) $letters[] = $i;
        $m = count($letters);
        $freq = array_fill(0, 26, 0);
        $best = 1e9;
        $bestFreqs = [];
        $dfs = null;
        $dfs = function($i) use (&$dfs, $m, &$letters, &$freq, &$best, &$bestFreqs, $words) {
            if ($i === $m) {
                foreach ($words as $w) {
                    $a = ord($w[0]) - 97;
                    $b = ord($w[1]) - 97;
                    if ($a === $b) {
                        if ($freq[$a] < 2) return;
                    } else if ($freq[$a] < 1 || $freq[$b] < 1) return;
                }
                $sum = 0;
                $f = $freq;
                for ($j = 0; $j < 26; $j++) $sum += $freq[$j];
                if ($sum < $best) {
                    $best = $sum;
                    $bestFreqs = [$f];
                } else if ($sum === $best) $bestFreqs[] = $f;
                return;
            }
            $L = $letters[$i];
            for ($c = 1; $c <= 2; $c++) {
                $freq[$L] = $c;
                $dfs($i + 1);
            }
            $freq[$L] = 0;
        };
        $dfs(0);
        return $bestFreqs;
    }
}
''')

w("3437_permutations_iii", r'''<?php
// LeetCode 3437 - Permutations III
// https://leetcode.com/problems/permutations-iii/

class Solution {
    function permute($n) {
        $ans = [];
        $used = array_fill(0, $n + 1, false);
        $cur = [];
        $dfs = null;
        $dfs = function() use (&$dfs, $n, &$ans, &$used, &$cur) {
            if (count($cur) === $n) {
                $ans[] = $cur;
                return;
            }
            for ($i = 1; $i <= $n; $i++) {
                if ($used[$i]) continue;
                if (count($cur) && ($cur[count($cur) - 1] % 2 === $i % 2)) continue;
                $used[$i] = true;
                $cur[] = $i;
                $dfs();
                array_pop($cur);
                $used[$i] = false;
            }
        };
        $dfs();
        return $ans;
    }
}
''')

w("3438_find_valid_pair_of_adjacent_digits_in_string", r'''<?php
// LeetCode 3438 - Find Valid Pair of Adjacent Digits in String
// https://leetcode.com/problems/find-valid-pair-of-adjacent-digits-in-string/

class Solution {
    function findValidPair($s) {
        $freq = array_fill(0, 10, 0);
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) $freq[ord($s[$i]) - 48]++;
        for ($i = 0; $i + 1 < $n; $i++) {
            $a = ord($s[$i]) - 48;
            $b = ord($s[$i + 1]) - 48;
            if ($a !== $b && $freq[$a] === $a && $freq[$b] === $b) return substr($s, $i, 2);
        }
        return "";
    }
}
''')

w("3439_reschedule_meetings_for_maximum_free_time_i", r'''<?php
// LeetCode 3439 - Reschedule Meetings for Maximum Free Time I
// https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-i/

class Solution {
    function maxFreeTime($eventTime, $k, $startTime, $endTime) {
        $n = count($startTime);
        $gaps = array_fill(0, $n + 1, 0);
        $gaps[0] = $startTime[0];
        for ($i = 1; $i < $n; $i++) $gaps[$i] = $startTime[$i] - $endTime[$i - 1];
        $gaps[$n] = $eventTime - $endTime[$n - 1];
        $window = $k + 1;
        $sum = 0;
        for ($i = 0; $i < $window && $i < count($gaps); $i++) $sum += $gaps[$i];
        $ans = $sum;
        for ($i = $window; $i < count($gaps); $i++) {
            $sum += $gaps[$i] - $gaps[$i - $window];
            if ($sum > $ans) $ans = $sum;
        }
        return $ans;
    }
}
''')

w("3440_reschedule_meetings_for_maximum_free_time_ii", r'''<?php
// LeetCode 3440 - Reschedule Meetings for Maximum Free Time II
// https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-ii/

class Solution {
    function maxFreeTime($eventTime, $startTime, $endTime) {
        $n = count($startTime);
        $gaps = array_fill(0, $n + 1, 0);
        $gaps[0] = $startTime[0];
        for ($i = 1; $i < $n; $i++) $gaps[$i] = $startTime[$i] - $endTime[$i - 1];
        $gaps[$n] = $eventTime - $endTime[$n - 1];
        $ans = 0;
        foreach ($gaps as $g) if ($g > $ans) $ans = $g;
        $leftMax = array_fill(0, $n + 1, 0);
        $rightMax = array_fill(0, $n + 1, 0);
        for ($i = 0; $i <= $n; $i++) {
            $leftMax[$i] = $gaps[$i];
            if ($i > 0 && $leftMax[$i - 1] > $leftMax[$i]) $leftMax[$i] = $leftMax[$i - 1];
        }
        for ($i = $n; $i >= 0; $i--) {
            $rightMax[$i] = $gaps[$i];
            if ($i < $n && $rightMax[$i + 1] > $rightMax[$i]) $rightMax[$i] = $rightMax[$i + 1];
        }
        for ($i = 0; $i < $n; $i++) {
            $dur = $endTime[$i] - $startTime[$i];
            $merged = $gaps[$i] + $gaps[$i + 1];
            $bestOther = 0;
            if ($i > 0 && $leftMax[$i - 1] > $bestOther) $bestOther = $leftMax[$i - 1];
            if ($i + 2 <= $n && $rightMax[$i + 2] > $bestOther) $bestOther = $rightMax[$i + 2];
            $cand = $merged;
            if ($bestOther >= $dur) $cand = $merged + $dur;
            if ($cand > $ans) $ans = $cand;
        }
        return $ans;
    }
}
''')

w("3441_minimum_cost_good_caption", r'''<?php
// LeetCode 3441 - Minimum Cost Good Caption
// https://leetcode.com/problems/minimum-cost-good-caption/

class Solution {
    function minCostGoodCaption($caption) {
        $n = strlen($caption);
        if ($n < 3) return "";
        $ans = str_split($caption);
        $i = 0;
        while ($i < $n) {
            $j = $i;
            while ($j < $n && $ans[$j] === $ans[$i]) $j++;
            if ($j - $i >= 3) { $i = $j; continue; }
            $need = 3 - ($j - $i);
            if ($j + $need <= $n) {
                for ($t = 0; $t < $need; $t++) $ans[$j + $t] = $ans[$i];
                $i = $j + $need;
            } else {
                $ch = "a";
                if ($i > 0) $ch = $ans[$i - 1];
                else if ($j < $n) $ch = $caption[$j];
                for ($t = $i; $t < $n; $t++) $ans[$t] = $ch;
                break;
            }
        }
        $i = 0;
        while ($i < $n) {
            $j = $i;
            while ($j < $n && $ans[$j] === $ans[$i]) $j++;
            if ($j - $i < 3) return "";
            $i = $j;
        }
        return implode("", $ans);
    }
}
''')

w("3442_maximum_difference_between_even_and_odd_frequency_i", r'''<?php
// LeetCode 3442 - Maximum Difference Between Even and Odd Frequency I
// https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-i/

class Solution {
    function maxDifference($s) {
        $freq = array_fill(0, 26, 0);
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) $freq[ord($s[$i]) - 97]++;
        $maxOdd = 0;
        $minEven = 1e9;
        foreach ($freq as $f) {
            if ($f === 0) continue;
            if ($f % 2 === 1) {
                if ($f > $maxOdd) $maxOdd = $f;
            } else if ($f < $minEven) $minEven = $f;
        }
        return $maxOdd - $minEven;
    }
}
''')

w("3443_maximum_manhattan_distance_after_k_changes", r'''<?php
// LeetCode 3443 - Maximum Manhattan Distance After K Changes
// https://leetcode.com/problems/maximum-manhattan-distance-after-k-changes/

class Solution {
    function maxDistance($s, $k) {
        $ans = 0;
        $lat = 0;
        $lon = 0;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $c = $s[$i];
            if ($c === "N") $lat++;
            else if ($c === "S") $lat--;
            else if ($c === "E") $lon++;
            else $lon--;
            $md = abs($lat) + abs($lon);
            $steps = $i + 1;
            $cur = $md + 2 * $k;
            if ($cur > $steps) $cur = $steps;
            if ($cur > $ans) $ans = $cur;
        }
        return $ans;
    }
}
''')

w("3444_minimum_increments_for_target_multiples_in_an_array", r'''<?php
// LeetCode 3444 - Minimum Increments for Target Multiples in an Array
// https://leetcode.com/problems/minimum-increments-for-target-multiples-in-an-array/

class Solution {
    private function gcd($a, $b) {
        while ($b) { $t = $a % $b; $a = $b; $b = $t; }
        return $a;
    }

    private function lcm($a, $b) {
        return intdiv($a, $this->gcd($a, $b)) * $b;
    }

    function minimumIncrements($nums, $target) {
        $m = count($target);
        $N = 1 << $m;
        $inf = 1e18;
        $dp = array_fill(0, $N, $inf);
        $dp[0] = 0;
        foreach ($nums as $x) {
            $ndp = $dp;
            for ($mask = 0; $mask < $N; $mask++) {
                for ($sub = 1; $sub < $N; $sub++) {
                    $L = 1;
                    $ok = true;
                    for ($i = 0; $i < $m; $i++) {
                        if ($sub & (1 << $i)) {
                            $L = $this->lcm($L, $target[$i]);
                            if ($L > 1000000000) { $ok = false; break; }
                        }
                    }
                    if (!$ok) continue;
                    $cost = ($L - $x % $L) % $L;
                    $nmask = $mask | $sub;
                    if ($dp[$mask] + $cost < $ndp[$nmask]) $ndp[$nmask] = $dp[$mask] + $cost;
                }
            }
            $dp = $ndp;
        }
        return $dp[$N - 1];
    }
}
''')

print("c done")
