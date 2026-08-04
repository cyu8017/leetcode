#!/usr/bin/env python3
"""Port Java solutions for problems 1220-1260 (non-SQL stubs)."""
from __future__ import annotations
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

S: dict[str, str] = {}

S["1220_count_vowels_permutation"] = r"""// LeetCode 1220 - Count Vowels Permutation
// https://leetcode.com/problems/count-vowels-permutation/

class Solution {
    public int countVowelPermutation(int n) {
        int mod = 1_000_000_007;
        long[] dp = {1, 1, 1, 1, 1};
        for (int i = 1; i < n; i++) {
            long a = (dp[1] + dp[2] + dp[4]) % mod;
            long e = (dp[0] + dp[2]) % mod;
            long ii = (dp[1] + dp[3]) % mod;
            long o = dp[2];
            long u = (dp[2] + dp[3]) % mod;
            dp = new long[]{a, e, ii, o, u};
        }
        long ans = 0;
        for (long x : dp) ans = (ans + x) % mod;
        return (int) ans;
    }
}
"""

S["1221_split_a_string_in_balanced_strings"] = r"""// LeetCode 1221 - Split a String in Balanced Strings
// https://leetcode.com/problems/split-a-string-in-balanced-strings/

class Solution {
    public int balancedStringSplit(String s) {
        int balance = 0, answer = 0;
        for (int i = 0; i < s.length(); i++) {
            balance += s.charAt(i) == 'L' ? 1 : -1;
            if (balance == 0) answer++;
        }
        return answer;
    }
}
"""

S["1222_queens_that_can_attack_the_king"] = r"""// LeetCode 1222 - Queens That Can Attack the King
// https://leetcode.com/problems/queens-that-can-attack-the-king/

import java.util.*;

class Solution {
    public List<List<Integer>> queensAttacktheKing(int[][] queens, int[] king) {
        Set<Long> occupied = new HashSet<>();
        for (int[] q : queens) occupied.add(key(q[0], q[1]));
        List<List<Integer>> answer = new ArrayList<>();
        for (int dr = -1; dr <= 1; dr++) {
            for (int dc = -1; dc <= 1; dc++) {
                if (dr == 0 && dc == 0) continue;
                int r = king[0] + dr, c = king[1] + dc;
                while (r >= 0 && r < 8 && c >= 0 && c < 8) {
                    if (occupied.contains(key(r, c))) {
                        answer.add(Arrays.asList(r, c));
                        break;
                    }
                    r += dr;
                    c += dc;
                }
            }
        }
        return answer;
    }

    private long key(int r, int c) {
        return ((long) r << 32) | (c & 0xffffffffL);
    }
}
"""

S["1223_dice_roll_simulation"] = r"""// LeetCode 1223 - Dice Roll Simulation
// https://leetcode.com/problems/dice-roll-simulation/

class Solution {
    public int dieSimulator(int n, int[] rollMax) {
        int mod = 1_000_000_007;
        int[][] dp = new int[6][];
        for (int j = 0; j < 6; j++) {
            dp[j] = new int[rollMax[j] + 1];
            dp[j][1] = 1;
        }
        for (int t = 1; t < n; t++) {
            int[] totals = new int[6];
            for (int j = 0; j < 6; j++) {
                for (int run = 1; run < dp[j].length; run++) {
                    totals[j] = (totals[j] + dp[j][run]) % mod;
                }
            }
            int[][] nxt = new int[6][];
            for (int j = 0; j < 6; j++) {
                nxt[j] = new int[dp[j].length];
                int sumOthers = 0;
                for (int k = 0; k < 6; k++) {
                    if (k != j) sumOthers = (sumOthers + totals[k]) % mod;
                }
                nxt[j][1] = sumOthers;
                for (int run = 2; run < dp[j].length; run++) {
                    nxt[j][run] = dp[j][run - 1];
                }
            }
            dp = nxt;
        }
        int ans = 0;
        for (int j = 0; j < 6; j++) {
            for (int run = 1; run < dp[j].length; run++) {
                ans = (ans + dp[j][run]) % mod;
            }
        }
        return ans;
    }
}
"""

S["1224_maximum_equal_frequency"] = r"""// LeetCode 1224 - Maximum Equal Frequency
// https://leetcode.com/problems/maximum-equal-frequency/

import java.util.*;

class Solution {
    public int maxEqualFreq(int[] nums) {
        Map<Integer, Integer> count = new HashMap<>();
        Map<Integer, Integer> freq = new HashMap<>();
        int answer = 0;
        for (int i = 0; i < nums.length; i++) {
            int x = nums[i];
            int old = count.getOrDefault(x, 0);
            if (old > 0) freq.put(old, freq.get(old) - 1);
            count.put(x, old + 1);
            freq.put(old + 1, freq.getOrDefault(old + 1, 0) + 1);
            int high = Collections.max(freq.keySet());
            if (high == 1
                    || freq.get(high) * high + 1 == i + 1
                    || (freq.get(high) == 1 && (high - 1) * freq.getOrDefault(high - 1, 0) + high == i + 1)) {
                answer = i + 1;
            }
        }
        return answer;
    }
}
"""

S["1226_the_dining_philosophers"] = r"""// LeetCode 1226 - The Dining Philosophers
// https://leetcode.com/problems/the-dining-philosophers/

import java.util.concurrent.locks.ReentrantLock;

class DiningPhilosophers {
    private final ReentrantLock[] forks = new ReentrantLock[5];

    public DiningPhilosophers() {
        for (int i = 0; i < 5; i++) forks[i] = new ReentrantLock();
    }

    public void wantsToEat(int philosopher, Runnable pickLeftFork, Runnable pickRightFork,
                           Runnable eat, Runnable putLeftFork, Runnable putRightFork) throws InterruptedException {
        int left = philosopher, right = (philosopher + 1) % 5;
        int first = philosopher % 2 == 0 ? left : right;
        int second = philosopher % 2 == 0 ? right : left;
        forks[first].lock();
        forks[second].lock();
        try {
            pickLeftFork.run();
            pickRightFork.run();
            eat.run();
            putLeftFork.run();
            putRightFork.run();
        } finally {
            forks[second].unlock();
            forks[first].unlock();
        }
    }
}
"""

S["1227_airplane_seat_assignment_probability"] = r"""// LeetCode 1227 - Airplane Seat Assignment Probability
// https://leetcode.com/problems/airplane-seat-assignment-probability/

class Solution {
    public double nthPersonGetsNthSeat(int n) {
        return n == 1 ? 1.0 : 0.5;
    }
}
"""

S["1228_missing_number_in_arithmetic_progression"] = r"""// LeetCode 1228 - Missing Number In Arithmetic Progression
// https://leetcode.com/problems/missing-number-in-arithmetic-progression/

class Solution {
    public int missingNumber(int[] arr) {
        int diff = (arr[arr.length - 1] - arr[0]) / arr.length;
        for (int i = 1; i < arr.length; i++) {
            int expected = arr[0] + i * diff;
            if (arr[i] != expected) return expected;
        }
        return arr[0];
    }
}
"""

S["1229_meeting_scheduler"] = r"""// LeetCode 1229 - Meeting Scheduler
// https://leetcode.com/problems/meeting-scheduler/

import java.util.*;

class Solution {
    public List<Integer> minAvailableDuration(int[][] slots1, int[][] slots2, int duration) {
        Arrays.sort(slots1, Comparator.comparingInt(a -> a[0]));
        Arrays.sort(slots2, Comparator.comparingInt(a -> a[0]));
        int i = 0, j = 0;
        while (i < slots1.length && j < slots2.length) {
            int start = Math.max(slots1[i][0], slots2[j][0]);
            int end = Math.min(slots1[i][1], slots2[j][1]);
            if (end - start >= duration) {
                return Arrays.asList(start, start + duration);
            }
            if (slots1[i][1] < slots2[j][1]) i++;
            else j++;
        }
        return new ArrayList<>();
    }
}
"""

S["1230_toss_strange_coins"] = r"""// LeetCode 1230 - Toss Strange Coins
// https://leetcode.com/problems/toss-strange-coins/

class Solution {
    public double probabilityOfHeads(double[] prob, int target) {
        double[] dp = new double[target + 1];
        dp[0] = 1.0;
        for (double p : prob) {
            for (int heads = target; heads >= 0; heads--) {
                dp[heads] = dp[heads] * (1 - p) + (heads > 0 ? dp[heads - 1] * p : 0);
            }
        }
        return dp[target];
    }
}
"""

S["1231_divide_chocolate"] = r"""// LeetCode 1231 - Divide Chocolate
// https://leetcode.com/problems/divide-chocolate/

class Solution {
    public int maximizeSweetness(int[] sweetness, int k) {
        int lo = 1, hi = 0;
        for (int x : sweetness) hi += x;
        hi /= k + 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            int pieces = 0, current = 0;
            for (int value : sweetness) {
                current += value;
                if (current >= mid) {
                    pieces++;
                    current = 0;
                }
            }
            if (pieces >= k + 1) lo = mid + 1;
            else hi = mid - 1;
        }
        return hi;
    }
}
"""

S["1232_check_if_it_is_a_straight_line"] = r"""// LeetCode 1232 - Check If It Is a Straight Line
// https://leetcode.com/problems/check-if-it-is-a-straight-line/

class Solution {
    public boolean checkStraightLine(int[][] coordinates) {
        int x0 = coordinates[0][0], y0 = coordinates[0][1];
        int dx = coordinates[1][0] - x0, dy = coordinates[1][1] - y0;
        for (int i = 2; i < coordinates.length; i++) {
            int x = coordinates[i][0], y = coordinates[i][1];
            if ((long) (x - x0) * dy != (long) (y - y0) * dx) return false;
        }
        return true;
    }
}
"""

S["1233_remove_sub_folders_from_the_filesystem"] = r"""// LeetCode 1233 - Remove Sub-Folders from the Filesystem
// https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/

import java.util.*;

class Solution {
    public List<String> removeSubfolders(String[] folder) {
        Arrays.sort(folder);
        List<String> answer = new ArrayList<>();
        for (String path : folder) {
            if (answer.isEmpty() || !path.startsWith(answer.get(answer.size() - 1) + "/")) {
                answer.add(path);
            }
        }
        return answer;
    }
}
"""

S["1234_replace_the_substring_for_balanced_string"] = r"""// LeetCode 1234 - Replace the Substring for Balanced String
// https://leetcode.com/problems/replace-the-substring-for-balanced-string/

class Solution {
    public int balancedString(String s) {
        int[] count = new int[128];
        for (char ch : s.toCharArray()) count[ch]++;
        int limit = s.length() / 4;
        int n = s.length(), left = 0, answer = n;
        for (int right = 0; right < n; right++) {
            count[s.charAt(right)]--;
            while (left < n && count['Q'] <= limit && count['W'] <= limit
                    && count['E'] <= limit && count['R'] <= limit) {
                answer = Math.min(answer, right - left + 1);
                count[s.charAt(left)]++;
                left++;
            }
        }
        return answer;
    }
}
"""

S["1235_maximum_profit_in_job_scheduling"] = r"""// LeetCode 1235 - Maximum Profit in Job Scheduling
// https://leetcode.com/problems/maximum-profit-in-job-scheduling/

import java.util.*;

class Solution {
    public int jobScheduling(int[] startTime, int[] endTime, int[] profit) {
        int n = startTime.length;
        int[][] jobs = new int[n][3];
        for (int i = 0; i < n; i++) jobs[i] = new int[]{endTime[i], startTime[i], profit[i]};
        Arrays.sort(jobs, Comparator.comparingInt(a -> a[0]));
        int[] ends = new int[n + 1];
        int[] dp = new int[n + 1];
        for (int i = 0; i < n; i++) {
            int end = jobs[i][0], start = jobs[i][1], gain = jobs[i][2];
            int idx = upperBound(ends, start, i);
            ends[i + 1] = end;
            dp[i + 1] = Math.max(dp[i], dp[idx] + gain);
        }
        return dp[n];
    }

    private int upperBound(int[] ends, int target, int limit) {
        int lo = 0, hi = limit;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (ends[mid] <= target) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    }
}
"""

S["1236_web_crawler"] = r"""// LeetCode 1236 - Web Crawler
// https://leetcode.com/problems/web-crawler/

import java.net.URI;
import java.util.*;

class HtmlParser {
    public List<String> getUrls(String url) {
        return new ArrayList<>();
    }
}

class Solution {
    public List<String> crawl(String startUrl, HtmlParser htmlParser) {
        String host = URI.create(startUrl).getHost();
        Set<String> seen = new HashSet<>();
        seen.add(startUrl);
        Deque<String> stack = new ArrayDeque<>();
        stack.push(startUrl);
        while (!stack.isEmpty()) {
            String current = stack.pop();
            for (String url : htmlParser.getUrls(current)) {
                if (host.equals(URI.create(url).getHost()) && seen.add(url)) {
                    stack.push(url);
                }
            }
        }
        List<String> answer = new ArrayList<>(seen);
        Collections.sort(answer);
        return answer;
    }
}
"""

S["1237_find_positive_integer_solution_for_a_given_equation"] = r"""// LeetCode 1237 - Find Positive Integer Solution for a Given Equation
// https://leetcode.com/problems/find-positive-integer-solution-for-a-given-equation/

import java.util.*;

class CustomFunction {
    public int f(int x, int y) {
        return 0;
    }
}

class Solution {
    public List<List<Integer>> findSolution(CustomFunction customfunction, int z) {
        List<List<Integer>> answer = new ArrayList<>();
        int x = 1, y = 1000;
        while (x <= 1000 && y >= 1) {
            int value = customfunction.f(x, y);
            if (value == z) {
                answer.add(Arrays.asList(x, y));
                x++;
                y--;
            } else if (value < z) {
                x++;
            } else {
                y--;
            }
        }
        return answer;
    }
}
"""

S["1238_circular_permutation_in_binary_representation"] = r"""// LeetCode 1238 - Circular Permutation in Binary Representation
// https://leetcode.com/problems/circular-permutation-in-binary-representation/

import java.util.*;

class Solution {
    public List<Integer> circularPermutation(int n, int start) {
        int size = 1 << n;
        List<Integer> answer = new ArrayList<>(size);
        for (int i = 0; i < size; i++) {
            answer.add(start ^ i ^ (i >> 1));
        }
        return answer;
    }
}
"""

S["1239_maximum_length_of_a_concatenated_string_with_unique_characters"] = r"""// LeetCode 1239 - Maximum Length of a Concatenated String with Unique Characters
// https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/

import java.util.*;

class Solution {
    public int maxLength(String[] arr) {
        List<int[]> masks = new ArrayList<>();
        masks.add(new int[]{0, 0});
        for (String word : arr) {
            int mask = 0;
            boolean ok = true;
            for (char ch : word.toCharArray()) {
                int bit = 1 << (ch - 'a');
                if ((mask & bit) != 0) {
                    ok = false;
                    break;
                }
                mask |= bit;
            }
            if (!ok) continue;
            int len = word.length();
            List<int[]> next = new ArrayList<>(masks);
            for (int[] state : masks) {
                if ((state[0] & mask) == 0) {
                    next.add(new int[]{state[0] | mask, state[1] + len});
                }
            }
            masks = next;
        }
        int best = 0;
        for (int[] state : masks) best = Math.max(best, state[1]);
        return best;
    }
}
"""

S["1240_tiling_a_rectangle_with_the_fewest_squares"] = r"""// LeetCode 1240 - Tiling a Rectangle with the Fewest Squares
// https://leetcode.com/problems/tiling-a-rectangle-with-the-fewest-squares/

class Solution {
    private int best;

    public int tilingRectangle(int n, int m) {
        if (n > m) {
            int t = n;
            n = m;
            m = t;
        }
        int[] heights = new int[m];
        best = n * m;
        search(heights, n, m, 0);
        return best;
    }

    private void search(int[] heights, int n, int m, int used) {
        if (used >= best) return;
        int low = Integer.MAX_VALUE;
        for (int h : heights) low = Math.min(low, h);
        if (low == n) {
            best = used;
            return;
        }
        int left = 0;
        while (left < m && heights[left] != low) left++;
        int right = left;
        while (right < m && heights[right] == low) right++;
        int maxSize = Math.min(n - low, right - left);
        for (int size = maxSize; size >= 1; size--) {
            for (int i = left; i < left + size; i++) heights[i] = low + size;
            search(heights, n, m, used + 1);
            for (int i = left; i < left + size; i++) heights[i] = low;
        }
    }
}
"""

S["1242_web_crawler_multithreaded"] = r"""// LeetCode 1242 - Web Crawler Multithreaded
// https://leetcode.com/problems/web-crawler-multithreaded/

import java.net.URI;
import java.util.*;
import java.util.concurrent.*;

class HtmlParser {
    public List<String> getUrls(String url) {
        return new ArrayList<>();
    }
}

class Solution {
    public List<String> crawl(String startUrl, HtmlParser htmlParser) {
        String host = URI.create(startUrl).getHost();
        Set<String> seen = ConcurrentHashMap.newKeySet();
        seen.add(startUrl);
        List<String> frontier = Collections.synchronizedList(new ArrayList<>(List.of(startUrl)));
        ExecutorService pool = Executors.newCachedThreadPool();
        try {
            while (!frontier.isEmpty()) {
                List<String> current = new ArrayList<>(frontier);
                frontier.clear();
                List<Future<?>> futures = new ArrayList<>();
                for (String url : current) {
                    futures.add(pool.submit(() -> {
                        for (String link : htmlParser.getUrls(url)) {
                            if (host.equals(URI.create(link).getHost()) && seen.add(link)) {
                                frontier.add(link);
                            }
                        }
                    }));
                }
                for (Future<?> f : futures) {
                    try {
                        f.get();
                    } catch (Exception e) {
                        throw new RuntimeException(e);
                    }
                }
            }
        } finally {
            pool.shutdown();
        }
        List<String> answer = new ArrayList<>(seen);
        Collections.sort(answer);
        return answer;
    }
}
"""

S["1243_array_transformation"] = r"""// LeetCode 1243 - Array Transformation
// https://leetcode.com/problems/array-transformation/

import java.util.*;

class Solution {
    public List<Integer> transformArray(int[] arr) {
        while (true) {
            int[] nxt = arr.clone();
            for (int i = 1; i < arr.length - 1; i++) {
                if (arr[i] < arr[i - 1] && arr[i] < arr[i + 1]) nxt[i]++;
                else if (arr[i] > arr[i - 1] && arr[i] > arr[i + 1]) nxt[i]--;
            }
            if (Arrays.equals(nxt, arr)) {
                List<Integer> answer = new ArrayList<>();
                for (int x : arr) answer.add(x);
                return answer;
            }
            arr = nxt;
        }
    }
}
"""

S["1244_design_a_leaderboard"] = r"""// LeetCode 1244 - Design A Leaderboard
// https://leetcode.com/problems/design-a-leaderboard/

import java.util.*;

class Leaderboard {
    private final Map<Integer, Integer> scores = new HashMap<>();

    public Leaderboard() {}

    public void addScore(int playerId, int score) {
        scores.put(playerId, scores.getOrDefault(playerId, 0) + score);
    }

    public int top(int K) {
        List<Integer> values = new ArrayList<>(scores.values());
        values.sort(Collections.reverseOrder());
        int sum = 0;
        for (int i = 0; i < Math.min(K, values.size()); i++) sum += values.get(i);
        return sum;
    }

    public void reset(int playerId) {
        scores.remove(playerId);
    }
}
"""

S["1245_tree_diameter"] = r"""// LeetCode 1245 - Tree Diameter
// https://leetcode.com/problems/tree-diameter/

import java.util.*;

class Solution {
    public int treeDiameter(int[][] edges) {
        if (edges.length == 0) return 0;
        Map<Integer, List<Integer>> graph = new HashMap<>();
        for (int[] e : edges) {
            graph.computeIfAbsent(e[0], k -> new ArrayList<>()).add(e[1]);
            graph.computeIfAbsent(e[1], k -> new ArrayList<>()).add(e[0]);
        }
        int[] first = farthest(edges[0][0], graph);
        return farthest(first[0], graph)[1];
    }

    private int[] farthest(int start, Map<Integer, List<Integer>> graph) {
        Deque<int[]> q = new ArrayDeque<>();
        Set<Integer> seen = new HashSet<>();
        q.offer(new int[]{start, 0});
        seen.add(start);
        int[] last = new int[]{start, 0};
        while (!q.isEmpty()) {
            last = q.poll();
            for (int v : graph.getOrDefault(last[0], List.of())) {
                if (seen.add(v)) q.offer(new int[]{v, last[1] + 1});
            }
        }
        return last;
    }
}
"""

S["1246_palindrome_removal"] = r"""// LeetCode 1246 - Palindrome Removal
// https://leetcode.com/problems/palindrome-removal/

class Solution {
    public int minimumMoves(int[] arr) {
        int n = arr.length;
        int[][] dp = new int[n][n];
        for (int i = 0; i < n; i++) dp[i][i] = 1;
        for (int length = 2; length <= n; length++) {
            for (int i = 0; i + length <= n; i++) {
                int j = i + length - 1;
                dp[i][j] = 1 + dp[i + 1][j];
                if (arr[i] == arr[i + 1]) {
                    dp[i][j] = Math.min(dp[i][j], 1 + (i + 2 <= j ? dp[i + 2][j] : 0));
                }
                for (int k = i + 2; k <= j; k++) {
                    if (arr[i] == arr[k]) {
                        dp[i][j] = Math.min(dp[i][j],
                                dp[i + 1][k - 1] + (k < j ? dp[k + 1][j] : 0));
                    }
                }
            }
        }
        return dp[0][n - 1];
    }
}
"""

S["1247_minimum_swaps_to_make_strings_equal"] = r"""// LeetCode 1247 - Minimum Swaps to Make Strings Equal
// https://leetcode.com/problems/minimum-swaps-to-make-strings-equal/

class Solution {
    public int minimumSwap(String s1, String s2) {
        int xy = 0, yx = 0;
        for (int i = 0; i < s1.length(); i++) {
            if (s1.charAt(i) == 'x' && s2.charAt(i) == 'y') xy++;
            if (s1.charAt(i) == 'y' && s2.charAt(i) == 'x') yx++;
        }
        if ((xy + yx) % 2 == 1) return -1;
        return xy / 2 + yx / 2 + 2 * (xy % 2);
    }
}
"""

S["1248_count_number_of_nice_subarrays"] = r"""// LeetCode 1248 - Count Number of Nice Subarrays
// https://leetcode.com/problems/count-number-of-nice-subarrays/

import java.util.*;

class Solution {
    public int numberOfSubarrays(int[] nums, int k) {
        Map<Integer, Integer> freq = new HashMap<>();
        freq.put(0, 1);
        int odd = 0, answer = 0;
        for (int x : nums) {
            odd += x & 1;
            answer += freq.getOrDefault(odd - k, 0);
            freq.put(odd, freq.getOrDefault(odd, 0) + 1);
        }
        return answer;
    }
}
"""

S["1249_minimum_remove_to_make_valid_parentheses"] = r"""// LeetCode 1249 - Minimum Remove to Make Valid Parentheses
// https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

import java.util.*;

class Solution {
    public String minRemoveToMakeValid(String s) {
        char[] chars = s.toCharArray();
        Deque<Integer> opens = new ArrayDeque<>();
        for (int i = 0; i < chars.length; i++) {
            if (chars[i] == '(') opens.push(i);
            else if (chars[i] == ')') {
                if (opens.isEmpty()) chars[i] = 0;
                else opens.pop();
            }
        }
        while (!opens.isEmpty()) chars[opens.pop()] = 0;
        StringBuilder sb = new StringBuilder();
        for (char ch : chars) if (ch != 0) sb.append(ch);
        return sb.toString();
    }
}
"""

S["1250_check_if_it_is_a_good_array"] = r"""// LeetCode 1250 - Check If It Is a Good Array
// https://leetcode.com/problems/check-if-it-is-a-good-array/

class Solution {
    public boolean isGoodArray(int[] nums) {
        int g = nums[0];
        for (int i = 1; i < nums.length; i++) g = gcd(g, nums[i]);
        return g == 1;
    }

    private int gcd(int a, int b) {
        while (b != 0) {
            int t = a % b;
            a = b;
            b = t;
        }
        return Math.abs(a);
    }
}
"""

S["1252_cells_with_odd_values_in_a_matrix"] = r"""// LeetCode 1252 - Cells with Odd Values in a Matrix
// https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/

class Solution {
    public int oddCells(int m, int n, int[][] indices) {
        int[] rows = new int[m], cols = new int[n];
        for (int[] idx : indices) {
            rows[idx[0]] ^= 1;
            cols[idx[1]] ^= 1;
        }
        int answer = 0;
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                answer += (rows[r] ^ cols[c]);
            }
        }
        return answer;
    }
}
"""

S["1253_reconstruct_a_2_row_binary_matrix"] = r"""// LeetCode 1253 - Reconstruct a 2 Row Binary Matrix
// https://leetcode.com/problems/reconstruct-a-2-row-binary-matrix/

import java.util.*;

class Solution {
    public List<List<Integer>> reconstructMatrix(int upper, int lower, int[] colsum) {
        int n = colsum.length;
        int[] top = new int[n], bottom = new int[n];
        for (int i = 0; i < n; i++) {
            if (colsum[i] == 2) {
                top[i] = bottom[i] = 1;
                upper--;
                lower--;
            }
        }
        if (upper < 0 || lower < 0) return new ArrayList<>();
        for (int i = 0; i < n; i++) {
            if (colsum[i] == 1) {
                if (upper > 0) {
                    top[i] = 1;
                    upper--;
                } else if (lower > 0) {
                    bottom[i] = 1;
                    lower--;
                } else {
                    return new ArrayList<>();
                }
            }
        }
        if (upper != 0 || lower != 0) return new ArrayList<>();
        List<List<Integer>> answer = new ArrayList<>();
        answer.add(toList(top));
        answer.add(toList(bottom));
        return answer;
    }

    private List<Integer> toList(int[] arr) {
        List<Integer> list = new ArrayList<>();
        for (int x : arr) list.add(x);
        return list;
    }
}
"""

S["1254_number_of_closed_islands"] = r"""// LeetCode 1254 - Number of Closed Islands
// https://leetcode.com/problems/number-of-closed-islands/

class Solution {
    public int closedIsland(int[][] grid) {
        int m = grid.length, n = grid[0].length, answer = 0;
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (grid[r][c] == 0 && flood(grid, r, c)) answer++;
            }
        }
        return answer;
    }

    private boolean flood(int[][] grid, int sr, int sc) {
        int m = grid.length, n = grid[0].length;
        boolean closed = true;
        int[][] dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        int[] stackR = new int[m * n], stackC = new int[m * n];
        int top = 0;
        stackR[top] = sr;
        stackC[top] = sc;
        grid[sr][sc] = 1;
        while (top >= 0) {
            int r = stackR[top], c = stackC[top];
            top--;
            if (r == 0 || r == m - 1 || c == 0 || c == n - 1) closed = false;
            for (int[] d : dirs) {
                int nr = r + d[0], nc = c + d[1];
                if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] == 0) {
                    grid[nr][nc] = 1;
                    top++;
                    stackR[top] = nr;
                    stackC[top] = nc;
                }
            }
        }
        return closed;
    }
}
"""

S["1255_maximum_score_words_formed_by_letters"] = r"""// LeetCode 1255 - Maximum Score Words Formed by Letters
// https://leetcode.com/problems/maximum-score-words-formed-by-letters/

import java.util.*;

class Solution {
    public int maxScoreWords(String[] words, char[] letters, int[] score) {
        int[] available = new int[26];
        for (char ch : letters) available[ch - 'a']++;
        int[][] counts = new int[words.length][26];
        int[] values = new int[words.length];
        for (int i = 0; i < words.length; i++) {
            for (char ch : words[i].toCharArray()) counts[i][ch - 'a']++;
            for (char ch : words[i].toCharArray()) values[i] += score[ch - 'a'];
        }
        return dfs(0, words.length, counts, values, available);
    }

    private int dfs(int i, int n, int[][] counts, int[] values, int[] available) {
        if (i == n) return 0;
        int best = dfs(i + 1, n, counts, values, available);
        if (canUse(counts[i], available)) {
            apply(counts[i], available, -1);
            best = Math.max(best, values[i] + dfs(i + 1, n, counts, values, available));
            apply(counts[i], available, 1);
        }
        return best;
    }

    private boolean canUse(int[] need, int[] available) {
        for (int j = 0; j < 26; j++) if (need[j] > available[j]) return false;
        return true;
    }

    private void apply(int[] need, int[] available, int sign) {
        for (int j = 0; j < 26; j++) available[j] += sign * need[j];
    }
}
"""

S["1256_encode_number"] = r"""// LeetCode 1256 - Encode Number
// https://leetcode.com/problems/encode-number/

class Solution {
    public String encode(int num) {
        return Integer.toBinaryString(num + 1).substring(1);
    }
}
"""

S["1257_smallest_common_region"] = r"""// LeetCode 1257 - Smallest Common Region
// https://leetcode.com/problems/smallest-common-region/

import java.util.*;

class Solution {
    public String findSmallestRegion(List<List<String>> regions, String region1, String region2) {
        Map<String, String> parent = new HashMap<>();
        for (List<String> group : regions) {
            for (int i = 1; i < group.size(); i++) parent.put(group.get(i), group.get(0));
        }
        Set<String> ancestors = new HashSet<>();
        while (region1 != null) {
            ancestors.add(region1);
            region1 = parent.get(region1);
        }
        while (!ancestors.contains(region2)) region2 = parent.get(region2);
        return region2;
    }
}
"""

S["1258_synonymous_sentences"] = r"""// LeetCode 1258 - Synonymous Sentences
// https://leetcode.com/problems/synonymous-sentences/

import java.util.*;

class Solution {
    public List<String> generateSentences(List<List<String>> synonyms, String text) {
        Map<String, String> parent = new HashMap<>();
        for (List<String> pair : synonyms) {
            String a = find(pair.get(0), parent), b = find(pair.get(1), parent);
            parent.put(a, b);
        }
        Map<String, List<String>> groups = new HashMap<>();
        for (String word : parent.keySet()) {
            groups.computeIfAbsent(find(word, parent), k -> new ArrayList<>()).add(word);
        }
        for (List<String> g : groups.values()) Collections.sort(g);
        String[] tokens = text.split(" ");
        List<List<String>> choices = new ArrayList<>();
        for (String w : tokens) {
            if (parent.containsKey(w)) choices.add(groups.get(find(w, parent)));
            else choices.add(List.of(w));
        }
        List<String> answer = new ArrayList<>();
        backtrack(choices, 0, new ArrayList<>(), answer);
        return answer;
    }

    private String find(String x, Map<String, String> parent) {
        parent.putIfAbsent(x, x);
        if (!parent.get(x).equals(x)) parent.put(x, find(parent.get(x), parent));
        return parent.get(x);
    }

    private void backtrack(List<List<String>> choices, int idx, List<String> cur, List<String> answer) {
        if (idx == choices.size()) {
            answer.add(String.join(" ", cur));
            return;
        }
        for (String w : choices.get(idx)) {
            cur.add(w);
            backtrack(choices, idx + 1, cur, answer);
            cur.remove(cur.size() - 1);
        }
    }
}
"""

S["1259_handshakes_that_dont_cross"] = r"""// LeetCode 1259 - Handshakes That Don't Cross
// https://leetcode.com/problems/handshakes-that-dont-cross/

class Solution {
    public int numberOfWays(int numPeople) {
        int mod = 1_000_000_007;
        int[] dp = new int[numPeople + 1];
        dp[0] = 1;
        for (int people = 2; people <= numPeople; people += 2) {
            long ways = 0;
            for (int left = 0; left < people; left += 2) {
                ways = (ways + (long) dp[left] * dp[people - 2 - left]) % mod;
            }
            dp[people] = (int) ways;
        }
        return dp[numPeople];
    }
}
"""

S["1260_shift_2d_grid"] = r"""// LeetCode 1260 - Shift 2D Grid
// https://leetcode.com/problems/shift-2d-grid/

import java.util.*;

class Solution {
    public List<List<Integer>> shiftGrid(int[][] grid, int k) {
        int m = grid.length, n = grid[0].length;
        List<Integer> flat = new ArrayList<>();
        for (int[] row : grid) for (int x : row) flat.add(x);
        k %= flat.size();
        if (k > 0) {
            List<Integer> rotated = new ArrayList<>(flat.subList(flat.size() - k, flat.size()));
            rotated.addAll(flat.subList(0, flat.size() - k));
            flat = rotated;
        }
        List<List<Integer>> answer = new ArrayList<>();
        for (int i = 0; i < m; i++) {
            answer.add(new ArrayList<>(flat.subList(i * n, (i + 1) * n)));
        }
        return answer;
    }
}
"""


def main() -> None:
    for folder, content in S.items():
        path = ROOT / folder / "Solution.java"
        path.write_text(content + "\n", encoding="utf-8")
        print(f"Wrote {path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
