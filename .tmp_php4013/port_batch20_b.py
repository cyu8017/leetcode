#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
SOLUTIONS = {}

def add(folder, body):
    SOLUTIONS[folder] = body


add("3745_maximize_expression_of_three_elements", r'''<?php
// LeetCode 3745 - Maximize Expression of Three Elements
// https://leetcode.com/problems/maximize-expression-of-three-elements/

class Solution {
    function maximizeExpressionOfThree($nums) {
        $inf = 1 << 30;
        $a = -$inf;
        $b = -$inf;
        $c = $inf;
        foreach ($nums as $x) {
            if ($x < $c) $c = $x;
            if ($x >= $a) { $b = $a; $a = $x; }
            else if ($x > $b) $b = $x;
        }
        return $a + $b - $c;
    }
}
''')

add("3746_minimum_string_length_after_balanced_removals", r'''<?php
// LeetCode 3746 - Minimum String Length After Balanced Removals
// https://leetcode.com/problems/minimum-string-length-after-balanced-removals/

class Solution {
    function minLengthAfterRemovals($s) {
        $a = 0;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) if ($s[$i] === 'a') $a++;
        $b = $n - $a;
        return abs($a - $b);
    }
}
''')

add("3747_count_distinct_integers_after_removing_zeros", r'''<?php
// LeetCode 3747 - Count Distinct Integers After Removing Zeros
// https://leetcode.com/problems/count-distinct-integers-after-removing-zeros/

class Solution {
    function countDistinct($n) {
        $s = strval($n);
        $m = strlen($s);
        $f = [];
        for ($i = 0; $i < 20; $i++) {
            $f[$i] = [];
            for ($z = 0; $z < 2; $z++) {
                $f[$i][$z] = [];
                for ($l = 0; $l < 2; $l++) $f[$i][$z][$l] = array_fill(0, 2, -1);
            }
        }
        $dfs = function($i, $zero, $lead, $limit) use (&$dfs, &$f, $s, $m) {
            if ($i === $m) return ($zero === 0 && $lead === 0) ? 1 : 0;
            if ($limit === 0 && $f[$i][$zero][$lead][$limit] !== -1) return $f[$i][$zero][$lead][$limit];
            $up = $limit === 1 ? ord($s[$i]) - 48 : 9;
            $ans = 0;
            for ($d = 0; $d <= $up; $d++) {
                $nxtZero = $zero;
                if ($d === 0 && $lead === 0) $nxtZero = 1;
                $nxtLead = ($lead === 1 && $d === 0) ? 1 : 0;
                $nxtLimit = ($limit === 1 && $d === $up) ? 1 : 0;
                $ans += $dfs($i + 1, $nxtZero, $nxtLead, $nxtLimit);
            }
            if ($limit === 0) $f[$i][$zero][$lead][$limit] = $ans;
            return $ans;
        };
        return $dfs(0, 0, 1, 1);
    }
}
''')

add("3748_count_stable_subarrays", r'''<?php
// LeetCode 3748 - Count Stable Subarrays
// https://leetcode.com/problems/count-stable-subarrays/

class Solution {
    function countStableSubarrays($nums, $queries) {
        $n = count($nums);
        $seg = [];
        $s = [0];
        $l = 0;
        for ($r = 0; $r < $n; $r++) {
            if ($r === $n - 1 || $nums[$r] > $nums[$r + 1]) {
                $seg[] = $l;
                $k = $r - $l + 1;
                $s[] = $s[count($s) - 1] + $k * ($k + 1) / 2;
                $l = $r + 1;
            }
        }
        $lowerBound = function($a, $x) {
            $lo = 0;
            $hi = count($a);
            while ($lo < $hi) {
                $mid = ($lo + $hi) >> 1;
                if ($a[$mid] < $x) $lo = $mid + 1;
                else $hi = $mid;
            }
            return $lo;
        };
        $ans = array_fill(0, count($queries), 0);
        for ($idx = 0; $idx < count($queries); $idx++) {
            $left = $queries[$idx][0];
            $right = $queries[$idx][1];
            $i = $lowerBound($seg, $left + 1);
            $j = $lowerBound($seg, $right + 1) - 1;
            if ($i > $j) {
                $k = $right - $left + 1;
                $ans[$idx] = $k * ($k + 1) / 2;
            } else {
                $a = $seg[$i] - $left;
                $b = $right - $seg[$j] + 1;
                $ans[$idx] = $a * ($a + 1) / 2 + $s[$j] - $s[$i] + $b * ($b + 1) / 2;
            }
        }
        return $ans;
    }
}
''')

add("3749_evaluate_valid_expressions", r'''<?php
// LeetCode 3749 - Evaluate Valid Expressions
// https://leetcode.com/problems/evaluate-valid-expressions/

class Solution {
    function evaluateExpression($expression) {
        $parse = function($i) use (&$parse, $expression) {
            $ch = $expression[$i];
            if (($ch >= '0' && $ch <= '9') || $ch === '-') {
                $j = $i;
                if ($expression[$j] === '-') $j++;
                while ($j < strlen($expression) && $expression[$j] >= '0' && $expression[$j] <= '9') $j++;
                return [intval(substr($expression, $i, $j - $i)), $j];
            }
            $j = $i;
            while ($expression[$j] !== '(') $j++;
            $op = substr($expression, $i, $j - $i);
            $j++;
            $p1 = $parse($j);
            $j = $p1[1] + 1;
            $p2 = $parse($j);
            $j = $p2[1] + 1;
            $res = 0;
            if ($op === "add") $res = $p1[0] + $p2[0];
            else if ($op === "sub") $res = $p1[0] - $p2[0];
            else if ($op === "mul") $res = $p1[0] * $p2[0];
            else if ($op === "div") $res = intdiv($p1[0], $p2[0]);
            return [$res, $j];
        };
        return $parse(0)[0];
    }
}
''')

add("3750_minimum_number_of_flips_to_reverse_binary_string", r'''<?php
// LeetCode 3750 - Minimum Number of Flips to Reverse Binary String
// https://leetcode.com/problems/minimum-number-of-flips-to-reverse-binary-string/

class Solution {
    function minimumFlips($n) {
        $x = $n;
        if ($x === 0) $s = "0";
        else {
            $bits = '';
            while ($x > 0) {
                $bits .= chr(48 + ($x & 1));
                $x >>= 1;
            }
            $s = strrev($bits);
        }
        $m = strlen($s);
        $cnt = 0;
        for ($i = 0; $i < intdiv($m, 2); $i++) {
            if ($s[$i] !== $s[$m - $i - 1]) $cnt++;
        }
        return $cnt * 2;
    }
}
''')

add("3751_total_waviness_of_numbers_in_range_i", r'''<?php
// LeetCode 3751 - Total Waviness of Numbers in Range I
// https://leetcode.com/problems/total-waviness-of-numbers-in-range-i/

class Solution {
    function totalWaviness($num1, $num2) {
        $F = function($x) {
            $nums = [];
            while ($x > 0) {
                $nums[] = $x % 10;
                $x = intdiv($x, 10);
            }
            $m = count($nums);
            if ($m < 3) return 0;
            $s = 0;
            for ($i = 1; $i < $m - 1; $i++) {
                if (($nums[$i] > $nums[$i - 1] && $nums[$i] > $nums[$i + 1]) ||
                    ($nums[$i] < $nums[$i - 1] && $nums[$i] < $nums[$i + 1])) $s++;
            }
            return $s;
        };
        $ans = 0;
        for ($x = $num1; $x <= $num2; $x++) $ans += $F($x);
        return $ans;
    }
}
''')

add("3752_lexicographically_smallest_negated_permutation_that_sums_to_target", r'''<?php
// LeetCode 3752 - Lexicographically Smallest Negated Permutation that Sums to Target
// https://leetcode.com/problems/lexicographically-smallest-negated-permutation-that-sums-to-target/

class Solution {
    function lexicographicallySmallest($n, $target) {
        $total = $n * ($n + 1) / 2;
        if ($target < -$total || $target > $total || ($total - $target) % 2 !== 0) return [];
        $remaining = ($total - $target) / 2;
        $negative = array_fill(0, $n + 1, false);
        for ($value = $n; $value >= 1; $value--) {
            if ($value <= $remaining) {
                $negative[$value] = true;
                $remaining -= $value;
            }
        }
        $answer = [];
        for ($value = $n; $value >= 1; $value--) {
            if ($negative[$value]) $answer[] = -$value;
        }
        for ($value = 1; $value <= $n; $value++) {
            if (!$negative[$value]) $answer[] = $value;
        }
        return $answer;
    }
}
''')

add("3753_total_waviness_of_numbers_in_range_ii", r'''<?php
// LeetCode 3753 - Total Waviness of Numbers in Range II
// https://leetcode.com/problems/total-waviness-of-numbers-in-range-ii/

class Solution {
    function totalWaviness($a, $b) {
        $wavinessUpTo = function($limit) {
            if ($limit < 0) return 0;
            $digits = [];
            if ($limit === 0) $digits[] = 0;
            else {
                for ($value = $limit; $value > 0; $value = intdiv($value, 10))
                    $digits[] = $value % 10;
                $digits = array_reverse($digits);
            }
            $memo = [];
            $dfs = function($position, $secondLast, $last, $started, $tight) use (&$dfs, &$memo, $digits) {
                if ($position === count($digits)) return ['count' => 1, 'sum' => 0];
                $key = $position . "," . $secondLast . "," . $last . "," . ($started ? 1 : 0);
                if (!$tight && isset($memo[$key])) return $memo[$key];
                $upper = $tight ? $digits[$position] : 9;
                $result = ['count' => 0, 'sum' => 0];
                for ($digit = 0; $digit <= $upper; $digit++) {
                    $nextTight = $tight && $digit === $upper;
                    $nextSecondLast = $secondLast;
                    $nextLast = $last;
                    $nextStarted = $started || $digit !== 0;
                    $add = 0;
                    if (!$nextStarted) {
                        $nextSecondLast = $nextLast = 10;
                    } else if (!$started) {
                        $nextSecondLast = 10;
                        $nextLast = $digit;
                    } else {
                        if ($secondLast !== 10 &&
                            (($last > $secondLast && $last > $digit) || ($last < $secondLast && $last < $digit))) {
                            $add = 1;
                        }
                        $nextSecondLast = $last;
                        $nextLast = $digit;
                    }
                    $child = $dfs($position + 1, $nextSecondLast, $nextLast, $nextStarted, $nextTight);
                    $result['count'] += $child['count'];
                    $result['sum'] += $child['sum'] + $add * $child['count'];
                }
                if (!$tight) $memo[$key] = $result;
                return $result;
            };
            return $dfs(0, 10, 10, false, true)['sum'];
        };
        return $wavinessUpTo($b) - $wavinessUpTo($a - 1);
    }
}
''')

add("3754_concatenate_non_zero_digits_and_multiply_by_sum_i", r'''<?php
// LeetCode 3754 - Concatenate Non Zero Digits And Multiply By Sum I
// https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-i/

class Solution {
    function sumAndMultiply($n) {
        $p = 1;
        $x = 0;
        $s = 0;
        while ($n > 0) {
            $v = $n % 10;
            if ($v !== 0) {
                $s += $v;
                $x += $p * $v;
                $p *= 10;
            }
            $n = intdiv($n, 10);
        }
        return $x * $s;
    }
}
''')

add("3755_find_maximum_balanced_xor_subarray_length", r'''<?php
// LeetCode 3755 - Find Maximum Balanced XOR Subarray Length
// https://leetcode.com/problems/find-maximum-balanced-xor-subarray-length/

class Solution {
    function maxBalancedSubarray($nums) {
        $d = [];
        $a = 0;
        $b = count($nums);
        $ans = 0;
        $d[$b] = -1;
        $n = count($nums);
        for ($i = 0; $i < $n; $i++) {
            $a ^= $nums[$i];
            if ($nums[$i] % 2 === 0) $b++;
            else $b--;
            $key = $a . "#" . $b;
            if (isset($d[$key])) $ans = max($ans, $i - $d[$key]);
            else $d[$key] = $i;
        }
        return $ans;
    }
}
''')

add("3756_concatenate_non_zero_digits_and_multiply_by_sum_ii", r'''<?php
// LeetCode 3756 - Concatenate Non Zero Digits And Multiply By Sum II
// https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-ii/

class Solution {
    function sumAndMultiply($s, $queries) {
        $MX = 100001;
        $MOD = 1000000007;
        $PW = array_fill(0, $MX, 0);
        $PW[0] = 1;
        for ($i = 1; $i < $MX; $i++) $PW[$i] = ($PW[$i - 1] * 10) % $MOD;
        $n = strlen($s);
        $sumD = array_fill(0, $n + 1, 0);
        $cntN0 = array_fill(0, $n + 1, 0);
        $p = array_fill(0, $n + 1, 0);
        for ($i = 1; $i <= $n; $i++) {
            $d = ord($s[$i - 1]) - 48;
            $sumD[$i] = $sumD[$i - 1] + $d;
            $cntN0[$i] = $cntN0[$i - 1];
            if ($d > 0) {
                $cntN0[$i]++;
                $p[$i] = ($p[$i - 1] * 10 + $d) % $MOD;
            } else $p[$i] = $p[$i - 1];
        }
        $ans = array_fill(0, count($queries), 0);
        for ($i = 0; $i < count($queries); $i++) {
            $l = $queries[$i][0];
            $r = $queries[$i][1];
            $n0 = $cntN0[$r + 1] - $cntN0[$l];
            $sd = $sumD[$r + 1] - $sumD[$l];
            $x = ($p[$r + 1] - ($p[$l] * $PW[$n0]) % $MOD + $MOD) % $MOD;
            $ans[$i] = ($x * $sd) % $MOD;
        }
        return $ans;
    }
}
''')

add("3757_number_of_effective_subsequences", r'''<?php
// LeetCode 3757 - Number of Effective Subsequences
// https://leetcode.com/problems/number-of-effective-subsequences/

class Solution {
    function countEffectiveSubsequences($nums) {
        $PopCount = function($x) {
            $c = 0;
            while ($x !== 0) { $c += $x & 1; $x >>= 1; }
            return $c;
        };
        $mod = 1000000007;
        $all = 0;
        foreach ($nums as $x) $all |= $x;
        $bits = [];
        for ($b = 0; $b < 20; $b++) if ((($all >> $b) & 1) !== 0) $bits[] = $b;
        $m = count($bits);
        $freq = array_fill(0, 1 << $m, 0);
        foreach ($nums as $x) {
            $mask = 0;
            for ($i = 0; $i < $m; $i++) if ((($x >> $bits[$i]) & 1) !== 0) $mask |= 1 << $i;
            $freq[$mask]++;
        }
        $disjoint = $freq;
        for ($b = 0; $b < $m; $b++) {
            for ($mask = 0; $mask < (1 << $m); $mask++) {
                if ((($mask >> $b) & 1) !== 0) $disjoint[$mask] += $disjoint[$mask ^ (1 << $b)];
            }
        }
        $pow2 = array_fill(0, count($nums) + 1, 0);
        $pow2[0] = 1;
        for ($i = 1; $i <= count($nums); $i++) $pow2[$i] = $pow2[$i - 1] * 2 % $mod;
        $ans = 0;
        $full = (1 << $m) - 1;
        for ($s = 1; $s <= $full; $s++) {
            $ways = $pow2[$disjoint[$full ^ $s]];
            $bc = $PopCount($s);
            if (($bc & 1) !== 0) {
                $ans += $ways;
                if ($ans >= $mod) $ans -= $mod;
            } else {
                $ans -= $ways;
                if ($ans < 0) $ans += $mod;
            }
        }
        return $ans;
    }
}
''')

add("3758_convert_number_words_to_digits", r'''<?php
// LeetCode 3758 - Convert Number Words to Digits
// https://leetcode.com/problems/convert-number-words-to-digits/

class Solution {
    function convertNumber($s) {
        $d = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"];
        $n = strlen($s);
        $ans = '';
        for ($i = 0; $i < $n; $i++) {
            for ($j = 0; $j < 10; $j++) {
                $m = strlen($d[$j]);
                if ($i + $m <= $n && substr($s, $i, $m) === $d[$j]) {
                    $ans .= chr(48 + $j);
                    $i += $m - 1;
                    break;
                }
            }
        }
        return $ans;
    }
}
''')

add("3759_count_elements_with_at_least_k_greater_values", r'''<?php
// LeetCode 3759 - Count Elements With At Least K Greater Values
// https://leetcode.com/problems/count-elements-with-at-least-k-greater-values/

class Solution {
    function countElements($nums, $k) {
        $n = count($nums);
        if ($k === 0) return $n;
        $a = $nums;
        sort($a);
        $ans = 0;
        for ($i = 0; $i < $n - $k; $i++) {
            if ($a[$n - $k] > $a[$i]) $ans++;
        }
        return $ans;
    }
}
''')

add("3760_maximum_substrings_with_distinct_start", r'''<?php
// LeetCode 3760 - Maximum Substrings With Distinct Start
// https://leetcode.com/problems/maximum-substrings-with-distinct-start/

class Solution {
    function maxDistinct($s) {
        $cnt = array_fill(0, 26, 0);
        $ans = 0;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $idx = ord($s[$i]) - 97;
            $cnt[$idx]++;
            if ($cnt[$idx] === 1) $ans++;
        }
        return $ans;
    }
}
''')

add("3761_minimum_absolute_distance_between_mirror_pairs", r'''<?php
// LeetCode 3761 - Minimum Absolute Distance Between Mirror Pairs
// https://leetcode.com/problems/minimum-absolute-distance-between-mirror-pairs/

class Solution {
    function minMirrorPairDistance($nums) {
        $reverse = function($x) {
            $y = 0;
            for (; $x > 0; $x = intdiv($x, 10)) $y = $y * 10 + $x % 10;
            return $y;
        };
        $n = count($nums);
        $pos = [];
        $ans = $n + 1;
        for ($i = 0; $i < $n; $i++) {
            if (isset($pos[$nums[$i]])) $ans = min($ans, $i - $pos[$nums[$i]]);
            $pos[$reverse($nums[$i])] = $i;
        }
        return $ans > $n ? -1 : $ans;
    }
}
''')

add("3762_minimum_operations_to_equalize_subarrays", r'''<?php
// LeetCode 3762 - Minimum Operations to Equalize Subarrays
// https://leetcode.com/problems/minimum-operations-to-equalize-subarrays/

class _MONode {
    public $left = 0;
    public $right = 0;
    public $count = 0;
    public $sum = 0;
    function __construct($o = null) {
        if ($o) {
            $this->left = $o->left;
            $this->right = $o->right;
            $this->count = $o->count;
            $this->sum = $o->sum;
        }
    }
}

class Solution {
    function minOperations($nums, $k, $queries) {
        $n = count($nums);
        $quotient = array_fill(0, $n, 0);
        $remainder = array_fill(0, $n, 0);
        $values = array_fill(0, $n, 0);
        for ($i = 0; $i < $n; $i++) {
            $quotient[$i] = intdiv($nums[$i], $k);
            $remainder[$i] = $nums[$i] % $k;
            $values[$i] = $quotient[$i];
        }
        sort($values);
        $vu = 1;
        for ($i = 1; $i < $n; $i++) if ($values[$i] !== $values[$vu - 1]) $values[$vu++] = $values[$i];
        $values = array_slice($values, 0, $vu);

        $nodes = [new _MONode()];
        $roots = array_fill(0, $n + 1, 0);
        $umax = count($values) - 1;

        $lowerBound = function($a, $x) {
            $lo = 0;
            $hi = count($a);
            while ($lo < $hi) {
                $mid = ($lo + $hi) >> 1;
                if ($a[$mid] < $x) $lo = $mid + 1;
                else $hi = $mid;
            }
            return $lo;
        };

        $update = function($previous, $lo, $hi, $position, $value) use (&$update, &$nodes) {
            $current = count($nodes);
            $nodes[] = new _MONode($nodes[$previous]);
            $nodes[$current]->count++;
            $nodes[$current]->sum += $value;
            if ($lo < $hi) {
                $mid = ($lo + $hi) >> 1;
                if ($position <= $mid) $nodes[$current]->left = $update($nodes[$previous]->left, $lo, $mid, $position, $value);
                else $nodes[$current]->right = $update($nodes[$previous]->right, $mid + 1, $hi, $position, $value);
            }
            return $current;
        };

        $kth = function($rightRoot, $leftRoot, $lo, $hi, $rank) use (&$kth, &$nodes) {
            if ($lo === $hi) return $lo;
            $leftCount = $nodes[$nodes[$rightRoot]->left]->count - $nodes[$nodes[$leftRoot]->left]->count;
            $mid = ($lo + $hi) >> 1;
            if ($rank <= $leftCount) return $kth($nodes[$rightRoot]->left, $nodes[$leftRoot]->left, $lo, $mid, $rank);
            return $kth($nodes[$rightRoot]->right, $nodes[$leftRoot]->right, $mid + 1, $hi, $rank - $leftCount);
        };

        $prefixStats = function($rightRoot, $leftRoot, $lo, $hi, $end) use (&$prefixStats, &$nodes) {
            if ($end < $lo) return [0, 0];
            if ($hi <= $end) return [
                $nodes[$rightRoot]->count - $nodes[$leftRoot]->count,
                $nodes[$rightRoot]->sum - $nodes[$leftRoot]->sum
            ];
            $mid = ($lo + $hi) >> 1;
            $left = $prefixStats($nodes[$rightRoot]->left, $nodes[$leftRoot]->left, $lo, $mid, $end);
            $count = $left[0];
            $sum = $left[1];
            if ($end > $mid) {
                $right = $prefixStats($nodes[$rightRoot]->right, $nodes[$leftRoot]->right, $mid + 1, $hi, $end);
                $count += $right[0];
                $sum += $right[1];
            }
            return [$count, $sum];
        };

        for ($i = 0; $i < $n; $i++) {
            $position = $lowerBound($values, $quotient[$i]);
            $roots[$i + 1] = $update($roots[$i], 0, $umax, $position, $quotient[$i]);
        }

        $logv = array_fill(0, $n + 1, 0);
        for ($i = 2; $i <= $n; $i++) $logv[$i] = $logv[$i >> 1] + 1;
        $levels = $logv[$n] + 1;
        $minTable = [];
        $maxTable = [];
        $minTable[0] = $remainder;
        $maxTable[0] = $remainder;
        for ($level = 1; $level < $levels; $level++) {
            $length = $n - (1 << $level) + 1;
            $minTable[$level] = array_fill(0, $length, 0);
            $maxTable[$level] = array_fill(0, $length, 0);
            $half = 1 << ($level - 1);
            for ($i = 0; $i < $length; $i++) {
                $minTable[$level][$i] = min($minTable[$level - 1][$i], $minTable[$level - 1][$i + $half]);
                $maxTable[$level][$i] = max($maxTable[$level - 1][$i], $maxTable[$level - 1][$i + $half]);
            }
        }

        $answer = array_fill(0, count($queries), 0);
        for ($qi = 0; $qi < count($queries); $qi++) {
            $left = $queries[$qi][0];
            $right = $queries[$qi][1];
            $length = $right - $left + 1;
            $level = $logv[$length];
            $offset = $right - (1 << $level) + 1;
            $minR = min($minTable[$level][$left], $minTable[$level][$offset]);
            $maxR = max($maxTable[$level][$left], $maxTable[$level][$offset]);
            if ($minR !== $maxR) {
                $answer[$qi] = -1;
                continue;
            }
            $medianIndex = $kth($roots[$right + 1], $roots[$left], 0, $umax, intdiv($length + 1, 2));
            $median = $values[$medianIndex];
            $stats = $prefixStats($roots[$right + 1], $roots[$left], 0, $umax, $medianIndex);
            $leftCount = $stats[0];
            $leftSum = $stats[1];
            $totalSum = $nodes[$roots[$right + 1]]->sum - $nodes[$roots[$left]]->sum;
            $answer[$qi] = $median * $leftCount - $leftSum + ($totalSum - $leftSum) - $median * ($length - $leftCount);
        }
        return $answer;
    }
}
''')

add("3763_maximum_total_sum_with_threshold_constraints", r'''<?php
// LeetCode 3763 - Maximum Total Sum With Threshold Constraints
// https://leetcode.com/problems/maximum-total-sum-with-threshold-constraints/

class Solution {
    function maxSum($nums, $threshold) {
        $n = count($nums);
        $idx = range(0, $n - 1);
        usort($idx, function($a, $b) use ($threshold) {
            return $threshold[$a] <=> $threshold[$b];
        });
        $tree = [];
        $push = function($x) use (&$tree) {
            $tree[] = $x;
            $i = count($tree) - 1;
            while ($i > 0) {
                $p = ($i - 1) >> 1;
                if ($tree[$i] <= $tree[$p]) break;
                $tmp = $tree[$i]; $tree[$i] = $tree[$p]; $tree[$p] = $tmp;
                $i = $p;
            }
        };
        $pop = function() use (&$tree) {
            $top = $tree[0];
            $last = array_pop($tree);
            if (count($tree)) {
                $tree[0] = $last;
                $i = 0;
                while (true) {
                    $s = $i;
                    $l = $i * 2 + 1;
                    $r = $l + 1;
                    if ($l < count($tree) && $tree[$l] > $tree[$s]) $s = $l;
                    if ($r < count($tree) && $tree[$r] > $tree[$s]) $s = $r;
                    if ($s === $i) break;
                    $tmp = $tree[$i]; $tree[$i] = $tree[$s]; $tree[$s] = $tmp;
                    $i = $s;
                }
            }
            return $top;
        };
        $ans = 0;
        $i = 0;
        for ($step = 1; ; $step++) {
            while ($i < $n && $threshold[$idx[$i]] <= $step) {
                $push($nums[$idx[$i]]);
                $i++;
            }
            if (!count($tree)) break;
            $ans += $pop();
        }
        return $ans;
    }
}
''')

add("3765_complete_prime_number", r'''<?php
// LeetCode 3765 - Complete Prime Number
// https://leetcode.com/problems/complete-prime-number/

class Solution {
    function completePrime($num) {
        $isPrime = function($x) {
            if ($x < 2) return false;
            for ($i = 2; $i * $i <= $x; $i++) if ($x % $i === 0) return false;
            return true;
        };
        $s = strval($num);
        $x = 0;
        $len = strlen($s);
        for ($i = 0; $i < $len; $i++) {
            $x = $x * 10 + (ord($s[$i]) - 48);
            if (!$isPrime($x)) return false;
        }
        $x = 0;
        $p = 1;
        for ($i = $len - 1; $i >= 0; $i--) {
            $x = $p * (ord($s[$i]) - 48) + $x;
            $p *= 10;
            if (!$isPrime($x)) return false;
        }
        return true;
    }
}
''')

add("3766_minimum_operations_to_make_binary_palindrome", r'''<?php
// LeetCode 3766 - Minimum Operations to Make Binary Palindrome
// https://leetcode.com/problems/minimum-operations-to-make-binary-palindrome/

class Solution {
    function minOperations($nums) {
        $PALS = [];
        $N = 1 << 14;
        $isPalindrome = function($s) {
            $m = strlen($s);
            for ($i = 0; $i < intdiv($m, 2); $i++) if ($s[$i] !== $s[$m - 1 - $i]) return false;
            return true;
        };
        for ($i = 0; $i < $N; $i++) {
            $sb = '';
            $x = $i;
            if ($x === 0) $sb = '0';
            else {
                while ($x > 0) {
                    $sb .= chr(48 + ($x & 1));
                    $x >>= 1;
                }
                $sb = strrev($sb);
            }
            if ($isPalindrome($sb)) $PALS[] = $i;
        }
        $lowerBound = function($x) use ($PALS) {
            $lo = 0;
            $hi = count($PALS);
            while ($lo < $hi) {
                $mid = ($lo + $hi) >> 1;
                if ($PALS[$mid] < $x) $lo = $mid + 1;
                else $hi = $mid;
            }
            return $lo;
        };
        $ans = array_fill(0, count($nums), 0);
        for ($k = 0; $k < count($nums); $k++) {
            $x = $nums[$k];
            $it = $lowerBound($x);
            $t = 9007199254740991;
            if ($it < count($PALS)) $t = $PALS[$it] - $x;
            if ($it > 0) $t = min($t, $x - $PALS[$it - 1]);
            $ans[$k] = $t;
        }
        return $ans;
    }
}
''')

add("3767_maximize_points_after_choosing_k_tasks", r'''<?php
// LeetCode 3767 - Maximize Points After Choosing K Tasks
// https://leetcode.com/problems/maximize-points-after-choosing-k-tasks/

class Solution {
    function maxPoints($technique1, $technique2, $k) {
        $n = count($technique1);
        $idx = range(0, $n - 1);
        usort($idx, function($i, $j) use ($technique1, $technique2) {
            return ($technique1[$j] - $technique2[$j]) <=> ($technique1[$i] - $technique2[$i]);
        });
        $ans = 0;
        foreach ($technique2 as $x) $ans += $x;
        for ($i = 0; $i < $k; $i++) {
            $index = $idx[$i];
            $ans -= $technique2[$index];
            $ans += $technique1[$index];
        }
        for ($i = $k; $i < $n; $i++) {
            $index = $idx[$i];
            if ($technique1[$index] >= $technique2[$index]) {
                $ans -= $technique2[$index];
                $ans += $technique1[$index];
            }
        }
        return $ans;
    }
}
''')

add("3768_minimum_inversion_count_in_subarrays_of_fixed_length", r'''<?php
// LeetCode 3768 - Minimum Inversion Count in Subarrays of Fixed Length
// https://leetcode.com/problems/minimum-inversion-count-in-subarrays-of-fixed-length/

class Solution {
    function minInversionCount($nums, $k) {
        $vals = $nums;
        sort($vals);
        $n = 0;
        for ($i = 0; $i < count($vals); $i++) {
            if ($n === 0 || $vals[$i] !== $vals[$n - 1]) $vals[$n++] = $vals[$i];
        }
        $vals = array_slice($vals, 0, $n);
        $bit = array_fill(0, count($vals) + 1, 0);
        $add = function($i, $delta) use (&$bit) {
            for (; $i < count($bit); $i += $i & -$i) $bit[$i] += $delta;
        };
        $sum = function($i) use (&$bit) {
            $res = 0;
            for (; $i > 0; $i -= $i & -$i) $res += $bit[$i];
            return $res;
        };
        $lowerBound = function($a, $x) {
            $lo = 0;
            $hi = count($a);
            while ($lo < $hi) {
                $mid = ($lo + $hi) >> 1;
                if ($a[$mid] < $x) $lo = $mid + 1;
                else $hi = $mid;
            }
            return $lo;
        };
        $rank = array_fill(0, count($nums), 0);
        $inv = 0;
        for ($i = 0; $i < count($nums); $i++) {
            $rank[$i] = $lowerBound($vals, $nums[$i]) + 1;
            if ($i < $k) {
                $inv += $i - $sum($rank[$i]);
                $add($rank[$i], 1);
            }
        }
        $best = $inv;
        for ($r = $k; $r < count($nums); $r++) {
            $left = $rank[$r - $k];
            $inv -= $sum($left - 1);
            $add($left, -1);
            $inv += $k - 1 - $sum($rank[$r]);
            $add($rank[$r], 1);
            if ($inv < $best) $best = $inv;
        }
        return $best;
    }
}
''')

add("3769_sort_integers_by_binary_reflection", r'''<?php
// LeetCode 3769 - Sort Integers by Binary Reflection
// https://leetcode.com/problems/sort-integers-by-binary-reflection/

class Solution {
    function sortByReflection($nums) {
        $f = function($x) {
            $y = 0;
            while ($x !== 0) {
                $y = ($y << 1) | ($x & 1);
                $x >>= 1;
            }
            return $y;
        };
        $arr = $nums;
        usort($arr, function($a, $b) use ($f) {
            $fa = $f($a);
            $fb = $f($b);
            if ($fa !== $fb) return $fa <=> $fb;
            return $a <=> $b;
        });
        for ($i = 0; $i < count($nums); $i++) $nums[$i] = $arr[$i];
        return $nums;
    }
}
''')


def main():
    for folder, body in SOLUTIONS.items():
        path = ROOT / folder / "solution.php"
        path.write_text(body, encoding="utf-8", newline="\n")
        print("wrote", folder)
    print("count", len(SOLUTIONS))

if __name__ == "__main__":
    main()
