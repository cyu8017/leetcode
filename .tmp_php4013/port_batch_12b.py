#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
SOLUTIONS = {}

def add(folder, body):
    SOLUTIONS[folder] = body


add("2878_get_the_size_of_a_dataframe", r'''<?php
// LeetCode 2878 - Get the Size of a DataFrame
// https://leetcode.com/problems/get-the-size-of-a-dataframe/

class Solution {
    function getDataframeSize($players) {
        if (!$players || count($players) === 0) return [0, 0];
        $rows = count($players);
        $first = $players[0];
        $cols = (is_array($first) && array_keys($first) === range(0, count($first) - 1))
            ? count($first)
            : count((array)$first);
        return [$rows, $cols];
    }
}
''')

add("2879_display_the_first_three_rows", r'''<?php
// LeetCode 2879 - Display the First Three Rows
// https://leetcode.com/problems/display-the-first-three-rows/

class Solution {
    function selectFirstRows($employees) {
        return array_slice($employees, 0, 3);
    }
}
''')

add("2880_select_data", r'''<?php
// LeetCode 2880 - Select Data
// https://leetcode.com/problems/select-data/

class Solution {
    function selectData($students) {
        $out = [];
        foreach ($students as $r) {
            $id = is_array($r) && isset($r[0]) && !isset($r['student_id']) ? $r[0] : ($r['student_id'] ?? null);
            if ($id !== 101) continue;
            if (is_array($r) && isset($r[1]) && !isset($r['name'])) $out[] = ['name' => $r[1], 'age' => $r[2]];
            else $out[] = ['name' => $r['name'], 'age' => $r['age']];
        }
        return $out;
    }
}
''')

add("2881_create_a_new_column", r'''<?php
// LeetCode 2881 - Create a New Column
// https://leetcode.com/problems/create-a-new-column/

class Solution {
    function createBonusColumn($employees) {
        $out = [];
        foreach ($employees as $r) {
            if (is_array($r) && isset($r[0]) && !isset($r['name']) && !isset($r['salary'])) {
                $out[] = ['name' => $r[0], 'salary' => $r[1], 'bonus' => $r[1] * 2];
            } else {
                $row = $r;
                $row['bonus'] = $r['salary'] * 2;
                $out[] = $row;
            }
        }
        return $out;
    }
}
''')

add("2882_drop_duplicate_rows", r'''<?php
// LeetCode 2882 - Drop Duplicate Rows
// https://leetcode.com/problems/drop-duplicate-rows/

class Solution {
    function dropDuplicateEmails($customers) {
        $seen = [];
        $out = [];
        foreach ($customers as $r) {
            $email = (is_array($r) && isset($r[2]) && !isset($r['email'])) ? $r[2] : $r['email'];
            if (isset($seen[$email])) continue;
            $seen[$email] = true;
            $out[] = $r;
        }
        return $out;
    }
}
''')

add("2883_drop_missing_data", r'''<?php
// LeetCode 2883 - Drop Missing Data
// https://leetcode.com/problems/drop-missing-data/

class Solution {
    function dropMissingData($students) {
        $out = [];
        foreach ($students as $r) {
            $name = (is_array($r) && isset($r[1]) && !isset($r['name'])) ? $r[1] : ($r['name'] ?? null);
            if ($name !== null && $name !== '') $out[] = $r;
        }
        return $out;
    }
}
''')

add("2884_modify_columns", r'''<?php
// LeetCode 2884 - Modify Columns
// https://leetcode.com/problems/modify-columns/

class Solution {
    function modifySalaryColumn($employees) {
        $out = [];
        foreach ($employees as $r) {
            if (is_array($r) && isset($r[1]) && !isset($r['salary'])) $out[] = [$r[0], $r[1] * 2];
            else {
                $row = $r;
                $row['salary'] = $r['salary'] * 2;
                $out[] = $row;
            }
        }
        return $out;
    }
}
''')

add("2885_rename_columns", r'''<?php
// LeetCode 2885 - Rename Columns
// https://leetcode.com/problems/rename-columns/

class Solution {
    function renameColumns($students) {
        $out = [];
        foreach ($students as $r) {
            if (is_array($r) && isset($r[0]) && !isset($r['id']) && !isset($r['first'])) {
                $out[] = [
                    'student_id' => $r[0],
                    'first_name' => $r[1],
                    'last_name' => $r[2],
                    'age_in_years' => $r[3],
                ];
            } else {
                $out[] = [
                    'student_id' => $r['id'],
                    'first_name' => $r['first'],
                    'last_name' => $r['last'],
                    'age_in_years' => $r['age'],
                ];
            }
        }
        return $out;
    }
}
''')

add("2886_change_data_type", r'''<?php
// LeetCode 2886 - Change Data Type
// https://leetcode.com/problems/change-data-type/

class Solution {
    function changeDatatype($students) {
        $out = [];
        foreach ($students as $r) {
            if (is_array($r) && isset($r[3]) && !isset($r['grade'])) $out[] = [$r[0], $r[1], $r[2], (int)$r[3]];
            else {
                $row = $r;
                $row['grade'] = (int)$r['grade'];
                $out[] = $row;
            }
        }
        return $out;
    }
}
''')

add("2887_fill_missing_data", r'''<?php
// LeetCode 2887 - Fill Missing Data
// https://leetcode.com/problems/fill-missing-data/

class Solution {
    function fillMissingValues($products) {
        $out = [];
        foreach ($products as $r) {
            if (is_array($r) && isset($r[0]) && !isset($r['quantity'])) {
                $q = $r[1] ?? 0;
                if ($q === null) $q = 0;
                $out[] = [$r[0], $q, $r[2] ?? null];
            } else {
                $row = $r;
                $row['quantity'] = ($r['quantity'] ?? null) === null ? 0 : $r['quantity'];
                $out[] = $row;
            }
        }
        return $out;
    }
}
''')

add("2888_reshape_data_concatenate", r'''<?php
// LeetCode 2888 - Reshape Data: Concatenate
// https://leetcode.com/problems/reshape-data-concatenate/

class Solution {
    function concatenateTables($df1, $df2) {
        return array_merge($df1, $df2);
    }
}
''')

add("2889_reshape_data_pivot", r'''<?php
// LeetCode 2889 - Reshape Data: Pivot
// https://leetcode.com/problems/reshape-data-pivot/

class Solution {
    function pivotTable($weather) {
        $months = [];
        $byMonth = [];
        foreach ($weather as $r) {
            $city = (is_array($r) && isset($r[0]) && !isset($r['city'])) ? $r[0] : $r['city'];
            $month = (is_array($r) && isset($r[1]) && !isset($r['month'])) ? $r[1] : $r['month'];
            $temperature = (is_array($r) && isset($r[2]) && !isset($r['temperature'])) ? $r[2] : $r['temperature'];
            if (!isset($byMonth[$month])) {
                $byMonth[$month] = [];
                $months[] = $month;
            }
            $byMonth[$month][$city] = $temperature;
        }
        $out = [];
        foreach ($months as $month) {
            $row = ['month' => $month];
            foreach ($byMonth[$month] as $city => $temp) $row[$city] = $temp;
            $out[] = $row;
        }
        return $out;
    }
}
''')

add("2890_reshape_data_melt", r'''<?php
// LeetCode 2890 - Reshape Data: Melt
// https://leetcode.com/problems/reshape-data-melt/

class Solution {
    function meltTable($report) {
        $out = [];
        foreach ($report as $r) {
            if (is_array($r) && isset($r[0]) && !isset($r['product'])) {
                $product = $r[0];
                for ($q = 1; $q <= 4; $q++) {
                    $out[] = ['product' => $product, 'quarter' => 'quarter_' . $q, 'sales' => $r[$q]];
                }
            } else {
                foreach (['quarter_1', 'quarter_2', 'quarter_3', 'quarter_4'] as $q) {
                    $out[] = ['product' => $r['product'], 'quarter' => $q, 'sales' => $r[$q]];
                }
            }
        }
        return $out;
    }
}
''')

add("2891_method_chaining", r'''<?php
// LeetCode 2891 - Method Chaining
// https://leetcode.com/problems/method-chaining/

class Solution {
    function findHeavyAnimals($animals) {
        $filtered = [];
        foreach ($animals as $r) {
            $w = (is_array($r) && isset($r[3]) && !isset($r['weight'])) ? $r[3] : $r['weight'];
            if ($w > 100) $filtered[] = $r;
        }
        usort($filtered, function($a, $b) {
            $wa = (is_array($a) && isset($a[3]) && !isset($a['weight'])) ? $a[3] : $a['weight'];
            $wb = (is_array($b) && isset($b[3]) && !isset($b['weight'])) ? $b[3] : $b['weight'];
            return $wb <=> $wa;
        });
        $out = [];
        foreach ($filtered as $r) {
            $name = (is_array($r) && isset($r[0]) && !isset($r['name'])) ? $r[0] : $r['name'];
            $out[] = ['name' => $name];
        }
        return $out;
    }
}
''')

add("2892_minimizing_array_after_replacing_pairs_with_their_product", r'''<?php
// LeetCode 2892 - Minimizing Array After Replacing Pairs With Their Product
// https://leetcode.com/problems/minimizing-array-after-replacing-pairs-with-their-product/

class Solution {
    function minArrayLength($nums, $k) {
        if (count($nums) === 0) return 0;
        $ans = 1;
        $prod = $nums[0];
        $n = count($nums);
        for ($i = 1; $i < $n; $i++) {
            if ($prod <= $k && $nums[$i] <= $k && ($nums[$i] === 0 || $prod <= intdiv($k, $nums[$i]))) {
                $prod *= $nums[$i];
            } else {
                $ans++;
                $prod = $nums[$i];
            }
        }
        return $ans;
    }
}
''')

add("2894_divisible_and_non_divisible_sums_difference", r'''<?php
// LeetCode 2894 - Divisible and Non-divisible Sums Difference
// https://leetcode.com/problems/divisible-and-non-divisible-sums-difference/

class Solution {
    function differenceOfSums($n, $m) {
        $num1 = 0;
        $num2 = 0;
        for ($i = 1; $i <= $n; $i++) {
            if ($i % $m === 0) $num2 += $i;
            else $num1 += $i;
        }
        return $num1 - $num2;
    }
}
''')

add("2895_minimum_processing_time", r'''<?php
// LeetCode 2895 - Minimum Processing Time
// https://leetcode.com/problems/minimum-processing-time/

class Solution {
    function minProcessingTime($processorTime, $tasks) {
        sort($processorTime);
        rsort($tasks);
        $ans = 0;
        $p = count($processorTime);
        for ($i = 0; $i < $p; $i++) {
            $fin = $processorTime[$i] + $tasks[$i * 4];
            if ($fin > $ans) $ans = $fin;
        }
        return $ans;
    }
}
''')

add("2896_apply_operations_to_make_two_strings_equal", r'''<?php
// LeetCode 2896 - Apply Operations to Make Two Strings Equal
// https://leetcode.com/problems/apply-operations-to-make-two-strings-equal/

class Solution {
    function minOperations($s1, $s2, $x) {
        $diff = [];
        $n = strlen($s1);
        for ($i = 0; $i < $n; $i++) if ($s1[$i] !== $s2[$i]) $diff[] = $i;
        $m = count($diff);
        if ($m % 2 === 1) return -1;
        if ($m === 0) return 0;
        $dp = array_fill(0, $m + 1, 0);
        $dp[1] = $x;
        for ($i = 1; $i < $m; $i++) {
            $dp[$i + 1] = min($dp[$i] + $x, $dp[$i - 1] + ($diff[$i] - $diff[$i - 1]) * 2);
        }
        return intdiv($dp[$m], 2);
    }
}
''')

add("2897_apply_operations_on_array_to_maximize_sum_of_squares", r'''<?php
// LeetCode 2897 - Apply Operations on Array to Maximize Sum of Squares
// https://leetcode.com/problems/apply-operations-on-array-to-maximize-sum-of-squares/

class Solution {
    function maxSum($nums, $k) {
        $mod = 1000000007;
        $cnt = array_fill(0, 32, 0);
        foreach ($nums as $v)
            for ($b = 0; $b < 32; $b++)
                if (($v & (1 << $b)) !== 0) $cnt[$b]++;
        $ans = 0;
        for ($i = 0; $i < $k; $i++) {
            $cur = 0;
            for ($b = 0; $b < 32; $b++) {
                if ($cnt[$b] > 0) {
                    $cur |= 1 << $b;
                    $cnt[$b]--;
                }
            }
            $ans = ($ans + (($cur % $mod) * ($cur % $mod)) % $mod) % $mod;
        }
        return $ans;
    }
}
''')

add("2898_maximum_linear_stock_score", r'''<?php
// LeetCode 2898 - Maximum Linear Stock Score
// https://leetcode.com/problems/maximum-linear-stock-score/

class Solution {
    function maxScore($prices) {
        $best = [];
        $ans = 0;
        $n = count($prices);
        for ($i = 0; $i < $n; $i++) {
            $key = $prices[$i] - ($i + 1);
            $cand = ($best[$key] ?? 0) + $prices[$i];
            if ($cand > ($best[$key] ?? 0)) $best[$key] = $cand;
            if ($best[$key] > $ans) $ans = $best[$key];
        }
        return $ans;
    }
}
''')

add("2899_last_visited_integers", r'''<?php
// LeetCode 2899 - Last Visited Integers
// https://leetcode.com/problems/last-visited-integers/

class Solution {
    function lastVisitedIntegers($nums) {
        $seen = [];
        $ans = [];
        $k = 0;
        foreach ($nums as $v) {
            if ($v !== -1) {
                $seen[] = $v;
                $k = 0;
            } else {
                $k++;
                if ($k > count($seen)) $ans[] = -1;
                else $ans[] = $seen[count($seen) - $k];
            }
        }
        return $ans;
    }
}
''')

add("2900_longest_unequal_adjacent_groups_subsequence_i", r'''<?php
// LeetCode 2900 - Longest Unequal Adjacent Groups Subsequence I
// https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-i/

class Solution {
    function getLongestSubsequence($words, $groups) {
        $ans = [$words[0]];
        $last = $groups[0];
        $n = count($words);
        for ($i = 1; $i < $n; $i++) {
            if ($groups[$i] !== $last) {
                $ans[] = $words[$i];
                $last = $groups[$i];
            }
        }
        return $ans;
    }
}
''')

add("2901_longest_unequal_adjacent_groups_subsequence_ii", r'''<?php
// LeetCode 2901 - Longest Unequal Adjacent Groups Subsequence II
// https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-ii/

class Solution {
    function getWordsInLongestSubsequence($words, $groups) {
        $n = count($words);
        $dp = array_fill(0, $n, 1);
        $prev = array_fill(0, $n, -1);
        $best = 1;
        $bestI = 0;
        for ($i = 0; $i < $n; $i++) {
            for ($j = 0; $j < $i; $j++) {
                if ($groups[$i] !== $groups[$j] && $this->hamming($words[$i], $words[$j]) === 1 && $dp[$j] + 1 > $dp[$i]) {
                    $dp[$i] = $dp[$j] + 1;
                    $prev[$i] = $j;
                }
            }
            if ($dp[$i] > $best) {
                $best = $dp[$i];
                $bestI = $i;
            }
        }
        $path = [];
        for ($i = $bestI; $i !== -1; $i = $prev[$i]) $path[] = $words[$i];
        return array_reverse($path);
    }

    private function hamming($a, $b) {
        if (strlen($a) !== strlen($b)) return 100;
        $d = 0;
        $n = strlen($a);
        for ($i = 0; $i < $n; $i++) if ($a[$i] !== $b[$i]) $d++;
        return $d;
    }
}
''')

add("2902_count_of_sub_multisets_with_bounded_sum", r'''<?php
// LeetCode 2902 - Count of Sub-Multisets With Bounded Sum
// https://leetcode.com/problems/count-of-sub-multisets-with-bounded-sum/

class Solution {
    function countSubMultisets($nums, $l, $r) {
        $mod = 1000000007;
        $freq = [];
        $total = 0;
        foreach ($nums as $v) {
            if (!isset($freq[$v])) $freq[$v] = 0;
            $freq[$v]++;
            $total += $v;
        }
        if ($total < $l) return 0;
        if ($r > $total) $r = $total;
        $dp = array_fill(0, $r + 1, 0);
        $dp[0] = 1;
        $zeros = $freq[0] ?? 0;
        unset($freq[0]);
        foreach ($freq as $v => $c) {
            $ndp = array_fill(0, $r + 1, 0);
            for ($sum = 0; $sum <= $r; $sum++) {
                if ($dp[$sum] === 0) continue;
                for ($k = 0; $k <= $c && $sum + $k * $v <= $r; $k++)
                    $ndp[$sum + $k * $v] = ($ndp[$sum + $k * $v] + $dp[$sum]) % $mod;
            }
            $dp = $ndp;
        }
        $ans = 0;
        for ($s = $l; $s <= $r; $s++) $ans = ($ans + $dp[$s]) % $mod;
        $ans = ($ans * ($zeros + 1)) % $mod;
        return (int)$ans;
    }
}
''')

add("2903_find_indices_with_index_and_value_difference_i", r'''<?php
// LeetCode 2903 - Find Indices With Index and Value Difference I
// https://leetcode.com/problems/find-indices-with-index-and-value-difference-i/

class Solution {
    function findIndices($nums, $indexDifference, $valueDifference) {
        $n = count($nums);
        for ($i = 0; $i < $n; $i++)
            for ($j = $i; $j < $n; $j++) {
                if (abs($j - $i) >= $indexDifference && abs($nums[$i] - $nums[$j]) >= $valueDifference)
                    return [$i, $j];
            }
        return [-1, -1];
    }
}
''')

add("2904_shortest_and_lexicographically_smallest_beautiful_string", r'''<?php
// LeetCode 2904 - Shortest and Lexicographically Smallest Beautiful String
// https://leetcode.com/problems/shortest-and-lexicographically-smallest-beautiful-string/

class Solution {
    function shortestBeautifulSubstring($s, $k) {
        $ans = '';
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $ones = 0;
            for ($j = $i; $j < $n; $j++) {
                if ($s[$j] === '1') $ones++;
                if ($ones === $k) {
                    $cand = substr($s, $i, $j - $i + 1);
                    if ($ans === '' || strlen($cand) < strlen($ans) || (strlen($cand) === strlen($ans) && $cand < $ans))
                        $ans = $cand;
                    break;
                }
                if ($ones > $k) break;
            }
        }
        return $ans;
    }
}
''')

add("2905_find_indices_with_index_and_value_difference_ii", r'''<?php
// LeetCode 2905 - Find Indices With Index and Value Difference II
// https://leetcode.com/problems/find-indices-with-index-and-value-difference-ii/

class Solution {
    function findIndices($nums, $indexDifference, $valueDifference) {
        $n = count($nums);
        $minIdx = 0;
        $maxIdx = 0;
        for ($j = $indexDifference; $j < $n; $j++) {
            $i = $j - $indexDifference;
            if ($nums[$i] < $nums[$minIdx]) $minIdx = $i;
            if ($nums[$i] > $nums[$maxIdx]) $maxIdx = $i;
            if ($nums[$j] - $nums[$minIdx] >= $valueDifference) return [$minIdx, $j];
            if ($nums[$maxIdx] - $nums[$j] >= $valueDifference) return [$maxIdx, $j];
        }
        return [-1, -1];
    }
}
''')

add("2906_construct_product_matrix", r'''<?php
// LeetCode 2906 - Construct Product Matrix
// https://leetcode.com/problems/construct-product-matrix/

class Solution {
    function constructProductMatrix($grid) {
        $mod = 12345;
        $m = count($grid);
        $n = count($grid[0]);
        $ans = [];
        for ($i = 0; $i < $m; $i++) $ans[$i] = array_fill(0, $n, 0);
        $pref = 1;
        for ($i = 0; $i < $m; $i++)
            for ($j = 0; $j < $n; $j++) {
                $ans[$i][$j] = $pref;
                $pref = ($pref * ($grid[$i][$j] % $mod)) % $mod;
            }
        $suf = 1;
        for ($i = $m - 1; $i >= 0; $i--)
            for ($j = $n - 1; $j >= 0; $j--) {
                $ans[$i][$j] = ($ans[$i][$j] * $suf) % $mod;
                $suf = ($suf * ($grid[$i][$j] % $mod)) % $mod;
            }
        return $ans;
    }
}
''')

add("2907_maximum_profitable_triplets_with_increasing_prices_i", r'''<?php
// LeetCode 2907 - Maximum Profitable Triplets With Increasing Prices I
// https://leetcode.com/problems/maximum-profitable-triplets-with-increasing-prices-i/

class Solution {
    function maxProfit($prices, $profits) {
        $n = count($prices);
        $ans = -1;
        for ($j = 0; $j < $n; $j++) {
            $bestL = -1;
            $bestR = -1;
            for ($i = 0; $i < $j; $i++)
                if ($prices[$i] < $prices[$j] && $profits[$i] > $bestL) $bestL = $profits[$i];
            for ($k = $j + 1; $k < $n; $k++)
                if ($prices[$k] > $prices[$j] && $profits[$k] > $bestR) $bestR = $profits[$k];
            if ($bestL >= 0 && $bestR >= 0) {
                $cand = $bestL + $profits[$j] + $bestR;
                if ($cand > $ans) $ans = $cand;
            }
        }
        return $ans;
    }
}
''')

add("2908_minimum_sum_of_mountain_triplets_i", r'''<?php
// LeetCode 2908 - Minimum Sum of Mountain Triplets I
// https://leetcode.com/problems/minimum-sum-of-mountain-triplets-i/

class Solution {
    function minimumSum($nums) {
        $n = count($nums);
        $INF = 1 << 30;
        $ans = $INF;
        for ($j = 1; $j < $n - 1; $j++) {
            $left = $INF;
            $right = $INF;
            for ($i = 0; $i < $j; $i++)
                if ($nums[$i] < $nums[$j] && $nums[$i] < $left) $left = $nums[$i];
            for ($k = $j + 1; $k < $n; $k++)
                if ($nums[$k] < $nums[$j] && $nums[$k] < $right) $right = $nums[$k];
            if ($left < $INF && $right < $INF) {
                $cand = $left + $nums[$j] + $right;
                if ($cand < $ans) $ans = $cand;
            }
        }
        return $ans === $INF ? -1 : $ans;
    }
}
''')

add("2909_minimum_sum_of_mountain_triplets_ii", r'''<?php
// LeetCode 2909 - Minimum Sum of Mountain Triplets II
// https://leetcode.com/problems/minimum-sum-of-mountain-triplets-ii/

class Solution {
    function minimumSum($nums) {
        $n = count($nums);
        $INF = 1 << 30;
        $left = array_fill(0, $n, 0);
        $right = array_fill(0, $n, 0);
        $mn = $INF;
        for ($i = 0; $i < $n; $i++) {
            $left[$i] = $mn;
            if ($nums[$i] < $mn) $mn = $nums[$i];
        }
        $mn = $INF;
        for ($i = $n - 1; $i >= 0; $i--) {
            $right[$i] = $mn;
            if ($nums[$i] < $mn) $mn = $nums[$i];
        }
        $ans = $INF;
        for ($j = 1; $j < $n - 1; $j++) {
            if ($left[$j] < $nums[$j] && $right[$j] < $nums[$j]) {
                $cand = $left[$j] + $nums[$j] + $right[$j];
                if ($cand < $ans) $ans = $cand;
            }
        }
        return $ans === $INF ? -1 : $ans;
    }
}
''')

add("2910_minimum_number_of_groups_to_create_a_valid_assignment", r'''<?php
// LeetCode 2910 - Minimum Number of Groups to Create a Valid Assignment
// https://leetcode.com/problems/minimum-number-of-groups-to-create-a-valid-assignment/

class Solution {
    function minGroupsForValidAssignment($balls) {
        $freq = [];
        foreach ($balls as $b) {
            if (!isset($freq[$b])) $freq[$b] = 0;
            $freq[$b]++;
        }
        $counts = array_values($freq);
        $minF = min($counts);
        for ($size = $minF; $size >= 1; $size--) {
            $ok = true;
            $groups = 0;
            foreach ($counts as $c) {
                $rem = $c % ($size + 1);
                $g2 = intdiv($c, $size + 1);
                if ($rem === 0) $groups += $g2;
                else if ($size - $rem <= $g2) $groups += $g2 + 1;
                else { $ok = false; break; }
            }
            if ($ok) return $groups;
        }
        return count($balls);
    }
}
''')

add("2911_minimum_changes_to_make_k_semi_palindromes", r'''<?php
// LeetCode 2911 - Minimum Changes to Make K Semi-palindromes
// https://leetcode.com/problems/minimum-changes-to-make-k-semi-palindromes/

class Solution {
    function minimumChanges($s, $k) {
        $n = strlen($s);
        $INF = 1 << 20;
        $cost = [];
        for ($i = 0; $i < $n; $i++) $cost[$i] = array_fill(0, $n, $INF);
        for ($i = 0; $i < $n; $i++)
            for ($j = $i + 1; $j < $n; $j++)
                $cost[$i][$j] = $this->semiCost($s, $i, $j, $INF);
        $dp = [];
        for ($p = 0; $p <= $k; $p++) $dp[$p] = array_fill(0, $n + 1, $INF);
        $dp[0][0] = 0;
        for ($p = 1; $p <= $k; $p++)
            for ($i = 1; $i <= $n; $i++)
                for ($t = 0; $t < $i - 1; $t++) {
                    $cand = $dp[$p - 1][$t] + $cost[$t][$i - 1];
                    if ($cand < $dp[$p][$i]) $dp[$p][$i] = $cand;
                }
        return $dp[$k][$n];
    }

    private function semiCost($s, $l, $r, $INF) {
        $length = $r - $l + 1;
        $best = $INF;
        for ($d = 1; $d < $length; $d++) {
            if ($length % $d !== 0) continue;
            $chg = 0;
            for ($start = 0; $start < $d; $start++) {
                $chars = [];
                for ($i = $l + $start; $i <= $r; $i += $d) $chars[] = $s[$i];
                $i = 0;
                $j = count($chars) - 1;
                while ($i < $j) {
                    if ($chars[$i] !== $chars[$j]) $chg++;
                    $i++;
                    $j--;
                }
            }
            if ($chg < $best) $best = $chg;
        }
        return $best;
    }
}
''')

add("2912_number_of_ways_to_reach_destination_in_the_grid", r'''<?php
// LeetCode 2912 - Number of Ways to Reach Destination in the Grid
// https://leetcode.com/problems/number-of-ways-to-reach-destination-in-the-grid/

class Solution {
    function numberOfWays($n, $m, $k, $source, $dest) {
        $mod = 1000000007;
        $sx = $source[0];
        $sy = $source[1];
        $tx = $dest[0];
        $ty = $dest[1];
        $same = 0;
        $row = 0;
        $col = 0;
        $other = 0;
        if ($sx === $tx && $sy === $ty) $same = 1;
        else if ($sx === $tx) $row = 1;
        else if ($sy === $ty) $col = 1;
        else $other = 1;
        for ($step = 0; $step < $k; $step++) {
            $ns = ($row * ($m - 1) + $col * ($n - 1)) % $mod;
            $nr = ($same + ($row * ($m - 2)) % $mod + ($other * ($n - 1)) % $mod) % $mod;
            $nc = ($same + ($col * ($n - 2)) % $mod + ($other * ($m - 1)) % $mod) % $mod;
            $no = ($row * ($n - 1) + $col * ($m - 1) + ($other * ($n + $m - 4)) % $mod) % $mod;
            $same = $ns;
            $row = $nr;
            $col = $nc;
            $other = $no;
        }
        if ($sx === $tx && $sy === $ty) return $same;
        if ($sx === $tx) return $row;
        if ($sy === $ty) return $col;
        return $other;
    }
}
''')

add("2913_subarrays_distinct_element_sum_of_squares_i", r'''<?php
// LeetCode 2913 - Subarrays Distinct Element Sum of Squares I
// https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-i/

class Solution {
    function sumCounts($nums) {
        $n = count($nums);
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            $seen = [];
            for ($j = $i; $j < $n; $j++) {
                $seen[$nums[$j]] = true;
                $d = count($seen);
                $ans += $d * $d;
            }
        }
        return $ans;
    }
}
''')

add("2914_minimum_number_of_changes_to_make_binary_string_beautiful", r'''<?php
// LeetCode 2914 - Minimum Number of Changes to Make Binary String Beautiful
// https://leetcode.com/problems/minimum-number-of-changes-to-make-binary-string-beautiful/

class Solution {
    function minChanges($s) {
        $ans = 0;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i += 2)
            if ($s[$i] !== $s[$i + 1]) $ans++;
        return $ans;
    }
}
''')

add("2915_length_of_the_longest_subsequence_that_sums_to_target", r'''<?php
// LeetCode 2915 - Length of the Longest Subsequence That Sums to Target
// https://leetcode.com/problems/length-of-the-longest-subsequence-that-sums-to-target/

class Solution {
    function lengthOfLongestSubsequence($nums, $target) {
        $dp = array_fill(0, $target + 1, -1);
        $dp[0] = 0;
        foreach ($nums as $v)
            for ($s = $target; $s >= $v; $s--)
                if ($dp[$s - $v] >= 0 && $dp[$s - $v] + 1 > $dp[$s]) $dp[$s] = $dp[$s - $v] + 1;
        return $dp[$target];
    }
}
''')

add("2916_subarrays_distinct_element_sum_of_squares_ii", r'''<?php
// LeetCode 2916 - Subarrays Distinct Element Sum of Squares II
// https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-ii/

class Solution {
    private $MOD = 1000000007;
    private $tree;

    function sumCounts($nums) {
        $n = count($nums);
        $this->tree = [];
        for ($i = 0; $i < 4 * ($n + 2); $i++) $this->tree[$i] = ['sum' => 0, 'sumSq' => 0, 'lazy' => 0];
        $last = [];
        $ans = 0;
        for ($i = 1; $i <= $n; $i++) {
            $v = $nums[$i - 1];
            $prev = $last[$v] ?? 0;
            $this->update(1, 1, $n, $prev + 1, $i, 1);
            $ans = ($ans + $this->tree[1]['sumSq']) % $this->MOD;
            $last[$v] = $i;
        }
        return $ans;
    }

    private function apply($idx, $l, $r, $val) {
        $length = $r - $l + 1;
        $this->tree[$idx]['sumSq'] = ($this->tree[$idx]['sumSq'] + 2 * $val % $this->MOD * $this->tree[$idx]['sum'] % $this->MOD
            + $val % $this->MOD * $val % $this->MOD * $length % $this->MOD) % $this->MOD;
        $this->tree[$idx]['sum'] = ($this->tree[$idx]['sum'] + $val % $this->MOD * $length % $this->MOD) % $this->MOD;
        $this->tree[$idx]['lazy'] = ($this->tree[$idx]['lazy'] + $val) % $this->MOD;
    }

    private function update($idx, $l, $r, $ql, $qr, $val) {
        if ($ql > $r || $qr < $l) return;
        if ($ql <= $l && $r <= $qr) {
            $this->apply($idx, $l, $r, $val);
            return;
        }
        if ($this->tree[$idx]['lazy'] !== 0 && $l !== $r) {
            $mid = intdiv($l + $r, 2);
            $this->apply($idx * 2, $l, $mid, $this->tree[$idx]['lazy']);
            $this->apply($idx * 2 + 1, $mid + 1, $r, $this->tree[$idx]['lazy']);
            $this->tree[$idx]['lazy'] = 0;
        }
        $mid = intdiv($l + $r, 2);
        $this->update($idx * 2, $l, $mid, $ql, $qr, $val);
        $this->update($idx * 2 + 1, $mid + 1, $r, $ql, $qr, $val);
        $this->tree[$idx]['sum'] = ($this->tree[$idx * 2]['sum'] + $this->tree[$idx * 2 + 1]['sum']) % $this->MOD;
        $this->tree[$idx]['sumSq'] = ($this->tree[$idx * 2]['sumSq'] + $this->tree[$idx * 2 + 1]['sumSq']) % $this->MOD;
    }
}
''')

add("2917_find_the_k_or_of_an_array", r'''<?php
// LeetCode 2917 - Find the K-or of an Array
// https://leetcode.com/problems/find-the-k-or-of-an-array/

class Solution {
    function findKOr($nums, $k) {
        $ans = 0;
        for ($b = 0; $b < 31; $b++) {
            $cnt = 0;
            foreach ($nums as $v) if (($v & (1 << $b)) !== 0) $cnt++;
            if ($cnt >= $k) $ans |= 1 << $b;
        }
        return $ans;
    }
}
''')

add("2918_minimum_equal_sum_of_two_arrays_after_replacing_zeros", r'''<?php
// LeetCode 2918 - Minimum Equal Sum of Two Arrays After Replacing Zeros
// https://leetcode.com/problems/minimum-equal-sum-of-two-arrays-after-replacing-zeros/

class Solution {
    function minSum($nums1, $nums2) {
        $s1 = 0;
        $s2 = 0;
        $z1 = 0;
        $z2 = 0;
        foreach ($nums1 as $v) {
            if ($v === 0) { $z1++; $s1++; }
            else $s1 += $v;
        }
        foreach ($nums2 as $v) {
            if ($v === 0) { $z2++; $s2++; }
            else $s2 += $v;
        }
        if ($z1 === 0 && $s1 < $s2) return -1;
        if ($z2 === 0 && $s2 < $s1) return -1;
        return $s1 > $s2 ? $s1 : $s2;
    }
}
''')

add("2919_minimum_increment_operations_to_make_array_beautiful", r'''<?php
// LeetCode 2919 - Minimum Increment Operations to Make Array Beautiful
// https://leetcode.com/problems/minimum-increment-operations-to-make-array-beautiful/

class Solution {
    function minIncrementOperations($nums, $k) {
        $dp0 = 0;
        $dp1 = 0;
        $dp2 = 0;
        foreach ($nums as $v) {
            $cost = $v < $k ? $k - $v : 0;
            $nd0 = $cost + min($dp0, $dp1, $dp2);
            $dp0 = $dp1;
            $dp1 = $dp2;
            $dp2 = $nd0;
        }
        return min($dp0, $dp1, $dp2);
    }
}
''')

add("2920_maximum_points_after_collecting_coins_from_all_nodes", r'''<?php
// LeetCode 2920 - Maximum Points After Collecting Coins From All Nodes
// https://leetcode.com/problems/maximum-points-after-collecting-coins-from-all-nodes/

class Solution {
    function maximumPoints($edges, $coins, $k) {
        $n = count($coins);
        $g = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $g[$e[0]][] = $e[1];
            $g[$e[1]][] = $e[0];
        }
        $memo = [];
        $dfs = function($u, $p, $shifts) use (&$dfs, &$g, &$coins, $k, &$memo) {
            if ($shifts > 14) $shifts = 14;
            $key = ($u << 5) | $shifts;
            if (isset($memo[$key])) return $memo[$key];
            $c = $coins[$u] >> $shifts;
            $opt1 = $c - $k;
            $opt2 = intdiv($c, 2);
            foreach ($g[$u] as $v) {
                if ($v === $p) continue;
                $opt1 += $dfs($v, $u, $shifts);
                $opt2 += $dfs($v, $u, $shifts + 1);
            }
            $best = max($opt1, $opt2);
            $memo[$key] = $best;
            return $best;
        };
        return $dfs(0, -1, 0);
    }
}
''')

add("2921_maximum_profitable_triplets_with_increasing_prices_ii", r'''<?php
// LeetCode 2921 - Maximum Profitable Triplets With Increasing Prices II
// https://leetcode.com/problems/maximum-profitable-triplets-with-increasing-prices-ii/

class Solution {
    function maxProfit($prices, $profits) {
        $n = count($prices);
        $ans = -1;
        $uniq = array_values(array_unique($prices));
        sort($uniq);
        $m = count($uniq);
        $bit = array_fill(0, $m + 2, -1);
        $idxOf = function($v) use ($uniq, $m) {
            $lo = 0;
            $hi = $m;
            while ($lo < $hi) {
                $mid = intdiv($lo + $hi, 2);
                if ($uniq[$mid] < $v) $lo = $mid + 1;
                else $hi = $mid;
            }
            return $lo + 1;
        };
        $update = function($i, $val) use (&$bit) {
            $len = count($bit);
            for (; $i < $len; $i += $i & -$i)
                if ($val > $bit[$i]) $bit[$i] = $val;
        };
        $query = function($i) use (&$bit) {
            $best = -1;
            for (; $i > 0; $i -= $i & -$i)
                if ($bit[$i] > $best) $best = $bit[$i];
            return $best;
        };
        $maxLeft = array_fill(0, $n, -1);
        for ($j = 0; $j < $n; $j++) {
            $id = $idxOf($prices[$j]);
            $maxLeft[$j] = $query($id - 1);
            $update($id, $profits[$j]);
        }
        for ($j = 0; $j < $n; $j++) {
            $bestR = -1;
            for ($k = $j + 1; $k < $n; $k++)
                if ($prices[$k] > $prices[$j] && $profits[$k] > $bestR) $bestR = $profits[$k];
            if ($maxLeft[$j] >= 0 && $bestR >= 0) {
                $cand = $maxLeft[$j] + $profits[$j] + $bestR;
                if ($cand > $ans) $ans = $cand;
            }
        }
        return $ans;
    }
}
''')

add("2923_find_champion_i", r'''<?php
// LeetCode 2923 - Find Champion I
// https://leetcode.com/problems/find-champion-i/

class Solution {
    function findChampion($grid) {
        $n = count($grid);
        for ($i = 0; $i < $n; $i++) {
            $win = true;
            for ($j = 0; $j < $n; $j++)
                if ($i !== $j && $grid[$i][$j] === 0) { $win = false; break; }
            if ($win) return $i;
        }
        return -1;
    }
}
''')

add("2924_find_champion_ii", r'''<?php
// LeetCode 2924 - Find Champion II
// https://leetcode.com/problems/find-champion-ii/

class Solution {
    function findChampion($n, $edges) {
        $indeg = array_fill(0, $n, 0);
        foreach ($edges as $e) $indeg[$e[1]]++;
        $ans = -1;
        for ($i = 0; $i < $n; $i++) {
            if ($indeg[$i] === 0) {
                if ($ans !== -1) return -1;
                $ans = $i;
            }
        }
        return $ans;
    }
}
''')

add("2925_maximum_score_after_applying_operations_on_a_tree", r'''<?php
// LeetCode 2925 - Maximum Score After Applying Operations on a Tree
// https://leetcode.com/problems/maximum-score-after-applying-operations-on-a-tree/

class Solution {
    function maximumScoreAfterOperations($edges, $values) {
        $n = count($values);
        $g = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $g[$e[0]][] = $e[1];
            $g[$e[1]][] = $e[0];
        }
        $total = 0;
        foreach ($values as $v) $total += $v;
        $dfs = function($u, $p) use (&$dfs, &$g, &$values) {
            $sumKids = 0;
            $isLeaf = true;
            foreach ($g[$u] as $v) {
                if ($v === $p) continue;
                $isLeaf = false;
                $sumKids += $dfs($v, $u);
            }
            if ($isLeaf) return $values[$u];
            return $values[$u] < $sumKids ? $values[$u] : $sumKids;
        };
        return $total - $dfs(0, -1);
    }
}
''')

add("2926_maximum_balanced_subsequence_sum", r'''<?php
// LeetCode 2926 - Maximum Balanced Subsequence Sum
// https://leetcode.com/problems/maximum-balanced-subsequence-sum/

class Solution {
    function maxBalancedSubsequenceSum($nums) {
        $NEG = -4000000000000000000;
        $n = count($nums);
        $keys = [];
        for ($i = 0; $i < $n; $i++) $keys[] = $nums[$i] - $i;
        $uniq = array_values(array_unique($keys));
        sort($uniq);
        $bit = array_fill(0, count($uniq) + 2, $NEG);
        $idxOf = function($v) use ($uniq) {
            $lo = 0;
            $hi = count($uniq);
            while ($lo < $hi) {
                $mid = intdiv($lo + $hi, 2);
                if ($uniq[$mid] < $v) $lo = $mid + 1;
                else $hi = $mid;
            }
            return $lo + 1;
        };
        $update = function($i, $val) use (&$bit) {
            $len = count($bit);
            for (; $i < $len; $i += $i & -$i)
                if ($val > $bit[$i]) $bit[$i] = $val;
        };
        $query = function($i) use (&$bit, $NEG) {
            $best = $NEG;
            for (; $i > 0; $i -= $i & -$i)
                if ($bit[$i] > $best) $best = $bit[$i];
            return $best;
        };
        $ans = $NEG;
        for ($i = 0; $i < $n; $i++) {
            $id = $idxOf($keys[$i]);
            $best = $query($id);
            $cur = $nums[$i];
            if ($best > $NEG / 2) {
                $cand = $best + $nums[$i];
                if ($cand > $cur) $cur = $cand;
            }
            $update($id, $cur);
            if ($cur > $ans) $ans = $cur;
        }
        return $ans;
    }
}
''')

add("2927_distribute_candies_among_children_iii", r'''<?php
// LeetCode 2927 - Distribute Candies Among Children III
// https://leetcode.com/problems/distribute-candies-among-children-iii/

class Solution {
    function distributeCandies($n, $limit) {
        $comb = function($x) {
            if ($x < 2) return 0;
            return $x * ($x - 1) / 2;
        };
        $ans = $comb($n + 2);
        $ans -= 3 * $comb($n - $limit + 1);
        $ans += 3 * $comb($n - 2 * ($limit + 1) + 2);
        $ans -= $comb($n - 3 * ($limit + 1) + 2);
        if ($ans < 0) $ans = 0;
        return (int)$ans;
    }
}
''')

add("2928_distribute_candies_among_children_i", r'''<?php
// LeetCode 2928 - Distribute Candies Among Children I
// https://leetcode.com/problems/distribute-candies-among-children-i/

class Solution {
    function distributeCandies($n, $limit) {
        $ans = 0;
        for ($i = 0; $i <= $limit; $i++)
            for ($j = 0; $j <= $limit; $j++) {
                $k = $n - $i - $j;
                if ($k >= 0 && $k <= $limit) $ans++;
            }
        return $ans;
    }
}
''')

add("2929_distribute_candies_among_children_ii", r'''<?php
// LeetCode 2929 - Distribute Candies Among Children II
// https://leetcode.com/problems/distribute-candies-among-children-ii/

class Solution {
    function distributeCandies($n, $limit) {
        $comb2 = function($x) {
            if ($x < 0) return 0;
            return ($x + 1) * ($x + 2) / 2;
        };
        $ans = $comb2($n);
        $ans -= 3 * $comb2($n - ($limit + 1));
        $ans += 3 * $comb2($n - 2 * ($limit + 1));
        $ans -= $comb2($n - 3 * ($limit + 1));
        return (int)$ans;
    }
}
''')

add("2930_number_of_strings_which_can_be_rearranged_to_contain_substring", r'''<?php
// LeetCode 2930 - Number of Strings Which Can Be Rearranged to Contain Substring
// https://leetcode.com/problems/number-of-strings-which-can-be-rearranged-to-contain-substring/

class Solution {
    private $MOD = 1000000007;

    function stringCount($n) {
        if ($n < 4) return 0;
        $ans = $this->modPow(26, $n);
        $ans = ($ans - 3 * $this->modPow(25, $n) % $this->MOD + $this->MOD) % $this->MOD;
        $ans = ($ans + 3 * $this->modPow(24, $n) % $this->MOD) % $this->MOD;
        $ans = ($ans - $this->modPow(23, $n) + $this->MOD) % $this->MOD;
        $ans = ($ans + $n % $this->MOD * $this->modPow(25, $n - 1) % $this->MOD) % $this->MOD;
        $ans = ($ans - 2 * ($n % $this->MOD) % $this->MOD * $this->modPow(24, $n - 1) % $this->MOD + $this->MOD) % $this->MOD;
        $ans = ($ans + $n % $this->MOD * $this->modPow(23, $n - 1) % $this->MOD) % $this->MOD;
        $ans = ($ans - $n % $this->MOD * (($n - 1 + $this->MOD) % $this->MOD) % $this->MOD * $this->modPow(24, $n - 2) % $this->MOD % $this->MOD + $this->MOD) % $this->MOD;
        $ans = ($ans + $n % $this->MOD * (($n - 1 + $this->MOD) % $this->MOD) % $this->MOD * $this->modPow(23, $n - 2) % $this->MOD) % $this->MOD;
        return (int)$ans;
    }

    private function modPow($a, $b) {
        $res = 1;
        $a %= $this->MOD;
        while ($b > 0) {
            if ($b % 2 === 1) $res = ($res * $a) % $this->MOD;
            $a = ($a * $a) % $this->MOD;
            $b = intdiv($b, 2);
        }
        return $res;
    }
}
''')

add("2931_maximum_spending_after_buying_items", r'''<?php
// LeetCode 2931 - Maximum Spending After Buying Items
// https://leetcode.com/problems/maximum-spending-after-buying-items/

class Solution {
    function maxSpending($values) {
        $m = count($values);
        $n = count($values[0]);
        $idx = array_fill(0, $m, $n - 1);
        $ans = 0;
        $day = 1;
        $total = $m * $n;
        for ($t = 0; $t < $total; $t++) {
            $bestI = -1;
            $bestV = PHP_INT_MAX;
            for ($i = 0; $i < $m; $i++) {
                if ($idx[$i] >= 0 && $values[$i][$idx[$i]] < $bestV) {
                    $bestV = $values[$i][$idx[$i]];
                    $bestI = $i;
                }
            }
            $ans += $bestV * $day;
            $idx[$bestI]--;
            $day++;
        }
        return $ans;
    }
}
''')

add("2932_maximum_strong_pair_xor_i", r'''<?php
// LeetCode 2932 - Maximum Strong Pair XOR I
// https://leetcode.com/problems/maximum-strong-pair-xor-i/

class Solution {
    function maximumStrongPairXor($nums) {
        $ans = 0;
        $n = count($nums);
        for ($i = 0; $i < $n; $i++)
            for ($j = $i; $j < $n; $j++) {
                $x = $nums[$i];
                $y = $nums[$j];
                if (abs($x - $y) <= min($x, $y)) {
                    $xorr = $x ^ $y;
                    if ($xorr > $ans) $ans = $xorr;
                }
            }
        return $ans;
    }
}
''')

add("2933_high_access_employees", r'''<?php
// LeetCode 2933 - High-Access Employees
// https://leetcode.com/problems/high-access-employees/

class Solution {
    function findHighAccessEmployees($access_times) {
        $m = [];
        foreach ($access_times as $at) {
            $name = $at[0];
            $t = $at[1];
            $hh = (ord($t[0]) - 48) * 10 + (ord($t[1]) - 48);
            $mm = (ord($t[2]) - 48) * 10 + (ord($t[3]) - 48);
            if (!isset($m[$name])) $m[$name] = [];
            $m[$name][] = $hh * 60 + $mm;
        }
        $ans = [];
        foreach ($m as $name => $times) {
            sort($times);
            $len = count($times);
            for ($i = 0; $i + 2 < $len; $i++) {
                if ($times[$i + 2] - $times[$i] < 60) {
                    $ans[] = $name;
                    break;
                }
            }
        }
        sort($ans);
        return $ans;
    }
}
''')

add("2934_minimum_operations_to_maximize_last_elements_in_arrays", r'''<?php
// LeetCode 2934 - Minimum Operations to Maximize Last Elements in Arrays
// https://leetcode.com/problems/minimum-operations-to-maximize-last-elements-in-arrays/

class Solution {
    function minOperations($nums1, $nums2) {
        $n = count($nums1);
        $ans = $this->calc($nums1, $nums2);
        $t = $nums1[$n - 1];
        $nums1[$n - 1] = $nums2[$n - 1];
        $nums2[$n - 1] = $t;
        $cand = $this->calc($nums1, $nums2) + 1;
        if ($cand < $ans) $ans = $cand;
        $nums2[$n - 1] = $nums1[$n - 1];
        $nums1[$n - 1] = $t;
        return $ans >= (1 << 30) ? -1 : $ans;
    }

    private function calc($a1, $a2) {
        $n = count($a1);
        $ops = 0;
        $last1 = $a1[$n - 1];
        $last2 = $a2[$n - 1];
        for ($i = 0; $i < $n - 1; $i++) {
            $x = $a1[$i];
            $y = $a2[$i];
            if ($x <= $last1 && $y <= $last2) continue;
            if ($y <= $last1 && $x <= $last2) { $ops++; continue; }
            return 1 << 30;
        }
        return $ops;
    }
}
''')

add("2935_maximum_strong_pair_xor_ii", r'''<?php
// LeetCode 2935 - Maximum Strong Pair XOR II
// https://leetcode.com/problems/maximum-strong-pair-xor-ii/

class Solution {
    function maximumStrongPairXor($nums) {
        sort($nums);
        $ans = 0;
        $n = count($nums);
        for ($i = 0; $i < $n; $i++) {
            $x = $nums[$i];
            for ($j = $i; $j < $n && $nums[$j] <= 2 * $x; $j++) {
                $xorr = $x ^ $nums[$j];
                if ($xorr > $ans) $ans = $xorr;
            }
        }
        return $ans;
    }
}
''')

add("2936_number_of_equal_numbers_blocks", r'''<?php
// LeetCode 2936 - Number of Equal Numbers Blocks
// https://leetcode.com/problems/number-of-equal-numbers-blocks/

class Solution {
    function blockCount($nums) {
        if (!count($nums)) return 0;
        $ans = 1;
        $n = count($nums);
        for ($i = 1; $i < $n; $i++)
            if ($nums[$i] !== $nums[$i - 1]) $ans++;
        return $ans;
    }
}
''')

add("2937_make_three_strings_equal", r'''<?php
// LeetCode 2937 - Make Three Strings Equal
// https://leetcode.com/problems/make-three-strings-equal/

class Solution {
    function findMinimumOperations($s1, $s2, $s3) {
        $n = min(strlen($s1), strlen($s2), strlen($s3));
        $i = 0;
        while ($i < $n && $s1[$i] === $s2[$i] && $s2[$i] === $s3[$i]) $i++;
        if ($i === 0) return -1;
        return strlen($s1) + strlen($s2) + strlen($s3) - 3 * $i;
    }
}
''')

written = 0
for folder, body in SOLUTIONS.items():
    path = ROOT / folder / "solution.php"
    path.write_text(body, encoding="utf-8", newline="\n")
    written += 1
print(f"wrote {written}")
