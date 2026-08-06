#!/usr/bin/env python3
"""Port stub solution.php files for problems 1227-1250 (non-SQL)."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOLUTIONS: dict[str, str] = {}


def add(name: str, content: str) -> None:
    SOLUTIONS[name] = content.strip() + "\n"


add("1227_airplane_seat_assignment_probability", r"""<?php
// LeetCode 1227 - Airplane Seat Assignment Probability
// https://leetcode.com/problems/airplane-seat-assignment-probability/

class Solution {
    /**
     * @param Integer $n
     * @return Float
     */
    function nthPersonGetsNthSeat($n) {
        return $n === 1 ? 1.0 : 0.5;
    }
}
""")

add("1228_missing_number_in_arithmetic_progression", r"""<?php
// LeetCode 1228 - Missing Number In Arithmetic Progression
// https://leetcode.com/problems/missing-number-in-arithmetic-progression/

class Solution {
    /**
     * @param Integer[] $arr
     * @return Integer
     */
    function missingNumber($arr) {
        $n = count($arr);
        $difference = intdiv($arr[$n - 1] - $arr[0], $n);
        for ($i = 1; $i < $n; $i++) {
            $expected = $arr[0] + $i * $difference;
            if ($arr[$i] !== $expected) return $expected;
        }
        return $arr[0];
    }
}
""")

add("1229_meeting_scheduler", r"""<?php
// LeetCode 1229 - Meeting Scheduler
// https://leetcode.com/problems/meeting-scheduler/

class Solution {
    /**
     * @param Integer[][] $slots1
     * @param Integer[][] $slots2
     * @param Integer $duration
     * @return Integer[]
     */
    function minAvailableDuration($slots1, $slots2, $duration) {
        usort($slots1, fn($a, $b) => $a[0] <=> $b[0]);
        usort($slots2, fn($a, $b) => $a[0] <=> $b[0]);
        $i = $j = 0;
        while ($i < count($slots1) && $j < count($slots2)) {
            $start = max($slots1[$i][0], $slots2[$j][0]);
            $end = min($slots1[$i][1], $slots2[$j][1]);
            if ($end - $start >= $duration) return [$start, $start + $duration];
            if ($slots1[$i][1] < $slots2[$j][1]) $i++;
            else $j++;
        }
        return [];
    }
}
""")

add("1230_toss_strange_coins", r"""<?php
// LeetCode 1230 - Toss Strange Coins
// https://leetcode.com/problems/toss-strange-coins/

class Solution {
    /**
     * @param Float[] $prob
     * @param Integer $target
     * @return Float
     */
    function probabilityOfHeads($prob, $target) {
        $dp = array_fill(0, $target + 1, 0.0);
        $dp[0] = 1.0;
        foreach ($prob as $p) {
            for ($heads = $target; $heads >= 0; $heads--) {
                $dp[$heads] = $dp[$heads] * (1 - $p) + ($heads ? $dp[$heads - 1] * $p : 0);
            }
        }
        return $dp[$target];
    }
}
""")

add("1231_divide_chocolate", r"""<?php
// LeetCode 1231 - Divide Chocolate
// https://leetcode.com/problems/divide-chocolate/

class Solution {
    /**
     * @param Integer[] $sweetness
     * @param Integer $k
     * @return Integer
     */
    function maximizeSweetness($sweetness, $k) {
        $lo = 1;
        $hi = intdiv(array_sum($sweetness), $k + 1);
        while ($lo <= $hi) {
            $mid = intdiv($lo + $hi, 2);
            $pieces = 0;
            $current = 0;
            foreach ($sweetness as $value) {
                $current += $value;
                if ($current >= $mid) {
                    $pieces++;
                    $current = 0;
                }
            }
            if ($pieces >= $k + 1) $lo = $mid + 1;
            else $hi = $mid - 1;
        }
        return $hi;
    }
}
""")

add("1232_check_if_it_is_a_straight_line", r"""<?php
// LeetCode 1232 - Check If It Is a Straight Line
// https://leetcode.com/problems/check-if-it-is-a-straight-line/

class Solution {
    /**
     * @param Integer[][] $coordinates
     * @return Boolean
     */
    function checkStraightLine($coordinates) {
        [$x0, $y0] = $coordinates[0];
        $dx = $coordinates[1][0] - $x0;
        $dy = $coordinates[1][1] - $y0;
        $n = count($coordinates);
        for ($i = 2; $i < $n; $i++) {
            [$x, $y] = $coordinates[$i];
            if (($x - $x0) * $dy !== ($y - $y0) * $dx) return false;
        }
        return true;
    }
}
""")

add("1233_remove_sub_folders_from_the_filesystem", r"""<?php
// LeetCode 1233 - Remove Sub-Folders from the Filesystem
// https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/

class Solution {
    /**
     * @param String[] $folder
     * @return String[]
     */
    function removeSubfolders($folder) {
        sort($folder);
        $answer = [];
        foreach ($folder as $path) {
            if (empty($answer) || !str_starts_with($path, end($answer) . '/')) {
                $answer[] = $path;
            }
        }
        return $answer;
    }
}
""")

add("1234_replace_the_substring_for_balanced_string", r"""<?php
// LeetCode 1234 - Replace the Substring for Balanced String
// https://leetcode.com/problems/replace-the-substring-for-balanced-string/

class Solution {
    /**
     * @param String $s
     * @return Integer
     */
    function balancedString($s) {
        $count = array_count_values(str_split($s));
        foreach (['Q','W','E','R'] as $c) if (!isset($count[$c])) $count[$c] = 0;
        $limit = intdiv(strlen($s), 4);
        $n = strlen($s);
        $left = 0;
        $answer = $n;
        for ($right = 0; $right < $n; $right++) {
            $count[$s[$right]]--;
            while ($left < $n && $count['Q'] <= $limit && $count['W'] <= $limit
                && $count['E'] <= $limit && $count['R'] <= $limit) {
                $answer = min($answer, $right - $left + 1);
                $count[$s[$left]]++;
                $left++;
            }
        }
        return $answer;
    }
}
""")

add("1235_maximum_profit_in_job_scheduling", r"""<?php
// LeetCode 1235 - Maximum Profit in Job Scheduling
// https://leetcode.com/problems/maximum-profit-in-job-scheduling/

class Solution {
    /**
     * @param Integer[] $startTime
     * @param Integer[] $endTime
     * @param Integer[] $profit
     * @return Integer
     */
    function jobScheduling($startTime, $endTime, $profit) {
        $jobs = [];
        $n = count($startTime);
        for ($i = 0; $i < $n; $i++) $jobs[] = [$endTime[$i], $startTime[$i], $profit[$i]];
        usort($jobs, fn($a, $b) => $a[0] <=> $b[0]);
        $ends = [0];
        $dp = [0];
        foreach ($jobs as [$end, $start, $gain]) {
            $lo = 0; $hi = count($ends);
            while ($lo < $hi) {
                $mid = ($lo + $hi) >> 1;
                if ($ends[$mid] <= $start) $lo = $mid + 1;
                else $hi = $mid;
            }
            $i = $lo - 1;
            $ends[] = $end;
            $dp[] = max(end($dp), $dp[$i] + $gain);
        }
        return end($dp);
    }
}
""")

add("1236_web_crawler", r"""<?php
// LeetCode 1236 - Web Crawler
// https://leetcode.com/problems/web-crawler/

class Solution {
    /**
     * @param String $startUrl
     * @param HtmlParser $htmlParser
     * @return String[]
     */
    function crawl($startUrl, $htmlParser) {
        $host = parse_url($startUrl, PHP_URL_HOST);
        $seen = [$startUrl => true];
        $stack = [$startUrl];
        while (!empty($stack)) {
            $cur = array_pop($stack);
            foreach ($htmlParser->getUrls($cur) as $url) {
                if (parse_url($url, PHP_URL_HOST) === $host && !isset($seen[$url])) {
                    $seen[$url] = true;
                    $stack[] = $url;
                }
            }
        }
        $ans = array_keys($seen);
        sort($ans);
        return $ans;
    }
}
""")

add("1237_find_positive_integer_solution_for_a_given_equation", r"""<?php
// LeetCode 1237 - Find Positive Integer Solution for a Given Equation
// https://leetcode.com/problems/find-positive-integer-solution-for-a-given-equation/

class Solution {
    /**
     * @param CustomFunction $customfunction
     * @param Integer $z
     * @return Integer[][]
     */
    function findSolution($customfunction, $z) {
        $answer = [];
        $x = 1; $y = 1000;
        while ($x <= 1000 && $y >= 1) {
            $value = $customfunction->f($x, $y);
            if ($value === $z) {
                $answer[] = [$x, $y];
                $x++; $y--;
            } elseif ($value < $z) $x++;
            else $y--;
        }
        return $answer;
    }
}
""")

add("1238_circular_permutation_in_binary_representation", r"""<?php
// LeetCode 1238 - Circular Permutation in Binary Representation
// https://leetcode.com/problems/circular-permutation-in-binary-representation/

class Solution {
    /**
     * @param Integer $n
     * @param Integer $start
     * @return Integer[]
     */
    function circularPermutation($n, $start) {
        $ans = [];
        $limit = 1 << $n;
        for ($i = 0; $i < $limit; $i++) {
            $ans[] = $start ^ $i ^ ($i >> 1);
        }
        return $ans;
    }
}
""")

add("1239_maximum_length_of_a_concatenated_string_with_unique_characters", r"""<?php
// LeetCode 1239 - Maximum Length of a Concatenated String with Unique Characters
// https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/

class Solution {
    /**
     * @param String[] $arr
     * @return Integer
     */
    function maxLength($arr) {
        $masks = [[0, 0]];
        foreach ($arr as $word) {
            $mask = 0;
            $len = strlen($word);
            $ok = true;
            for ($i = 0; $i < $len; $i++) {
                $bit = 1 << (ord($word[$i]) - 97);
                if ($mask & $bit) { $ok = false; break; }
                $mask |= $bit;
            }
            if (!$ok || substr_count(decbin($mask), '1') !== $len) continue;
            $extra = [];
            foreach ($masks as [$used, $length]) {
                if (($used & $mask) === 0) $extra[] = [$used | $mask, $length + $len];
            }
            foreach ($extra as $e) $masks[] = $e;
        }
        $best = 0;
        foreach ($masks as [, $length]) $best = max($best, $length);
        return $best;
    }
}
""")

add("1240_tiling_a_rectangle_with_the_fewest_squares", r"""<?php
// LeetCode 1240 - Tiling a Rectangle with the Fewest Squares
// https://leetcode.com/problems/tiling-a-rectangle-with-the-fewest-squares/

class Solution {
    private $heights;
    private $best;
    private $n;
    private $m;

    /**
     * @param Integer $n
     * @param Integer $m
     * @return Integer
     */
    function tilingRectangle($n, $m) {
        if ($n > $m) [$n, $m] = [$m, $n];
        $this->n = $n;
        $this->m = $m;
        $this->heights = array_fill(0, $m, 0);
        $this->best = $n * $m;
        $this->search(0);
        return $this->best;
    }

    private function search($used) {
        if ($used >= $this->best) return;
        $low = min($this->heights);
        if ($low === $this->n) {
            $this->best = $used;
            return;
        }
        $left = array_search($low, $this->heights, true);
        $right = $left;
        while ($right < $this->m && $this->heights[$right] === $low) $right++;
        $maxSize = min($this->n - $low, $right - $left);
        for ($size = $maxSize; $size >= 1; $size--) {
            for ($i = $left; $i < $left + $size; $i++) $this->heights[$i] = $low + $size;
            $this->search($used + 1);
            for ($i = $left; $i < $left + $size; $i++) $this->heights[$i] = $low;
        }
    }
}
""")

add("1242_web_crawler_multithreaded", r"""<?php
// LeetCode 1242 - Web Crawler Multithreaded
// https://leetcode.com/problems/web-crawler-multithreaded/

class Solution {
    /**
     * @param String $startUrl
     * @param HtmlParser $htmlParser
     * @return String[]
     */
    function crawl($startUrl, $htmlParser) {
        $host = parse_url($startUrl, PHP_URL_HOST);
        $seen = [$startUrl => true];
        $frontier = [$startUrl];
        while (!empty($frontier)) {
            $next = [];
            foreach ($frontier as $cur) {
                foreach ($htmlParser->getUrls($cur) as $url) {
                    if (parse_url($url, PHP_URL_HOST) === $host && !isset($seen[$url])) {
                        $seen[$url] = true;
                        $next[] = $url;
                    }
                }
            }
            $frontier = $next;
        }
        $ans = array_keys($seen);
        sort($ans);
        return $ans;
    }
}
""")

add("1243_array_transformation", r"""<?php
// LeetCode 1243 - Array Transformation
// https://leetcode.com/problems/array-transformation/

class Solution {
    /**
     * @param Integer[] $arr
     * @return Integer[]
     */
    function transformArray($arr) {
        while (true) {
            $nxt = $arr;
            $n = count($arr);
            for ($i = 1; $i < $n - 1; $i++) {
                if ($arr[$i] < $arr[$i - 1] && $arr[$i] < $arr[$i + 1]) $nxt[$i]++;
                elseif ($arr[$i] > $arr[$i - 1] && $arr[$i] > $arr[$i + 1]) $nxt[$i]--;
            }
            if ($nxt === $arr) return $arr;
            $arr = $nxt;
        }
    }
}
""")

add("1244_design_a_leaderboard", r"""<?php
// LeetCode 1244 - Design A Leaderboard
// https://leetcode.com/problems/design-a-leaderboard/

class Leaderboard {
    private $scores = [];

    function __construct() {}

    /**
     * @param Integer $playerId
     * @param Integer $score
     * @return NULL
     */
    function addScore($playerId, $score) {
        $this->scores[$playerId] = ($this->scores[$playerId] ?? 0) + $score;
    }

    /**
     * @param Integer $K
     * @return Integer
     */
    function top($K) {
        $vals = array_values($this->scores);
        rsort($vals);
        return array_sum(array_slice($vals, 0, $K));
    }

    /**
     * @param Integer $playerId
     * @return NULL
     */
    function reset($playerId) {
        unset($this->scores[$playerId]);
    }
}
""")

add("1245_tree_diameter", r"""<?php
// LeetCode 1245 - Tree Diameter
// https://leetcode.com/problems/tree-diameter/

class Solution {
    /**
     * @param Integer[][] $edges
     * @return Integer
     */
    function treeDiameter($edges) {
        if (empty($edges)) return 0;
        $graph = [];
        foreach ($edges as [$a, $b]) {
            $graph[$a][] = $b;
            $graph[$b][] = $a;
        }
        $farthest = function ($start) use ($graph) {
            $queue = [[$start, 0]];
            $seen = [$start => true];
            $head = 0;
            $last = [$start, 0];
            while ($head < count($queue)) {
                $last = $queue[$head++];
                foreach ($graph[$last[0]] ?? [] as $v) {
                    if (!isset($seen[$v])) {
                        $seen[$v] = true;
                        $queue[] = [$v, $last[1] + 1];
                    }
                }
            }
            return $last;
        };
        [$endpoint] = $farthest($edges[0][0]);
        return $farthest($endpoint)[1];
    }
}
""")

add("1246_palindrome_removal", r"""<?php
// LeetCode 1246 - Palindrome Removal
// https://leetcode.com/problems/palindrome-removal/

class Solution {
    /**
     * @param Integer[] $arr
     * @return Integer
     */
    function minimumMoves($arr) {
        $n = count($arr);
        $dp = array_fill(0, $n, array_fill(0, $n, 0));
        for ($i = 0; $i < $n; $i++) $dp[$i][$i] = 1;
        for ($length = 2; $length <= $n; $length++) {
            for ($i = 0; $i <= $n - $length; $i++) {
                $j = $i + $length - 1;
                $dp[$i][$j] = 1 + $dp[$i + 1][$j];
                if ($arr[$i] === $arr[$i + 1]) {
                    $dp[$i][$j] = min($dp[$i][$j], 1 + ($i + 2 <= $j ? $dp[$i + 2][$j] : 0));
                }
                for ($k = $i + 2; $k <= $j; $k++) {
                    if ($arr[$i] === $arr[$k]) {
                        $dp[$i][$j] = min($dp[$i][$j], $dp[$i + 1][$k - 1] + ($k < $j ? $dp[$k + 1][$j] : 0));
                    }
                }
            }
        }
        return $dp[0][$n - 1];
    }
}
""")

add("1247_minimum_swaps_to_make_strings_equal", r"""<?php
// LeetCode 1247 - Minimum Swaps to Make Strings Equal
// https://leetcode.com/problems/minimum-swaps-to-make-strings-equal/

class Solution {
    /**
     * @param String $s1
     * @param String $s2
     * @return Integer
     */
    function minimumSwap($s1, $s2) {
        $xy = $yx = 0;
        $n = strlen($s1);
        for ($i = 0; $i < $n; $i++) {
            if ($s1[$i] === 'x' && $s2[$i] === 'y') $xy++;
            if ($s1[$i] === 'y' && $s2[$i] === 'x') $yx++;
        }
        if (($xy + $yx) % 2) return -1;
        return intdiv($xy, 2) + intdiv($yx, 2) + 2 * ($xy % 2);
    }
}
""")

add("1248_count_number_of_nice_subarrays", r"""<?php
// LeetCode 1248 - Count Number of Nice Subarrays
// https://leetcode.com/problems/count-number-of-nice-subarrays/

class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer
     */
    function numberOfSubarrays($nums, $k) {
        $atMost = function ($k) use ($nums) {
            if ($k < 0) return 0;
            $left = $odd = $ans = 0;
            $n = count($nums);
            for ($right = 0; $right < $n; $right++) {
                $odd += $nums[$right] & 1;
                while ($odd > $k) {
                    $odd -= $nums[$left] & 1;
                    $left++;
                }
                $ans += $right - $left + 1;
            }
            return $ans;
        };
        return $atMost($k) - $atMost($k - 1);
    }
}
""")

add("1249_minimum_remove_to_make_valid_parentheses", r"""<?php
// LeetCode 1249 - Minimum Remove to Make Valid Parentheses
// https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

class Solution {
    /**
     * @param String $s
     * @return String
     */
    function minRemoveToMakeValid($s) {
        $chars = str_split($s);
        $stack = [];
        $n = count($chars);
        for ($i = 0; $i < $n; $i++) {
            if ($chars[$i] === '(') $stack[] = $i;
            elseif ($chars[$i] === ')') {
                if (!empty($stack)) array_pop($stack);
                else $chars[$i] = '';
            }
        }
        foreach ($stack as $i) $chars[$i] = '';
        return implode('', $chars);
    }
}
""")

add("1250_check_if_it_is_a_good_array", r"""<?php
// LeetCode 1250 - Check If It Is a Good Array
// https://leetcode.com/problems/check-if-it-is-a-good-array/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Boolean
     */
    function isGoodArray($nums) {
        $g = $nums[0];
        foreach ($nums as $x) {
            while ($x) {
                [$g, $x] = [$x, $g % $x];
            }
            if ($g === 1) return true;
        }
        return $g === 1;
    }
}
""")


def is_stub(path: Path) -> bool:
    return "function solve()" in path.read_text(encoding="utf-8")


def main() -> None:
    ported = 0
    for folder, content in SOLUTIONS.items():
        path = ROOT / folder / "solution.php"
        if not path.exists():
            print(f"MISSING {folder}")
            continue
        if not is_stub(path):
            print(f"skip done {folder}")
            continue
        path.write_text(content, encoding="utf-8", newline="\n")
        ported += 1
        print(f"ported {folder}")
    print(f"ported={ported} total={len(SOLUTIONS)}")


if __name__ == "__main__":
    main()
