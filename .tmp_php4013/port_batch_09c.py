#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
SOLUTIONS = {}

def add(folder, body):
    SOLUTIONS[folder] = body


add("2586_count_the_number_of_vowel_strings_in_range", r'''<?php
// LeetCode 2586 - Count the Number of Vowel Strings in Range
// https://leetcode.com/problems/count-the-number-of-vowel-strings-in-range/

class Solution {
    function vowelStrings($words, $left, $right) {
        $isV = function($c) {
            return $c === 'a' || $c === 'e' || $c === 'i' || $c === 'o' || $c === 'u';
        };
        $ans = 0;
        for ($i = $left; $i <= $right; $i++) {
            $w = $words[$i];
            if ($isV($w[0]) && $isV($w[strlen($w) - 1])) $ans++;
        }
        return $ans;
    }
}
''')

add("2587_rearrange_array_to_maximize_prefix_score", r'''<?php
// LeetCode 2587 - Rearrange Array to Maximize Prefix Score
// https://leetcode.com/problems/rearrange-array-to-maximize-prefix-score/

class Solution {
    function maxScore($nums) {
        sort($nums);
        $sum = 0;
        $ans = 0;
        for ($i = count($nums) - 1; $i >= 0; $i--) {
            $sum += $nums[$i];
            if ($sum > 0) $ans++;
            else break;
        }
        return $ans;
    }
}
''')

add("2588_count_the_number_of_beautiful_subarrays", r'''<?php
// LeetCode 2588 - Count the Number of Beautiful Subarrays
// https://leetcode.com/problems/count-the-number-of-beautiful-subarrays/

class Solution {
    function beautifulSubarrays($nums) {
        $freq = [0 => 1];
        $xorv = 0;
        $ans = 0;
        foreach ($nums as $x) {
            $xorv ^= $x;
            $ans += $freq[$xorv] ?? 0;
            $freq[$xorv] = ($freq[$xorv] ?? 0) + 1;
        }
        return $ans;
    }
}
''')

add("2589_minimum_time_to_complete_all_tasks", r'''<?php
// LeetCode 2589 - Minimum Time to Complete All Tasks
// https://leetcode.com/problems/minimum-time-to-complete-all-tasks/

class Solution {
    function findMinimumTime($tasks) {
        usort($tasks, function($a, $b) { return $a[1] <=> $b[1]; });
        $on = array_fill(0, 2001, false);
        $ans = 0;
        foreach ($tasks as $t) {
            $start = $t[0];
            $end = $t[1];
            $dur = $t[2];
            $have = 0;
            for ($i = $start; $i <= $end; $i++) if ($on[$i]) $have++;
            $need = $dur - $have;
            for ($i = $end; $i >= $start && $need > 0; $i--) {
                if (!$on[$i]) {
                    $on[$i] = true;
                    $need--;
                    $ans++;
                }
            }
        }
        return $ans;
    }
}
''')

add("2590_design_a_todo_list", r'''<?php
// LeetCode 2590 - Design a Todo List
// https://leetcode.com/problems/design-a-todo-list/

class TodoList {
    private $nextID;
    private $tasks;
    private $users;

    function __construct() {
        $this->nextID = 1;
        $this->tasks = [];
        $this->users = [];
    }

    function addTask($userId, $taskDescription, $dueDate, $tags) {
        $id = $this->nextID++;
        $tagSet = [];
        foreach ($tags as $tag) $tagSet[$tag] = true;
        $this->tasks[$id] = [
            'id' => $id,
            'description' => $taskDescription,
            'dueDate' => $dueDate,
            'userId' => $userId,
            'tags' => $tagSet,
            'done' => false,
        ];
        if (!isset($this->users[$userId])) $this->users[$userId] = [];
        $this->users[$userId][] = $id;
        return $id;
    }

    function getAllTasks($userId) {
        if (!isset($this->users[$userId])) return [];
        $ids = $this->users[$userId];
        usort($ids, function($a, $b) {
            return $this->tasks[$a]['dueDate'] <=> $this->tasks[$b]['dueDate'];
        });
        $ans = [];
        foreach ($ids as $id) {
            if (!$this->tasks[$id]['done']) $ans[] = $this->tasks[$id]['description'];
        }
        return $ans;
    }

    function getTasksForTag($userId, $tag) {
        if (!isset($this->users[$userId])) return [];
        $ids = $this->users[$userId];
        usort($ids, function($a, $b) {
            return $this->tasks[$a]['dueDate'] <=> $this->tasks[$b]['dueDate'];
        });
        $ans = [];
        foreach ($ids as $id) {
            $tk = $this->tasks[$id];
            if (!$tk['done'] && isset($tk['tags'][$tag])) $ans[] = $tk['description'];
        }
        return $ans;
    }

    function completeTask($userId, $taskId) {
        if (!isset($this->tasks[$taskId])) return;
        $tk = &$this->tasks[$taskId];
        if ($tk['userId'] !== $userId || $tk['done']) return;
        $tk['done'] = true;
    }
}
''')

add("2591_distribute_money_to_maximum_children", r'''<?php
// LeetCode 2591 - Distribute Money to Maximum Children
// https://leetcode.com/problems/distribute-money-to-maximum-children/

class Solution {
    function distMoney($money, $children) {
        if ($money < $children) return -1;
        $money -= $children;
        $ans = intdiv($money, 7);
        if ($ans > $children) $ans = $children;
        $remainMoney = $money - $ans * 7;
        $remainChild = $children - $ans;
        if ($remainChild === 0 && $remainMoney > 0) $ans--;
        else if ($remainChild === 1 && $remainMoney === 3) $ans--;
        if ($ans < 0) return 0;
        return $ans;
    }
}
''')

add("2592_maximize_greatness_of_an_array", r'''<?php
// LeetCode 2592 - Maximize Greatness of an Array
// https://leetcode.com/problems/maximize-greatness-of-an-array/

class Solution {
    function maximizeGreatness($nums) {
        sort($nums);
        $i = 0;
        foreach ($nums as $x) {
            if ($x > $nums[$i]) $i++;
        }
        return $i;
    }
}
''')

add("2593_find_score_of_an_array_after_marking_all_elements", r'''<?php
// LeetCode 2593 - Find Score of an Array After Marking All Elements
// https://leetcode.com/problems/find-score-of-an-array-after-marking-all-elements/

class Solution {
    function findScore($nums) {
        $n = count($nums);
        $idx = range(0, $n - 1);
        usort($idx, function($a, $b) use ($nums) {
            if ($nums[$a] !== $nums[$b]) return $nums[$a] <=> $nums[$b];
            return $a <=> $b;
        });
        $marked = array_fill(0, $n, false);
        $ans = 0;
        foreach ($idx as $i) {
            if ($marked[$i]) continue;
            $ans += $nums[$i];
            $marked[$i] = true;
            if ($i - 1 >= 0) $marked[$i - 1] = true;
            if ($i + 1 < $n) $marked[$i + 1] = true;
        }
        return $ans;
    }
}
''')

add("2594_minimum_time_to_repair_cars", r'''<?php
// LeetCode 2594 - Minimum Time to Repair Cars
// https://leetcode.com/problems/minimum-time-to-repair-cars/

class Solution {
    function repairCars($ranks, $cars) {
        $mn = min($ranks);
        $lo = 1;
        $hi = $mn * $cars * $cars;
        $ok = function($t) use ($ranks, $cars) {
            $done = 0;
            foreach ($ranks as $r) {
                $l = 0;
                $h = $cars;
                while ($l < $h) {
                    $mid = intdiv($l + $h + 1, 2);
                    if ($r * $mid * $mid <= $t) $l = $mid;
                    else $h = $mid - 1;
                }
                $done += $l;
                if ($done >= $cars) return true;
            }
            return $done >= $cars;
        };
        while ($lo < $hi) {
            $mid = intdiv($lo + $hi, 2);
            if ($ok($mid)) $hi = $mid;
            else $lo = $mid + 1;
        }
        return $lo;
    }
}
''')

add("2595_number_of_even_and_odd_bits", r'''<?php
// LeetCode 2595 - Number of Even and Odd Bits
// https://leetcode.com/problems/number-of-even-and-odd-bits/

class Solution {
    function evenOddBit($n) {
        $even = 0;
        $odd = 0;
        for ($i = 0; $n > 0; $i++, $n >>= 1) {
            if (($n & 1) !== 0) {
                if ($i % 2 === 0) $even++;
                else $odd++;
            }
        }
        return [$even, $odd];
    }
}
''')

add("2596_check_knight_tour_configuration", r'''<?php
// LeetCode 2596 - Check Knight Tour Configuration
// https://leetcode.com/problems/check-knight-tour-configuration/

class Solution {
    function checkValidGrid($grid) {
        $n = count($grid);
        if ($grid[0][0] !== 0) return false;
        $pos = array_fill(0, $n * $n, null);
        for ($i = 0; $i < $n; $i++)
            for ($j = 0; $j < $n; $j++)
                $pos[$grid[$i][$j]] = [$i, $j];
        $dirs = [
            [1, 2], [1, -2], [-1, 2], [-1, -2],
            [2, 1], [2, -1], [-2, 1], [-2, -1],
        ];
        for ($v = 0; $v + 1 < $n * $n; $v++) {
            $r = $pos[$v][0];
            $c = $pos[$v][1];
            $ok = false;
            foreach ($dirs as $d) {
                if ($r + $d[0] === $pos[$v + 1][0] && $c + $d[1] === $pos[$v + 1][1]) {
                    $ok = true;
                    break;
                }
            }
            if (!$ok) return false;
        }
        return true;
    }
}
''')

add("2597_the_number_of_beautiful_subsets", r'''<?php
// LeetCode 2597 - The Number of Beautiful Subsets
// https://leetcode.com/problems/the-number-of-beautiful-subsets/

class Solution {
    function beautifulSubsets($nums, $k) {
        $freq = [];
        foreach ($nums as $x) $freq[$x] = ($freq[$x] ?? 0) + 1;
        $groups = [];
        foreach ($freq as $key => $_) {
            $rem = $key % $k;
            if (!isset($groups[$rem])) $groups[$rem] = [];
            $groups[$rem][] = $key;
        }
        $ans = 1;
        foreach ($groups as $vals) {
            sort($vals);
            $prevTake = 0;
            $prevSkip = 1;
            $prevVal = -PHP_INT_MAX;
            foreach ($vals as $v) {
                $ways = 1;
                for ($i = 0; $i < $freq[$v]; $i++) $ways *= 2;
                $ways--;
                $skip = $prevTake + $prevSkip;
                $take = $ways * $prevSkip;
                if ($prevVal + $k !== $v) $take += $ways * $prevTake;
                $prevTake = $take;
                $prevSkip = $skip;
                $prevVal = $v;
            }
            $ans *= $prevTake + $prevSkip;
        }
        return $ans - 1;
    }
}
''')

add("2598_smallest_missing_non_negative_integer_after_operations", r'''<?php
// LeetCode 2598 - Smallest Missing Non-negative Integer After Operations
// https://leetcode.com/problems/smallest-missing-non-negative-integer-after-operations/

class Solution {
    function findSmallestInteger($nums, $value) {
        $cnt = array_fill(0, $value, 0);
        foreach ($nums as $x) {
            $r = $x % $value;
            if ($r < 0) $r += $value;
            $cnt[$r]++;
        }
        $mex = 0;
        while ($cnt[$mex % $value] > 0) {
            $cnt[$mex % $value]--;
            $mex++;
        }
        return $mex;
    }
}
''')

add("2599_make_the_prefix_sum_non_negative", r'''<?php
// LeetCode 2599 - Make the Prefix Sum Non-negative
// https://leetcode.com/problems/make-the-prefix-sum-non-negative/

class Solution {
    function makePrefSumNonNegative($nums) {
        $h = new SplPriorityQueue();
        $sum = 0;
        $ans = 0;
        foreach ($nums as $x) {
            $sum += $x;
            if ($x < 0) $h->insert($x, -$x);
            if ($sum < 0) {
                $worst = $h->extract();
                $sum -= $worst;
                $ans++;
            }
        }
        return $ans;
    }
}
''')

add("2600_k_items_with_the_maximum_sum", r'''<?php
// LeetCode 2600 - K Items With the Maximum Sum
// https://leetcode.com/problems/k-items-with-the-maximum-sum/

class Solution {
    function kItemsWithMaximumSum($numOnes, $numZeros, $numNegOnes, $k) {
        $ans = 0;
        $take = min($numOnes, $k);
        $ans += $take;
        $k -= $take;
        $take = min($numZeros, $k);
        $k -= $take;
        $take = min($numNegOnes, $k);
        $ans -= $take;
        return $ans;
    }
}
''')

add("2601_prime_subtraction_operation", r'''<?php
// LeetCode 2601 - Prime Subtraction Operation
// https://leetcode.com/problems/prime-subtraction-operation/

class Solution {
    function primeSubOperation($nums) {
        $maxV = 0;
        foreach ($nums as $x) if ($x > $maxV) $maxV = $x;
        $isP = array_fill(0, $maxV + 1, true);
        if ($maxV >= 0) $isP[0] = false;
        if ($maxV >= 1) $isP[1] = false;
        for ($i = 2; $i * $i <= $maxV; $i++) {
            if (!$isP[$i]) continue;
            for ($j = $i * $i; $j <= $maxV; $j += $i) $isP[$j] = false;
        }
        $primes = [];
        for ($i = 2; $i <= $maxV; $i++) if ($isP[$i]) $primes[] = $i;
        $prev = 0;
        foreach ($nums as $x) {
            $need = $x - $prev;
            $best = -1;
            foreach ($primes as $p) {
                if ($p >= $need) break;
                $best = $p;
            }
            $cur = $best < 0 ? $x : $x - $best;
            if ($cur <= $prev) return false;
            $prev = $cur;
        }
        return true;
    }
}
''')

add("2602_minimum_operations_to_make_all_array_elements_equal", r'''<?php
// LeetCode 2602 - Minimum Operations to Make All Array Elements Equal
// https://leetcode.com/problems/minimum-operations-to-make-all-array-elements-equal/

class Solution {
    function minOperations($nums, $queries) {
        sort($nums);
        $n = count($nums);
        $pref = array_fill(0, $n + 1, 0);
        for ($i = 0; $i < $n; $i++) $pref[$i + 1] = $pref[$i] + $nums[$i];
        $lowerBound = function($x) use ($nums, $n) {
            $lo = 0;
            $hi = $n;
            while ($lo < $hi) {
                $mid = ($lo + $hi) >> 1;
                if ($nums[$mid] < $x) $lo = $mid + 1;
                else $hi = $mid;
            }
            return $lo;
        };
        $ans = [];
        foreach ($queries as $q) {
            $i = $lowerBound($q);
            $left = $q * $i - $pref[$i];
            $right = $pref[$n] - $pref[$i] - $q * ($n - $i);
            $ans[] = $left + $right;
        }
        return $ans;
    }
}
''')

add("2603_collect_coins_in_a_tree", r'''<?php
// LeetCode 2603 - Collect Coins in a Tree
// https://leetcode.com/problems/collect-coins-in-a-tree/

class Solution {
    function collectTheCoins($coins, $edges) {
        $n = count($coins);
        $g = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $g[$e[0]][$e[1]] = true;
            $g[$e[1]][$e[0]] = true;
        }
        $deg = array_fill(0, $n, 0);
        for ($i = 0; $i < $n; $i++) $deg[$i] = count($g[$i]);
        $q = [];
        for ($i = 0; $i < $n; $i++) {
            if ($deg[$i] === 1 && $coins[$i] === 0) $q[] = $i;
        }
        while ($q) {
            $u = array_shift($q);
            foreach (array_keys($g[$u]) as $v) {
                unset($g[$v][$u]);
                $deg[$v]--;
                if ($deg[$v] === 1 && $coins[$v] === 0) $q[] = $v;
            }
            $g[$u] = [];
            $deg[$u] = 0;
        }
        for ($round = 0; $round < 2; $round++) {
            $leaves = [];
            for ($i = 0; $i < $n; $i++) if ($deg[$i] === 1) $leaves[] = $i;
            foreach ($leaves as $u) {
                foreach (array_keys($g[$u]) as $v) {
                    unset($g[$v][$u]);
                    $deg[$v]--;
                }
                $g[$u] = [];
                $deg[$u] = 0;
            }
        }
        $remain = 0;
        for ($i = 0; $i < $n; $i++) $remain += count($g[$i]);
        return $remain;
    }
}
''')

add("2604_minimum_time_to_eat_all_grains", r'''<?php
// LeetCode 2604 - Minimum Time to Eat All Grains
// https://leetcode.com/problems/minimum-time-to-eat-all-grains/

class Solution {
    function minimumTime($hens, $grains) {
        sort($hens);
        sort($grains);
        $ok = function($t) use ($hens, $grains) {
            $j = 0;
            $m = count($grains);
            foreach ($hens as $h) {
                if ($j >= $m) return true;
                if ($grains[$j] >= $h) {
                    while ($j < $m && $grains[$j] - $h <= $t) $j++;
                } else {
                    if ($h - $grains[$j] > $t) return false;
                    $left = $h - $grains[$j];
                    $maxRight1 = $t - 2 * $left;
                    $maxRight2 = intdiv($t - $left, 2);
                    $reach = $h;
                    if ($maxRight1 > $maxRight2) {
                        if ($maxRight1 > 0) $reach = $h + $maxRight1;
                    } else {
                        if ($maxRight2 > 0) $reach = $h + $maxRight2;
                    }
                    while ($j < $m && $grains[$j] <= $reach) $j++;
                }
            }
            return $j >= $m;
        };
        $lo = 0;
        $hi = 2000000000;
        while ($lo < $hi) {
            $mid = $lo + intdiv($hi - $lo, 2);
            if ($ok($mid)) $hi = $mid;
            else $lo = $mid + 1;
        }
        return $lo;
    }
}
''')

add("2605_form_smallest_number_from_two_digit_arrays", r'''<?php
// LeetCode 2605 - Form Smallest Number From Two Digit Arrays
// https://leetcode.com/problems/form-smallest-number-from-two-digit-arrays/

class Solution {
    function minNumber($nums1, $nums2) {
        $s1 = [];
        $s2 = [];
        foreach ($nums1 as $x) $s1[$x] = true;
        foreach ($nums2 as $x) $s2[$x] = true;
        $common = 10;
        foreach ($s1 as $x => $_) if (isset($s2[$x]) && $x < $common) $common = $x;
        if ($common < 10) return $common;
        $a = 10;
        $b = 10;
        foreach ($nums1 as $x) if ($x < $a) $a = $x;
        foreach ($nums2 as $x) if ($x < $b) $b = $x;
        return min($a * 10 + $b, $b * 10 + $a);
    }
}
''')

add("2606_find_the_substring_with_maximum_cost", r'''<?php
// LeetCode 2606 - Find the Substring With Maximum Cost
// https://leetcode.com/problems/find-the-substring-with-maximum-cost/

class Solution {
    function maximumCostSubstring($s, $chars, $vals) {
        $val = [];
        for ($i = 0; $i < 26; $i++) $val[$i] = $i + 1;
        $cn = strlen($chars);
        for ($i = 0; $i < $cn; $i++) $val[ord($chars[$i]) - 97] = $vals[$i];
        $best = 0;
        $cur = 0;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $cur += $val[ord($s[$i]) - 97];
            if ($cur < 0) $cur = 0;
            if ($cur > $best) $best = $cur;
        }
        return $best;
    }
}
''')

add("2607_make_k_subarray_sums_equal", r'''<?php
// LeetCode 2607 - Make K-Subarray Sums Equal
// https://leetcode.com/problems/make-k-subarray-sums-equal/

class Solution {
    function makeSubKSumEqual($arr, $k) {
        $gcd = function($a, $b) {
            while ($b !== 0) {
                $t = $a % $b;
                $a = $b;
                $b = $t;
            }
            return $a;
        };
        $n = count($arr);
        $g = $gcd($n, $k);
        $ans = 0;
        for ($r = 0; $r < $g; $r++) {
            $group = [];
            for ($i = $r; $i < $n; $i += $g) $group[] = $arr[$i];
            sort($group);
            $med = $group[intdiv(count($group), 2)];
            foreach ($group as $x) $ans += abs($x - $med);
        }
        return $ans;
    }
}
''')

add("2608_shortest_cycle_in_a_graph", r'''<?php
// LeetCode 2608 - Shortest Cycle in a Graph
// https://leetcode.com/problems/shortest-cycle-in-a-graph/

class Solution {
    function findShortestCycle($n, $edges) {
        $g = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $g[$e[0]][] = $e[1];
            $g[$e[1]][] = $e[0];
        }
        $INF = 1000000000;
        $ans = $INF;
        for ($start = 0; $start < $n; $start++) {
            $dist = array_fill(0, $n, -1);
            $parent = array_fill(0, $n, -1);
            $q = [$start];
            $dist[$start] = 0;
            while ($q) {
                $u = array_shift($q);
                foreach ($g[$u] as $v) {
                    if ($dist[$v] < 0) {
                        $dist[$v] = $dist[$u] + 1;
                        $parent[$v] = $u;
                        $q[] = $v;
                    } else if ($parent[$u] !== $v) {
                        $c = $dist[$u] + $dist[$v] + 1;
                        if ($c < $ans) $ans = $c;
                    }
                }
            }
        }
        return $ans === $INF ? -1 : $ans;
    }
}
''')

add("2609_find_the_longest_balanced_substring_of_a_binary_string", r'''<?php
// LeetCode 2609 - Find the Longest Balanced Substring of a Binary String
// https://leetcode.com/problems/find-the-longest-balanced-substring-of-a-binary-string/

class Solution {
    function findTheLongestBalancedSubstring($s) {
        $ans = 0;
        $zeros = 0;
        $ones = 0;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            if ($s[$i] === '0') {
                if ($ones > 0) $zeros = $ones = 0;
                $zeros++;
            } else {
                $ones++;
                $cur = min($ones, $zeros);
                if (2 * $cur > $ans) $ans = 2 * $cur;
            }
        }
        return $ans;
    }
}
''')

add("2610_convert_an_array_into_a_2d_array_with_conditions", r'''<?php
// LeetCode 2610 - Convert an Array Into a 2D Array With Conditions
// https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/

class Solution {
    function findMatrix($nums) {
        $freq = [];
        $ans = [];
        foreach ($nums as $x) {
            $f = $freq[$x] ?? 0;
            if ($f === count($ans)) $ans[] = [];
            $ans[$f][] = $x;
            $freq[$x] = $f + 1;
        }
        return $ans;
    }
}
''')

add("2611_mice_and_cheese", r'''<?php
// LeetCode 2611 - Mice and Cheese
// https://leetcode.com/problems/mice-and-cheese/

class Solution {
    function miceAndCheese($reward1, $reward2, $k) {
        $n = count($reward1);
        $diff = [];
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            $ans += $reward2[$i];
            $diff[] = $reward1[$i] - $reward2[$i];
        }
        rsort($diff);
        for ($i = 0; $i < $k; $i++) $ans += $diff[$i];
        return $ans;
    }
}
''')

add("2612_minimum_reverse_operations", r'''<?php
// LeetCode 2612 - Minimum Reverse Operations
// https://leetcode.com/problems/minimum-reverse-operations/

class Solution {
    function minReverseOperations($n, $p, $banned, $k) {
        $ban = [];
        foreach ($banned as $x) $ban[$x] = true;
        $ans = array_fill(0, $n, -1);
        $ans[$p] = 0;
        $q = [[$p, 0]];
        while ($q) {
            $cur = array_shift($q);
            $i = $cur[0];
            $d = $cur[1];
            $lo = $i - ($k - 1);
            if ($lo < 0) $lo = 0;
            $hi = $i;
            if ($hi > $n - $k) $hi = $n - $k;
            for ($L = $lo; $L <= $hi; $L++) {
                $R = $L + $k - 1;
                $ni = $L + $R - $i;
                if ($ni < 0 || $ni >= $n || isset($ban[$ni]) || $ans[$ni] !== -1) continue;
                $ans[$ni] = $d + 1;
                $q[] = [$ni, $d + 1];
            }
        }
        return $ans;
    }
}
''')

add("2613_beautiful_pairs", r'''<?php
// LeetCode 2613 - Beautiful Pairs
// https://leetcode.com/problems/beautiful-pairs/

class Solution {
    function beautifulPair($nums1, $nums2) {
        $n = count($nums1);
        $best = PHP_INT_MAX;
        $ans = [0, 1];
        for ($i = 0; $i < $n; $i++) {
            for ($j = $i + 1; $j < $n; $j++) {
                $d = abs($nums1[$i] - $nums1[$j]) + abs($nums2[$i] - $nums2[$j]);
                if ($d < $best || ($d === $best && ($i < $ans[0] || ($i === $ans[0] && $j < $ans[1])))) {
                    $best = $d;
                    $ans = [$i, $j];
                }
            }
        }
        return $ans;
    }
}
''')

add("2614_prime_in_diagonal", r'''<?php
// LeetCode 2614 - Prime In Diagonal
// https://leetcode.com/problems/prime-in-diagonal/

class Solution {
    function diagonalPrime($nums) {
        $isPrime = function($x) {
            if ($x < 2) return false;
            for ($i = 2; $i * $i <= $x; $i++) if ($x % $i === 0) return false;
            return true;
        };
        $n = count($nums);
        $best = 0;
        for ($i = 0; $i < $n; $i++) {
            $a = $nums[$i][$i];
            $b = $nums[$i][$n - 1 - $i];
            if ($isPrime($a) && $a > $best) $best = $a;
            if ($isPrime($b) && $b > $best) $best = $b;
        }
        return $best;
    }
}
''')

add("2615_sum_of_distances", r'''<?php
// LeetCode 2615 - Sum of Distances
// https://leetcode.com/problems/sum-of-distances/

class Solution {
    function distance($nums) {
        $n = count($nums);
        $ans = array_fill(0, $n, 0);
        $pos = [];
        for ($i = 0; $i < $n; $i++) {
            if (!isset($pos[$nums[$i]])) $pos[$nums[$i]] = [];
            $pos[$nums[$i]][] = $i;
        }
        foreach ($pos as $idxs) {
            $m = count($idxs);
            $pref = array_fill(0, $m + 1, 0);
            for ($i = 0; $i < $m; $i++) $pref[$i + 1] = $pref[$i] + $idxs[$i];
            for ($j = 0; $j < $m; $j++) {
                $idx = $idxs[$j];
                $left = $j * $idx - $pref[$j];
                $right = $pref[$m] - $pref[$j + 1] - ($m - 1 - $j) * $idx;
                $ans[$idx] = $left + $right;
            }
        }
        return $ans;
    }
}
''')

add("2616_minimize_the_maximum_difference_of_pairs", r'''<?php
// LeetCode 2616 - Minimize the Maximum Difference of Pairs
// https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs/

class Solution {
    function minimizeMax($nums, $p) {
        sort($nums);
        $lo = 0;
        $hi = $nums[count($nums) - 1] - $nums[0];
        $ok = function($d) use ($nums, $p) {
            $cnt = 0;
            $n = count($nums);
            for ($i = 0; $i + 1 < $n; ) {
                if ($nums[$i + 1] - $nums[$i] <= $d) {
                    $cnt++;
                    $i += 2;
                } else $i++;
            }
            return $cnt >= $p;
        };
        while ($lo < $hi) {
            $mid = ($lo + $hi) >> 1;
            if ($ok($mid)) $hi = $mid;
            else $lo = $mid + 1;
        }
        return $lo;
    }
}
''')

add("2617_minimum_number_of_visited_cells_in_a_grid", r'''<?php
// LeetCode 2617 - Minimum Number of Visited Cells in a Grid
// https://leetcode.com/problems/minimum-number-of-visited-cells-in-a-grid/

class Solution {
    function minimumVisitedCells($grid) {
        $m = count($grid);
        $n = count($grid[0]);
        $dist = [];
        for ($i = 0; $i < $m; $i++) $dist[] = array_fill(0, $n, -1);
        $q = [[0, 0]];
        $dist[0][0] = 1;
        while ($q) {
            $cur = array_shift($q);
            $r = $cur[0];
            $c = $cur[1];
            if ($r === $m - 1 && $c === $n - 1) return $dist[$r][$c];
            for ($nc = $c + 1; $nc <= $c + $grid[$r][$c] && $nc < $n; $nc++) {
                if ($dist[$r][$nc] === -1) {
                    $dist[$r][$nc] = $dist[$r][$c] + 1;
                    $q[] = [$r, $nc];
                }
            }
            for ($nr = $r + 1; $nr <= $r + $grid[$r][$c] && $nr < $m; $nr++) {
                if ($dist[$nr][$c] === -1) {
                    $dist[$nr][$c] = $dist[$r][$c] + 1;
                    $q[] = [$nr, $c];
                }
            }
        }
        return -1;
    }
}
''')

add("2618_check_if_object_instance_of_class", r'''<?php
// LeetCode 2618 - Check if Object Instance of Class
// https://leetcode.com/problems/check-if-object-instance-of-class/

class Solution {
    function checkIfInstanceOf($obj, $classFunction) {
        if ($obj === null) return false;
        if (is_object($classFunction)) {
            $classFunction = get_class($classFunction);
        }
        if (!is_string($classFunction) || $classFunction === '') return false;
        if (is_object($obj)) return $obj instanceof $classFunction;
        $map = [
            'integer' => ['int', 'integer'],
            'double' => ['float', 'double'],
            'string' => ['string'],
            'boolean' => ['bool', 'boolean'],
            'array' => ['array'],
        ];
        $t = gettype($obj);
        if (!isset($map[$t])) return false;
        return in_array(strtolower($classFunction), $map[$t], true);
    }
}
''')

add("2619_array_prototype_last", r'''<?php
// LeetCode 2619 - Array Prototype Last
// https://leetcode.com/problems/array-prototype-last/

class Solution {
    function last($nums) {
        $n = count($nums);
        if ($n === 0) return -1;
        return $nums[$n - 1];
    }
}
''')

written = 0
for folder, body in SOLUTIONS.items():
    path = ROOT / folder / "solution.php"
    path.write_text(body, encoding="utf-8", newline="\n")
    written += 1
print(f"wrote {written}")
