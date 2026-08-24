#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
SOLUTIONS = {}

def add(folder, body):
    SOLUTIONS[folder] = body


add("2520_count_the_digits_that_divide_a_number", r'''<?php
// LeetCode 2520 - Count the Digits That Divide a Number
// https://leetcode.com/problems/count-the-digits-that-divide-a-number/

class Solution {
    function countDigits($num) {
        $ans = 0;
        $x = $num;
        while ($x > 0) {
            $d = $x % 10;
            if ($d !== 0 && $num % $d === 0) $ans++;
            $x = intdiv($x, 10);
        }
        return $ans;
    }
}
''')

add("2521_distinct_prime_factors_of_product_of_array", r'''<?php
// LeetCode 2521 - Distinct Prime Factors of Product of Array
// https://leetcode.com/problems/distinct-prime-factors-of-product-of-array/

class Solution {
    function distinctPrimeFactors($nums) {
        $set = [];
        foreach ($nums as $num) {
            $x = $num;
            for ($p = 2; $p * $p <= $x; $p++) {
                if ($x % $p === 0) {
                    $set[$p] = true;
                    while ($x % $p === 0) $x = intdiv($x, $p);
                }
            }
            if ($x > 1) $set[$x] = true;
        }
        return count($set);
    }
}
''')

add("2522_partition_string_into_substrings_with_values_at_most_k", r'''<?php
// LeetCode 2522 - Partition String Into Substrings With Values At Most K
// https://leetcode.com/problems/partition-string-into-substrings-with-values-at-most-k/

class Solution {
    function minimumPartition($s, $k) {
        $ans = 1;
        $cur = 0;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $d = ord($s[$i]) - 48;
            if ($d > $k) return -1;
            $nxt = $cur * 10 + $d;
            if ($nxt > $k) {
                $ans++;
                $cur = $d;
            } else {
                $cur = $nxt;
            }
        }
        return $ans;
    }
}
''')

add("2523_closest_prime_numbers_in_range", r'''<?php
// LeetCode 2523 - Closest Prime Numbers in Range
// https://leetcode.com/problems/closest-prime-numbers-in-range/

class Solution {
    function closestPrimes($left, $right) {
        $isPrime = array_fill(0, $right + 1, true);
        if ($right >= 0) $isPrime[0] = false;
        if ($right >= 1) $isPrime[1] = false;
        for ($i = 2; $i * $i <= $right; $i++) {
            if (!$isPrime[$i]) continue;
            for ($j = $i * $i; $j <= $right; $j += $i) $isPrime[$j] = false;
        }
        $primes = [];
        for ($i = $left; $i <= $right; $i++) if ($isPrime[$i]) $primes[] = $i;
        if (count($primes) < 2) return [-1, -1];
        $bestDiff = PHP_INT_MAX;
        $best = [-1, -1];
        $m = count($primes);
        for ($i = 0; $i + 1 < $m; $i++) {
            $d = $primes[$i + 1] - $primes[$i];
            if ($d < $bestDiff) {
                $bestDiff = $d;
                $best = [$primes[$i], $primes[$i + 1]];
            }
        }
        return $best;
    }
}
''')

add("2524_maximum_frequency_score_of_a_subarray", r'''<?php
// LeetCode 2524 - Maximum Frequency Score of a Subarray
// https://leetcode.com/problems/maximum-frequency-score-of-a-subarray/

class Solution {
    function maxFrequencyScore($nums, $k) {
        $MOD = 1000000007;
        $modPow = function($a, $e) use ($MOD) {
            $res = 1;
            $a %= $MOD;
            while ($e > 0) {
                if ($e & 1) $res = $res * $a % $MOD;
                $a = $a * $a % $MOD;
                $e >>= 1;
            }
            return $res;
        };
        $freq = [];
        $add = function($score, $x) use (&$freq, $modPow, $MOD) {
            $c = $freq[$x] ?? 0;
            if ($c > 0) $score = ($score - $modPow($x, $c) + $MOD) % $MOD;
            $freq[$x] = $c + 1;
            return ($score + $modPow($x, $c + 1)) % $MOD;
        };
        $remove = function($score, $x) use (&$freq, $modPow, $MOD) {
            $c = $freq[$x];
            $score = ($score - $modPow($x, $c) + $MOD) % $MOD;
            if ($c === 1) unset($freq[$x]);
            else {
                $freq[$x] = $c - 1;
                $score = ($score + $modPow($x, $c - 1)) % $MOD;
            }
            return $score;
        };
        $score = 0;
        $best = 0;
        $n = count($nums);
        for ($i = 0; $i < $n; $i++) {
            $score = $add($score, $nums[$i]);
            if ($i >= $k) $score = $remove($score, $nums[$i - $k]);
            if ($i >= $k - 1 && $score > $best) $best = $score;
        }
        return $best;
    }
}
''')

add("2525_categorize_box_according_to_criteria", r'''<?php
// LeetCode 2525 - Categorize Box According to Criteria
// https://leetcode.com/problems/categorize-box-according-to-criteria/

class Solution {
    function categorizeBox($length, $width, $height, $mass) {
        $bulky = $length >= 10000 || $width >= 10000 || $height >= 10000 ||
            $length * $width * $height >= 1000000000;
        $heavy = $mass >= 100;
        if ($bulky && $heavy) return "Both";
        if ($bulky) return "Bulky";
        if ($heavy) return "Heavy";
        return "Neither";
    }
}
''')

add("2526_find_consecutive_integers_from_a_data_stream", r'''<?php
// LeetCode 2526 - Find Consecutive Integers from a Data Stream
// https://leetcode.com/problems/find-consecutive-integers-from-a-data-stream/

class DataStream {
    private $value;
    private $k;
    private $streak;

    function __construct($value, $k) {
        $this->value = $value;
        $this->k = $k;
        $this->streak = 0;
    }

    function consec($num) {
        if ($num === $this->value) $this->streak++;
        else $this->streak = 0;
        return $this->streak >= $this->k;
    }
}
''')

add("2527_find_xor_beauty_of_array", r'''<?php
// LeetCode 2527 - Find Xor-Beauty of Array
// https://leetcode.com/problems/find-xor-beauty-of-array/

class Solution {
    function xorBeauty($nums) {
        $ans = 0;
        foreach ($nums as $x) $ans ^= $x;
        return $ans;
    }
}
''')

add("2528_maximize_the_minimum_powered_city", r'''<?php
// LeetCode 2528 - Maximize the Minimum Powered City
// https://leetcode.com/problems/maximize-the-minimum-powered-city/

class Solution {
    function maxPower($stations, $r, $k) {
        $n = count($stations);
        $diff = array_fill(0, $n + 1, 0);
        for ($i = 0; $i < $n; $i++) {
            $L = max(0, $i - $r);
            $R = min($n - 1, $i + $r);
            $diff[$L] += $stations[$i];
            $diff[$R + 1] -= $stations[$i];
        }
        $power = array_fill(0, $n, 0);
        $cur = 0;
        for ($i = 0; $i < $n; $i++) {
            $cur += $diff[$i];
            $power[$i] = $cur;
        }
        $lo = 0;
        $hi = $k;
        foreach ($power as $p) if ($p > $hi) $hi = $p;
        $hi += $k;
        $ok = function($x) use ($n, $r, $k, $power) {
            $extra = array_fill(0, $n + 1, 0);
            $have = 0;
            $used = 0;
            for ($i = 0; $i < $n; $i++) {
                $have += $extra[$i];
                $need = $x - ($power[$i] + $have);
                if ($need > 0) {
                    $used += $need;
                    if ($used > $k) return false;
                    $have += $need;
                    $end = $i + 2 * $r;
                    if ($end + 1 <= $n) $extra[$end + 1] -= $need;
                }
            }
            return true;
        };
        while ($lo < $hi) {
            $mid = intdiv($lo + $hi + 1, 2);
            if ($ok($mid)) $lo = $mid;
            else $hi = $mid - 1;
        }
        return $lo;
    }
}
''')

add("2529_maximum_count_of_positive_integer_and_negative_integer", r'''<?php
// LeetCode 2529 - Maximum Count of Positive Integer and Negative Integer
// https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/

class Solution {
    function maximumCount($nums) {
        $pos = 0;
        $neg = 0;
        foreach ($nums as $x) {
            if ($x > 0) $pos++;
            else if ($x < 0) $neg++;
        }
        return max($pos, $neg);
    }
}
''')

add("2530_maximal_score_after_applying_k_operations", r'''<?php
// LeetCode 2530 - Maximal Score After Applying K Operations
// https://leetcode.com/problems/maximal-score-after-applying-k-operations/

class Solution {
    function maxKelements($nums, $k) {
        $pq = new SplPriorityQueue();
        foreach ($nums as $x) $pq->insert($x, $x);
        $ans = 0;
        for ($i = 0; $i < $k; $i++) {
            $x = $pq->extract();
            $ans += $x;
            $nxt = intdiv($x + 2, 3);
            $pq->insert($nxt, $nxt);
        }
        return $ans;
    }
}
''')

add("2531_make_number_of_distinct_characters_equal", r'''<?php
// LeetCode 2531 - Make Number of Distinct Characters Equal
// https://leetcode.com/problems/make-number-of-distinct-characters-equal/

class Solution {
    function isItPossible($word1, $word2) {
        $c1 = array_fill(0, 26, 0);
        $c2 = array_fill(0, 26, 0);
        $n1 = strlen($word1);
        $n2 = strlen($word2);
        for ($i = 0; $i < $n1; $i++) $c1[ord($word1[$i]) - 97]++;
        for ($i = 0; $i < $n2; $i++) $c2[ord($word2[$i]) - 97]++;
        $d1 = 0;
        $d2 = 0;
        for ($i = 0; $i < 26; $i++) {
            if ($c1[$i] > 0) $d1++;
            if ($c2[$i] > 0) $d2++;
        }
        for ($a = 0; $a < 26; $a++) {
            if ($c1[$a] === 0) continue;
            for ($b = 0; $b < 26; $b++) {
                if ($c2[$b] === 0) continue;
                $nd1 = $d1;
                $nd2 = $d2;
                if ($a === $b) {
                    if ($nd1 === $nd2) return true;
                    continue;
                }
                if ($c1[$a] === 1) $nd1--;
                if ($c1[$b] === 0) $nd1++;
                if ($c2[$b] === 1) $nd2--;
                if ($c2[$a] === 0) $nd2++;
                if ($nd1 === $nd2) return true;
            }
        }
        return false;
    }
}
''')

add("2532_time_to_cross_a_bridge", r'''<?php
// LeetCode 2532 - Time to Cross a Bridge
// https://leetcode.com/problems/time-to-cross-a-bridge/

class _Heap2532 {
    public $a = [];
    public $cmp;
    function __construct($cmp) { $this->cmp = $cmp; }
    function _up($i) {
        $a = &$this->a;
        $cmp = $this->cmp;
        while ($i > 0) {
            $p = ($i - 1) >> 1;
            if ($cmp($a[$i], $a[$p]) >= 0) break;
            $t = $a[$i]; $a[$i] = $a[$p]; $a[$p] = $t;
            $i = $p;
        }
    }
    function _down($i) {
        $a = &$this->a;
        $cmp = $this->cmp;
        $n = count($a);
        while (true) {
            $s = $i;
            $l = $i * 2 + 1;
            $r = $l + 1;
            if ($l < $n && $cmp($a[$l], $a[$s]) < 0) $s = $l;
            if ($r < $n && $cmp($a[$r], $a[$s]) < 0) $s = $r;
            if ($s === $i) break;
            $t = $a[$i]; $a[$i] = $a[$s]; $a[$s] = $t;
            $i = $s;
        }
    }
    function push($x) { $this->a[] = $x; $this->_up(count($this->a) - 1); }
    function pop() {
        $a = &$this->a;
        if (!$a) return null;
        $top = $a[0];
        $last = array_pop($a);
        if ($a) { $a[0] = $last; $this->_down(0); }
        return $top;
    }
    function peek() { return $this->a[0]; }
    function size() { return count($this->a); }
}

class Solution {
    function findCrossingTime($n, $k, $time) {
        $cmpW = function($a, $b) {
            if ($a['efficiency'] !== $b['efficiency']) return $b['efficiency'] - $a['efficiency'];
            return $b['idx'] - $a['idx'];
        };
        $left = new _Heap2532($cmpW);
        $right = new _Heap2532($cmpW);
        $ws = [];
        for ($i = 0; $i < $k; $i++) {
            $t = $time[$i];
            $ws[$i] = [
                'idx' => $i,
                'leftToRight' => $t[0],
                'pickOld' => $t[1],
                'rightToLeft' => $t[2],
                'putNew' => $t[3],
                'efficiency' => $t[0] + $t[2],
            ];
            $left->push($ws[$i]);
        }
        $events = new _Heap2532(function($a, $b) { return $a[0] - $b[0]; });
        $cur = 0;
        $bridgeFree = 0;
        $remain = $n;
        $done = 0;
        while ($done < $n) {
            while ($events->size() && $events->peek()[0] <= $cur) {
                $e = $events->pop();
                $w = $ws[$e[2]];
                if ($e[1] === 0) $left->push($w);
                else $right->push($w);
            }
            if ($cur < $bridgeFree) {
                $cur = $bridgeFree;
                continue;
            }
            if ($right->size()) {
                $w = $right->pop();
                $cur += $w['rightToLeft'];
                $bridgeFree = $cur;
                $events->push([$cur + $w['putNew'], 0, $w['idx']]);
                $done++;
                continue;
            }
            if ($left->size() && $remain > 0) {
                $w = $left->pop();
                $cur += $w['leftToRight'];
                $bridgeFree = $cur;
                $remain--;
                $events->push([$cur + $w['pickOld'], 1, $w['idx']]);
                continue;
            }
            if (!$events->size()) break;
            $cur = $events->peek()[0];
        }
        return $cur;
    }
}
''')

add("2533_number_of_good_binary_strings", r'''<?php
// LeetCode 2533 - Number of Good Binary Strings
// https://leetcode.com/problems/number-of-good-binary-strings/

class Solution {
    function goodBinaryStrings($minLength, $maxLength, $oneGroup, $zeroGroup) {
        $MOD = 1000000007;
        $dp = array_fill(0, $maxLength + 1, 0);
        $dp[0] = 1;
        for ($i = 0; $i <= $maxLength; $i++) {
            if ($dp[$i] === 0) continue;
            if ($i + $oneGroup <= $maxLength) $dp[$i + $oneGroup] = ($dp[$i + $oneGroup] + $dp[$i]) % $MOD;
            if ($i + $zeroGroup <= $maxLength) $dp[$i + $zeroGroup] = ($dp[$i + $zeroGroup] + $dp[$i]) % $MOD;
        }
        $ans = 0;
        for ($i = $minLength; $i <= $maxLength; $i++) $ans = ($ans + $dp[$i]) % $MOD;
        return $ans;
    }
}
''')

add("2534_time_taken_to_cross_the_door", r'''<?php
// LeetCode 2534 - Time Taken to Cross the Door
// https://leetcode.com/problems/time-taken-to-cross-the-door/

class Solution {
    function timeTaken($arrival, $state) {
        $n = count($arrival);
        $ans = array_fill(0, $n, 0);
        $enter = [];
        $exitq = [];
        $i = 0;
        $t = 0;
        $prev = 1;
        while ($i < $n || $enter || $exitq) {
            while ($i < $n && $arrival[$i] <= $t) {
                if ($state[$i] === 0) $enter[] = $i;
                else $exitq[] = $i;
                $i++;
            }
            if (!$enter && !$exitq) {
                if ($i < $n) {
                    $t = $arrival[$i];
                    $prev = 1;
                }
                continue;
            }
            if ($prev === 1) {
                if ($exitq) {
                    $ans[array_shift($exitq)] = $t;
                    $prev = 1;
                } else {
                    $ans[array_shift($enter)] = $t;
                    $prev = 0;
                }
            } else {
                if ($enter) {
                    $ans[array_shift($enter)] = $t;
                    $prev = 0;
                } else {
                    $ans[array_shift($exitq)] = $t;
                    $prev = 1;
                }
            }
            $t++;
        }
        return $ans;
    }
}
''')

add("2535_difference_between_element_sum_and_digit_sum_of_an_array", r'''<?php
// LeetCode 2535 - Difference Between Element Sum and Digit Sum of an Array
// https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array/

class Solution {
    function differenceOfSum($nums) {
        $elem = 0;
        $digit = 0;
        foreach ($nums as $num) {
            $elem += $num;
            $x = $num;
            while ($x > 0) {
                $digit += $x % 10;
                $x = intdiv($x, 10);
            }
        }
        return abs($elem - $digit);
    }
}
''')

add("2536_increment_submatrices_by_one", r'''<?php
// LeetCode 2536 - Increment Submatrices by One
// https://leetcode.com/problems/increment-submatrices-by-one/

class Solution {
    function rangeAddQueries($n, $queries) {
        $diff = [];
        for ($i = 0; $i <= $n; $i++) $diff[] = array_fill(0, $n + 1, 0);
        foreach ($queries as $q) {
            $r1 = $q[0]; $c1 = $q[1]; $r2 = $q[2]; $c2 = $q[3];
            $diff[$r1][$c1]++;
            $diff[$r1][$c2 + 1]--;
            $diff[$r2 + 1][$c1]--;
            $diff[$r2 + 1][$c2 + 1]++;
        }
        $mat = [];
        for ($i = 0; $i < $n; $i++) $mat[] = array_fill(0, $n, 0);
        for ($i = 0; $i < $n; $i++) {
            for ($j = 0; $j < $n; $j++) {
                $v = $diff[$i][$j];
                if ($i > 0) $v += $mat[$i - 1][$j];
                if ($j > 0) $v += $mat[$i][$j - 1];
                if ($i > 0 && $j > 0) $v -= $mat[$i - 1][$j - 1];
                $mat[$i][$j] = $v;
            }
        }
        return $mat;
    }
}
''')

add("2537_count_the_number_of_good_subarrays", r'''<?php
// LeetCode 2537 - Count the Number of Good Subarrays
// https://leetcode.com/problems/count-the-number-of-good-subarrays/

class Solution {
    function countGood($nums, $k) {
        $freq = [];
        $pairs = 0;
        $ans = 0;
        $left = 0;
        $n = count($nums);
        for ($right = 0; $right < $n; $right++) {
            $pairs += $freq[$nums[$right]] ?? 0;
            $freq[$nums[$right]] = ($freq[$nums[$right]] ?? 0) + 1;
            while ($pairs >= $k) {
                $ans += $n - $right;
                $freq[$nums[$left]]--;
                $pairs -= $freq[$nums[$left]];
                $left++;
            }
        }
        return $ans;
    }
}
''')

add("2538_difference_between_maximum_and_minimum_price_sum", r'''<?php
// LeetCode 2538 - Difference Between Maximum and Minimum Price Sum
// https://leetcode.com/problems/difference-between-maximum-and-minimum-price-sum/

class Solution {
    function maxOutput($n, $edges, $price) {
        $g = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $g[$e[0]][] = $e[1];
            $g[$e[1]][] = $e[0];
        }
        $ans = 0;
        $dfs = function($u, $p) use (&$dfs, &$g, $price, &$ans) {
            $maxChild = 0;
            foreach ($g[$u] as $v) {
                if ($v === $p) continue;
                $child = $dfs($v, $u);
                if ($child > $maxChild) $maxChild = $child;
                if ($child > $ans) $ans = $child;
            }
            return $price[$u] + $maxChild;
        };
        $dfs(0, -1);
        return $ans;
    }
}
''')

add("2539_count_the_number_of_good_subsequences", r'''<?php
// LeetCode 2539 - Count the Number of Good Subsequences
// https://leetcode.com/problems/count-the-number-of-good-subsequences/

class Solution {
    function countGoodSubsequences($s) {
        $MOD = 1000000007;
        $cnt = array_fill(0, 26, 0);
        $maxf = 0;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $idx = ord($s[$i]) - 97;
            $cnt[$idx]++;
            if ($cnt[$idx] > $maxf) $maxf = $cnt[$idx];
        }
        $fact = array_fill(0, $maxf + 1, 0);
        $invFact = array_fill(0, $maxf + 1, 0);
        $modPow = function($a, $e) use ($MOD) {
            $res = 1;
            while ($e > 0) {
                if ($e & 1) $res = $res * $a % $MOD;
                $a = $a * $a % $MOD;
                $e >>= 1;
            }
            return $res;
        };
        $fact[0] = 1;
        for ($i = 1; $i <= $maxf; $i++) $fact[$i] = $fact[$i - 1] * $i % $MOD;
        $invFact[$maxf] = $modPow($fact[$maxf], $MOD - 2);
        for ($i = $maxf; $i > 0; $i--) $invFact[$i - 1] = $invFact[$i] * $i % $MOD;
        $comb = function($n, $k) use ($fact, $invFact, $MOD) {
            if ($k < 0 || $k > $n) return 0;
            return $fact[$n] * $invFact[$k] % $MOD * $invFact[$n - $k] % $MOD;
        };
        $ans = 0;
        for ($k = 1; $k <= $maxf; $k++) {
            $ways = 1;
            for ($i = 0; $i < 26; $i++) {
                if ($cnt[$i] >= $k) $ways = $ways * (1 + $comb($cnt[$i], $k)) % $MOD;
            }
            $ans = ($ans + $ways - 1 + $MOD) % $MOD;
        }
        return $ans;
    }
}
''')

add("2540_minimum_common_value", r'''<?php
// LeetCode 2540 - Minimum Common Value
// https://leetcode.com/problems/minimum-common-value/

class Solution {
    function getCommon($nums1, $nums2) {
        $i = 0;
        $j = 0;
        $n1 = count($nums1);
        $n2 = count($nums2);
        while ($i < $n1 && $j < $n2) {
            if ($nums1[$i] === $nums2[$j]) return $nums1[$i];
            if ($nums1[$i] < $nums2[$j]) $i++;
            else $j++;
        }
        return -1;
    }
}
''')

add("2541_minimum_operations_to_make_array_equal_ii", r'''<?php
// LeetCode 2541 - Minimum Operations to Make Array Equal II
// https://leetcode.com/problems/minimum-operations-to-make-array-equal-ii/

class Solution {
    function minOperations($nums1, $nums2, $k) {
        $n = count($nums1);
        if ($k === 0) {
            for ($i = 0; $i < $n; $i++) {
                if ($nums1[$i] !== $nums2[$i]) return -1;
            }
            return 0;
        }
        $pos = 0;
        $neg = 0;
        for ($i = 0; $i < $n; $i++) {
            $d = $nums1[$i] - $nums2[$i];
            if ($d % $k !== 0) return -1;
            if ($d > 0) $pos += intdiv($d, $k);
            else $neg += intdiv(-$d, $k);
        }
        return $pos !== $neg ? -1 : $pos;
    }
}
''')

add("2542_maximum_subsequence_score", r'''<?php
// LeetCode 2542 - Maximum Subsequence Score
// https://leetcode.com/problems/maximum-subsequence-score/

class Solution {
    function maxScore($nums1, $nums2, $k) {
        $n = count($nums1);
        $idx = range(0, $n - 1);
        usort($idx, function($a, $b) use ($nums2) { return $nums2[$b] <=> $nums2[$a]; });
        $pq = new SplPriorityQueue();
        $sum = 0;
        $ans = 0;
        foreach ($idx as $i) {
            $pq->insert($nums1[$i], -$nums1[$i]);
            $sum += $nums1[$i];
            if ($pq->count() > $k) $sum -= $pq->extract();
            if ($pq->count() === $k) {
                $cand = $sum * $nums2[$i];
                if ($cand > $ans) $ans = $cand;
            }
        }
        return $ans;
    }
}
''')

add("2543_check_if_point_is_reachable", r'''<?php
// LeetCode 2543 - Check if Point Is Reachable
// https://leetcode.com/problems/check-if-point-is-reachable/

class Solution {
    function isReachable($targetX, $targetY) {
        $gcd = function($a, $b) {
            while ($b !== 0) {
                $t = $a % $b;
                $a = $b;
                $b = $t;
            }
            return $a;
        };
        $g = $gcd($targetX, $targetY);
        while ($g % 2 === 0) $g = intdiv($g, 2);
        return $g === 1;
    }
}
''')

add("2544_alternating_digit_sum", r'''<?php
// LeetCode 2544 - Alternating Digit Sum
// https://leetcode.com/problems/alternating-digit-sum/

class Solution {
    function alternateDigitSum($n) {
        $digits = [];
        $x = $n;
        while ($x > 0) {
            $digits[] = $x % 10;
            $x = intdiv($x, 10);
        }
        $ans = 0;
        $sign = 1;
        for ($i = count($digits) - 1; $i >= 0; $i--) {
            $ans += $sign * $digits[$i];
            $sign = -$sign;
        }
        return $ans;
    }
}
''')

add("2545_sort_the_students_by_their_kth_score", r'''<?php
// LeetCode 2545 - Sort the Students by Their Kth Score
// https://leetcode.com/problems/sort-the-students-by-their-kth-score/

class Solution {
    function sortTheStudents($score, $k) {
        usort($score, function($a, $b) use ($k) { return $b[$k] <=> $a[$k]; });
        return $score;
    }
}
''')

add("2546_apply_bitwise_operations_to_make_strings_equal", r'''<?php
// LeetCode 2546 - Apply Bitwise Operations to Make Strings Equal
// https://leetcode.com/problems/apply-bitwise-operations-to-make-strings-equal/

class Solution {
    function makeStringsEqual($s, $target) {
        $has1s = false;
        $has1t = false;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            if ($s[$i] === '1') $has1s = true;
            if ($target[$i] === '1') $has1t = true;
        }
        return $has1s === $has1t;
    }
}
''')

add("2547_minimum_cost_to_split_an_array", r'''<?php
// LeetCode 2547 - Minimum Cost to Split an Array
// https://leetcode.com/problems/minimum-cost-to-split-an-array/

class Solution {
    function minCost($nums, $k) {
        $n = count($nums);
        $INF = intdiv(PHP_INT_MAX, 2);
        $dp = array_fill(0, $n + 1, $INF);
        $dp[0] = 0;
        for ($i = 0; $i < $n; $i++) {
            $freq = [];
            $trimmed = 0;
            for ($j = $i; $j < $n; $j++) {
                $c = ($freq[$nums[$j]] ?? 0) + 1;
                $freq[$nums[$j]] = $c;
                if ($c === 2) $trimmed += 2;
                else if ($c > 2) $trimmed++;
                $cost = $dp[$i] + $k + $trimmed;
                if ($cost < $dp[$j + 1]) $dp[$j + 1] = $cost;
            }
        }
        return $dp[$n];
    }
}
''')

add("2548_maximum_price_to_fill_a_bag", r'''<?php
// LeetCode 2548 - Maximum Price to Fill a Bag
// https://leetcode.com/problems/maximum-price-to-fill-a-bag/

class Solution {
    function maxPrice($items, $capacity) {
        usort($items, function($a, $b) {
            return $b[0] / $b[1] <=> $a[0] / $a[1];
        });
        $ans = 0.0;
        $remain = $capacity;
        foreach ($items as $it) {
            $price = $it[0];
            $weight = $it[1];
            if ($remain >= $weight) {
                $ans += $price;
                $remain -= $weight;
            } else {
                $ans += $price * $remain / $weight;
                $remain = 0;
                break;
            }
        }
        if ($remain > 0) return -1;
        return $ans;
    }
}
''')

add("2549_count_distinct_numbers_on_board", r'''<?php
// LeetCode 2549 - Count Distinct Numbers on Board
// https://leetcode.com/problems/count-distinct-numbers-on-board/

class Solution {
    function distinctIntegers($n) {
        if ($n === 1) return 1;
        return $n - 1;
    }
}
''')

add("2550_count_collisions_of_monkeys_on_a_polygon", r'''<?php
// LeetCode 2550 - Count Collisions of Monkeys on a Polygon
// https://leetcode.com/problems/count-collisions-of-monkeys-on-a-polygon/

class Solution {
    function monkeyMove($n) {
        $MOD = 1000000007;
        $powMod = function($a, $e) use ($MOD) {
            $res = 1;
            while ($e > 0) {
                if ($e & 1) $res = $res * $a % $MOD;
                $a = $a * $a % $MOD;
                $e >>= 1;
            }
            return $res;
        };
        return ($powMod(2, $n) - 2 + $MOD) % $MOD;
    }
}
''')

add("2551_put_marbles_in_bags", r'''<?php
// LeetCode 2551 - Put Marbles in Bags
// https://leetcode.com/problems/put-marbles-in-bags/

class Solution {
    function putMarbles($weights, $k) {
        $n = count($weights);
        if ($k === 1 || $k === $n) return 0;
        $pair = [];
        for ($i = 0; $i < $n - 1; $i++) $pair[] = $weights[$i] + $weights[$i + 1];
        sort($pair);
        $mn = 0;
        $mx = 0;
        for ($i = 0; $i < $k - 1; $i++) {
            $mn += $pair[$i];
            $mx += $pair[$n - 2 - $i];
        }
        return $mx - $mn;
    }
}
''')

add("2552_count_increasing_quadruplets", r'''<?php
// LeetCode 2552 - Count Increasing Quadruplets
// https://leetcode.com/problems/count-increasing-quadruplets/

class Solution {
    function countQuadruplets($nums) {
        $n = count($nums);
        $ans = 0;
        $great = array_fill(0, $n, 0);
        for ($j = 0; $j < $n; $j++) {
            for ($i = 0; $i < $j; $i++) {
                if ($nums[$i] < $nums[$j]) $ans += $great[$i];
                else if ($nums[$i] > $nums[$j]) $great[$i]++;
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
