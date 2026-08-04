#!/usr/bin/env python3
"""Port stub Solution.java files for problems 1175-1220 (non-SQL)."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

SQL_NUMBERS = {
    1179, 1193, 1194, 1204, 1205, 1211, 1212,
}

SOLUTIONS: dict[str, str] = {}


def _add(name: str, content: str) -> None:
    SOLUTIONS[name] = content.strip() + "\n"


_add(
    "1175_prime_arrangements",
    r"""// LeetCode 1175 - Prime Arrangements
// https://leetcode.com/problems/prime-arrangements/

class Solution {
    public int numPrimeArrangements(int n) {
        final int MOD = 1_000_000_007;
        int primes = 0;
        for (int i = 1; i <= n; i++) {
            if (isPrime(i)) primes++;
        }
        return (int) (fact(primes, MOD) * fact(n - primes, MOD) % MOD);
    }

    private boolean isPrime(int x) {
        if (x < 2) return false;
        for (int d = 2; d * d <= x; d++) {
            if (x % d == 0) return false;
        }
        return true;
    }

    private long fact(int x, int mod) {
        long ans = 1;
        for (int i = 2; i <= x; i++) {
            ans = ans * i % mod;
        }
        return ans;
    }
}""",
)

_add(
    "1176_diet_plan_performance",
    r"""// LeetCode 1176 - Diet Plan Performance
// https://leetcode.com/problems/diet-plan-performance/

class Solution {
    public int dietPlanPerformance(int[] calories, int k, int lower, int upper) {
        int window = 0;
        for (int i = 0; i < k; i++) window += calories[i];
        int ans = 0;
        if (window < lower) ans--;
        else if (window > upper) ans++;
        for (int i = k; i < calories.length; i++) {
            window += calories[i] - calories[i - k];
            if (window < lower) ans--;
            else if (window > upper) ans++;
        }
        return ans;
    }
}""",
)

_add(
    "1177_can_make_palindrome_from_substring",
    r"""// LeetCode 1177 - Can Make Palindrome from Substring
// https://leetcode.com/problems/can-make-palindrome-from-substring/

import java.util.*;

class Solution {
    public List<Boolean> canMakePaliQueries(String s, int[][] queries) {
        int[] prefix = new int[s.length() + 1];
        int mask = 0;
        for (int i = 0; i < s.length(); i++) {
            mask ^= 1 << (s.charAt(i) - 'a');
            prefix[i + 1] = mask;
        }
        List<Boolean> ans = new ArrayList<>();
        for (int[] q : queries) {
            int bits = Integer.bitCount(prefix[q[1] + 1] ^ prefix[q[0]]);
            ans.add(bits / 2 <= q[2]);
        }
        return ans;
    }
}""",
)

_add(
    "1178_number_of_valid_words_for_each_puzzle",
    r"""// LeetCode 1178 - Number of Valid Words for Each Puzzle
// https://leetcode.com/problems/number-of-valid-words-for-each-puzzle/

import java.util.*;

class Solution {
    public List<Integer> findNumOfValidWords(String[] words, String[] puzzles) {
        Map<Integer, Integer> freq = new HashMap<>();
        for (String w : words) {
            freq.merge(maskOf(w), 1, Integer::sum);
        }
        List<Integer> ans = new ArrayList<>();
        for (String puzzle : puzzles) {
            int first = 1 << (puzzle.charAt(0) - 'a');
            int full = maskOf(puzzle);
            int sub = full;
            int total = 0;
            while (true) {
                if ((sub & first) != 0) total += freq.getOrDefault(sub, 0);
                if (sub == 0) break;
                sub = (sub - 1) & full;
            }
            ans.add(total);
        }
        return ans;
    }

    private int maskOf(String s) {
        int mask = 0;
        for (char ch : s.toCharArray()) mask |= 1 << (ch - 'a');
        return mask;
    }
}""",
)

_add(
    "1180_count_substrings_with_only_one_distinct_letter",
    r"""// LeetCode 1180 - Count Substrings with Only One Distinct Letter
// https://leetcode.com/problems/count-substrings-with-only-one-distinct-letter/

class Solution {
    public int countLetters(String s) {
        int ans = 1;
        int length = 1;
        for (int i = 1; i < s.length(); i++) {
            length = s.charAt(i) == s.charAt(i - 1) ? length + 1 : 1;
            ans += length;
        }
        return ans;
    }
}""",
)

_add(
    "1181_before_and_after_puzzle",
    r"""// LeetCode 1181 - Before and After Puzzle
// https://leetcode.com/problems/before-and-after-puzzle/

import java.util.*;

class Solution {
    public List<String> beforeAndAfterPuzzles(String[] phrases) {
        String[][] split = new String[phrases.length][];
        for (int i = 0; i < phrases.length; i++) split[i] = phrases[i].split(" ");
        Set<String> result = new TreeSet<>();
        for (int i = 0; i < split.length; i++) {
            for (int j = 0; j < split.length; j++) {
                if (i == j) continue;
                if (split[i][split[i].length - 1].equals(split[j][0])) {
                    StringBuilder sb = new StringBuilder();
                    for (int k = 0; k < split[i].length; k++) {
                        if (k > 0) sb.append(' ');
                        sb.append(split[i][k]);
                    }
                    for (int k = 1; k < split[j].length; k++) {
                        sb.append(' ').append(split[j][k]);
                    }
                    result.add(sb.toString());
                }
            }
        }
        return new ArrayList<>(result);
    }
}""",
)

_add(
    "1182_shortest_distance_to_target_color",
    r"""// LeetCode 1182 - Shortest Distance to Target Color
// https://leetcode.com/problems/shortest-distance-to-target-color/

import java.util.*;

class Solution {
    public List<Integer> shortestDistanceColor(int[] colors, int[][] queries) {
        Map<Integer, List<Integer>> pos = new HashMap<>();
        for (int i = 0; i < colors.length; i++) {
            pos.computeIfAbsent(colors[i], k -> new ArrayList<>()).add(i);
        }
        List<Integer> ans = new ArrayList<>();
        for (int[] q : queries) {
            int i = q[0];
            int c = q[1];
            if (!pos.containsKey(c)) {
                ans.add(-1);
                continue;
            }
            List<Integer> arr = pos.get(c);
            int idx = Collections.binarySearch(arr, i);
            if (idx < 0) idx = -idx - 1;
            int best = Integer.MAX_VALUE;
            if (idx < arr.size()) best = Math.min(best, arr.get(idx) - i);
            if (idx > 0) best = Math.min(best, i - arr.get(idx - 1));
            ans.add(best == Integer.MAX_VALUE ? -1 : best);
        }
        return ans;
    }
}""",
)

_add(
    "1183_maximum_number_of_ones",
    r"""// LeetCode 1183 - Maximum Number of Ones
// https://leetcode.com/problems/maximum-number-of-ones/

import java.util.*;

class Solution {
    public int maximumNumberOfOnes(int width, int height, int sideLength, int maxOnes) {
        List<Integer> counts = new ArrayList<>();
        for (int r = 0; r < sideLength; r++) {
            for (int c = 0; c < sideLength; c++) {
                int rows = (height - r + sideLength - 1) / sideLength;
                int cols = (width - c + sideLength - 1) / sideLength;
                counts.add(rows * cols);
            }
        }
        counts.sort(Collections.reverseOrder());
        int ans = 0;
        for (int i = 0; i < maxOnes && i < counts.size(); i++) ans += counts.get(i);
        return ans;
    }
}""",
)

_add(
    "1184_distance_between_bus_stops",
    r"""// LeetCode 1184 - Distance Between Bus Stops
// https://leetcode.com/problems/distance-between-bus-stops/

class Solution {
    public int distanceBetweenBusStops(int[] distance, int start, int destination) {
        if (start > destination) {
            int t = start;
            start = destination;
            destination = t;
        }
        int clockwise = 0;
        int total = 0;
        for (int i = 0; i < distance.length; i++) {
            total += distance[i];
            if (i >= start && i < destination) clockwise += distance[i];
        }
        return Math.min(clockwise, total - clockwise);
    }
}""",
)

_add(
    "1185_day_of_the_week",
    r"""// LeetCode 1185 - Day of the Week
// https://leetcode.com/problems/day-of-the-week/

class Solution {
    public String dayOfTheWeek(int day, int month, int year) {
        int[] t = {0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4};
        int y = year;
        if (month < 3) y--;
        int w = (y + y / 4 - y / 100 + y / 400 + t[month - 1] + day) % 7;
        String[] days = {
            "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"
        };
        return days[w];
    }
}""",
)

_add(
    "1186_maximum_subarray_sum_with_one_deletion",
    r"""// LeetCode 1186 - Maximum Subarray Sum with One Deletion
// https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/

class Solution {
    public int maximumSum(int[] arr) {
        int keep = arr[0];
        int delete = arr[0];
        int ans = arr[0];
        for (int i = 1; i < arr.length; i++) {
            int x = arr[i];
            delete = Math.max(keep, delete + x);
            keep = Math.max(keep + x, x);
            ans = Math.max(ans, Math.max(keep, delete));
        }
        return ans;
    }
}""",
)

_add(
    "1187_make_array_strictly_increasing",
    r"""// LeetCode 1187 - Make Array Strictly Increasing
// https://leetcode.com/problems/make-array-strictly-increasing/

import java.util.*;

class Solution {
    public int makeArrayIncreasing(int[] arr1, int[] arr2) {
        TreeSet<Integer> set = new TreeSet<>();
        for (int x : arr2) set.add(x);
        Integer[] sorted = set.toArray(new Integer[0]);
        Map<Integer, Integer> dp = new HashMap<>();
        dp.put(-1, 0);
        for (int num : arr1) {
            Map<Integer, Integer> next = new HashMap<>();
            for (Map.Entry<Integer, Integer> e : dp.entrySet()) {
                int prev = e.getKey();
                int ops = e.getValue();
                if (num > prev) next.merge(num, ops, Math::min);
                int idx = upperBound(sorted, prev);
                if (idx < sorted.length) {
                    int chosen = sorted[idx];
                    next.merge(chosen, ops + 1, Math::min);
                }
            }
            dp = next;
            if (dp.isEmpty()) return -1;
        }
        int ans = Integer.MAX_VALUE;
        for (int v : dp.values()) ans = Math.min(ans, v);
        return ans;
    }

    private int upperBound(Integer[] a, int target) {
        int lo = 0;
        int hi = a.length;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (a[mid] <= target) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    }
}""",
)

_add(
    "1188_design_bounded_blocking_queue",
    r"""// LeetCode 1188 - Design Bounded Blocking Queue
// https://leetcode.com/problems/design-bounded-blocking-queue/

import java.util.*;
import java.util.concurrent.*;

class BoundedBlockingQueue {
    private final Deque<Integer> queue = new ArrayDeque<>();
    private final Semaphore notFull;
    private final Semaphore notEmpty = new Semaphore(0);
    private final Object lock = new Object();

    public BoundedBlockingQueue(int capacity) {
        this.notFull = new Semaphore(capacity);
    }

    public void enqueue(int element) throws InterruptedException {
        notFull.acquire();
        synchronized (lock) {
            queue.addLast(element);
        }
        notEmpty.release();
    }

    public int dequeue() throws InterruptedException {
        notEmpty.acquire();
        int value;
        synchronized (lock) {
            value = queue.removeFirst();
        }
        notFull.release();
        return value;
    }

    public int size() {
        synchronized (lock) {
            return queue.size();
        }
    }
}""",
)

_add(
    "1189_maximum_number_of_balloons",
    r"""// LeetCode 1189 - Maximum Number of Balloons
// https://leetcode.com/problems/maximum-number-of-balloons/

class Solution {
    public int maxNumberOfBalloons(String text) {
        int[] count = new int[26];
        for (char c : text.toCharArray()) count[c - 'a']++;
        return Math.min(
            Math.min(count['b' - 'a'], count['a' - 'a']),
            Math.min(Math.min(count['l' - 'a'] / 2, count['o' - 'a'] / 2), count['n' - 'a'])
        );
    }
}""",
)

_add(
    "1190_reverse_substrings_between_each_pair_of_parentheses",
    r"""// LeetCode 1190 - Reverse Substrings Between Each Pair of Parentheses
// https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/

import java.util.*;

class Solution {
    public String reverseParentheses(String s) {
        Deque<Character> stack = new ArrayDeque<>();
        for (char ch : s.toCharArray()) {
            if (ch == ')') {
                List<Character> chunk = new ArrayList<>();
                while (!stack.isEmpty() && stack.peek() != '(') chunk.add(stack.pop());
                stack.pop();
                for (char c : chunk) stack.push(c);
            } else {
                stack.push(ch);
            }
        }
        StringBuilder sb = new StringBuilder();
        while (!stack.isEmpty()) sb.append(stack.removeLast());
        return sb.toString();
    }
}""",
)

_add(
    "1191_k_concatenation_maximum_sum",
    r"""// LeetCode 1191 - K-Concatenation Maximum Sum
// https://leetcode.com/problems/k-concatenation-maximum-sum/

class Solution {
    public int kConcatenationMaxSum(int[] arr, int k) {
        final int MOD = 1_000_000_007;
        long one = kadane(arr);
        if (k == 1) return (int) (one % MOD);
        int[] twice = new int[arr.length * 2];
        System.arraycopy(arr, 0, twice, 0, arr.length);
        System.arraycopy(arr, 0, twice, arr.length, arr.length);
        long two = kadane(twice);
        long total = 0;
        for (int x : arr) total += x;
        long ans = total > 0 ? Math.max(one, two + total * (k - 2)) : Math.max(one, two);
        return (int) (ans % MOD);
    }

    private long kadane(int[] nums) {
        long best = 0;
        long cur = 0;
        for (int x : nums) {
            cur = Math.max(0, cur + x);
            best = Math.max(best, cur);
        }
        return best;
    }
}""",
)

_add(
    "1192_critical_connections_in_a_network",
    r"""// LeetCode 1192 - Critical Connections in a Network
// https://leetcode.com/problems/critical-connections-in-a-network/

import java.util.*;

class Solution {
    private int time = 0;

    public List<List<Integer>> criticalConnections(int n, List<List<Integer>> connections) {
        List<Integer>[] graph = new List[n];
        for (int i = 0; i < n; i++) graph[i] = new ArrayList<>();
        for (List<Integer> e : connections) {
            graph[e.get(0)].add(e.get(1));
            graph[e.get(1)].add(e.get(0));
        }
        int[] disc = new int[n];
        int[] low = new int[n];
        Arrays.fill(disc, -1);
        List<List<Integer>> bridges = new ArrayList<>();
        dfs(0, -1, graph, disc, low, bridges);
        for (List<Integer> b : bridges) {
            if (b.get(0) > b.get(1)) Collections.swap(b, 0, 1);
        }
        return bridges;
    }

    private void dfs(
        int node,
        int parent,
        List<Integer>[] graph,
        int[] disc,
        int[] low,
        List<List<Integer>> bridges
    ) {
        disc[node] = low[node] = time++;
        for (int nxt : graph[node]) {
            if (nxt == parent) continue;
            if (disc[nxt] == -1) {
                dfs(nxt, node, graph, disc, low, bridges);
                low[node] = Math.min(low[node], low[nxt]);
                if (low[nxt] > disc[node]) {
                    bridges.add(new ArrayList<>(Arrays.asList(node, nxt)));
                }
            } else {
                low[node] = Math.min(low[node], disc[nxt]);
            }
        }
    }
}""",
)

_add(
    "1195_fizz_buzz_multithreaded",
    r"""// LeetCode 1195 - Fizz Buzz Multithreaded
// https://leetcode.com/problems/fizz-buzz-multithreaded/

import java.util.function.IntConsumer;
import java.util.function.IntPredicate;

class FizzBuzz {
    private final int n;
    private int current = 1;
    private final Object lock = new Object();

    public FizzBuzz(int n) {
        this.n = n;
    }

    public void fizz(Runnable printFizz) throws InterruptedException {
        run(x -> x % 3 == 0 && x % 5 != 0, printFizz);
    }

    public void buzz(Runnable printBuzz) throws InterruptedException {
        run(x -> x % 5 == 0 && x % 3 != 0, printBuzz);
    }

    public void fizzbuzz(Runnable printFizzBuzz) throws InterruptedException {
        run(x -> x % 15 == 0, printFizzBuzz);
    }

    public void number(IntConsumer printNumber) throws InterruptedException {
        run(x -> x % 3 != 0 && x % 5 != 0, () -> printNumber.accept(current));
    }

    private void run(IntPredicate pred, Runnable action) throws InterruptedException {
        synchronized (lock) {
            while (current <= n) {
                if (pred.test(current)) {
                    action.run();
                    current++;
                    lock.notifyAll();
                } else {
                    lock.wait();
                }
            }
        }
    }
}""",
)

_add(
    "1196_how_many_apples_can_you_put_into_the_basket",
    r"""// LeetCode 1196 - How Many Apples Can You Put into the Basket
// https://leetcode.com/problems/how-many-apples-can-you-put-into-the-basket/

import java.util.*;

class Solution {
    public int maxNumberOfApples(int[] weight) {
        Arrays.sort(weight);
        int total = 0;
        for (int i = 0; i < weight.length; i++) {
            total += weight[i];
            if (total > 5000) return i;
        }
        return weight.length;
    }
}""",
)

_add(
    "1197_minimum_knight_moves",
    r"""// LeetCode 1197 - Minimum Knight Moves
// https://leetcode.com/problems/minimum-knight-moves/

import java.util.*;

class Solution {
    private final Map<String, Integer> memo = new HashMap<>();

    public int minKnightMoves(int x, int y) {
        return dfs(Math.abs(x), Math.abs(y));
    }

    private int dfs(int a, int b) {
        if (a + b == 0) return 0;
        if (a + b == 2) return 2;
        String key = a + "," + b;
        if (memo.containsKey(key)) return memo.get(key);
        int ans = Math.min(dfs(Math.abs(a - 1), Math.abs(b - 2)), dfs(Math.abs(a - 2), Math.abs(b - 1))) + 1;
        memo.put(key, ans);
        return ans;
    }
}""",
)

_add(
    "1198_find_smallest_common_element_in_all_rows",
    r"""// LeetCode 1198 - Find Smallest Common Element in All Rows
// https://leetcode.com/problems/find-smallest-common-element-in-all-rows/

import java.util.*;

class Solution {
    public int smallestCommonElement(int[][] mat) {
        Set<Integer> common = new HashSet<>();
        for (int x : mat[0]) common.add(x);
        for (int i = 1; i < mat.length; i++) {
            Set<Integer> row = new HashSet<>();
            for (int x : mat[i]) row.add(x);
            common.retainAll(row);
            if (common.isEmpty()) return -1;
        }
        int ans = Integer.MAX_VALUE;
        for (int x : common) ans = Math.min(ans, x);
        return ans;
    }
}""",
)

_add(
    "1199_minimum_time_to_build_blocks",
    r"""// LeetCode 1199 - Minimum Time to Build Blocks
// https://leetcode.com/problems/minimum-time-to-build-blocks/

import java.util.*;

class Solution {
    public int minBuildTime(int[] blocks, int split) {
        PriorityQueue<Integer> heap = new PriorityQueue<>();
        for (int b : blocks) heap.offer(b);
        while (heap.size() > 1) {
            heap.poll();
            heap.offer(heap.poll() + split);
        }
        return heap.peek();
    }
}""",
)

_add(
    "1200_minimum_absolute_difference",
    r"""// LeetCode 1200 - Minimum Absolute Difference
// https://leetcode.com/problems/minimum-absolute-difference/

import java.util.*;

class Solution {
    public List<List<Integer>> minimumAbsDifference(int[] arr) {
        Arrays.sort(arr);
        int best = Integer.MAX_VALUE;
        for (int i = 0; i + 1 < arr.length; i++) {
            best = Math.min(best, arr[i + 1] - arr[i]);
        }
        List<List<Integer>> ans = new ArrayList<>();
        for (int i = 0; i + 1 < arr.length; i++) {
            if (arr[i + 1] - arr[i] == best) {
                ans.add(Arrays.asList(arr[i], arr[i + 1]));
            }
        }
        return ans;
    }
}""",
)

_add(
    "1201_ugly_number_iii",
    r"""// LeetCode 1201 - Ugly Number III
// https://leetcode.com/problems/ugly-number-iii/

class Solution {
    public int nthUglyNumber(int n, int a, int b, int c) {
        long ab = lcm(a, b);
        long ac = lcm(a, c);
        long bc = lcm(b, c);
        long abc = lcm(ab, c);
        long lo = 1;
        long hi = 2_000_000_000L;
        while (lo < hi) {
            long mid = (lo + hi) / 2;
            if (count(mid, a, b, c, ab, ac, bc, abc) >= n) hi = mid;
            else lo = mid + 1;
        }
        return (int) lo;
    }

    private long gcd(long x, long y) {
        while (y != 0) {
            long t = x % y;
            x = y;
            y = t;
        }
        return x;
    }

    private long lcm(long x, long y) {
        return x / gcd(x, y) * y;
    }

    private long count(long x, int a, int b, int c, long ab, long ac, long bc, long abc) {
        return x / a + x / b + x / c - x / ab - x / ac - x / bc + x / abc;
    }
}""",
)

_add(
    "1202_smallest_string_with_swaps",
    r"""// LeetCode 1202 - Smallest String With Swaps
// https://leetcode.com/problems/smallest-string-with-swaps/

import java.util.*;

class Solution {
    public String smallestStringWithSwaps(String s, int[][] pairs) {
        int n = s.length();
        int[] parent = new int[n];
        for (int i = 0; i < n; i++) parent[i] = i;
        for (int[] p : pairs) {
            int ra = find(parent, p[0]);
            int rb = find(parent, p[1]);
            parent[ra] = rb;
        }
        Map<Integer, List<Character>> groups = new HashMap<>();
        for (int i = 0; i < n; i++) {
            groups.computeIfAbsent(find(parent, i), k -> new ArrayList<>()).add(s.charAt(i));
        }
        for (List<Character> chars : groups.values()) {
            chars.sort(Collections.reverseOrder());
        }
        StringBuilder sb = new StringBuilder(n);
        for (int i = 0; i < n; i++) {
            List<Character> list = groups.get(find(parent, i));
            sb.append(list.remove(list.size() - 1));
        }
        return sb.toString();
    }

    private int find(int[] parent, int x) {
        while (x != parent[x]) {
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    }
}""",
)

_add(
    "1203_sort_items_by_groups_respecting_dependencies",
    r"""// LeetCode 1203 - Sort Items by Groups Respecting Dependencies
// https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/

import java.util.*;

class Solution {
    public int[] sortItems(int n, int m, int[] group, List<List<Integer>> beforeItems) {
        for (int i = 0; i < n; i++) {
            if (group[i] == -1) {
                group[i] = m;
                m++;
            }
        }
        List<Integer>[] itemGraph = new List[n];
        int[] itemIndeg = new int[n];
        for (int i = 0; i < n; i++) itemGraph[i] = new ArrayList<>();
        Set<Integer>[] groupGraph = new Set[m];
        int[] groupIndeg = new int[m];
        for (int i = 0; i < m; i++) groupGraph[i] = new HashSet<>();
        for (int v = 0; v < n; v++) {
            for (int u : beforeItems.get(v)) {
                itemGraph[u].add(v);
                itemIndeg[v]++;
                if (group[u] != group[v] && groupGraph[group[u]].add(group[v])) {
                    groupIndeg[group[v]]++;
                }
            }
        }
        List<Integer> items = topo(itemGraph, itemIndeg);
        List<Integer>[] groupAdj = new List[m];
        for (int i = 0; i < m; i++) groupAdj[i] = new ArrayList<>(groupGraph[i]);
        List<Integer> groups = topo(groupAdj, groupIndeg);
        if (items.isEmpty() || groups.isEmpty()) return new int[0];
        List<Integer>[] buckets = new List[m];
        for (int i = 0; i < m; i++) buckets[i] = new ArrayList<>();
        for (int item : items) buckets[group[item]].add(item);
        List<Integer> ans = new ArrayList<>();
        for (int g : groups) ans.addAll(buckets[g]);
        return ans.stream().mapToInt(Integer::intValue).toArray();
    }

    private List<Integer> topo(List<Integer>[] graph, int[] indeg) {
        ArrayDeque<Integer> q = new ArrayDeque<>();
        for (int i = 0; i < graph.length; i++) {
            if (indeg[i] == 0) q.add(i);
        }
        List<Integer> order = new ArrayList<>();
        while (!q.isEmpty()) {
            int u = q.removeFirst();
            order.add(u);
            for (int v : graph[u]) {
                indeg[v]--;
                if (indeg[v] == 0) q.add(v);
            }
        }
        return order.size() == graph.length ? order : Collections.emptyList();
    }
}""",
)

_add(
    "1206_design_skiplist",
    r"""// LeetCode 1206 - Design Skiplist
// https://leetcode.com/problems/design-skiplist/

import java.util.*;

class Skiplist {
    private final List<Integer> values = new ArrayList<>();

    public boolean search(int target) {
        int i = Collections.binarySearch(values, target);
        return i >= 0;
    }

    public void add(int num) {
        int i = Collections.binarySearch(values, num);
        if (i < 0) i = -i - 1;
        values.add(i, num);
    }

    public boolean erase(int num) {
        int i = Collections.binarySearch(values, num);
        if (i < 0) return false;
        values.remove(i);
        return true;
    }
}""",
)

_add(
    "1207_unique_number_of_occurrences",
    r"""// LeetCode 1207 - Unique Number of Occurrences
// https://leetcode.com/problems/unique-number-of-occurrences/

import java.util.*;

class Solution {
    public boolean uniqueOccurrences(int[] arr) {
        Map<Integer, Integer> freq = new HashMap<>();
        for (int x : arr) freq.merge(x, 1, Integer::sum);
        Set<Integer> seen = new HashSet<>();
        for (int count : freq.values()) {
            if (!seen.add(count)) return false;
        }
        return true;
    }
}""",
)

_add(
    "1208_get_equal_substrings_within_budget",
    r"""// LeetCode 1208 - Get Equal Substrings Within Budget
// https://leetcode.com/problems/get-equal-substrings-within-budget/

class Solution {
    public int equalSubstring(String s, String t, int maxCost) {
        int left = 0;
        int cost = 0;
        int answer = 0;
        for (int right = 0; right < s.length(); right++) {
            cost += Math.abs(s.charAt(right) - t.charAt(right));
            while (cost > maxCost) {
                cost -= Math.abs(s.charAt(left) - t.charAt(left));
                left++;
            }
            answer = Math.max(answer, right - left + 1);
        }
        return answer;
    }
}""",
)

_add(
    "1209_remove_all_adjacent_duplicates_in_string_ii",
    r"""// LeetCode 1209 - Remove All Adjacent Duplicates in String II
// https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/

import java.util.*;

class Solution {
    public String removeDuplicates(String s, int k) {
        Deque<int[]> stack = new ArrayDeque<>();
        for (char ch : s.toCharArray()) {
            if (!stack.isEmpty() && stack.peek()[0] == ch) {
                stack.peek()[1]++;
            } else {
                stack.push(new int[] {ch, 1});
            }
            if (stack.peek()[1] == k) stack.pop();
        }
        StringBuilder sb = new StringBuilder();
        while (!stack.isEmpty()) {
            int[] top = stack.removeLast();
            sb.append(String.valueOf((char) top[0]).repeat(top[1]));
        }
        return sb.toString();
    }
}""",
)

_add(
    "1210_minimum_moves_to_reach_target_with_rotations",
    r"""// LeetCode 1210 - Minimum Moves to Reach Target With Rotations
// https://leetcode.com/problems/minimum-moves-to-reach-target-with-rotations/

import java.util.*;

class Solution {
    public int minimumMoves(int[][] grid) {
        int n = grid.length;
        int[] start = {0, 0, 0};
        int[] target = {n - 1, n - 2, 0};
        ArrayDeque<int[]> q = new ArrayDeque<>();
        q.add(new int[] {start[0], start[1], start[2], 0});
        Set<String> seen = new HashSet<>();
        seen.add(key(start[0], start[1], start[2]));
        while (!q.isEmpty()) {
            int[] cur = q.removeFirst();
            int r = cur[0];
            int c = cur[1];
            int orient = cur[2];
            int moves = cur[3];
            if (r == target[0] && c == target[1] && orient == target[2]) return moves;
            List<int[]> next = new ArrayList<>();
            if (orient == 0) {
                if (c + 2 < n && grid[r][c + 2] == 0) next.add(new int[] {r, c + 1, 0});
                if (r + 1 < n && grid[r + 1][c] == 0 && grid[r + 1][c + 1] == 0) {
                    next.add(new int[] {r + 1, c, 0});
                    next.add(new int[] {r, c, 1});
                }
            } else {
                if (r + 2 < n && grid[r + 2][c] == 0) next.add(new int[] {r + 1, c, 1});
                if (c + 1 < n && grid[r][c + 1] == 0 && grid[r + 1][c + 1] == 0) {
                    next.add(new int[] {r, c + 1, 1});
                    next.add(new int[] {r, c, 0});
                }
            }
            for (int[] state : next) {
                String k = key(state[0], state[1], state[2]);
                if (seen.add(k)) {
                    q.add(new int[] {state[0], state[1], state[2], moves + 1});
                }
            }
        }
        return -1;
    }

    private String key(int r, int c, int orient) {
        return r + "," + c + "," + orient;
    }
}""",
)

_add(
    "1213_intersection_of_three_sorted_arrays",
    r"""// LeetCode 1213 - Intersection of Three Sorted Arrays
// https://leetcode.com/problems/intersection-of-three-sorted-arrays/

import java.util.*;

class Solution {
    public List<Integer> arraysIntersection(int[] arr1, int[] arr2, int[] arr3) {
        Set<Integer> common = new HashSet<>();
        for (int x : arr1) common.add(x);
        Set<Integer> s2 = new HashSet<>();
        for (int x : arr2) s2.add(x);
        common.retainAll(s2);
        Set<Integer> s3 = new HashSet<>();
        for (int x : arr3) s3.add(x);
        common.retainAll(s3);
        List<Integer> ans = new ArrayList<>(common);
        Collections.sort(ans);
        return ans;
    }
}""",
)

_add(
    "1214_two_sum_bsts",
    r"""// LeetCode 1214 - Two Sum BSTs
// https://leetcode.com/problems/two-sum-bsts/

import java.util.*;

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode() {}

    TreeNode(int val) {
        this.val = val;
    }

    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class Solution {
    public boolean twoSumBSTs(TreeNode root1, TreeNode root2, int target) {
        Set<Integer> values = new HashSet<>();
        Deque<TreeNode> stack = new ArrayDeque<>();
        if (root1 != null) stack.push(root1);
        while (!stack.isEmpty()) {
            TreeNode node = stack.pop();
            values.add(node.val);
            if (node.left != null) stack.push(node.left);
            if (node.right != null) stack.push(node.right);
        }
        stack.clear();
        if (root2 != null) stack.push(root2);
        while (!stack.isEmpty()) {
            TreeNode node = stack.pop();
            if (values.contains(target - node.val)) return true;
            if (node.left != null) stack.push(node.left);
            if (node.right != null) stack.push(node.right);
        }
        return false;
    }
}""",
)

_add(
    "1215_stepping_numbers",
    r"""// LeetCode 1215 - Stepping Numbers
// https://leetcode.com/problems/stepping-numbers/

import java.util.*;

class Solution {
    public List<Integer> countSteppingNumbers(int low, int high) {
        List<Integer> answer = new ArrayList<>();
        if (low == 0) answer.add(0);
        ArrayDeque<Integer> q = new ArrayDeque<>();
        for (int i = 1; i < 10; i++) q.add(i);
        while (!q.isEmpty()) {
            int x = q.removeFirst();
            if (x > high) continue;
            if (x >= low) answer.add(x);
            int last = x % 10;
            if (last > 0) q.add(x * 10 + last - 1);
            if (last < 9) q.add(x * 10 + last + 1);
        }
        Collections.sort(answer);
        return answer;
    }
}""",
)

_add(
    "1216_valid_palindrome_iii",
    r"""// LeetCode 1216 - Valid Palindrome III
// https://leetcode.com/problems/valid-palindrome-iii/

class Solution {
    public boolean isValidPalindrome(String s, int k) {
        int n = s.length();
        int[] dp = new int[n];
        for (int i = n - 1; i >= 0; i--) {
            int previous = 0;
            for (int j = i + 1; j < n; j++) {
                int old = dp[j];
                if (s.charAt(i) == s.charAt(j)) dp[j] = previous;
                else dp[j] = 1 + Math.min(dp[j], dp[j - 1]);
                previous = old;
            }
        }
        return n == 0 || dp[n - 1] <= k;
    }
}""",
)

_add(
    "1217_minimum_cost_to_move_chips_to_the_same_position",
    r"""// LeetCode 1217 - Minimum Cost to Move Chips to The Same Position
// https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/

class Solution {
    public int minCostToMoveChips(int[] position) {
        int odd = 0;
        for (int x : position) {
            if ((x & 1) == 1) odd++;
        }
        return Math.min(odd, position.length - odd);
    }
}""",
)

_add(
    "1218_longest_arithmetic_subsequence_of_given_difference",
    r"""// LeetCode 1218 - Longest Arithmetic Subsequence of Given Difference
// https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/

import java.util.*;

class Solution {
    public int longestSubsequence(int[] arr, int difference) {
        Map<Integer, Integer> dp = new HashMap<>();
        int ans = 0;
        for (int x : arr) {
            int len = dp.getOrDefault(x - difference, 0) + 1;
            dp.put(x, len);
            ans = Math.max(ans, len);
        }
        return ans;
    }
}""",
)

_add(
    "1219_path_with_maximum_gold",
    r"""// LeetCode 1219 - Path with Maximum Gold
// https://leetcode.com/problems/path-with-maximum-gold/

class Solution {
    public int getMaximumGold(int[][] grid) {
        int rows = grid.length;
        int cols = grid[0].length;
        int ans = 0;
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (grid[r][c] != 0) ans = Math.max(ans, dfs(grid, r, c));
            }
        }
        return ans;
    }

    private int dfs(int[][] grid, int r, int c) {
        int gold = grid[r][c];
        grid[r][c] = 0;
        int best = 0;
        int[][] dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        for (int[] d : dirs) {
            int nr = r + d[0];
            int nc = c + d[1];
            if (nr >= 0 && nr < grid.length && nc >= 0 && nc < grid[0].length && grid[nr][nc] != 0) {
                best = Math.max(best, dfs(grid, nr, nc));
            }
        }
        grid[r][c] = gold;
        return gold + best;
    }
}""",
)

_add(
    "1220_count_vowels_permutation",
    r"""// LeetCode 1220 - Count Vowels Permutation
// https://leetcode.com/problems/count-vowels-permutation/

class Solution {
    public int countVowelPermutation(int n) {
        final int MOD = 1_000_000_007;
        long a = 1;
        long e = 1;
        long i = 1;
        long o = 1;
        long u = 1;
        for (int t = 0; t < n - 1; t++) {
            long na = (e + i + u) % MOD;
            long ne = (a + i) % MOD;
            long ni = (e + o) % MOD;
            long no = i;
            long nu = (i + o) % MOD;
            a = na;
            e = ne;
            i = ni;
            o = no;
            u = nu;
        }
        return (int) ((a + e + i + o + u) % MOD);
    }
}""",
)


def java_path(folder: Path) -> Path | None:
    for name in ("Solution.java", "solution.java"):
        p = folder / name
        if p.exists():
            return p
    return None


def is_sql_folder(folder: Path) -> bool:
    num = int(folder.name[:4])
    if num in SQL_NUMBERS:
        return True
    for rel in ("tests/config.json", "tests/cases.json"):
        p = folder / rel
        if not p.exists():
            continue
        try:
            data = json.loads(p.read_text(encoding="utf-8"))
            if isinstance(data, dict) and data.get("kind") == "sql":
                return True
            if isinstance(data, dict) and "cases" in data:
                for case in data["cases"]:
                    if isinstance(case, dict) and case.get("kind") == "sql":
                        return True
        except json.JSONDecodeError:
            pass
    return False


def is_stub(text: str) -> bool:
    return bool(re.search(r"void\s+solve\s*\(\s*\)\s*\{\s*\}", text))


def is_design(folder: Path) -> bool:
    cfg = folder / "tests/config.json"
    if not cfg.exists():
        return False
    try:
        return json.loads(cfg.read_text(encoding="utf-8")).get("kind") == "design"
    except json.JSONDecodeError:
        return False


def main() -> None:
    stubs_found = 0
    ported = 0
    sql_skipped = 0
    design_count = 0
    remaining = []

    for num in range(1175, 1221):
        matches = list(ROOT.glob(f"{num:04d}_*"))
        if not matches:
            continue
        folder = matches[0]
        if is_sql_folder(folder):
            sql_skipped += 1
            continue
        path = java_path(folder)
        if path is None:
            remaining.append(folder.name)
            continue
        text = path.read_text(encoding="utf-8")
        if not is_stub(text):
            continue
        stubs_found += 1
        if is_design(folder):
            design_count += 1
        content = SOLUTIONS.get(folder.name)
        if content is None:
            remaining.append(folder.name)
            continue
        path.write_text(content, encoding="utf-8", newline="\n")
        ported += 1
        print(f"WROTE {folder.name}")

    print()
    print(f"stubs_found={stubs_found}")
    print(f"ported={ported}")
    print(f"remaining={len(remaining)}")
    print(f"sql_skipped={sql_skipped}")
    print(f"design_count={design_count}")
    if remaining:
        print("remaining_folders:", ", ".join(remaining))


if __name__ == "__main__":
    main()
