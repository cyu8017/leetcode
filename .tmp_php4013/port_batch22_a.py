#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
SOLUTIONS = {}

def add(folder, body):
    SOLUTIONS[folder] = body

add("3951_minimum_energy_to_maintain_brightness", r'''<?php
// LeetCode 3951 - Minimum Energy To Maintain Brightness
// https://leetcode.com/problems/minimum-energy-to-maintain-brightness/

class Solution {
    function minEnergy($n, $brightness, $intervals) {
        usort($intervals, function ($a, $b) { return $a[0] <=> $b[0]; });
        $merged = [[$intervals[0][0], $intervals[0][1]]];
        for ($i = 1; $i < count($intervals); $i++) {
            $x = $intervals[$i];
            $last = count($merged) - 1;
            if ($merged[$last][1] < $x[0]) $merged[] = [$x[0], $x[1]];
            else if ($x[1] > $merged[$last][1]) $merged[$last][1] = $x[1];
        }
        $ans = 0;
        foreach ($merged as $interval) {
            $m = $interval[1] - $interval[0] + 1;
            $ans += intdiv($brightness + 2, 3) * $m;
        }
        return $ans;
    }
}
''')

add("3952_maximum_total_value_of_covered_indices", r'''<?php
// LeetCode 3952 - Maximum Total Value of Covered Indices
// https://leetcode.com/problems/maximum-total-value-of-covered-indices/

class Solution {
    function maxTotalValue($nums, $s) {
        $answer = 0;
        $n = strlen($s);
        for ($i = 0; $i < $n; ) {
            if ($s[$i] == '0') { $i++; continue; }
            $start = $i;
            while ($i < $n && $s[$i] == '1') $i++;
            $end = $i - 1;
            if ($start == 0) {
                for ($index = $start; $index <= $end; $index++) $answer += $nums[$index];
                continue;
            }
            $minimum = $nums[$start - 1];
            $total = 0;
            for ($index = $start - 1; $index <= $end; $index++) {
                $total += $nums[$index];
                if ($nums[$index] < $minimum) $minimum = $nums[$index];
            }
            $answer += $total - $minimum;
        }
        return $answer;
    }
}
''')

add("3954_sum_of_compatible_numbers_in_range_i", r'''<?php
// LeetCode 3954 - Sum Of Compatible Numbers In Range I
// https://leetcode.com/problems/sum-of-compatible-numbers-in-range-i/

class Solution {
    function sumOfGoodIntegers($n, $k) {
        $start = max(1, $n - $k);
        $end = $n + $k;
        $ans = 0;
        for ($x = $start; $x <= $end; $x++) {
            if (($n & $x) == 0) $ans += $x;
        }
        return $ans;
    }
}
''')

add("3955_valid_binary_strings_with_cost_limit", r'''<?php
// LeetCode 3955 - Valid Binary Strings With Cost Limit
// https://leetcode.com/problems/valid-binary-strings-with-cost-limit/

class Solution {
    function generateValidStrings($n, $k) {
        $ans = [];
        $this->dfs(0, 0, $n, $k, '', $ans);
        return $ans;
    }

    private function dfs($i, $tot, $n, $k, $path, &$ans) {
        if ($i >= $n) {
            $ans[] = $path;
            return;
        }
        $this->dfs($i + 1, $tot, $n, $k, $path . '0', $ans);
        if (($path === '' || $path[strlen($path) - 1] == '0') && $tot + $i <= $k) {
            $this->dfs($i + 1, $tot + $i, $n, $k, $path . '1', $ans);
        }
    }
}
''')

add("3958_minimum_cost_to_split_into_ones_ii", r'''<?php
// LeetCode 3958 - Minimum Cost To Split Into Ones II
// https://leetcode.com/problems/minimum-cost-to-split-into-ones-ii/

class Solution {
    function minCost($n) {
        return intdiv($n * ($n - 1), 2);
    }
}
''')

add("3959_check_good_integer", r'''<?php
// LeetCode 3959 - Check Good Integer
// https://leetcode.com/problems/check-good-integer/

class Solution {
    function checkGoodInteger($n) {
        $s = 0;
        for (; $n > 0; $n = intdiv($n, 10)) {
            $x = $n % 10;
            $s += $x * ($x - 1);
        }
        return $s >= 50;
    }
}
''')

add("3961_maximize_sum_of_device_ratings", r'''<?php
// LeetCode 3961 - Maximize Sum Of Device Ratings
// https://leetcode.com/problems/maximize-sum-of-device-ratings/

class Solution {
    function maxRatings($units) {
        $n = count($units[0]);
        if ($n == 1) {
            $ans = 0;
            foreach ($units as $x) $ans += $x[0];
            return $ans;
        }
        $answer = 0;
        $mn = 2147483647;
        $mn2 = 2147483647;
        foreach ($units as $x) {
            sort($x);
            $answer += $x[1];
            $mn2 = min($mn2, $x[1]);
            $mn = min($mn, $x[0]);
        }
        return $answer - ($mn2 - $mn);
    }
}
''')

add("3963_create_grid_with_exactly_one_path", r'''<?php
// LeetCode 3963 - Create Grid With Exactly One Path
// https://leetcode.com/problems/create-grid-with-exactly-one-path/

class Solution {
    function createGrid($m, $n) {
        $g = [];
        for ($i = 0; $i < $m; $i++) {
            $row = array_fill(0, $n, '#');
            if ($i == 0) {
                for ($j = 0; $j < $n; $j++) $row[$j] = '.';
            }
            $row[$n - 1] = '.';
            $g[] = implode('', $row);
        }
        return $g;
    }
}
''')

add("3964_minimum_lights_to_illuminate_a_road", r'''<?php
// LeetCode 3964 - Minimum Lights To Illuminate A Road
// https://leetcode.com/problems/minimum-lights-to-illuminate-a-road/

class Solution {
    function minLights($lights) {
        $n = count($lights);
        $d = array_fill(0, $n, 0);
        for ($i = 0; $i < $n; $i++) {
            $v = $lights[$i];
            if ($v > 0) {
                $l = max(0, $i - $v);
                $r = min($n - 1, $i + $v);
                $d[$l]++;
                if ($r + 1 < $n) $d[$r + 1]--;
            }
        }
        $s = 0;
        $cnt = 0;
        $ans = 0;
        foreach ($d as $x) {
            $s += $x;
            if ($s == 0) $cnt++;
            else {
                $ans += intdiv($cnt + 2, 3);
                $cnt = 0;
            }
        }
        $ans += intdiv($cnt + 2, 3);
        return $ans;
    }
}
''')

add("3968_maximum_manhattan_distance_after_all_moves", r'''<?php
// LeetCode 3968 - Maximum Manhattan Distance After All Moves
// https://leetcode.com/problems/maximum-manhattan-distance-after-all-moves/

class Solution {
    function maxDistance($moves) {
        $x = 0;
        $y = 0;
        $z = 0;
        $n = strlen($moves);
        for ($i = 0; $i < $n; $i++) {
            $c = $moves[$i];
            if ($c == 'U') $x -= 1;
            else if ($c == 'D') $x += 1;
            else if ($c == 'L') $y -= 1;
            else if ($c == 'R') $y += 1;
            else $z += 1;
        }
        return abs($x) + abs($y) + $z;
    }
}
''')

add("3969_valid_subarrays_with_matching_sum_digits_i", r'''<?php
// LeetCode 3969 - Valid Subarrays With Matching Sum Digits I
// https://leetcode.com/problems/valid-subarrays-with-matching-sum-digits-i/

class Solution {
    function countValidSubarrays($nums, $x) {
        $n = count($nums);
        $ans = 0;
        for ($l = 0; $l < $n; $l++) {
            $s = 0;
            for ($r = $l; $r < $n; $r++) {
                $s += $nums[$r];
                if ($s % 10 === $x) {
                    $t = strval($s);
                    if (intval($t[0]) === $x) $ans++;
                }
            }
        }
        return $ans;
    }
}
''')

add("3974_maximum_total_sum_of_k_selected_elements", r'''<?php
// LeetCode 3974 - Maximum Total Sum Of K Selected Elements
// https://leetcode.com/problems/maximum-total-sum-of-k-selected-elements/

class Solution {
    function maxSum($nums, $k, $mul) {
        sort($nums);
        $n = count($nums);
        $ans = 0;
        for ($i = $n - 1; $i >= $n - $k; $i--) {
            $m = max(1, $mul);
            $ans += $nums[$i] * $m;
            $mul--;
        }
        return $ans;
    }
}
''')

add("3975_filter_occupied_intervals", r'''<?php
// LeetCode 3975 - Filter Occupied Intervals
// https://leetcode.com/problems/filter-occupied-intervals/

class Solution {
    function filterOccupiedIntervals($occupiedIntervals, $freeStart, $freeEnd) {
        usort($occupiedIntervals, function ($a, $b) { return $a[0] <=> $b[0]; });
        $busy = [[$occupiedIntervals[0][0], $occupiedIntervals[0][1]]];
        for ($i = 1; $i < count($occupiedIntervals); $i++) {
            $cur = $occupiedIntervals[$i];
            $last = count($busy) - 1;
            if ($busy[$last][1] + 1 < $cur[0]) $busy[] = [$cur[0], $cur[1]];
            else if ($cur[1] > $busy[$last][1]) $busy[$last][1] = $cur[1];
        }
        $ans = [];
        foreach ($busy as $it) {
            $s = $it[0];
            $e = $it[1];
            if ($e < $freeStart || $s > $freeEnd) $ans[] = [$s, $e];
            else {
                if ($s < $freeStart) $ans[] = [$s, $freeStart - 1];
                if ($e > $freeEnd) $ans[] = [$freeEnd + 1, $e];
            }
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

add("3979_maximum_valid_pair_sum", r'''<?php
// LeetCode 3979 - Maximum Valid Pair Sum
// https://leetcode.com/problems/maximum-valid-pair-sum/

class Solution {
    function maxValidPairSum($nums, $k) {
        $ans = 0;
        $x = 0;
        for ($j = $k; $j < count($nums); $j++) {
            $y = $nums[$j];
            $x = max($x, $nums[$j - $k]);
            $ans = max($ans, $x + $y);
        }
        return $ans;
    }
}
''')

add("3982_sum_of_integers_with_maximum_digit_range", r'''<?php
// LeetCode 3982 - Sum of Integers with Maximum Digit Range
// https://leetcode.com/problems/sum-of-integers-with-maximum-digit-range/

class Solution {
    function maxDigitRange($nums) {
        $mx = 0;
        $ans = 0;
        foreach ($nums as $x) {
            $a = 10;
            $b = 0;
            for ($y = $x; $y > 0; $y = intdiv($y, 10)) {
                $v = $y % 10;
                $a = min($a, $v);
                $b = max($b, $v);
            }
            $r = $b - $a;
            if ($mx < $r) {
                $mx = $r;
                $ans = $x;
            } else if ($mx == $r) {
                $ans += $x;
            }
        }
        return $ans;
    }
}
''')

add("3983_subsequence_after_one_replacement", r'''<?php
// LeetCode 3983 - Subsequence After One Replacement
// https://leetcode.com/problems/subsequence-after-one-replacement/

class Solution {
    function canMakeSubsequence($s, $t) {
        $m = strlen($s);
        $n = strlen($t);
        $i0 = 0;
        $i1 = 0;
        $j = 0;
        while ($i1 < $m && $j < $n) {
            if ($s[$i1] == $t[$j]) $i1++;
            if ($i1 < $i0 + 1) $i1 = $i0 + 1;
            if ($s[$i0] == $t[$j]) $i0++;
            $j++;
        }
        return $i1 == $m;
    }
}
''')

add("3986_number_of_elapsed_seconds_between_two_times", r'''<?php
// LeetCode 3986 - Number of Elapsed Seconds Between Two Times
// https://leetcode.com/problems/number-of-elapsed-seconds-between-two-times/

class Solution {
    function secondsBetweenTimes($startTime, $endTime) {
        return $this->toSeconds($endTime) - $this->toSeconds($startTime);
    }

    private function toSeconds($s) {
        $h = intval($s[0]) * 10 + intval($s[1]);
        $m = intval($s[3]) * 10 + intval($s[4]);
        $sec = intval($s[6]) * 10 + intval($s[7]);
        return $h * 3600 + $m * 60 + $sec;
    }
}
''')

add("3987_minimum_total_cost_to_process_all_elements", r'''<?php
// LeetCode 3987 - Minimum Total Cost to Process All Elements
// https://leetcode.com/problems/minimum-total-cost-to-process-all-elements/

class Solution {
    function minimumCost($nums, $k) {
        $mod = 1000000007;
        $cnt = 0;
        $cur = $k;
        foreach ($nums as $x0) {
            $x = $x0;
            $diff = $x - $cur;
            if ($diff > 0) {
                $m = intdiv($diff + $k - 1, $k);
                $cur += $m * $k;
                $cnt += $m;
            }
            $cur -= $x;
        }
        $cnt %= $mod;
        return intdiv(($cnt + 1) * $cnt, 2) % $mod;
    }
}
''')

add("3989_maximum_consistent_columns_in_a_grid", r'''<?php
// LeetCode 3989 - Maximum Consistent Columns in a Grid
// https://leetcode.com/problems/maximum-consistent-columns-in-a-grid/

class Solution {
    function maxConsistentColumns($grid, $limit) {
        $m = count($grid);
        $n = count($grid[0]);
        $dp = array_fill(0, $n, 0);
        $ans = 1;
        for ($j = 0; $j < $n; $j++) {
            $dp[$j] = 1;
            for ($i = 0; $i < $j; $i++) {
                if ($dp[$i] + 1 <= $dp[$j]) continue;
                $ok = true;
                for ($r = 0; $r < $m; $r++) {
                    $d = abs($grid[$r][$j] - $grid[$r][$i]);
                    if ($d > $limit) { $ok = false; break; }
                }
                if ($ok) $dp[$j] = $dp[$i] + 1;
            }
            if ($dp[$j] > $ans) $ans = $dp[$j];
        }
        return $ans;
    }
}
''')

add("3992_rearrange_string_to_avoid_character_pair", r'''<?php
// LeetCode 3992 - Rearrange String to Avoid Character Pair
// https://leetcode.com/problems/rearrange-string-to-avoid-character-pair/

class Solution {
    function rearrangeString($s, $x, $y) {
        $arr = str_split($s);
        $i = 0;
        for ($j = 0; $j < count($arr); $j++) {
            if ($arr[$j] == $y) {
                $tmp = $arr[$i];
                $arr[$i] = $arr[$j];
                $arr[$j] = $tmp;
                $i++;
            }
        }
        return implode('', $arr);
    }
}
''')

add("3993_maximum_value_of_an_alternating_sequence", r'''<?php
// LeetCode 3993 - Maximum Value of an Alternating Sequence
// https://leetcode.com/problems/maximum-value-of-an-alternating-sequence/

class Solution {
    function maximumValue($n, $s, $m) {
        if ($n == 1) return $s;
        return $s + intdiv($n, 2) * ($m - 1) + 1;
    }
}
''')

add("3994_minimum_adjacent_swaps_to_partition_array", r'''<?php
// LeetCode 3994 - Minimum Adjacent Swaps to Partition Array
// https://leetcode.com/problems/minimum-adjacent-swaps-to-partition-array/

class Solution {
    function minAdjacentSwaps($nums, $a, $b) {
        $MOD = 1000000007;
        $result = 0;
        $cnt1 = 0;
        $cnt2 = 0;
        foreach ($nums as $x) {
            if ($x < $a) {
                $result = ($result + $cnt1 + $cnt2) % $MOD;
            } else if ($x <= $b) {
                $cnt1++;
                $result = ($result + $cnt2) % $MOD;
            } else {
                $cnt2++;
            }
        }
        return $result;
    }
}
''')

add("3996_even_number_of_knight_moves", r'''<?php
// LeetCode 3996 - Even Number of Knight Moves
// https://leetcode.com/problems/even-number-of-knight-moves/

class Solution {
    function canReach($start, $target) {
        return (($start[0] + $start[1]) % 2) == (($target[0] + $target[1]) % 2);
    }
}
''')

add("4000_largest_integer_with_given_digit_sum", r'''<?php
// LeetCode 4000 - Largest Integer With Given Digit Sum
// https://leetcode.com/problems/largest-integer-with-given-digit-sum/

class Solution {
    function largestInteger($n, $s) {
        if ($n * 9 < $s) return -1;
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            $x = $s < 9 ? $s : 9;
            $ans = $ans * 10 + $x;
            $s -= $x;
        }
        return $ans;
    }
}
''')

add("4001_aggregate_two_time_series", r'''<?php
// LeetCode 4001 - Aggregate Two Time Series
// https://leetcode.com/problems/aggregate-two-time-series/

class Solution {
    function aggregateTimeSeries($series1, $series2) {
        $m = count($series1);
        $n = count($series2);
        $i = 0;
        $j = 0;
        $ans = [];
        while ($i < $m && $j < $n) {
            $t1 = $series1[$i][0];
            $v1 = $series1[$i][1];
            $t2 = $series2[$j][0];
            $v2 = $series2[$j][1];
            if ($t1 === $t2) {
                $ans[] = [$t1, $v1 + $v2];
                $i++;
                $j++;
            } else if ($t1 < $t2) {
                $ans[] = [$t1, $v1 + $v2];
                $i++;
            } else {
                $ans[] = [$t2, $v1 + $v2];
                $j++;
            }
        }
        while ($i < $m) {
            $ans[] = [$series1[$i][0], $series1[$i][1]];
            $i++;
        }
        while ($j < $n) {
            $ans[] = [$series2[$j][0], $series2[$j][1]];
            $j++;
        }
        return $ans;
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

add("4010_maximize_pair_strength_using_gcd", r'''<?php
// LeetCode 4010 - Maximize Pair Strength Using GCD
// https://leetcode.com/problems/maximize-pair-strength-using-gcd/

class Solution {
    function maxPairStrength($nums) {
        $n = count($nums);
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            for ($j = $i + 1; $j < $n; $j++) {
                $g = $this->gcd($nums[$i], $nums[$j]);
                $x = intdiv($nums[$i] * $nums[$j], $g * $g);
                $ans = max($ans, $x);
            }
        }
        return $ans;
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

add("4011_count_subarrays_with_even_odd_ratio_i", r'''<?php
// LeetCode 4011 - Count Subarrays With Even Odd Ratio I
// https://leetcode.com/problems/count-subarrays-with-even-odd-ratio-i/

class Solution {
    function countRatioSubarrays($nums, $a, $b) {
        $n = count($nums);
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            $y = 0;
            for ($j = $i; $j < $n; $j++) {
                $y += $nums[$j] % 2;
                $x = $j - $i + 1 - $y;
                if ($y > 0 && $x * $b <= $y * $a) $ans++;
            }
        }
        return $ans;
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
