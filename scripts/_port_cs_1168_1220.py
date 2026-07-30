#!/usr/bin/env python3
"""Write C# solutions for folders 1168-1220 (non-SQL stubs)."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(r"c:\Users\Charlie Yu\Documents\leetcode")

SOLUTIONS: dict[str, str] = {}

SOLUTIONS["1168_optimize_water_distribution_in_a_village"] = """// LeetCode 1168 - Optimize Water Distribution in a Village
// https://leetcode.com/problems/optimize-water-distribution-in-a-village/

using System;
using System.Collections.Generic;

public class Solution {
    public int MinCostToSupplyWater(int n, int[] wells, int[][] pipes) {
        int[] parent = new int[n + 1];
        for (int i = 0; i <= n; i++) parent[i] = i;

        int Find(int x) {
            while (parent[x] != x) {
                parent[x] = parent[parent[x]];
                x = parent[x];
            }
            return x;
        }

        var edges = new List<int[]>();
        for (int i = 0; i < wells.Length; i++) {
            edges.Add(new[] { 0, i + 1, wells[i] });
        }
        foreach (var p in pipes) edges.Add(p);
        edges.Sort((a, b) => a[2].CompareTo(b[2]));

        int ans = 0;
        foreach (var e in edges) {
            int ra = Find(e[0]), rb = Find(e[1]);
            if (ra == rb) continue;
            parent[rb] = ra;
            ans += e[2];
        }
        return ans;
    }
}
"""

SOLUTIONS["1169_invalid_transactions"] = """// LeetCode 1169 - Invalid Transactions
// https://leetcode.com/problems/invalid-transactions/

using System;
using System.Collections.Generic;

public class Solution {
    public IList<string> InvalidTransactions(string[] transactions) {
        var parsed = new List<(string name, int time, int amount, string city, string raw)>();
        foreach (var t in transactions) {
            var parts = t.Split(',');
            parsed.Add((parts[0], int.Parse(parts[1]), int.Parse(parts[2]), parts[3], t));
        }
        var invalid = new HashSet<string>();
        for (int i = 0; i < parsed.Count; i++) {
            var (name, time, amount, city, raw) = parsed[i];
            if (amount > 1000) invalid.Add(raw);
            for (int j = 0; j < parsed.Count; j++) {
                if (i == j) continue;
                var p2 = parsed[j];
                if (name == p2.name && city != p2.city && Math.Abs(time - p2.time) <= 60) {
                    invalid.Add(raw);
                    invalid.Add(p2.raw);
                }
            }
        }
        return new List<string>(invalid);
    }
}
"""

SOLUTIONS["1170_compare_strings_by_frequency_of_the_smallest_character"] = """// LeetCode 1170 - Compare Strings by Frequency of the Smallest Character
// https://leetcode.com/problems/compare-strings-by-frequency-of-the-smallest-character/

using System;
using System.Collections.Generic;

public class Solution {
    public int[] NumSmallerByFrequency(string[] queries, string[] words) {
        int F(string s) {
            char min = s[0];
            foreach (char ch in s) {
                if (ch < min) min = ch;
            }
            int count = 0;
            foreach (char ch in s) {
                if (ch == min) count++;
            }
            return count;
        }

        var freqs = new List<int>();
        foreach (var w in words) freqs.Add(F(w));
        freqs.Sort();

        var ans = new int[queries.Length];
        for (int i = 0; i < queries.Length; i++) {
            int target = F(queries[i]);
            int lo = 0, hi = freqs.Count;
            while (lo < hi) {
                int mid = (lo + hi) / 2;
                if (freqs[mid] <= target) lo = mid + 1;
                else hi = mid;
            }
            ans[i] = freqs.Count - lo;
        }
        return ans;
    }
}
"""

SOLUTIONS["1171_remove_zero_sum_consecutive_nodes_from_linked_list"] = """// LeetCode 1171 - Remove Zero Sum Consecutive Nodes from Linked List
// https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/

using System.Collections.Generic;

public class ListNode {
    public int val;
    public ListNode next;
    public ListNode(int val = 0, ListNode next = null) {
        this.val = val;
        this.next = next;
    }
}

public class Solution {
    public ListNode RemoveZeroSumSublists(ListNode head) {
        var dummy = new ListNode(0, head);
        int prefix = 0;
        var seen = new Dictionary<int, ListNode> { [0] = dummy };
        var node = dummy;
        while (node != null) {
            prefix += node.val;
            seen[prefix] = node;
            node = node.next;
        }
        prefix = 0;
        node = dummy;
        while (node != null) {
            prefix += node.val;
            node.next = seen[prefix].next;
            node = node.next;
        }
        return dummy.next;
    }
}
"""

SOLUTIONS["1172_dinner_plate_stacks"] = """// LeetCode 1172 - Dinner Plate Stacks
// https://leetcode.com/problems/dinner-plate-stacks/

using System.Collections.Generic;

public class DinnerPlates {
    private readonly int capacity;
    private readonly List<List<int>> stacks = new List<List<int>>();
    private readonly PriorityQueue<int, int> available = new PriorityQueue<int, int>();

    public DinnerPlates(int capacity) {
        this.capacity = capacity;
    }

    public void Push(int val) {
        while (available.Count > 0 &&
               (available.Peek() >= stacks.Count || stacks[available.Peek()].Count == capacity)) {
            available.Dequeue();
        }
        if (available.Count == 0) {
            stacks.Add(new List<int>());
            available.Enqueue(stacks.Count - 1, stacks.Count - 1);
        }
        int idx = available.Peek();
        stacks[idx].Add(val);
        if (stacks[idx].Count == capacity) available.Dequeue();
    }

    public int Pop() {
        while (stacks.Count > 0 && stacks[stacks.Count - 1].Count == 0) stacks.RemoveAt(stacks.Count - 1);
        return stacks.Count == 0 ? -1 : PopAtStack(stacks.Count - 1);
    }

    public int PopAtStack(int index) {
        if (index < 0 || index >= stacks.Count || stacks[index].Count == 0) return -1;
        if (stacks[index].Count == capacity) available.Enqueue(index, index);
        var stack = stacks[index];
        int val = stack[stack.Count - 1];
        stack.RemoveAt(stack.Count - 1);
        return val;
    }
}
"""

SOLUTIONS["1175_prime_arrangements"] = """// LeetCode 1175 - Prime Arrangements
// https://leetcode.com/problems/prime-arrangements/

public class Solution {
    private const int Mod = 1_000_000_007;

    public int NumPrimeArrangements(int n) {
        bool IsPrime(int x) {
            if (x < 2) return false;
            for (int d = 2; d * d <= x; d++) {
                if (x % d == 0) return false;
            }
            return true;
        }

        int primes = 0;
        for (int i = 1; i <= n; i++) {
            if (IsPrime(i)) primes++;
        }
        return (int)(Fact(primes) * Fact(n - primes) % Mod);
    }

    private static long Fact(int n) {
        long result = 1;
        for (int i = 2; i <= n; i++) result = result * i % Mod;
        return result;
    }
}
"""

SOLUTIONS["1176_diet_plan_performance"] = """// LeetCode 1176 - Diet Plan Performance
// https://leetcode.com/problems/diet-plan-performance/

public class Solution {
    public int DietPlanPerformance(int[] calories, int k, int lower, int upper) {
        int window = 0;
        for (int i = 0; i < k; i++) window += calories[i];
        int ans = 0;
        if (window < lower) ans--;
        else if (window > upper) ans++;
        for (int i = k; i < calories.Length; i++) {
            window += calories[i] - calories[i - k];
            if (window < lower) ans--;
            else if (window > upper) ans++;
        }
        return ans;
    }
}
"""

SOLUTIONS["1177_can_make_palindrome_from_substring"] = """// LeetCode 1177 - Can Make Palindrome from Substring
// https://leetcode.com/problems/can-make-palindrome-from-substring/

using System;
using System.Collections.Generic;
using System.Numerics;

public class Solution {
    public IList<bool> CanMakePaliQueries(string s, int[][] queries) {
        var prefix = new List<int> { 0 };
        int mask = 0;
        foreach (char ch in s) {
            mask ^= 1 << (ch - 'a');
            prefix.Add(mask);
        }
        var ans = new List<bool>();
        foreach (var q in queries) {
            int left = q[0], right = q[1], k = q[2];
            int bits = BitOperations.PopCount((uint)(prefix[right + 1] ^ prefix[left]));
            ans.Add(bits / 2 <= k);
        }
        return ans;
    }
}
"""

SOLUTIONS["1178_number_of_valid_words_for_each_puzzle"] = """// LeetCode 1178 - Number of Valid Words for Each Puzzle
// https://leetcode.com/problems/number-of-valid-words-for-each-puzzle/

using System.Collections.Generic;

public class Solution {
    public int[] FindNumOfValidWords(string[] words, string[] puzzles) {
        int MaskOf(string s) {
            int mask = 0;
            foreach (char ch in s) mask |= 1 << (ch - 'a');
            return mask;
        }

        var freq = new Dictionary<int, int>();
        foreach (var w in words) {
            int m = MaskOf(w);
            freq[m] = freq.GetValueOrDefault(m) + 1;
        }

        var ans = new int[puzzles.Length];
        for (int i = 0; i < puzzles.Length; i++) {
            string puzzle = puzzles[i];
            int first = 1 << (puzzle[0] - 'a');
            int full = MaskOf(puzzle);
            int sub = full;
            int total = 0;
            while (true) {
                if ((sub & first) != 0) total += freq.GetValueOrDefault(sub);
                if (sub == 0) break;
                sub = (sub - 1) & full;
            }
            ans[i] = total;
        }
        return ans;
    }
}
"""

SOLUTIONS["1180_count_substrings_with_only_one_distinct_letter"] = """// LeetCode 1180 - Count Substrings with Only One Distinct Letter
// https://leetcode.com/problems/count-substrings-with-only-one-distinct-letter/

public class Solution {
    public int CountLetters(string s) {
        int ans = 1, length = 1;
        for (int i = 1; i < s.Length; i++) {
            length = s[i] == s[i - 1] ? length + 1 : 1;
            ans += length;
        }
        return ans;
    }
}
"""

SOLUTIONS["1181_before_and_after_puzzle"] = """// LeetCode 1181 - Before and After Puzzle
// https://leetcode.com/problems/before-and-after-puzzle/

using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public IList<string> BeforeAndAfterPuzzles(string[] phrases) {
        var split = phrases.Select(p => p.Split(' ')).ToArray();
        var result = new HashSet<string>();
        for (int i = 0; i < split.Length; i++) {
            for (int j = 0; j < split.Length; j++) {
                if (i == j) continue;
                if (split[i][^1] == split[j][0]) {
                    var parts = new List<string>(split[i]);
                    parts.AddRange(split[j].Skip(1));
                    result.Add(string.Join(" ", parts));
                }
            }
        }
        return result.OrderBy(x => x).ToList();
    }
}
"""

SOLUTIONS["1182_shortest_distance_to_target_color"] = """// LeetCode 1182 - Shortest Distance to Target Color
// https://leetcode.com/problems/shortest-distance-to-target-color/

using System;
using System.Collections.Generic;

public class Solution {
    public int[] ShortestDistanceColor(int[] colors, int[][] queries) {
        var pos = new Dictionary<int, List<int>>();
        for (int i = 0; i < colors.Length; i++) {
            if (!pos.ContainsKey(colors[i])) pos[colors[i]] = new List<int>();
            pos[colors[i]].Add(i);
        }

        var ans = new int[queries.Length];
        for (int i = 0; i < queries.Length; i++) {
            int idx = queries[i][0], c = queries[i][1];
            if (!pos.ContainsKey(c)) {
                ans[i] = -1;
                continue;
            }
            var arr = pos[c];
            int lo = 0, hi = arr.Count;
            while (lo < hi) {
                int mid = (lo + hi) / 2;
                if (arr[mid] < idx) lo = mid + 1;
                else hi = mid;
            }
            int best = int.MaxValue;
            if (lo < arr.Count) best = Math.Min(best, arr[lo] - idx);
            if (lo > 0) best = Math.Min(best, idx - arr[lo - 1]);
            ans[i] = best == int.MaxValue ? -1 : best;
        }
        return ans;
    }
}
"""

SOLUTIONS["1183_maximum_number_of_ones"] = """// LeetCode 1183 - Maximum Number of Ones
// https://leetcode.com/problems/maximum-number-of-ones/

using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int MaximumNumberOfOnes(int width, int height, int sideLength, int maxOnes) {
        var counts = new List<int>();
        for (int r = 0; r < sideLength; r++) {
            for (int c = 0; c < sideLength; c++) {
                int rows = (height - r + sideLength - 1) / sideLength;
                int cols = (width - c + sideLength - 1) / sideLength;
                counts.Add(rows * cols);
            }
        }
        counts.Sort((a, b) => b.CompareTo(a));
        return counts.Take(maxOnes).Sum();
    }
}
"""

SOLUTIONS["1184_distance_between_bus_stops"] = """// LeetCode 1184 - Distance Between Bus Stops
// https://leetcode.com/problems/distance-between-bus-stops/

using System;
using System.Linq;

public class Solution {
    public int DistanceBetweenBusStops(int[] distance, int start, int destination) {
        if (start > destination) (start, destination) = (destination, start);
        int clockwise = 0;
        for (int i = start; i < destination; i++) clockwise += distance[i];
        return Math.Min(clockwise, distance.Sum() - clockwise);
    }
}
"""

SOLUTIONS["1185_day_of_the_week"] = """// LeetCode 1185 - Day of the Week
// https://leetcode.com/problems/day-of-the-week/

using System;

public class Solution {
    public string DayOfTheWeek(int day, int month, int year) {
        return new DateTime(year, month, day).DayOfWeek.ToString();
    }
}
"""

SOLUTIONS["1186_maximum_subarray_sum_with_one_deletion"] = """// LeetCode 1186 - Maximum Subarray Sum with One Deletion
// https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/

using System;

public class Solution {
    public int MaximumSum(int[] arr) {
        int keep = arr[0], delete = arr[0], ans = arr[0];
        for (int i = 1; i < arr.Length; i++) {
            int x = arr[i];
            delete = Math.Max(keep, delete + x);
            keep = Math.Max(keep + x, x);
            ans = Math.Max(ans, Math.Max(keep, delete));
        }
        return ans;
    }
}
"""

SOLUTIONS["1187_make_array_strictly_increasing"] = """// LeetCode 1187 - Make Array Strictly Increasing
// https://leetcode.com/problems/make-array-strictly-increasing/

using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int MakeArrayIncreasing(int[] arr1, int[] arr2) {
        arr2 = arr2.Distinct().OrderBy(x => x).ToArray();
        var dp = new Dictionary<int, int> { [-1] = 0 };

        foreach (int num in arr1) {
            var newDp = new Dictionary<int, int>();
            foreach (var kv in dp) {
                int prev = kv.Key, ops = kv.Value;
                if (num > prev) {
                    if (!newDp.ContainsKey(num) || newDp[num] > ops) newDp[num] = ops;
                }
                int lo = 0, hi = arr2.Length;
                while (lo < hi) {
                    int mid = (lo + hi) / 2;
                    if (arr2[mid] <= prev) lo = mid + 1;
                    else hi = mid;
                }
                if (lo < arr2.Length) {
                    int chosen = arr2[lo];
                    int nextOps = ops + 1;
                    if (!newDp.ContainsKey(chosen) || newDp[chosen] > nextOps) newDp[chosen] = nextOps;
                }
            }
            dp = newDp;
            if (dp.Count == 0) return -1;
        }
        return dp.Values.Min();
    }
}
"""

SOLUTIONS["1188_design_bounded_blocking_queue"] = """// LeetCode 1188 - Design Bounded Blocking Queue
// https://leetcode.com/problems/design-bounded-blocking-queue/

using System.Collections.Generic;
using System.Threading;

public class BoundedBlockingQueue {
    private readonly int capacity;
    private readonly Queue<int> queue = new Queue<int>();
    private readonly SemaphoreSlim notFull;
    private readonly SemaphoreSlim notEmpty = new SemaphoreSlim(0);
    private readonly object sync = new object();

    public BoundedBlockingQueue(int capacity) {
        this.capacity = capacity;
        notFull = new SemaphoreSlim(capacity);
    }

    public void Enqueue(int element) {
        notFull.Wait();
        lock (sync) {
            queue.Enqueue(element);
        }
        notEmpty.Release();
    }

    public int Dequeue() {
        notEmpty.Wait();
        int value;
        lock (sync) {
            value = queue.Dequeue();
        }
        notFull.Release();
        return value;
    }

    public int Size() {
        lock (sync) {
            return queue.Count;
        }
    }
}
"""

SOLUTIONS["1189_maximum_number_of_balloons"] = """// LeetCode 1189 - Maximum Number of Balloons
// https://leetcode.com/problems/maximum-number-of-balloons/

using System.Collections.Generic;

public class Solution {
    public int MaxNumberOfBalloons(string text) {
        var count = new Dictionary<char, int>();
        foreach (char ch in text) {
            count[ch] = count.GetValueOrDefault(ch) + 1;
        }
        int Get(char ch) => count.GetValueOrDefault(ch);
        return System.Math.Min(Get('b'),
            System.Math.Min(Get('a'),
            System.Math.Min(Get('l') / 2,
            System.Math.Min(Get('o') / 2, Get('n')))));
    }
}
"""

SOLUTIONS["1190_reverse_substrings_between_each_pair_of_parentheses"] = """// LeetCode 1190 - Reverse Substrings Between Each Pair of Parentheses
// https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/

using System.Collections.Generic;
using System.Text;

public class Solution {
    public string ReverseParentheses(string s) {
        var stack = new Stack<char>();
        foreach (char ch in s) {
            if (ch == ')') {
                var chunk = new List<char>();
                while (stack.Count > 0 && stack.Peek() != '(') chunk.Add(stack.Pop());
                stack.Pop();
                chunk.Reverse();
                foreach (char c in chunk) stack.Push(c);
            } else {
                stack.Push(ch);
            }
        }
        var sb = new StringBuilder(stack.Count);
        foreach (char ch in stack) sb.Append(ch);
        return sb.ToString();
    }
}
"""

SOLUTIONS["1191_k_concatenation_maximum_sum"] = """// LeetCode 1191 - K-Concatenation Maximum Sum
// https://leetcode.com/problems/k-concatenation-maximum-sum/

using System;
using System.Linq;

public class Solution {
    private const int Mod = 1_000_000_007;

    public int KConcatenationMaxSum(int[] arr, int k) {
        int Kadane(int[] nums) {
            int best = 0, cur = 0;
            foreach (int x in nums) {
                cur = Math.Max(0, cur + x);
                best = Math.Max(best, cur);
            }
            return best;
        }

        int one = Kadane(arr);
        if (k == 1) return one % Mod;
        int two = Kadane(arr.Concat(arr).ToArray());
        long total = arr.Sum(x => (long)x);
        if (total > 0) return (int)Math.Max(one, two + total * (k - 2)) % Mod;
        return Math.Max(one, two) % Mod;
    }
}
"""

SOLUTIONS["1192_critical_connections_in_a_network"] = """// LeetCode 1192 - Critical Connections in a Network
// https://leetcode.com/problems/critical-connections-in-a-network/

using System;
using System.Collections.Generic;

public class Solution {
    public IList<IList<int>> CriticalConnections(int n, IList<IList<int>> connections) {
        var graph = new List<int>[n];
        for (int i = 0; i < n; i++) graph[i] = new List<int>();
        foreach (var c in connections) {
            graph[c[0]].Add(c[1]);
            graph[c[1]].Add(c[0]);
        }

        var disc = new int[n];
        var low = new int[n];
        Array.Fill(disc, -1);
        Array.Fill(low, -1);
        int time = 0;
        var bridges = new List<IList<int>>();

        void Dfs(int node, int parent) {
            disc[node] = low[node] = time++;
            foreach (int nxt in graph[node]) {
                if (nxt == parent) continue;
                if (disc[nxt] == -1) {
                    Dfs(nxt, node);
                    low[node] = Math.Min(low[node], low[nxt]);
                    if (low[nxt] > disc[node]) {
                        bridges.Add(new List<int> { Math.Min(node, nxt), Math.Max(node, nxt) });
                    }
                } else {
                    low[node] = Math.Min(low[node], disc[nxt]);
                }
            }
        }

        Dfs(0, -1);
        return bridges;
    }
}
"""

SOLUTIONS["1195_fizz_buzz_multithreaded"] = """// LeetCode 1195 - Fizz Buzz Multithreaded
// https://leetcode.com/problems/fizz-buzz-multithreaded/

using System;
using System.Threading;

public class FizzBuzz {
    private readonly int n;
    private int current = 1;
    private readonly object sync = new object();

    public FizzBuzz(int n) {
        this.n = n;
    }

    public void Fizz(Action printFizz) {
        Run(x => x % 3 == 0 && x % 5 != 0, printFizz);
    }

    public void Buzz(Action printBuzz) {
        Run(x => x % 5 == 0 && x % 3 != 0, printBuzz);
    }

    public void Fizzbuzz(Action printFizzBuzz) {
        Run(x => x % 15 == 0, printFizzBuzz);
    }

    public void Number(Action<int> printNumber) {
        Run(x => x % 3 != 0 && x % 5 != 0, () => printNumber(current));
    }

    private void Run(Func<int, bool> predicate, Action action) {
        while (true) {
            lock (sync) {
                while (current <= n && !predicate(current)) {
                    Monitor.Wait(sync);
                }
                if (current > n) return;
                action();
                current++;
                Monitor.PulseAll(sync);
            }
        }
    }
}
"""

SOLUTIONS["1196_how_many_apples_can_you_put_into_the_basket"] = """// LeetCode 1196 - How Many Apples Can You Put into the Basket
// https://leetcode.com/problems/how-many-apples-can-you-put-into-the-basket/

using System;
using System.Linq;

public class Solution {
    public int MaxNumberOfApples(int[] weight) {
        Array.Sort(weight);
        int total = 0;
        for (int i = 0; i < weight.Length; i++) {
            total += weight[i];
            if (total > 5000) return i;
        }
        return weight.Length;
    }
}
"""

SOLUTIONS["1197_minimum_knight_moves"] = """// LeetCode 1197 - Minimum Knight Moves
// https://leetcode.com/problems/minimum-knight-moves/

using System;
using System.Collections.Generic;

public class Solution {
    public int MinKnightMoves(int x, int y) {
        x = Math.Abs(x);
        y = Math.Abs(y);
        var memo = new Dictionary<(int, int), int>();

        int Dfs(int a, int b) {
            if (a + b == 0) return 0;
            if (a + b == 2) return 2;
            var key = (a, b);
            if (memo.TryGetValue(key, out int cached)) return cached;
            int ans = Math.Min(Dfs(Math.Abs(a - 1), Math.Abs(b - 2)), Dfs(Math.Abs(a - 2), Math.Abs(b - 1))) + 1;
            memo[key] = ans;
            return ans;
        }

        return Dfs(x, y);
    }
}
"""

SOLUTIONS["1198_find_smallest_common_element_in_all_rows"] = """// LeetCode 1198 - Find Smallest Common Element in All Rows
// https://leetcode.com/problems/find-smallest-common-element-in-all-rows/

using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int SmallestCommonElement(int[][] mat) {
        var common = new HashSet<int>(mat[0]);
        for (int i = 1; i < mat.Length; i++) {
            common.IntersectWith(mat[i]);
            if (common.Count == 0) return -1;
        }
        return common.Min();
    }
}
"""

SOLUTIONS["1199_minimum_time_to_build_blocks"] = """// LeetCode 1199 - Minimum Time to Build Blocks
// https://leetcode.com/problems/minimum-time-to-build-blocks/

using System.Collections.Generic;

public class Solution {
    public int MinBuildTime(int[] blocks, int split) {
        var heap = new PriorityQueue<int, int>();
        foreach (int b in blocks) heap.Enqueue(b, b);
        while (heap.Count > 1) {
            heap.Dequeue();
            int top = heap.Dequeue();
            heap.Enqueue(top + split, top + split);
        }
        return heap.Peek();
    }
}
"""

SOLUTIONS["1200_minimum_absolute_difference"] = """// LeetCode 1200 - Minimum Absolute Difference
// https://leetcode.com/problems/minimum-absolute-difference/

using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public IList<IList<int>> MinimumAbsDifference(int[] arr) {
        Array.Sort(arr);
        int best = int.MaxValue;
        for (int i = 0; i < arr.Length - 1; i++) {
            best = Math.Min(best, arr[i + 1] - arr[i]);
        }
        var ans = new List<IList<int>>();
        for (int i = 0; i < arr.Length - 1; i++) {
            if (arr[i + 1] - arr[i] == best) ans.Add(new List<int> { arr[i], arr[i + 1] });
        }
        return ans;
    }
}
"""

SOLUTIONS["1201_ugly_number_iii"] = """// LeetCode 1201 - Ugly Number III
// https://leetcode.com/problems/ugly-number-iii/

using System;

public class Solution {
    public int NthUglyNumber(int n, int a, int b, int c) {
        long Lcm(long x, long y) => x / Gcd(x, y) * y;
        long ab = Lcm(a, b), ac = Lcm(a, c), bc = Lcm(b, c), abc = Lcm(ab, c);

        long Count(long x) => x / a + x / b + x / c - x / ab - x / ac - x / bc + x / abc;

        long lo = 1, hi = 2_000_000_000;
        while (lo < hi) {
            long mid = (lo + hi) / 2;
            if (Count(mid) >= n) hi = mid;
            else lo = mid + 1;
        }
        return (int)lo;
    }

    private static long Gcd(long x, long y) {
        while (y != 0) (x, y) = (y, x % y);
        return x;
    }
}
"""

SOLUTIONS["1202_smallest_string_with_swaps"] = """// LeetCode 1202 - Smallest String With Swaps
// https://leetcode.com/problems/smallest-string-with-swaps/

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

public class Solution {
    public string SmallestStringWithSwaps(string s, int[][] pairs) {
        int n = s.Length;
        var parent = new int[n];
        for (int i = 0; i < n; i++) parent[i] = i;

        int Find(int x) {
            while (x != parent[x]) {
                parent[x] = parent[parent[x]];
                x = parent[x];
            }
            return x;
        }

        foreach (var p in pairs) {
            int ra = Find(p[0]), rb = Find(p[1]);
            parent[ra] = rb;
        }

        var groups = new Dictionary<int, List<char>>();
        for (int i = 0; i < n; i++) {
            int root = Find(i);
            if (!groups.ContainsKey(root)) groups[root] = new List<char>();
            groups[root].Add(s[i]);
        }
        foreach (var kv in groups) kv.Value.Sort((a, b) => b.CompareTo(a));

        var sb = new StringBuilder(n);
        for (int i = 0; i < n; i++) {
            var list = groups[Find(i)];
            char ch = list[^1];
            list.RemoveAt(list.Count - 1);
            sb.Append(ch);
        }
        return sb.ToString();
    }
}
"""

SOLUTIONS["1203_sort_items_by_groups_respecting_dependencies"] = """// LeetCode 1203 - Sort Items by Groups Respecting Dependencies
// https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/

using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int[] SortItems(int n, int m, int[] group, IList<IList<int>> beforeItems) {
        for (int i = 0; i < n; i++) {
            if (group[i] == -1) {
                group[i] = m;
                m++;
            }
        }

        var itemGraph = new List<int>[n];
        var itemIndeg = new int[n];
        for (int i = 0; i < n; i++) itemGraph[i] = new List<int>();

        var groupGraph = new HashSet<int>[m];
        var groupIndeg = new int[m];
        for (int i = 0; i < m; i++) groupGraph[i] = new HashSet<int>();

        for (int v = 0; v < n; v++) {
            foreach (int u in beforeItems[v]) {
                itemGraph[u].Add(v);
                itemIndeg[v]++;
                if (group[u] != group[v] && groupGraph[group[u]].Add(group[v])) {
                    groupIndeg[group[v]]++;
                }
            }
        }

        List<int> Topo(List<int>[] graph, int[] indeg) {
            var q = new Queue<int>();
            for (int i = 0; i < graph.Length; i++) {
                if (indeg[i] == 0) q.Enqueue(i);
            }
            var order = new List<int>();
            while (q.Count > 0) {
                int u = q.Dequeue();
                order.Add(u);
                foreach (int v in graph[u]) {
                    indeg[v]--;
                    if (indeg[v] == 0) q.Enqueue(v);
                }
            }
            return order.Count == graph.Length ? order : new List<int>();
        }

        var groupAdj = new List<int>[m];
        for (int i = 0; i < m; i++) groupAdj[i] = groupGraph[i].ToList();

        var items = Topo(itemGraph, itemIndeg);
        var groups = Topo(groupAdj, groupIndeg);
        if (items.Count == 0 || groups.Count == 0) return new int[0];

        var buckets = new List<int>[m];
        for (int i = 0; i < m; i++) buckets[i] = new List<int>();
        foreach (int item in items) buckets[group[item]].Add(item);

        var ans = new List<int>();
        foreach (int g in groups) ans.AddRange(buckets[g]);
        return ans.ToArray();
    }
}
"""

SOLUTIONS["1206_design_skiplist"] = """// LeetCode 1206 - Design Skiplist
// https://leetcode.com/problems/design-skiplist/

using System.Collections.Generic;

public class Skiplist {
    private readonly List<int> values = new List<int>();

    public bool Search(int target) {
        int i = values.BinarySearch(target);
        return i >= 0;
    }

    public void Add(int num) {
        int i = values.BinarySearch(num);
        if (i < 0) i = ~i;
        values.Insert(i, num);
    }

    public bool Erase(int num) {
        int i = values.BinarySearch(num);
        if (i < 0) return false;
        values.RemoveAt(i);
        return true;
    }
}
"""

SOLUTIONS["1207_unique_number_of_occurrences"] = """// LeetCode 1207 - Unique Number of Occurrences
// https://leetcode.com/problems/unique-number-of-occurrences/

using System.Collections.Generic;
using System.Linq;

public class Solution {
    public bool UniqueOccurrences(int[] arr) {
        var freq = new Dictionary<int, int>();
        foreach (int x in arr) freq[x] = freq.GetValueOrDefault(x) + 1;
        var counts = freq.Values;
        return counts.Count() == counts.Distinct().Count();
    }
}
"""

SOLUTIONS["1208_get_equal_substrings_within_budget"] = """// LeetCode 1208 - Get Equal Substrings Within Budget
// https://leetcode.com/problems/get-equal-substrings-within-budget/

using System;

public class Solution {
    public int EqualSubstring(string s, string t, int maxCost) {
        int left = 0, cost = 0, answer = 0;
        for (int right = 0; right < s.Length; right++) {
            cost += Math.Abs(s[right] - t[right]);
            while (cost > maxCost) {
                cost -= Math.Abs(s[left] - t[left]);
                left++;
            }
            answer = Math.Max(answer, right - left + 1);
        }
        return answer;
    }
}
"""

SOLUTIONS["1209_remove_all_adjacent_duplicates_in_string_ii"] = """// LeetCode 1209 - Remove All Adjacent Duplicates in String II
// https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/

using System.Collections.Generic;
using System.Text;

public class Solution {
    public string RemoveDuplicates(string s, int k) {
        var stack = new List<(char ch, int count)>();
        foreach (char ch in s) {
            if (stack.Count > 0 && stack[^1].ch == ch) {
                var top = stack[^1];
                stack[^1] = (top.ch, top.count + 1);
            } else {
                stack.Add((ch, 1));
            }
            if (stack[^1].count == k) stack.RemoveAt(stack.Count - 1);
        }
        var sb = new StringBuilder();
        foreach (var (ch, count) in stack) sb.Append(ch, count);
        return sb.ToString();
    }
}
"""

SOLUTIONS["1210_minimum_moves_to_reach_target_with_rotations"] = """// LeetCode 1210 - Minimum Moves to Reach Target With Rotations
// https://leetcode.com/problems/minimum-moves-to-reach-target-with-rotations/

using System.Collections.Generic;

public class Solution {
    public int MinimumMoves(int[][] grid) {
        int n = grid.Length;
        var start = (0, 0, 0);
        var target = (n - 1, n - 2, 0);
        var q = new Queue<(int r, int c, int orient, int moves)>();
        var seen = new HashSet<(int, int, int)> { start };
        q.Enqueue((start.Item1, start.Item2, start.Item3, 0));

        while (q.Count > 0) {
            var (r, c, orient, moves) = q.Dequeue();
            if ((r, c, orient) == target) return moves;

            var next = new List<(int, int, int)>();
            if (orient == 0) {
                if (c + 2 < n && grid[r][c + 2] == 0) next.Add((r, c + 1, 0));
                if (r + 1 < n && grid[r + 1][c] == 0 && grid[r + 1][c + 1] == 0) {
                    next.Add((r + 1, c, 0));
                    next.Add((r, c, 1));
                }
            } else {
                if (r + 2 < n && grid[r + 2][c] == 0) next.Add((r + 1, c, 1));
                if (c + 1 < n && grid[r][c + 1] == 0 && grid[r + 1][c + 1] == 0) {
                    next.Add((r, c + 1, 1));
                    next.Add((r, c, 0));
                }
            }

            foreach (var state in next) {
                if (seen.Add(state)) q.Enqueue((state.Item1, state.Item2, state.Item3, moves + 1));
            }
        }
        return -1;
    }
}
"""

SOLUTIONS["1213_intersection_of_three_sorted_arrays"] = """// LeetCode 1213 - Intersection of Three Sorted Arrays
// https://leetcode.com/problems/intersection-of-three-sorted-arrays/

using System.Collections.Generic;
using System.Linq;

public class Solution {
    public IList<int> ArraysIntersection(int[] arr1, int[] arr2, int[] arr3) {
        return arr1.Intersect(arr2).Intersect(arr3).OrderBy(x => x).ToList();
    }
}
"""

SOLUTIONS["1214_two_sum_bsts"] = """// LeetCode 1214 - Two Sum BSTs
// https://leetcode.com/problems/two-sum-bsts/

using System.Collections.Generic;

public class TreeNode {
    public int val;
    public TreeNode left;
    public TreeNode right;
    public TreeNode(int val = 0, TreeNode left = null, TreeNode right = null) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

public class Solution {
    public bool TwoSumBSTs(TreeNode root1, TreeNode root2, int target) {
        var values = new HashSet<int>();
        var stack = new Stack<TreeNode>();
        if (root1 != null) stack.Push(root1);
        while (stack.Count > 0) {
            var node = stack.Pop();
            values.Add(node.val);
            if (node.left != null) stack.Push(node.left);
            if (node.right != null) stack.Push(node.right);
        }

        stack.Clear();
        if (root2 != null) stack.Push(root2);
        while (stack.Count > 0) {
            var node = stack.Pop();
            if (values.Contains(target - node.val)) return true;
            if (node.left != null) stack.Push(node.left);
            if (node.right != null) stack.Push(node.right);
        }
        return false;
    }
}
"""

SOLUTIONS["1215_stepping_numbers"] = """// LeetCode 1215 - Stepping Numbers
// https://leetcode.com/problems/stepping-numbers/

using System.Collections.Generic;
using System.Linq;

public class Solution {
    public IList<int> CountSteppingNumbers(int low, int high) {
        var answer = new List<int>();
        if (low == 0) answer.Add(0);
        var q = new Queue<int>();
        for (int i = 1; i < 10; i++) q.Enqueue(i);

        while (q.Count > 0) {
            int x = q.Dequeue();
            if (x > high) continue;
            if (x >= low) answer.Add(x);
            int last = x % 10;
            if (last > 0) q.Enqueue(x * 10 + last - 1);
            if (last < 9) q.Enqueue(x * 10 + last + 1);
        }
        return answer.OrderBy(v => v).ToList();
    }
}
"""

SOLUTIONS["1216_valid_palindrome_iii"] = """// LeetCode 1216 - Valid Palindrome III
// https://leetcode.com/problems/valid-palindrome-iii/

using System;

public class Solution {
    public bool IsValidPalindrome(string s, int k) {
        int n = s.Length;
        var dp = new int[n];
        for (int i = n - 1; i >= 0; i--) {
            int previous = 0;
            for (int j = i + 1; j < n; j++) {
                int old = dp[j];
                if (s[i] == s[j]) dp[j] = previous;
                else dp[j] = 1 + Math.Min(dp[j], dp[j - 1]);
                previous = old;
            }
        }
        return n == 0 || dp[n - 1] <= k;
    }
}
"""

SOLUTIONS["1217_minimum_cost_to_move_chips_to_the_same_position"] = """// LeetCode 1217 - Minimum Cost to Move Chips to The Same Position
// https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/

using System.Linq;

public class Solution {
    public int MinCostToMoveChips(int[] position) {
        int odd = position.Count(x => (x & 1) == 1);
        return System.Math.Min(odd, position.Length - odd);
    }
}
"""

SOLUTIONS["1218_longest_arithmetic_subsequence_of_given_difference"] = """// LeetCode 1218 - Longest Arithmetic Subsequence of Given Difference
// https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/

using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int LongestSubsequence(int[] arr, int difference) {
        var dp = new Dictionary<int, int>();
        foreach (int x in arr) dp[x] = dp.GetValueOrDefault(x - difference) + 1;
        return dp.Values.Max();
    }
}
"""

SOLUTIONS["1219_path_with_maximum_gold"] = """// LeetCode 1219 - Path with Maximum Gold
// https://leetcode.com/problems/path-with-maximum-gold/

using System;

public class Solution {
    public int GetMaximumGold(int[][] grid) {
        int rows = grid.Length, cols = grid[0].Length;
        int ans = 0;

        int Dfs(int r, int c) {
            int gold = grid[r][c];
            grid[r][c] = 0;
            int best = 0;
            int[] dr = { 1, -1, 0, 0 };
            int[] dc = { 0, 0, 1, -1 };
            for (int k = 0; k < 4; k++) {
                int nr = r + dr[k], nc = c + dc[k];
                if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && grid[nr][nc] != 0) {
                    best = Math.Max(best, Dfs(nr, nc));
                }
            }
            grid[r][c] = gold;
            return gold + best;
        }

        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (grid[r][c] != 0) ans = Math.Max(ans, Dfs(r, c));
            }
        }
        return ans;
    }
}
"""

SOLUTIONS["1220_count_vowels_permutation"] = """// LeetCode 1220 - Count Vowels Permutation
// https://leetcode.com/problems/count-vowels-permutation/

public class Solution {
    private const int Mod = 1_000_000_007;

    public int CountVowelPermutation(int n) {
        long a = 1, e = 1, i = 1, o = 1, u = 1;
        for (int t = 0; t < n - 1; t++) {
            long na = (e + i + u) % Mod;
            long ne = (a + i) % Mod;
            long ni = (e + o) % Mod;
            long no = i;
            long nu = (i + o) % Mod;
            a = na; e = ne; i = ni; o = no; u = nu;
        }
        return (int)((a + e + i + o + u) % Mod);
    }
}
"""


def is_sql(folder: Path) -> bool:
    for rel in ("tests/config.json", "tests/cases.json"):
        p = folder / rel
        if p.exists():
            try:
                if json.loads(p.read_text(encoding="utf-8")).get("kind") == "sql":
                    return True
            except Exception:
                pass
    return False


def is_stub(text: str) -> bool:
    return bool(re.search(r"(public\s+)?void\s+Solve\s*\(\s*\)\s*\{\s*\}", text))


def main() -> None:
    written = []
    for name, content in sorted(SOLUTIONS.items()):
        folder = ROOT / name
        if not folder.is_dir():
            print(f"SKIP missing folder {name}")
            continue
        if is_sql(folder):
            print(f"SKIP sql {name}")
            continue
        cs_path = folder / "Solution.cs"
        if not cs_path.exists():
            cs_path = folder / "solution.cs"
        if cs_path.exists() and not is_stub(cs_path.read_text(encoding="utf-8")):
            print(f"SKIP already done {name}")
            continue
        cs_path.write_text(content, encoding="utf-8", newline="\n")
        written.append(name)
        print(f"WROTE {name}")
    print(f"\nTotal written: {len(written)}")


if __name__ == "__main__":
    main()
