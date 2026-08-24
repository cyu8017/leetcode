#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
SOLUTIONS = {}

def add(folder, body):
    SOLUTIONS[folder] = body


add("3667_sort_array_by_absolute_value", r'''<?php
// LeetCode 3667 - Sort Array By Absolute Value
// https://leetcode.com/problems/sort-array-by-absolute-value/

class Solution {
    function sortByAbsoluteValue($nums) {
        usort($nums, function($a, $b) { return abs($a) <=> abs($b); });
        return $nums;
    }
}
''')

add("3668_restore_finishing_order", r'''<?php
// LeetCode 3668 - Restore Finishing Order
// https://leetcode.com/problems/restore-finishing-order/

class Solution {
    function recoverOrder($order, $friends) {
        $n = count($order);
        $d = array_fill(0, $n + 1, 0);
        for ($i = 0; $i < $n; $i++) $d[$order[$i]] = $i;
        usort($friends, function($a, $b) use ($d) { return $d[$a] <=> $d[$b]; });
        return $friends;
    }
}
''')

add("3669_balanced_k_factor_decomposition", r'''<?php
// LeetCode 3669 - Balanced K-Factor Decomposition
// https://leetcode.com/problems/balanced-k-factor-decomposition/

class Solution {
    private static $g = null;

    function minDifference($n, $k) {
        $MX = 100001;
        if (self::$g === null) {
            $g = array_fill(0, $MX, []);
            for ($i = 1; $i < $MX; $i++)
                for ($j = $i; $j < $MX; $j += $i) $g[$j][] = $i;
            self::$g = $g;
        }
        $g = self::$g;
        $cur = PHP_INT_MAX;
        $ans = [];
        $path = array_fill(0, $k, 0);
        $dfs = function($i, $x, $mi, $mx) use (&$dfs, &$cur, &$ans, &$path, $g) {
            if ($i === 0) {
                $d = max($mx, $x) - min($mi, $x);
                if ($d < $cur) {
                    $cur = $d;
                    $path[$i] = $x;
                    $ans = $path;
                }
                return;
            }
            foreach ($g[$x] as $y) {
                $path[$i] = $y;
                $dfs($i - 1, intdiv($x, $y), min($mi, $y), max($mx, $y));
            }
        };
        $dfs($k - 1, $n, PHP_INT_MAX, 0);
        return $ans;
    }
}
''')

add("3670_maximum_product_of_two_integers_with_no_common_bits", r'''<?php
// LeetCode 3670 - Maximum Product of Two Integers With No Common Bits
// https://leetcode.com/problems/maximum-product-of-two-integers-with-no-common-bits/

class Solution {
    function maxProduct($nums) {
        $maxV = 0;
        foreach ($nums as $v) if ($v > $maxV) $maxV = $v;
        $bitsN = 0;
        for ($x = $maxV; $x > 0; $x >>= 1) $bitsN++;
        if ($bitsN === 0) $bitsN = 1;
        $size = 1 << $bitsN;
        $best = array_fill(0, $size, 0);
        foreach ($nums as $v) if ($v > $best[$v]) $best[$v] = $v;
        for ($mask = 0; $mask < $size; $mask++) {
            for ($b = 0; $b < $bitsN; $b++) {
                if (($mask & (1 << $b)) !== 0) {
                    $sub = $mask ^ (1 << $b);
                    if ($best[$sub] > $best[$mask]) $best[$mask] = $best[$sub];
                }
            }
        }
        $ans = 0;
        foreach ($nums as $v) {
            $comp = ($size - 1) ^ $v;
            if ($best[$comp] > 0) {
                $p = $v * $best[$comp];
                if ($p > $ans) $ans = $p;
            }
        }
        return $ans;
    }
}
''')

add("3671_sum_of_beautiful_subsequences", r'''<?php
// LeetCode 3671 - Sum of Beautiful Subsequences
// https://leetcode.com/problems/sum-of-beautiful-subsequences/

class Solution {
    function totalBeauty($nums) {
        $MOD = 1000000007;
        $mx = 0;
        foreach ($nums as $v) if ($v > $mx) $mx = $v;
        $pos = array_fill(0, $mx + 1, []);
        $n = count($nums);
        for ($i = 0; $i < $n; $i++) $pos[$nums[$i]][] = $i;
        $cnt = array_fill(0, $mx + 1, 0);
        for ($g = 1; $g <= $mx; $g++) {
            $seq = [];
            for ($m = $g; $m <= $mx; $m += $g)
                foreach ($pos[$m] as $p) $seq[] = $p;
            if (count($seq) === 0) continue;
            sort($seq);
            $ways = 1;
            for ($i = 0; $i < count($seq); $i++) $ways = ($ways * 2) % $MOD;
            $cnt[$g] = ($ways - 1 + $MOD) % $MOD;
        }
        $ans = 0;
        for ($g = $mx; $g >= 1; $g--) {
            for ($m = 2 * $g; $m <= $mx; $m += $g)
                $cnt[$g] = ($cnt[$g] - $cnt[$m] + $MOD) % $MOD;
            $ans = ($ans + $cnt[$g] * $g) % $MOD;
        }
        return $ans;
    }
}
''')

add("3672_sum_of_weighted_modes_in_subarrays", r'''<?php
// LeetCode 3672 - Sum of Weighted Modes in Subarrays
// https://leetcode.com/problems/sum-of-weighted-modes-in-subarrays/

class Solution {
    function modeWeight($nums, $k) {
        $cnt = [];
        $pq = [];
        $push = function($freq, $val) use (&$pq) {
            $pq[] = [$freq, -$val];
            usort($pq, function($a, $b) {
                if ($a[0] !== $b[0]) return $b[0] <=> $a[0];
                return $a[1] <=> $b[1];
            });
        };
        $getMode = function() use (&$pq, &$cnt) {
            while (true) {
                $top = $pq[0];
                $freq = $top[0];
                $val = -$top[1];
                if ((isset($cnt[$val]) ? $cnt[$val] : 0) === $freq) return $freq * $val;
                array_shift($pq);
            }
        };
        for ($i = 0; $i < $k; $i++) {
            $x = $nums[$i];
            if (!isset($cnt[$x])) $cnt[$x] = 0;
            $cnt[$x]++;
            $push($cnt[$x], $x);
        }
        $ans = $getMode();
        $n = count($nums);
        for ($i = $k; $i < $n; $i++) {
            $x = $nums[$i];
            $y = $nums[$i - $k];
            if (!isset($cnt[$x])) $cnt[$x] = 0;
            $cnt[$x]++;
            $cnt[$y]--;
            $push($cnt[$x], $x);
            $push($cnt[$y], $y);
            $ans += $getMode();
        }
        return $ans;
    }
}
''')

add("3674_minimum_operations_to_equalize_array", r'''<?php
// LeetCode 3674 - Minimum Operations to Equalize Array
// https://leetcode.com/problems/minimum-operations-to-equalize-array/

class Solution {
    function minOperations($nums) {
        foreach ($nums as $x) if ($x !== $nums[0]) return 1;
        return 0;
    }
}
''')

add("3675_minimum_operations_to_transform_string", r'''<?php
// LeetCode 3675 - Minimum Operations to Transform String
// https://leetcode.com/problems/minimum-operations-to-transform-string/

class Solution {
    function minOperations($s) {
        $ans = 0;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $c = $s[$i];
            if ($c !== 'a') $ans = max($ans, 26 - (ord($c) - 97));
        }
        return $ans;
    }
}
''')

add("3676_count_bowl_subarrays", r'''<?php
// LeetCode 3676 - Count Bowl Subarrays
// https://leetcode.com/problems/count-bowl-subarrays/

class Solution {
    function bowlSubarrays($nums) {
        $n = count($nums);
        $ans = 0;
        $ngr = array_fill(0, $n, -1);
        $ngl = array_fill(0, $n, -1);
        $stack = [];
        for ($i = $n - 1; $i >= 0; $i--) {
            while ($stack && $nums[$stack[count($stack) - 1]] < $nums[$i]) array_pop($stack);
            if ($stack) $ngr[$i] = $stack[count($stack) - 1];
            $stack[] = $i;
        }
        $stack = [];
        for ($i = 0; $i < $n; $i++) {
            while ($stack && $nums[$stack[count($stack) - 1]] < $nums[$i]) array_pop($stack);
            if ($stack) $ngl[$i] = $stack[count($stack) - 1];
            $stack[] = $i;
        }
        for ($i = 0; $i < $n; $i++) {
            if ($ngr[$i] !== -1 && $ngr[$i] - $i >= 2) $ans++;
            if ($ngl[$i] !== -1 && $i - $ngl[$i] >= 2) $ans++;
        }
        return $ans;
    }
}
''')

add("3677_count_binary_palindromic_numbers", r'''<?php
// LeetCode 3677 - Count Binary Palindromic Numbers
// https://leetcode.com/problems/count-binary-palindromic-numbers/

class Solution {
    function countBinaryPalindromes($n) {
        if ($n === 0) return 1;
        $ans = 1;
        $s = '';
        for ($x = $n; $x > 0; $x = intdiv($x, 2)) $s .= (string)($x & 1);
        $s = strrev($s);
        $L = strlen($s);
        for ($len = 1; $len < $L; $len++) {
            $half = intdiv($len + 1, 2);
            $ans += 1 << ($half - 1);
        }
        $half = intdiv($L + 1, 2);
        $prefix = substr($s, 0, $half);
        $start = 1 << ($half - 1);
        $prefVal = 0;
        $pn = strlen($prefix);
        for ($i = 0; $i < $pn; $i++) $prefVal = ($prefVal << 1) | (ord($prefix[$i]) - 48);
        $ans += $prefVal - $start;
        $pal = $prefix;
        for ($i = $half - 1 - ($L % 2); $i >= 0; $i--) $pal .= $prefix[$i];
        $pval = 0;
        $pl = strlen($pal);
        for ($i = 0; $i < $pl; $i++) $pval = ($pval << 1) | (ord($pal[$i]) - 48);
        if ($pval <= $n) $ans++;
        return $ans;
    }
}
''')

add("3678_smallest_absent_positive_greater_than_average", r'''<?php
// LeetCode 3678 - Smallest Absent Positive Greater Than Average
// https://leetcode.com/problems/smallest-absent-positive-greater-than-average/

class Solution {
    function smallestAbsent($nums) {
        $s = [];
        $sum = 0;
        foreach ($nums as $x) {
            $s[$x] = true;
            $sum += $x;
        }
        $ans = max(1, intdiv($sum, count($nums)) + 1);
        while (isset($s[$ans])) $ans++;
        return $ans;
    }
}
''')

add("3679_minimum_discards_to_balance_inventory", r'''<?php
// LeetCode 3679 - Minimum Discards to Balance Inventory
// https://leetcode.com/problems/minimum-discards-to-balance-inventory/

class Solution {
    function minArrivalsToDiscard($arrivals, $w, $m) {
        $cnt = [];
        $n = count($arrivals);
        $marked = array_fill(0, $n, 0);
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            $x = $arrivals[$i];
            if ($i >= $w) {
                if (!isset($cnt[$arrivals[$i - $w]])) $cnt[$arrivals[$i - $w]] = 0;
                $cnt[$arrivals[$i - $w]] -= $marked[$i - $w];
            }
            if ((isset($cnt[$x]) ? $cnt[$x] : 0) >= $m) $ans++;
            else {
                $marked[$i] = 1;
                if (!isset($cnt[$x])) $cnt[$x] = 0;
                $cnt[$x]++;
            }
        }
        return $ans;
    }
}
''')

add("3680_generate_schedule", r'''<?php
// LeetCode 3680 - Generate Schedule
// https://leetcode.com/problems/generate-schedule/

class Solution {
    function generateSchedule($n) {
        if ($n < 5) return [];
        $matches = [];
        for ($i = 0; $i < $n; $i++)
            for ($j = 0; $j < $n; $j++)
                if ($i !== $j) $matches[] = [$i, $j];
        $used = array_fill(0, count($matches), false);
        $sched = [];
        $last0 = -1;
        $last1 = -1;
        $dfs = function() use (&$dfs, &$matches, &$used, &$sched, &$last0, &$last1) {
            if (count($sched) === count($matches)) return true;
            $mn = count($matches);
            for ($i = 0; $i < $mn; $i++) {
                if ($used[$i]) continue;
                $m = $matches[$i];
                if ($m[0] === $last0 || $m[0] === $last1 || $m[1] === $last0 || $m[1] === $last1) continue;
                $used[$i] = true;
                $sched[] = $m;
                $p0 = $last0;
                $p1 = $last1;
                $last0 = $m[0];
                $last1 = $m[1];
                if ($dfs()) return true;
                $last0 = $p0;
                $last1 = $p1;
                array_pop($sched);
                $used[$i] = false;
            }
            return false;
        };
        if ($dfs()) return $sched;
        return [];
    }
}
''')

add("3681_maximum_xor_of_subsequences", r'''<?php
// LeetCode 3681 - Maximum XOR of Subsequences
// https://leetcode.com/problems/maximum-xor-of-subsequences/

class Solution {
    function maxXorSubsequences($nums) {
        $basis = array_fill(0, 32, 0);
        foreach ($nums as $x) {
            $cur = $x;
            for ($b = 31; $b >= 0; $b--) {
                if (($cur & (1 << $b)) === 0) continue;
                if ($basis[$b] === 0) {
                    $basis[$b] = $cur;
                    break;
                }
                $cur ^= $basis[$b];
            }
        }
        $ans = 0;
        for ($b = 31; $b >= 0; $b--) {
            if (($ans ^ $basis[$b]) > $ans) $ans ^= $basis[$b];
        }
        return $ans;
    }
}
''')

add("3682_minimum_index_sum_of_common_elements", r'''<?php
// LeetCode 3682 - Minimum Index Sum of Common Elements
// https://leetcode.com/problems/minimum-index-sum-of-common-elements/

class Solution {
    function minimumSum($nums1, $nums2) {
        $inf = 1 << 30;
        $d = [];
        $n2 = count($nums2);
        for ($i = 0; $i < $n2; $i++)
            if (!isset($d[$nums2[$i]])) $d[$nums2[$i]] = $i;
        $ans = $inf;
        $n1 = count($nums1);
        for ($i = 0; $i < $n1; $i++) {
            if (isset($d[$nums1[$i]])) $ans = min($ans, $i + $d[$nums1[$i]]);
        }
        return $ans === $inf ? -1 : $ans;
    }
}
''')

add("3683_earliest_time_to_finish_one_task", r'''<?php
// LeetCode 3683 - Earliest Time to Finish One Task
// https://leetcode.com/problems/earliest-time-to-finish-one-task/

class Solution {
    function earliestTime($tasks) {
        $ans = 200;
        foreach ($tasks as $task) $ans = min($ans, $task[0] + $task[1]);
        return $ans;
    }
}
''')

add("3684_maximize_sum_of_at_most_k_distinct_elements", r'''<?php
// LeetCode 3684 - Maximize Sum of At Most K Distinct Elements
// https://leetcode.com/problems/maximize-sum-of-at-most-k-distinct-elements/

class Solution {
    function maxKDistinct($nums, $k) {
        sort($nums);
        $n = count($nums);
        $ans = [];
        for ($i = $n - 1; $i >= 0; $i--) {
            if ($i + 1 < $n && $nums[$i] === $nums[$i + 1]) continue;
            $ans[] = $nums[$i];
            if (--$k === 0) break;
        }
        return $ans;
    }
}
''')

add("3685_subsequence_sum_after_capping_elements", r'''<?php
// LeetCode 3685 - Subsequence Sum After Capping Elements
// https://leetcode.com/problems/subsequence-sum-after-capping-elements/

class Solution {
    function subsequenceSumAfterCapping($nums, $k) {
        $n = count($nums);
        $sorted = $nums;
        sort($sorted);
        $ans = array_fill(0, $n, false);
        $reach = array_fill(0, $k + 1, false);
        $reach[0] = true;
        $idx = 0;
        for ($x = 1; $x <= $n; $x++) {
            while ($idx < $n && $sorted[$idx] <= $x) {
                $v = $sorted[$idx];
                for ($s = $k; $s >= $v; $s--) {
                    if ($reach[$s - $v]) $reach[$s] = true;
                }
                $idx++;
            }
            $tmp = $reach;
            $rem = $n - $idx;
            for ($s = 0; $s <= $k; $s++) {
                if (!$reach[$s]) continue;
                for ($t = 1; $t <= $rem && $s + $t * $x <= $k; $t++) $tmp[$s + $t * $x] = true;
            }
            $ans[$x - 1] = $tmp[$k];
        }
        return $ans;
    }
}
''')

add("3686_number_of_stable_subsequences", r'''<?php
// LeetCode 3686 - Number of Stable Subsequences
// https://leetcode.com/problems/number-of-stable-subsequences/

class Solution {
    function countStableSubsequences($nums) {
        $MOD = 1000000007;
        $a1 = 0;
        $a2 = 0;
        $b1 = 0;
        $b2 = 0;
        foreach ($nums as $x) {
            if ($x % 2 === 1) {
                $na1 = (1 + $b1 + $b2) % $MOD;
                $na2 = $a1;
                $a1 = ($a1 + $na1) % $MOD;
                $a2 = ($a2 + $na2) % $MOD;
            } else {
                $nb1 = (1 + $a1 + $a2) % $MOD;
                $nb2 = $b1;
                $b1 = ($b1 + $nb1) % $MOD;
                $b2 = ($b2 + $nb2) % $MOD;
            }
        }
        return ((($a1 + $a2) % $MOD + $b1) % $MOD + $b2) % $MOD;
    }
}
''')

add("3687_library_late_fee_calculator", r'''<?php
// LeetCode 3687 - Library Late Fee Calculator
// https://leetcode.com/problems/library-late-fee-calculator/

class Solution {
    function lateFee($daysLate) {
        $fee = function($x) {
            if ($x === 1) return 1;
            if ($x > 5) return 3 * $x;
            return 2 * $x;
        };
        $ans = 0;
        foreach ($daysLate as $x) $ans += $fee($x);
        return $ans;
    }
}
''')

add("3688_bitwise_or_of_even_numbers_in_an_array", r'''<?php
// LeetCode 3688 - Bitwise OR of Even Numbers in an Array
// https://leetcode.com/problems/bitwise-or-of-even-numbers-in-an-array/

class Solution {
    function evenNumberBitwiseORs($nums) {
        $ans = 0;
        foreach ($nums as $x) if ($x % 2 === 0) $ans |= $x;
        return $ans;
    }
}
''')

add("3689_maximum_total_subarray_value_i", r'''<?php
// LeetCode 3689 - Maximum Total Subarray Value I
// https://leetcode.com/problems/maximum-total-subarray-value-i/

class Solution {
    function maxTotalValue($nums, $k) {
        $mn = $nums[0];
        $mx = $nums[0];
        foreach ($nums as $x) {
            $mn = min($mn, $x);
            $mx = max($mx, $x);
        }
        return $k * ($mx - $mn);
    }
}
''')

add("3690_split_and_merge_array_transformation", r'''<?php
// LeetCode 3690 - Split and Merge Array Transformation
// https://leetcode.com/problems/split-and-merge-array-transformation/

class Solution {
    function minSplitMerge($nums1, $nums2) {
        $n = count($nums1);
        $toArr = function($nums) use ($n) {
            $t = array_fill(0, 6, 0);
            for ($i = 0; $i < $n; $i++) $t[$i] = $nums[$i];
            return $t;
        };
        $key = function($a) { return implode(',', $a); };
        $start = $toArr($nums1);
        $target = $toArr($nums2);
        $vis = [];
        $vis[$key($start)] = true;
        $q = [$start];
        for ($ans = 0; ; $ans++) {
            $nq = [];
            foreach ($q as $cur) {
                if ($key($cur) === $key($target)) return $ans;
                for ($l = 0; $l < $n; $l++) {
                    for ($r = $l; $r < $n; $r++) {
                        $remain = [];
                        $sub = [];
                        for ($i = 0; $i < $l; $i++) $remain[] = $cur[$i];
                        for ($i = $r + 1; $i < $n; $i++) $remain[] = $cur[$i];
                        for ($i = $l; $i <= $r; $i++) $sub[] = $cur[$i];
                        $rn = count($remain);
                        for ($pos = 0; $pos <= $rn; $pos++) {
                            $nxtSlice = array_merge(array_slice($remain, 0, $pos), $sub, array_slice($remain, $pos));
                            $nxt = $toArr($nxtSlice);
                            $k = $key($nxt);
                            if (!isset($vis[$k])) {
                                $vis[$k] = true;
                                $nq[] = $nxt;
                            }
                        }
                    }
                }
            }
            $q = $nq;
        }
    }
}
''')

add("3691_maximum_total_subarray_value_ii", r'''<?php
// LeetCode 3691 - Maximum Total Subarray Value II
// https://leetcode.com/problems/maximum-total-subarray-value-ii/

class SparseTableRMQ {
    public $n;
    public $fMax;
    public $fMin;
    public $lg;

    function __construct($data) {
        $this->n = count($data);
        $maxLog = 0;
        while ((1 << $maxLog) <= $this->n) $maxLog++;
        $maxLog++;
        $this->fMax = [];
        $this->fMin = [];
        for ($i = 0; $i < $this->n; $i++) {
            $this->fMax[$i] = array_fill(0, $maxLog, 0);
            $this->fMin[$i] = array_fill(0, $maxLog, 0);
        }
        $this->lg = array_fill(0, $this->n + 1, 0);
        for ($i = 2; $i <= $this->n; $i++) $this->lg[$i] = $this->lg[$i >> 1] + 1;
        for ($i = 0; $i < $this->n; $i++) {
            $this->fMax[$i][0] = $data[$i];
            $this->fMin[$i][0] = $data[$i];
        }
        for ($j = 1; $j < $maxLog; $j++) {
            for ($i = 0; $i <= $this->n - (1 << $j); $i++) {
                $this->fMax[$i][$j] = max($this->fMax[$i][$j - 1], $this->fMax[$i + (1 << ($j - 1))][$j - 1]);
                $this->fMin[$i][$j] = min($this->fMin[$i][$j - 1], $this->fMin[$i + (1 << ($j - 1))][$j - 1]);
            }
        }
    }

    function queryMax($l, $r) {
        $k = $this->lg[$r - $l + 1];
        return max($this->fMax[$l][$k], $this->fMax[$r - (1 << $k) + 1][$k]);
    }

    function queryMin($l, $r) {
        $k = $this->lg[$r - $l + 1];
        return min($this->fMin[$l][$k], $this->fMin[$r - (1 << $k) + 1][$k]);
    }
}

class Solution {
    function maxTotalValue($nums, $k) {
        $n = count($nums);
        $st = new SparseTableRMQ($nums);
        $pq = new SplPriorityQueue();
        $pq->setExtractFlags(SplPriorityQueue::EXTR_DATA);
        for ($l = 0; $l < $n; $l++) {
            $val = $st->queryMax($l, $n - 1) - $st->queryMin($l, $n - 1);
            $pq->insert([$val, $l, $n - 1], $val);
        }
        $ans = 0;
        for ($i = 0; $i < $k; $i++) {
            $top = $pq->extract();
            $val = $top[0];
            $l = $top[1];
            $r = $top[2];
            $ans += $val;
            if ($r > $l) {
                $nextVal = $st->queryMax($l, $r - 1) - $st->queryMin($l, $r - 1);
                $pq->insert([$nextVal, $l, $r - 1], $nextVal);
            }
        }
        return $ans;
    }
}
''')

add("3692_majority_frequency_characters", r'''<?php
// LeetCode 3692 - Majority Frequency Characters
// https://leetcode.com/problems/majority-frequency-characters/

class Solution {
    function majorityFrequencyGroup($s) {
        $cnt = array_fill(0, 26, 0);
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) $cnt[ord($s[$i]) - 97]++;
        $f = [];
        for ($i = 0; $i < 26; $i++) {
            if ($cnt[$i] > 0) {
                if (!isset($f[$cnt[$i]])) $f[$cnt[$i]] = '';
                $f[$cnt[$i]] .= chr(97 + $i);
            }
        }
        $mx = 0;
        $mv = 0;
        $ans = '';
        foreach ($f as $v => $cs) {
            if (strlen($cs) > $mx || (strlen($cs) === $mx && $v > $mv)) {
                $mx = strlen($cs);
                $mv = $v;
                $ans = $cs;
            }
        }
        return $ans;
    }
}
''')

written = 0
for folder, body in SOLUTIONS.items():
    path = ROOT / folder / "solution.php"
    path.write_text(body, encoding="utf-8", newline="\n")
    written += 1
print(f"wrote {written}")
