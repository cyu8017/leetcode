#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
SOLUTIONS = {}

def add(folder, body):
    SOLUTIONS[folder] = body

add("3953_maximum_score_with_co_prime_element", r'''<?php
// LeetCode 3953 - Maximum Score with Co-Prime Element
// https://leetcode.com/problems/maximum-score-with-co-prime-element/

class Solution {
    function maxScore($nums, $maxVal) {
        $limit = $maxVal;
        $frequency = array_fill(0, 100001, 0);
        foreach ($nums as $x) {
            $frequency[$x]++;
            if ($x > $limit) $limit = $x;
        }
        $divisible = array_fill(0, $limit + 1, 0);
        for ($d = 1; $d <= $limit; $d++) {
            for ($multiple = $d; $multiple <= $limit; $multiple += $d) {
                if ($multiple < count($frequency)) $divisible[$d] += $frequency[$multiple];
            }
        }
        $best = -count($nums);
        $checked = array_fill(0, $limit + 1, false);
        for ($x = 1; $x <= $maxVal; $x++) {
            $best = max($best, $this->evaluate($x, $x < count($frequency) && $frequency[$x] > 0, $checked, $divisible));
        }
        foreach ($nums as $x) {
            $best = max($best, $this->evaluate($x, true, $checked, $divisible));
        }
        return $best;
    }

    private function evaluate($x, $exists, &$checked, $divisible) {
        if ($checked[$x]) return intdiv(-2147483648, 4);
        $checked[$x] = true;
        $bad = $this->badCount($x, $divisible);
        if ($exists) $cost = $x > 1 ? $bad - 1 : 0;
        else $cost = $bad > 0 ? $bad : 1;
        return $x - $cost;
    }

    private function badCount($x, $divisible) {
        $primes = [];
        $y = $x;
        for ($p = 2; $p * $p <= $y; $p++) {
            if ($y % $p === 0) {
                $primes[] = $p;
                while ($y % $p === 0) $y = intdiv($y, $p);
            }
        }
        if ($y > 1) $primes[] = $y;
        $bad = 0;
        $psz = count($primes);
        for ($mask = 1; $mask < (1 << $psz); $mask++) {
            $product = 1;
            $bits = 0;
            for ($i = 0; $i < $psz; $i++) {
                if ((($mask >> $i) & 1) !== 0) {
                    $product *= $primes[$i];
                    $bits++;
                }
            }
            if ($bits % 2 === 1) $bad += $divisible[$product];
            else $bad -= $divisible[$product];
        }
        return $bad;
    }
}
''')

add("3956_maximum_sum_of_m_non_overlapping_subarrays_i", r'''<?php
// LeetCode 3956 - Maximum Sum of M Non-Overlapping Subarrays I
// https://leetcode.com/problems/maximum-sum-of-m-non-overlapping-subarrays-i/

class Solution {
    function maxSum($nums, $m, $l, $r) {
        $n = count($nums);
        $prefix = array_fill(0, $n + 1, 0);
        for ($i = 0; $i < $n; $i++) $prefix[$i + 1] = $prefix[$i] + $nums[$i];
        $dp = array_fill(0, $n + 1, 0);
        $bestSelected = -(1 << 62);
        for ($count = 1; $count <= $m; $count++) {
            $next = $dp;
            $deque = [];
            for ($end = 1; $end <= $n; $end++) {
                $addIndex = $end - $l;
                if ($addIndex >= 0) {
                    $value = $dp[$addIndex] - $prefix[$addIndex];
                    while (count($deque) > 0) {
                        $last = $deque[count($deque) - 1];
                        if ($dp[$last] - $prefix[$last] > $value) break;
                        array_pop($deque);
                    }
                    $deque[] = $addIndex;
                }
                $minIndex = $end - $r;
                while (count($deque) > 0 && $deque[0] < $minIndex) array_shift($deque);
                if (count($deque) > 0) {
                    $candidate = $prefix[$end] + $dp[$deque[0]] - $prefix[$deque[0]];
                    if ($candidate > $next[$end]) $next[$end] = $candidate;
                    if ($candidate > $bestSelected) $bestSelected = $candidate;
                }
                if ($next[$end - 1] > $next[$end]) $next[$end] = $next[$end - 1];
            }
            $dp = $next;
        }
        return $bestSelected;
    }
}
''')

add("3960_frequency_balance_subarray", r'''<?php
// LeetCode 3960 - Frequency Balance Subarray
// https://leetcode.com/problems/frequency-balance-subarray/

class Solution {
    function getLength($nums) {
        $n = count($nums);
        $ans = 1;
        for ($l = 0; $l < $n; $l++) {
            $cnt = [];
            $freq = [];
            for ($r = $l; $r < $n; $r++) {
                $x = $nums[$r];
                $c = $cnt[$x] ?? 0;
                if (($freq[$c] ?? 0) > 0) {
                    $fc = $freq[$c] - 1;
                    if ($fc === 0) unset($freq[$c]);
                    else $freq[$c] = $fc;
                }
                $cnt[$x] = $c + 1;
                $cx = $cnt[$x];
                $freq[$cx] = ($freq[$cx] ?? 0) + 1;
                if (count($cnt) === 1 || (count($freq) === 2 && ((($freq[$cx * 2] ?? 0) > 0) || ($cx % 2 === 0 && ($freq[intdiv($cx, 2)] ?? 0) > 0)))) {
                    $ans = max($ans, $r - $l + 1);
                }
            }
        }
        return $ans;
    }
}
''')

add("3965_finish_time_of_tasks_i", r'''<?php
// LeetCode 3965 - Finish Time Of Tasks I
// https://leetcode.com/problems/finish-time-of-tasks-i/

class Solution {
    private $baseTime;
    private $g;

    function finishTime($n, $edges, $baseTime) {
        $this->baseTime = $baseTime;
        $this->g = array_fill(0, $n, []);
        foreach ($edges as $e) $this->g[$e[0]][] = $e[1];
        return $this->dfs(0);
    }

    private function dfs($i) {
        if (count($this->g[$i]) === 0) return $this->baseTime[$i];
        $INF = 1 << 62;
        $earliest = $INF;
        $latest = -$INF;
        foreach ($this->g[$i] as $j) {
            $a = $this->dfs($j);
            $earliest = min($earliest, $a);
            $latest = max($latest, $a);
        }
        $ownDuration = ($latest - $earliest) + $this->baseTime[$i];
        return $latest + $ownDuration;
    }
}
''')

add("3966_count_good_integers_in_a_range", r'''<?php
// LeetCode 3966 - Count Good Integers in a Range
// https://leetcode.com/problems/count-good-integers-in-a-range/

class Solution {
    function countGoodIntegers($l, $r, $k) {
        return $this->countBound($r, $k) - $this->countBound($l - 1, $k);
    }

    private function countBound($bound, $k) {
        if ($bound <= 0) return 0;
        $digits = strval($bound);
        $memo = [];
        return $this->dfs(0, 0, false, true, $digits, $k, $memo);
    }

    private function dfs($position, $previous, $started, $tight, $digits, $k, &$memo) {
        if ($position === strlen($digits)) return $started ? 1 : 0;
        $key = $position . "," . $previous . "," . ($started ? 1 : 0);
        if (!$tight && isset($memo[$key])) return $memo[$key];
        $limit = $tight ? intval($digits[$position]) : 9;
        $result = 0;
        for ($digit = 0; $digit <= $limit; $digit++) {
            $nextStarted = $started || $digit !== 0;
            if ($started && abs($previous - $digit) > $k) continue;
            $nextPrevious = $nextStarted ? $digit : $previous;
            $result += $this->dfs($position + 1, $nextPrevious, $nextStarted, $tight && $digit === $limit, $digits, $k, $memo);
        }
        if (!$tight) $memo[$key] = $result;
        return $result;
    }
}
''')

add("3970_shortest_path_with_at_most_k_consecutive_identical_characters", r'''<?php
// LeetCode 3970 - Shortest Path With At Most K Consecutive Identical Characters
// https://leetcode.com/problems/shortest-path-with-at-most-k-consecutive-identical-characters/

class Solution {
    function shortestPath($n, $edges, $labels, $k) {
        $graph = array_fill(0, $n, []);
        foreach ($edges as $edge) $graph[$edge[0]][] = [$edge[1], $edge[2]];
        $infinity = PHP_INT_MAX / 4;
        $distances = array_fill(0, $n, array_fill(0, $k + 1, $infinity));
        $distances[0][1] = 0;
        $pq = new SplPriorityQueue();
        $pq->setExtractFlags(SplPriorityQueue::EXTR_DATA);
        $pq->insert([0, 0, 1], 0);
        while (!$pq->isEmpty()) {
            $cur = $pq->extract();
            $distance = $cur[0];
            $node = $cur[1];
            $run = $cur[2];
            if ($distance !== $distances[$node][$run]) continue;
            if ($node === $n - 1) return $distance;
            foreach ($graph[$node] as $e) {
                $to = $e[0];
                $weight = $e[1];
                $nextRun = 1;
                if ($labels[$node] === $labels[$to]) $nextRun = $run + 1;
                if ($nextRun > $k) continue;
                $nextDistance = $distance + $weight;
                if ($nextDistance < $distances[$to][$nextRun]) {
                    $distances[$to][$nextRun] = $nextDistance;
                    $pq->insert([$nextDistance, $to, $nextRun], -$nextDistance);
                }
            }
        }
        return -1;
    }
}
''')

add("3976_maximum_subarray_sum_after_multiplier", r'''<?php
// LeetCode 3976 - Maximum Subarray Sum After Multiplier
// https://leetcode.com/problems/maximum-subarray-sum-after-multiplier/

class Solution {
    function maxSubarraySum($nums, $k) {
        $n = count($nums);
        $inf = -PHP_INT_MAX / 4;
        $f = array_fill(0, $n + 1, array_fill(0, 4, $inf));
        $f[0][0] = 0;
        $ans = $inf;
        for ($i = 1; $i <= $n; $i++) {
            $x = $nums[$i - 1];
            $f[$i][0] = max($f[$i - 1][0], 0) + $x;
            $f[$i][1] = max(max($f[$i - 1][0], $f[$i - 1][1]), 0) + $x * $k;
            $f[$i][2] = max(max($f[$i - 1][0], $f[$i - 1][2]), 0) + intdiv($x, $k);
            $f[$i][3] = max(max($f[$i - 1][1], $f[$i - 1][2]), $f[$i - 1][3]) + $x;
            $ans = max($ans, max(max($f[$i][0], $f[$i][1]), max($f[$i][2], $f[$i][3])));
        }
        return $ans;
    }
}
''')

add("3978_unique_middle_element", r'''<?php
// LeetCode 3978 - Unique Middle Element
// https://leetcode.com/problems/unique-middle-element/

class Solution {
    function isMiddleElementUnique($nums) {
        $mid = $nums[intdiv(count($nums), 2)];
        $cnt = 0;
        foreach ($nums as $x) {
            if ($x == $mid) $cnt++;
        }
        return $cnt == 1;
    }
}
''')

add("3980_minimum_operations_to_transform_binary_string", r'''<?php
// LeetCode 3980 - Minimum Operations to Transform Binary String
// https://leetcode.com/problems/minimum-operations-to-transform-binary-string/

class Solution {
    function minOperations($s1, $s2) {
        $infinity = 1000000000;
        $dp = [0, $infinity];
        $n = strlen($s1);
        for ($i = 0; $i < $n; $i++) {
            $next = [$infinity, $infinity];
            for ($forcedZero = 0; $forcedZero <= 1; $forcedZero++) {
                if ($dp[$forcedZero] == $infinity) continue;
                $current = $s1[$i];
                if ($forcedZero == 1) $current = '0';
                $direct = $dp[$forcedZero];
                if ($current == '0' && $s2[$i] == '1') $direct++;
                else if ($current == '1' && $s2[$i] == '0') $direct = $infinity;
                $next[0] = min($next[0], $direct);
                if ($i + 1 < $n) {
                    $cost = $dp[$forcedZero] + 1;
                    if ($current == '0') $cost++;
                    if ($s1[$i + 1] == '0') $cost++;
                    if ($s2[$i] == '1') $cost++;
                    $next[1] = min($next[1], $cost);
                }
            }
            $dp = $next;
        }
        return $dp[0] == $infinity ? -1 : $dp[0];
    }
}
''')

add("3985_palindromic_subarray_sum", r'''<?php
// LeetCode 3985 - Palindromic Subarray Sum
// https://leetcode.com/problems/palindromic-subarray-sum/

class Solution {
    function maxPalindromicSubarraySum($nums) {
        $n = count($nums);
        $prefix = array_fill(0, $n + 1, 0);
        for ($i = 0; $i < $n; $i++) $prefix[$i + 1] = $prefix[$i] + $nums[$i];
        $odd = array_fill(0, $n, 0);
        $left = 0;
        $right = -1;
        for ($i = 0; $i < $n; $i++) {
            $radius = 1;
            if ($i <= $right) {
                $mirror = $left + $right - $i;
                $radius = $odd[$mirror];
                if ($right - $i + 1 < $radius) $radius = $right - $i + 1;
            }
            while ($i - $radius >= 0 && $i + $radius < $n && $nums[$i - $radius] == $nums[$i + $radius]) $radius++;
            $odd[$i] = $radius;
            if ($i + $radius - 1 > $right) {
                $left = $i - $radius + 1;
                $right = $i + $radius - 1;
            }
        }
        $even = array_fill(0, $n, 0);
        $left = 0;
        $right = -1;
        for ($i = 0; $i < $n; $i++) {
            $radius = 0;
            if ($i <= $right) {
                $mirror = $left + $right - $i + 1;
                $radius = $even[$mirror];
                if ($right - $i + 1 < $radius) $radius = $right - $i + 1;
            }
            while ($i - $radius - 1 >= 0 && $i + $radius < $n && $nums[$i - $radius - 1] == $nums[$i + $radius]) $radius++;
            $even[$i] = $radius;
            if ($i + $radius - 1 > $right) {
                $left = $i - $radius;
                $right = $i + $radius - 1;
            }
        }
        $answer = 0;
        for ($i = 0; $i < $n; $i++) {
            $sum = $prefix[$i + $odd[$i]] - $prefix[$i - $odd[$i] + 1];
            if ($sum > $answer) $answer = $sum;
            if ($even[$i] > 0) {
                $sum = $prefix[$i + $even[$i]] - $prefix[$i - $even[$i]];
                if ($sum > $answer) $answer = $sum;
            }
        }
        return $answer;
    }
}
''')

add("3988_create_grid_with_exactly_k_paths_i", r'''<?php
// LeetCode 3988 - Create Grid With Exactly K Paths I
// https://leetcode.com/problems/create-grid-with-exactly-k-paths-i/

class Solution {
    function createGrid($m, $n, $k) {
        $cands = [];
        if ($k === 1) $cands[] = ["."];
        else if ($k === 2) $cands[] = ["..", ".."];
        else if ($k === 3) {
            $cands[] = ["..", "..", ".."];
            $cands[] = ["...", "..."];
        } else if ($k === 4) {
            $cands[] = ["..", "..", "..", ".."];
            $cands[] = ["....", "...."];
            $cands[] = ["..#", "...", "#.."];
        }
        foreach ($cands as $pat) {
            $pr = count($pat);
            $pc = strlen($pat[0]);
            if ($pr > $m || $pc > $n) continue;
            $result = array_fill(0, $m, str_repeat('#', $n));
            for ($i = 0; $i < $pr; $i++) {
                $row = str_split($result[$i]);
                for ($j = 0; $j < $pc; $j++) $row[$j] = $pat[$i][$j];
                $result[$i] = implode('', $row);
            }
            for ($i = $pr; $i < $m; $i++) {
                $row = str_split($result[$i]);
                $row[$pc - 1] = '.';
                $result[$i] = implode('', $row);
            }
            for ($j = $pc; $j < $n; $j++) {
                $row = str_split($result[$m - 1]);
                $row[$j] = '.';
                $result[$m - 1] = implode('', $row);
            }
            return $result;
        }
        return [];
    }
}
''')

add("3990_create_grid_with_exactly_k_paths_ii", r'''<?php
// LeetCode 3990 - Create Grid With Exactly K Paths II
// https://leetcode.com/problems/create-grid-with-exactly-k-paths-ii/

class Solution {
    function createGrid($k) {
        if ($k <= 0) return [];
        $l = $this->bitWidth($k);
        $m = 2 * $l;
        $n = $l + 3;
        $result = [];
        for ($i = 0; $i < $m; $i++) $result[] = str_repeat('#', $n);
        for ($i = 0; $i < $l; $i++) {
            $r = 2 * $i;
            $row0 = str_split($result[$r]);
            $row1 = str_split($result[$r + 1]);
            $row0[$i] = $row0[$i + 1] = $row1[$i] = $row1[$i + 1] = '.';
            if (($k & (1 << $i)) != 0) {
                for ($c = $i + 2; $c < $n; $c++) $row0[$c] = '.';
            }
            $result[$r] = implode('', $row0);
            $result[$r + 1] = implode('', $row1);
        }
        for ($r = 0; $r < $m; $r++) {
            $row = str_split($result[$r]);
            $row[$n - 1] = '.';
            $result[$r] = implode('', $row);
        }
        return $result;
    }

    private function bitWidth($k) {
        $w = 0;
        while ($k != 0) { $w++; $k >>= 1; }
        return $w;
    }
}
''')

add("3995_minimum_cost_to_convert_string_iii", r'''<?php
// LeetCode 3995 - Minimum Cost to Convert String III
// https://leetcode.com/problems/minimum-cost-to-convert-string-iii/

class Solution {
    function minCost($source, $target, $rules, $costs) {
        $n = strlen($source);
        if (strlen($target) != $n) return -1;
        $dp = array_fill(0, $n + 1, 2147483647);
        $dp[0] = 0;
        for ($i = 0; $i < $n; $i++) {
            if ($dp[$i] == 2147483647) continue;
            if ($source[$i] == $target[$i] && $dp[$i] < $dp[$i + 1]) $dp[$i + 1] = $dp[$i];
            for ($j = 0; $j < count($rules); $j++) {
                $p = $rules[$j][0];
                $r = $rules[$j][1];
                $plen = strlen($p);
                if ($i + $plen > $n) continue;
                $c = $costs[$j];
                $ok = true;
                for ($k = 0; $k < $plen; $k++) {
                    if ($r[$k] != $target[$i + $k]) { $ok = false; break; }
                    if ($p[$k] == '*') $c++;
                    else if ($p[$k] != $source[$i + $k]) { $ok = false; break; }
                }
                if ($ok && $dp[$i] <= 2147483647 - $c && $dp[$i] + $c < $dp[$i + $plen]) {
                    $dp[$i + $plen] = $dp[$i] + $c;
                }
            }
        }
        return $dp[$n] == 2147483647 ? -1 : $dp[$n];
    }
}
''')

add("3997_count_dominant_nodes_in_a_binary_tree", r'''<?php
// LeetCode 3997 - Count Dominant Nodes in a Binary Tree
// https://leetcode.com/problems/count-dominant-nodes-in-a-binary-tree/

class TreeNode {
    public $val = null;
    public $left = null;
    public $right = null;
    function __construct($val = 0, $left = null, $right = null) {
        $this->val = $val;
        $this->left = $left;
        $this->right = $right;
    }
}

class Solution {
    private $ans;

    function countDominantNodes($root) {
        $this->ans = 0;
        $this->dfs($root);
        return $this->ans;
    }

    private function dfs($node) {
        if ($node == null) return -2147483648;
        $l = $this->dfs($node->left);
        $r = $this->dfs($node->right);
        $mx = max(max($l, $r), $node->val);
        if ($mx == $node->val) $this->ans++;
        return $mx;
    }
}
''')

add("3998_transform_binary_string_using_subsequence_sort", r'''<?php
// LeetCode 3998 - Transform Binary String Using Subsequence Sort
// https://leetcode.com/problems/transform-binary-string-using-subsequence-sort/

class Solution {
    function transformStr($s, $strs) {
        $n = strlen($s);
        $prefix = array_fill(0, $n + 1, 0);
        for ($i = 0; $i < $n; $i++) $prefix[$i + 1] = $prefix[$i] + ($s[$i] == '1' ? 1 : 0);
        $result = array_fill(0, count($strs), false);
        for ($i = 0; $i < count($strs); $i++) {
            $left = 0;
            $right = 0;
            $ok = true;
            for ($j = 0; $j < $n; $j++) {
                $left += ($strs[$i][$j] == '1' ? 1 : 0);
                $add = ($strs[$i][$j] != '0' ? 1 : 0);
                $right = $right + $add;
                if ($right > $prefix[$j + 1]) $right = $prefix[$j + 1];
                if ($left > $right) {
                    $ok = false;
                    break;
                }
            }
            $result[$i] = $ok && $left <= $prefix[$n] && $prefix[$n] <= $right;
        }
        return $result;
    }
}
''')

add("4005_minimum_operations_to_make_array_equal_iii", r'''<?php
// LeetCode 4005 - Minimum Operations to Make Array Equal III
// https://leetcode.com/problems/minimum-operations-to-make-array-equal-iii/

class Solution {
    function minOperations($nums) {
        $n = count($nums);
        if ($n <= 1) return 0;
        $g = $nums[0];
        $mn = $nums[0];
        for ($i = 1; $i < $n; $i++) {
            $g = $this->gcd($g, $nums[$i]);
            $mn = min($mn, $nums[$i]);
        }
        $cands = [];
        foreach ($nums as $x) $cands[$x] = true;
        for ($d = 1; $d * $d <= $mn; $d++) {
            if ($mn % $d == 0) {
                $cands[$d] = true;
                $cands[intdiv($mn, $d)] = true;
            }
        }
        $cands[$g] = true;
        $ans = 2147483647;
        foreach ($cands as $t => $_) {
            $sum = 0;
            foreach ($nums as $x) {
                $sum += $this->cost($x, $t);
                if ($sum >= $ans) break;
            }
            $ans = min($ans, $sum);
        }
        return $ans;
    }

    private function cost($x, $t) {
        if ($x == $t) return 0;
        if ($x % $t == 0 || $t % $x == 0) return 1;
        return 2;
    }

    private function gcd($a, $b) {
        while ($b != 0) {
            $t = $a % $b;
            $a = $b;
            $b = $t;
        }
        return $a;
    }
}
''')

add("4006_count_valid_prefixes", r'''<?php
// LeetCode 4006 - Count Valid Prefixes
// https://leetcode.com/problems/count-valid-prefixes/

class Solution {
    function countValidPrefixes($s) {
        $ans = 0;
        $t = 0;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            if ($s[$i] == '1') $t++;
            else $t--;
            if ($t >= -1 && $t <= 1) $ans++;
        }
        return $ans;
    }
}
''')

add("4007_widest_possible_fence", r'''<?php
// LeetCode 4007 - Widest Possible Fence
// https://leetcode.com/problems/widest-possible-fence/

class Solution {
    function maximumWidth($planks) {
        $cnt = [];
        foreach ($planks as $x) $cnt[$x] = ($cnt[$x] ?? 0) + 1;
        $t = [];
        $ans = 0;
        foreach ($cnt as $x => $v1) {
            $t[$x] = ($t[$x] ?? 0) + $v1;
            $ans = max($ans, $t[$x]);
            $t[$x * 2] = ($t[$x * 2] ?? 0) + intdiv($v1, 2);
            $ans = max($ans, $t[$x * 2]);
            foreach ($cnt as $y => $v2) {
                if ($y > $x) {
                    $key = $x + $y;
                    $t[$key] = ($t[$key] ?? 0) + min($v1, $v2);
                    $ans = max($ans, $t[$key]);
                }
            }
        }
        return $ans;
    }
}
''')

n = 0
for folder, body in SOLUTIONS.items():
    if folder == "3978_unique_middle_element" or folder == "4006_count_valid_prefixes":
        continue
    path = ROOT / folder / "solution.php"
    path.write_text(body)
    n += 1
    print("wrote", folder)
print("total", n)
