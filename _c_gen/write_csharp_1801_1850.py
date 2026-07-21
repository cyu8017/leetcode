#!/usr/bin/env python3
"""Write C# Solution.cs for LeetCode 1801-1850 (non-SQL)."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

FOLDERS: dict[int, str] = {
    1801: "1801_number_of_orders_in_the_backlog",
    1802: "1802_maximum_value_at_a_given_index_in_a_bounded_array",
    1803: "1803_count_pairs_with_xor_in_a_range",
    1804: "1804_implement_trie_ii_prefix_tree",
    1805: "1805_number_of_different_integers_in_a_string",
    1806: "1806_minimum_number_of_operations_to_reinitialize_a_permutation",
    1807: "1807_evaluate_the_bracket_pairs_of_a_string",
    1808: "1808_maximize_number_of_nice_divisors",
    1810: "1810_minimum_path_cost_in_a_hidden_grid",
    1812: "1812_determine_color_of_a_chessboard_square",
    1813: "1813_sentence_similarity_iii",
    1814: "1814_count_nice_pairs_in_an_array",
    1815: "1815_maximum_number_of_groups_getting_fresh_donuts",
    1816: "1816_truncate_sentence",
    1817: "1817_finding_the_users_active_minutes",
    1818: "1818_minimum_absolute_sum_difference",
    1819: "1819_number_of_different_subsequences_gcds",
    1820: "1820_maximum_number_of_accepted_invitations",
    1822: "1822_sign_of_the_product_of_an_array",
    1823: "1823_find_the_winner_of_the_circular_game",
    1824: "1824_minimum_sideway_jumps",
    1825: "1825_finding_mk_average",
    1826: "1826_faulty_sensor",
    1827: "1827_minimum_operations_to_make_the_array_increasing",
    1828: "1828_queries_on_number_of_points_inside_a_circle",
    1829: "1829_maximum_xor_for_each_query",
    1830: "1830_minimum_number_of_operations_to_make_string_sorted",
    1832: "1832_check_if_the_sentence_is_pangram",
    1833: "1833_maximum_ice_cream_bars",
    1834: "1834_single_threaded_cpu",
    1835: "1835_find_xor_sum_of_all_pairs_bitwise_and",
    1836: "1836_remove_duplicates_from_an_unsorted_linked_list",
    1837: "1837_sum_of_digits_in_base_k",
    1838: "1838_frequency_of_the_most_frequent_element",
    1839: "1839_longest_substring_of_all_vowels_in_order",
    1840: "1840_maximum_building_height",
    1842: "1842_next_palindrome_using_same_digits",
    1844: "1844_replace_all_digits_with_characters",
    1845: "1845_seat_reservation_manager",
    1846: "1846_maximum_element_after_decreasing_and_rearranging",
    1847: "1847_closest_room",
    1848: "1848_minimum_distance_to_the_target_element",
    1849: "1849_splitting_a_string_into_descending_consecutive_values",
    1850: "1850_minimum_adjacent_swaps_to_reach_the_kth_smallest_number",
}

SOLUTIONS: dict[int, str] = {}

SOLUTIONS[1801] = r'''// LeetCode 1801 - Number of Orders in the Backlog
// https://leetcode.com/problems/number-of-orders-in-the-backlog/

using System;
using System.Collections.Generic;

public class Solution {
    public int GetNumberOfBacklogOrders(int[][] orders) {
        const int MOD = 1_000_000_007;
        var buy = new PriorityQueue<(int price, int amount), int>();
        var sell = new PriorityQueue<(int price, int amount), int>();

        foreach (var order in orders) {
            int price = order[0], amount = order[1], orderType = order[2];
            if (orderType == 0) {
                buy.Enqueue((price, amount), -price);
            } else {
                sell.Enqueue((price, amount), price);
            }

            while (buy.Count > 0 && sell.Count > 0 && buy.Peek().price >= sell.Peek().price) {
                var (buyPrice, buyAmount) = buy.Dequeue();
                var (sellPrice, sellAmount) = sell.Dequeue();
                int matched = Math.Min(buyAmount, sellAmount);
                buyAmount -= matched;
                sellAmount -= matched;
                if (buyAmount > 0) buy.Enqueue((buyPrice, buyAmount), -buyPrice);
                if (sellAmount > 0) sell.Enqueue((sellPrice, sellAmount), sellPrice);
            }
        }

        long total = 0;
        while (buy.Count > 0) total = (total + buy.Dequeue().amount) % MOD;
        while (sell.Count > 0) total = (total + sell.Dequeue().amount) % MOD;
        return (int)total;
    }
}
'''

SOLUTIONS[1802] = r'''// LeetCode 1802 - Maximum Value at a Given Index in a Bounded Array
// https://leetcode.com/problems/maximum-value-at-a-given-index-in-a-bounded-array/

public class Solution {
    public int MaxValue(int n, int index, int maxSum) {
        long MinSideSum(long value, long count) {
            if (value > count) return (value - 1 + value - count) * count / 2;
            return value * (value - 1) / 2 + (count - value + 1);
        }

        int lo = 1, hi = maxSum;
        while (lo < hi) {
            int mid = (lo + hi + 1) / 2;
            long total = MinSideSum(mid, index) + mid + MinSideSum(mid, n - index - 1);
            if (total <= maxSum) lo = mid;
            else hi = mid - 1;
        }
        return lo;
    }
}
'''

SOLUTIONS[1803] = r'''// LeetCode 1803 - Count Pairs With XOR in a Range
// https://leetcode.com/problems/count-pairs-with-xor-in-a-range/

public class Solution {
    private class TrieNode {
        public int Count;
        public readonly TrieNode[] Children = new TrieNode[2];
    }

    public int CountPairs(int[] nums, int low, int high) {
        return CountSmallerThan(nums, high + 1) - CountSmallerThan(nums, low);
    }

    private int CountSmallerThan(int[] nums, int limit) {
        if (limit <= 0) return 0;
        var root = new TrieNode();
        int total = 0;
        const int maxBit = 15;
        foreach (int num in nums) {
            total += Query(root, num, limit, maxBit);
            Insert(root, num, maxBit);
        }
        return total;
    }

    private void Insert(TrieNode root, int num, int bit) {
        var node = root;
        for (int i = bit; i >= 0; i--) {
            int b = (num >> i) & 1;
            if (node.Children[b] == null) node.Children[b] = new TrieNode();
            node = node.Children[b];
            node.Count++;
        }
    }

    private int Query(TrieNode root, int num, int limit, int bit) {
        if (root == null || bit < 0) return 0;
        int numBit = (num >> bit) & 1;
        int limitBit = (limit >> bit) & 1;
        var child = root.Children[numBit];
        if (limitBit == 1) {
            int result = child != null ? child.Count : 0;
            result += Query(root.Children[1 - numBit], num, limit, bit - 1);
            return result;
        }
        return Query(child, num, limit, bit - 1);
    }
}
'''

SOLUTIONS[1804] = r'''// LeetCode 1804 - Implement Trie II (Prefix Tree)
// https://leetcode.com/problems/implement-trie-ii-prefix-tree/

using System.Collections.Generic;

public class Trie {
    private class TrieNode {
        public readonly Dictionary<char, TrieNode> Children = new();
        public int WordCount;
        public int PrefixCount;
    }

    private readonly TrieNode root = new();

    public void Insert(string word) {
        var node = root;
        foreach (char ch in word) {
            if (!node.Children.TryGetValue(ch, out var child)) {
                child = new TrieNode();
                node.Children[ch] = child;
            }
            node = child;
            node.PrefixCount++;
        }
        node.WordCount++;
    }

    public int CountWordsEqualTo(string word) {
        var node = Find(word);
        return node?.WordCount ?? 0;
    }

    public int CountWordsStartingWith(string prefix) {
        var node = Find(prefix);
        return node?.PrefixCount ?? 0;
    }

    public void Erase(string word) {
        var node = root;
        foreach (char ch in word) {
            node = node.Children[ch];
            node.PrefixCount--;
        }
        node.WordCount--;
    }

    private TrieNode Find(string text) {
        var node = root;
        foreach (char ch in text) {
            if (!node.Children.TryGetValue(ch, out node)) return null;
        }
        return node;
    }
}
'''

SOLUTIONS[1805] = r'''// LeetCode 1805 - Number of Different Integers in a String
// https://leetcode.com/problems/number-of-different-integers-in-a-string/

using System.Collections.Generic;

public class Solution {
    public int NumDifferentIntegers(string word) {
        var seen = new HashSet<string>();
        int i = 0, n = word.Length;
        while (i < n) {
            if (!char.IsDigit(word[i])) {
                i++;
                continue;
            }
            int j = i;
            while (j < n && char.IsDigit(word[j])) j++;
            string num = word.Substring(i, j - i).TrimStart('0');
            if (num.Length == 0) num = "0";
            seen.Add(num);
            i = j;
        }
        return seen.Count;
    }
}
'''

SOLUTIONS[1806] = r'''// LeetCode 1806 - Minimum Number of Operations to Reinitialize a Permutation
// https://leetcode.com/problems/minimum-number-of-operations-to-reinitialize-a-permutation/

public class Solution {
    public int ReinitializePermutation(int n) {
        int[] perm = new int[n];
        int[] target = new int[n];
        for (int i = 0; i < n; i++) {
            perm[i] = i;
            target[i] = i;
        }
        int operations = 0;
        while (true) {
            int[] next = new int[n];
            for (int i = 0; i < n; i++) {
                next[i] = i % 2 == 0 ? perm[i / 2] : perm[n / 2 + (i - 1) / 2];
            }
            perm = next;
            operations++;
            bool same = true;
            for (int i = 0; i < n; i++) {
                if (perm[i] != target[i]) { same = false; break; }
            }
            if (same) return operations;
        }
    }
}
'''

SOLUTIONS[1807] = r'''// LeetCode 1807 - Evaluate the Bracket Pairs of a String
// https://leetcode.com/problems/evaluate-the-bracket-pairs-of-a-string/

using System.Collections.Generic;
using System.Text;

public class Solution {
    public string Evaluate(string s, IList<IList<string>> knowledge) {
        var lookup = new Dictionary<string, string>();
        foreach (var pair in knowledge) lookup[pair[0]] = pair[1];

        var sb = new StringBuilder();
        int i = 0;
        while (i < s.Length) {
            if (s[i] == '(') {
                int j = s.IndexOf(')', i + 1);
                string key = s.Substring(i + 1, j - i - 1);
                sb.Append(lookup.TryGetValue(key, out var value) ? value : "?");
                i = j + 1;
            } else {
                sb.Append(s[i]);
                i++;
            }
        }
        return sb.ToString();
    }
}
'''

SOLUTIONS[1808] = r'''// LeetCode 1808 - Maximize Number of Nice Divisors
// https://leetcode.com/problems/maximize-number-of-nice-divisors/

public class Solution {
    private const int MOD = 1_000_000_007;

    public int MaxNiceDivisors(int primeFactors) {
        if (primeFactors <= 3) return primeFactors;
        if (primeFactors % 3 == 0) return (int)ModPow(3, primeFactors / 3);
        if (primeFactors % 3 == 1) return (int)(ModPow(3, primeFactors / 3 - 1) * 4 % MOD);
        return (int)(ModPow(3, primeFactors / 3) * 2 % MOD);
    }

    private long ModPow(long baseVal, long exp) {
        long result = 1;
        baseVal %= MOD;
        while (exp > 0) {
            if ((exp & 1) == 1) result = result * baseVal % MOD;
            baseVal = baseVal * baseVal % MOD;
            exp >>= 1;
        }
        return result;
    }
}
'''

SOLUTIONS[1810] = r'''// LeetCode 1810 - Minimum Path Cost in a Hidden Grid
// https://leetcode.com/problems/minimum-path-cost-in-a-hidden-grid/

using System;
using System.Collections.Generic;

public class Solution {
    // Test harness passes the revealed grid plus start/target coordinates.
    public int FindShortestPath(int[][] grid, int r1, int c1, int r2, int c2) {
        if (r1 == r2 && c1 == c2) return 0;
        int m = grid.Length, n = grid[0].Length;
        int[][] dirs = new int[][] {
            new[] { -1, 0 }, new[] { 1, 0 }, new[] { 0, -1 }, new[] { 0, 1 }
        };
        var dist = new int[m, n];
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                dist[i, j] = int.MaxValue;

        var heap = new PriorityQueue<(int d, int r, int c), int>();
        dist[r1, c1] = 0;
        heap.Enqueue((0, r1, c1), 0);

        while (heap.Count > 0) {
            var (d, r, c) = heap.Dequeue();
            if (r == r2 && c == c2) return d;
            if (d > dist[r, c]) continue;
            foreach (var dir in dirs) {
                int nr = r + dir[0], nc = c + dir[1];
                if (nr < 0 || nr >= m || nc < 0 || nc >= n || grid[nr][nc] == 0) continue;
                int nd = d + grid[nr][nc];
                if (nd < dist[nr, nc]) {
                    dist[nr, nc] = nd;
                    heap.Enqueue((nd, nr, nc), nd);
                }
            }
        }
        return -1;
    }
}
'''

SOLUTIONS[1812] = r'''// LeetCode 1812 - Determine Color of a Chessboard Square
// https://leetcode.com/problems/determine-color-of-a-chessboard-square/

public class Solution {
    public bool SquareIsWhite(string coordinates) {
        int col = coordinates[0] - 'a' + 1;
        int row = coordinates[1] - '0';
        return (col + row) % 2 == 1;
    }
}
'''

SOLUTIONS[1813] = r'''// LeetCode 1813 - Sentence Similarity III
// https://leetcode.com/problems/sentence-similarity-iii/

public class Solution {
    public bool AreSentencesSimilar(string sentence1, string sentence2) {
        string[] words1 = sentence1.Split(' ');
        string[] words2 = sentence2.Split(' ');
        int n1 = words1.Length, n2 = words2.Length;

        int i = 0;
        while (i < n1 && i < n2 && words1[i] == words2[i]) i++;
        if (i == n1 || i == n2) return true;

        int j1 = n1 - 1, j2 = n2 - 1;
        while (j1 >= i && j2 >= i && words1[j1] == words2[j2]) {
            j1--;
            j2--;
        }
        return j1 < i || j2 < i;
    }
}
'''

SOLUTIONS[1814] = r'''// LeetCode 1814 - Count Nice Pairs in an Array
// https://leetcode.com/problems/count-nice-pairs-in-an-array/

using System.Collections.Generic;

public class Solution {
    public int CountNicePairs(int[] nums) {
        const int MOD = 1_000_000_007;
        var freq = new Dictionary<int, int>();
        long ans = 0;
        foreach (int num in nums) {
            int diff = num - Rev(num);
            if (freq.TryGetValue(diff, out int count)) {
                ans = (ans + count) % MOD;
                freq[diff] = count + 1;
            } else {
                freq[diff] = 1;
            }
        }
        return (int)ans;
    }

    private int Rev(int x) {
        int result = 0;
        while (x > 0) {
            result = result * 10 + x % 10;
            x /= 10;
        }
        return result;
    }
}
'''

SOLUTIONS[1815] = r'''// LeetCode 1815 - Maximum Number of Groups Getting Fresh Donuts
// https://leetcode.com/problems/maximum-number-of-groups-getting-fresh-donuts/

using System;
using System.Collections.Generic;

public class Solution {
    private int batchSize;
    private Dictionary<long, int> memo;

    public int MaxHappyGroups(int batchSize, int[] groups) {
        this.batchSize = batchSize;
        int[] count = new int[batchSize];
        foreach (int size in groups) count[size % batchSize]++;

        memo = new Dictionary<long, int>();
        int ans = Dfs(0, count);
        if (count[0] > 0) ans += count[0] - 1;
        return ans;
    }

    private int Dfs(int remainder, int[] count) {
        long key = Encode(remainder, count);
        if (memo.TryGetValue(key, out int cached)) return cached;

        int best = 0;
        for (int mod = 1; mod < batchSize; mod++) {
            if (count[mod] == 0) continue;
            count[mod]--;
            best = Math.Max(best, Dfs((remainder + mod) % batchSize, count));
            count[mod]++;
        }

        int result = remainder == 0 ? best + 1 : best;
        memo[key] = result;
        return result;
    }

    private long Encode(int remainder, int[] count) {
        long key = remainder;
        foreach (int value in count) key = key * 31 + value;
        return key;
    }
}
'''

SOLUTIONS[1816] = r'''// LeetCode 1816 - Truncate Sentence
// https://leetcode.com/problems/truncate-sentence/

public class Solution {
    public string TruncateSentence(string s, int k) {
        string[] words = s.Split(' ');
        return string.Join(" ", words, 0, k);
    }
}
'''

SOLUTIONS[1817] = r'''// LeetCode 1817 - Finding the Users Active Minutes
// https://leetcode.com/problems/finding-the-users-active-minutes/

using System.Collections.Generic;

public class Solution {
    public int[] FindingUsersActiveMinutes(int[][] logs, int k) {
        var userMinutes = new Dictionary<int, HashSet<int>>();
        foreach (var log in logs) {
            int userId = log[0], minute = log[1];
            if (!userMinutes.TryGetValue(userId, out var set)) {
                set = new HashSet<int>();
                userMinutes[userId] = set;
            }
            set.Add(minute);
        }

        int[] answer = new int[k];
        foreach (var minutes in userMinutes.Values) {
            int uam = minutes.Count;
            if (uam <= k) answer[uam - 1]++;
        }
        return answer;
    }
}
'''

SOLUTIONS[1818] = r'''// LeetCode 1818 - Minimum Absolute Sum Difference
// https://leetcode.com/problems/minimum-absolute-sum-difference/

using System;

public class Solution {
    public int MinAbsoluteSumDiff(int[] nums1, int[] nums2) {
        const int MOD = 1_000_000_007;
        int n = nums1.Length;
        int[] sorted = (int[])nums1.Clone();
        Array.Sort(sorted);

        long total = 0;
        for (int i = 0; i < n; i++) total += Math.Abs(nums1[i] - nums2[i]);

        int bestGain = 0;
        for (int i = 0; i < n; i++) {
            int target = nums2[i];
            int current = Math.Abs(nums1[i] - target);
            int idx = Array.BinarySearch(sorted, target);
            if (idx < 0) idx = ~idx;
            foreach (int j in new[] { idx - 1, idx }) {
                if (j >= 0 && j < n) {
                    bestGain = Math.Max(bestGain, current - Math.Abs(sorted[j] - target));
                }
            }
        }
        return (int)((total - bestGain) % MOD);
    }
}
'''

SOLUTIONS[1819] = r'''// LeetCode 1819 - Number of Different Subsequences GCDs
// https://leetcode.com/problems/number-of-different-subsequences-gcds/

using System;

public class Solution {
    public int CountDifferentSubsequenceGCDs(int[] nums) {
        int maxVal = 0;
        foreach (int num in nums) maxVal = Math.Max(maxVal, num);
        bool[] present = new bool[maxVal + 1];
        foreach (int num in nums) present[num] = true;

        int ans = 0;
        for (int g = 1; g <= maxVal; g++) {
            int gcdVal = 0;
            bool has = false;
            for (int multiple = g; multiple <= maxVal; multiple += g) {
                if (!present[multiple]) continue;
                has = true;
                gcdVal = Gcd(gcdVal, multiple / g);
                if (gcdVal == 1) break;
            }
            if (has && gcdVal == 1) ans++;
        }
        return ans;
    }

    private int Gcd(int a, int b) {
        while (b != 0) {
            int t = a % b;
            a = b;
            b = t;
        }
        return a;
    }
}
'''

SOLUTIONS[1820] = r'''// LeetCode 1820 - Maximum Number of Accepted Invitations
// https://leetcode.com/problems/maximum-number-of-accepted-invitations/

public class Solution {
    public int MaximumInvitations(int[][] grid) {
        int boys = grid.Length, girls = grid[0].Length;
        int[] matchGirl = new int[girls];
        for (int i = 0; i < girls; i++) matchGirl[i] = -1;

        bool Dfs(int boy, bool[] seen) {
            for (int girl = 0; girl < girls; girl++) {
                if (grid[boy][girl] == 1 && !seen[girl]) {
                    seen[girl] = true;
                    if (matchGirl[girl] == -1 || Dfs(matchGirl[girl], seen)) {
                        matchGirl[girl] = boy;
                        return true;
                    }
                }
            }
            return false;
        }

        int ans = 0;
        for (int boy = 0; boy < boys; boy++) {
            if (Dfs(boy, new bool[girls])) ans++;
        }
        return ans;
    }
}
'''

SOLUTIONS[1822] = r'''// LeetCode 1822 - Sign of the Product of an Array
// https://leetcode.com/problems/sign-of-the-product-of-an-array/

public class Solution {
    public int ArraySign(int[] nums) {
        int sign = 1;
        foreach (int num in nums) {
            if (num == 0) return 0;
            if (num < 0) sign = -sign;
        }
        return sign;
    }
}
'''

SOLUTIONS[1823] = r'''// LeetCode 1823 - Find the Winner of the Circular Game
// https://leetcode.com/problems/find-the-winner-of-the-circular-game/

public class Solution {
    public int FindTheWinner(int n, int k) {
        int pos = 0;
        for (int size = 2; size <= n; size++) {
            pos = (pos + k) % size;
        }
        return pos + 1;
    }
}
'''

SOLUTIONS[1824] = r'''// LeetCode 1824 - Minimum Sideway Jumps
// https://leetcode.com/problems/minimum-sideway-jumps/

using System;

public class Solution {
    public int MinSideJumps(int[] obstacles) {
        const int INF = 1_000_000_000;
        int[] dp = { 1, 0, 1 };

        foreach (int obs in obstacles) {
            bool[] blocked = { obs == 1, obs == 2, obs == 3 };
            int[] ndp = { INF, INF, INF };
            for (int lane = 0; lane < 3; lane++) {
                if (blocked[lane]) continue;
                for (int other = 0; other < 3; other++) {
                    if (blocked[other] || dp[other] == INF) continue;
                    ndp[lane] = Math.Min(ndp[lane], dp[other] + (lane != other ? 1 : 0));
                }
            }
            dp = ndp;
        }
        return Math.Min(dp[0], Math.Min(dp[1], dp[2]));
    }
}
'''

SOLUTIONS[1825] = r'''// LeetCode 1825 - Finding MK Average
// https://leetcode.com/problems/finding-mk-average/

using System;
using System.Collections.Generic;

public class MKAverage {
    private readonly int m;
    private readonly int k;
    private readonly Queue<int> stream = new();

    public MKAverage(int m, int k) {
        this.m = m;
        this.k = k;
    }

    public void AddElement(int num) {
        stream.Enqueue(num);
        if (stream.Count > m) stream.Dequeue();
    }

    public int CalculateMKAverage() {
        if (stream.Count < m) return -1;
        var window = stream.ToArray();
        Array.Sort(window);
        long sum = 0;
        for (int i = k; i < window.Length - k; i++) sum += window[i];
        return (int)(sum / (window.Length - 2 * k));
    }
}
'''

SOLUTIONS[1826] = r'''// LeetCode 1826 - Faulty Sensor
// https://leetcode.com/problems/faulty-sensor/

public class Solution {
    public int BadSensor(int[] sensor1, int[] sensor2) {
        bool equal = true;
        for (int i = 0; i < sensor1.Length; i++) {
            if (sensor1[i] != sensor2[i]) { equal = false; break; }
        }
        if (equal) return -1;

        bool IsDefective(int[] correct, int[] faulty) {
            int n = correct.Length;
            int i = 0;
            while (i < n && correct[i] == faulty[i]) i++;
            if (i == n) return false;
            int j = i;
            while (j < n - 1 && correct[j + 1] == faulty[j]) j++;
            return j == n - 1;
        }

        bool sensor1Bad = IsDefective(sensor2, sensor1);
        bool sensor2Bad = IsDefective(sensor1, sensor2);
        if (sensor1Bad && sensor2Bad) return -1;
        if (sensor1Bad) return 1;
        if (sensor2Bad) return 2;
        return -1;
    }
}
'''

SOLUTIONS[1827] = r'''// LeetCode 1827 - Minimum Operations to Make the Array Increasing
// https://leetcode.com/problems/minimum-operations-to-make-the-array-increasing/

public class Solution {
    public int MinOperations(int[] nums) {
        int ops = 0;
        int prev = nums[0];
        for (int i = 1; i < nums.Length; i++) {
            if (nums[i] <= prev) {
                int needed = prev + 1;
                ops += needed - nums[i];
                prev = needed;
            } else {
                prev = nums[i];
            }
        }
        return ops;
    }
}
'''

SOLUTIONS[1828] = r'''// LeetCode 1828 - Queries on Number of Points Inside a Circle
// https://leetcode.com/problems/queries-on-number-of-points-inside-a-circle/

public class Solution {
    public int[] CountPoints(int[][] points, int[][] queries) {
        int[] result = new int[queries.Length];
        for (int qi = 0; qi < queries.Length; qi++) {
            int xq = queries[qi][0], yq = queries[qi][1], r = queries[qi][2];
            int radiusSq = r * r;
            int count = 0;
            foreach (var point in points) {
                int dx = point[0] - xq, dy = point[1] - yq;
                if (dx * dx + dy * dy <= radiusSq) count++;
            }
            result[qi] = count;
        }
        return result;
    }
}
'''

SOLUTIONS[1829] = r'''// LeetCode 1829 - Maximum XOR for Each Query
// https://leetcode.com/problems/maximum-xor-for-each-query/

public class Solution {
    public int[] GetMaximumXor(int[] nums, int maximumBit) {
        int limit = (1 << maximumBit) - 1;
        int current = 0;
        foreach (int num in nums) current ^= num;

        int[] result = new int[nums.Length];
        for (int i = nums.Length - 1; i >= 0; i--) {
            result[nums.Length - 1 - i] = current ^ limit;
            current ^= nums[i];
        }
        return result;
    }
}
'''

SOLUTIONS[1830] = r'''// LeetCode 1830 - Minimum Number of Operations to Make String Sorted
// https://leetcode.com/problems/minimum-number-of-operations-to-make-string-sorted/

public class Solution {
    public int MakeStringSorted(string s) {
        const int MOD = 1_000_000_007;
        int n = s.Length;
        long[] fact = new long[n + 1];
        long[] invFact = new long[n + 1];
        fact[0] = 1;
        for (int i = 1; i <= n; i++) fact[i] = fact[i - 1] * i % MOD;
        invFact[n] = ModPow(fact[n], MOD - 2, MOD);
        for (int i = n - 1; i >= 0; i--) invFact[i] = invFact[i + 1] * (i + 1) % MOD;

        int[] freq = new int[26];
        foreach (char ch in s) freq[ch - 'a']++;

        long ans = 0;
        for (int i = 0; i < n; i++) {
            int c = s[i] - 'a';
            for (int smaller = 0; smaller < c; smaller++) {
                if (freq[smaller] == 0) continue;
                freq[smaller]--;
                long ways = fact[n - i - 1];
                foreach (int count in freq) ways = ways * invFact[count] % MOD;
                ans = (ans + ways) % MOD;
                freq[smaller]++;
            }
            freq[c]--;
        }
        return (int)ans;
    }

    private long ModPow(long baseVal, long exp, int mod) {
        long result = 1;
        baseVal %= mod;
        while (exp > 0) {
            if ((exp & 1) == 1) result = result * baseVal % mod;
            baseVal = baseVal * baseVal % mod;
            exp >>= 1;
        }
        return result;
    }
}
'''

SOLUTIONS[1832] = r'''// LeetCode 1832 - Check if the Sentence Is Pangram
// https://leetcode.com/problems/check-if-the-sentence-is-pangram/

using System.Collections.Generic;

public class Solution {
    public bool CheckIfPangram(string sentence) {
        return new HashSet<char>(sentence).Count == 26;
    }
}
'''

SOLUTIONS[1833] = r'''// LeetCode 1833 - Maximum Ice Cream Bars
// https://leetcode.com/problems/maximum-ice-cream-bars/

using System;

public class Solution {
    public int MaxIceCream(int[] costs, int coins) {
        Array.Sort(costs);
        int count = 0;
        foreach (int cost in costs) {
            if (coins < cost) break;
            coins -= cost;
            count++;
        }
        return count;
    }
}
'''

SOLUTIONS[1834] = r'''// LeetCode 1834 - Single-Threaded CPU
// https://leetcode.com/problems/single-threaded-cpu/

using System;
using System.Collections.Generic;

public class Solution {
    public int[] GetOrder(int[][] tasks) {
        int n = tasks.Length;
        var indexed = new (int idx, int enqueue, int proc)[n];
        for (int i = 0; i < n; i++) {
            indexed[i] = (i, tasks[i][0], tasks[i][1]);
        }
        Array.Sort(indexed, (a, b) => {
            int cmp = a.enqueue.CompareTo(b.enqueue);
            return cmp != 0 ? cmp : a.idx.CompareTo(b.idx);
        });

        var heap = new PriorityQueue<int, (int proc, int idx)>();
        var order = new List<int>();
        long time = 0;
        int iPtr = 0;

        while (iPtr < n || heap.Count > 0) {
            if (iPtr < n && heap.Count == 0) {
                time = Math.Max(time, indexed[iPtr].enqueue);
            }
            while (iPtr < n && indexed[iPtr].enqueue <= time) {
                heap.Enqueue(indexed[iPtr].idx, (indexed[iPtr].proc, indexed[iPtr].idx));
                iPtr++;
            }
            heap.TryDequeue(out int idx, out var priority);
            time += priority.proc;
            order.Add(idx);
        }
        return order.ToArray();
    }
}
'''

SOLUTIONS[1835] = r'''// LeetCode 1835 - Find XOR Sum of All Pairs Bitwise AND
// https://leetcode.com/problems/find-xor-sum-of-all-pairs-bitwise-and/

public class Solution {
    public int GetXORSum(int[] arr1, int[] arr2) {
        int xor1 = 0, xor2 = 0;
        foreach (int x in arr1) xor1 ^= x;
        foreach (int x in arr2) xor2 ^= x;
        return xor1 & xor2;
    }
}
'''

SOLUTIONS[1836] = r'''// LeetCode 1836 - Remove Duplicates From an Unsorted Linked List
// https://leetcode.com/problems/remove-duplicates-from-an-unsorted-linked-list/

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
    public ListNode DeleteDuplicatesUnsorted(ListNode head) {
        var counts = new Dictionary<int, int>();
        for (var node = head; node != null; node = node.next) {
            counts.TryGetValue(node.val, out int c);
            counts[node.val] = c + 1;
        }

        var dummy = new ListNode(0, head);
        var prev = dummy;
        var cur = head;
        while (cur != null) {
            if (counts[cur.val] > 1) {
                prev.next = cur.next;
                cur = cur.next;
            } else {
                prev = cur;
                cur = cur.next;
            }
        }
        return dummy.next;
    }
}
'''

SOLUTIONS[1837] = r'''// LeetCode 1837 - Sum of Digits in Base K
// https://leetcode.com/problems/sum-of-digits-in-base-k/

public class Solution {
    public int SumBase(int n, int k) {
        int total = 0;
        while (n > 0) {
            total += n % k;
            n /= k;
        }
        return total;
    }
}
'''

SOLUTIONS[1838] = r'''// LeetCode 1838 - Frequency of the Most Frequent Element
// https://leetcode.com/problems/frequency-of-the-most-frequent-element/

using System;

public class Solution {
    public int MaxFrequency(int[] nums, int k) {
        Array.Sort(nums);
        int left = 0;
        long windowSum = 0;
        int best = 0;
        for (int right = 0; right < nums.Length; right++) {
            windowSum += nums[right];
            while ((long)nums[right] * (right - left + 1) - windowSum > k) {
                windowSum -= nums[left];
                left++;
            }
            best = Math.Max(best, right - left + 1);
        }
        return best;
    }
}
'''

SOLUTIONS[1839] = r'''// LeetCode 1839 - Longest Substring Of All Vowels in Order
// https://leetcode.com/problems/longest-substring-of-all-vowels-in-order/

using System;

public class Solution {
    public int LongestBeautifulSubstring(string word) {
        const string vowels = "aeiou";
        int best = 0;
        for (int start = 0; start < word.Length; start++) {
            if (word[start] != 'a') continue;
            int[] counts = new int[5];
            for (int end = start; end < word.Length; end++) {
                char current = word[end];
                if (end > start && current < word[end - 1]) break;
                int idx = vowels.IndexOf(current);
                if (idx < 0) break;
                counts[idx]++;
                if (idx > 0 && counts[idx - 1] == 0) break;
                bool all = true;
                foreach (int c in counts) if (c == 0) { all = false; break; }
                if (all) best = Math.Max(best, end - start + 1);
            }
        }
        return best;
    }
}
'''

SOLUTIONS[1840] = r'''// LeetCode 1840 - Maximum Building Height
// https://leetcode.com/problems/maximum-building-height/

using System;
using System.Collections.Generic;

public class Solution {
    public int MaxBuilding(int n, int[][] restrictions) {
        var points = new List<int[]> { new[] { 1, 0 } };
        Array.Sort(restrictions, (a, b) => a[0].CompareTo(b[0]));
        foreach (var r in restrictions) points.Add(new[] { r[0], r[1] });
        if (points[^1][0] != n) points.Add(new[] { n, n - 1 });

        for (int i = 1; i < points.Count; i++) {
            int prevId = points[i - 1][0], prevH = points[i - 1][1];
            int currId = points[i][0], currH = points[i][1];
            points[i][1] = Math.Min(currH, prevH + currId - prevId);
        }
        for (int i = points.Count - 2; i >= 0; i--) {
            int nextId = points[i + 1][0], nextH = points[i + 1][1];
            int currId = points[i][0], currH = points[i][1];
            points[i][1] = Math.Min(currH, nextH + nextId - currId);
        }

        int best = 0;
        foreach (var p in points) best = Math.Max(best, p[1]);
        for (int i = 0; i < points.Count - 1; i++) {
            int id1 = points[i][0], h1 = points[i][1];
            int id2 = points[i + 1][0], h2 = points[i + 1][1];
            best = Math.Max(best, (h1 + h2 + id2 - id1) / 2);
        }
        return best;
    }
}
'''

SOLUTIONS[1842] = r'''// LeetCode 1842 - Next Palindrome Using Same Digits
// https://leetcode.com/problems/next-palindrome-using-same-digits/

public class Solution {
    public string NextPalindrome(string num) {
        char[] chars = num.ToCharArray();
        if (!NextPermutation(chars)) return "";
        int n = chars.Length;
        for (int i = 0; i < n / 2; i++) chars[n - i - 1] = chars[i];
        return new string(chars);
    }

    private bool NextPermutation(char[] nums) {
        int half = nums.Length / 2;
        int i = half - 2;
        while (i >= 0 && nums[i] >= nums[i + 1]) i--;
        if (i < 0) return false;
        int j = half - 1;
        while (nums[j] <= nums[i]) j--;
        (nums[i], nums[j]) = (nums[j], nums[i]);
        System.Array.Reverse(nums, i + 1, half - i - 1);
        return true;
    }
}
'''

SOLUTIONS[1844] = r'''// LeetCode 1844 - Replace All Digits with Characters
// https://leetcode.com/problems/replace-all-digits-with-characters/

public class Solution {
    public string ReplaceDigits(string s) {
        char[] chars = s.ToCharArray();
        for (int i = 1; i < chars.Length; i += 2) {
            chars[i] = (char)(chars[i - 1] + (chars[i] - '0'));
        }
        return new string(chars);
    }
}
'''

SOLUTIONS[1845] = r'''// LeetCode 1845 - Seat Reservation Manager
// https://leetcode.com/problems/seat-reservation-manager/

using System.Collections.Generic;

public class SeatManager {
    private readonly PriorityQueue<int, int> available = new();

    public SeatManager(int n) {
        for (int i = 1; i <= n; i++) available.Enqueue(i, i);
    }

    public int Reserve() {
        return available.Dequeue();
    }

    public void Unreserve(int seatNumber) {
        available.Enqueue(seatNumber, seatNumber);
    }
}
'''

SOLUTIONS[1846] = r'''// LeetCode 1846 - Maximum Element After Decreasing and Rearranging
// https://leetcode.com/problems/maximum-element-after-decreasing-and-rearranging/

using System;

public class Solution {
    public int MaximumElementAfterDecrementingAndRearranging(int[] arr) {
        Array.Sort(arr);
        arr[0] = 1;
        for (int i = 1; i < arr.Length; i++) {
            arr[i] = Math.Min(arr[i], arr[i - 1] + 1);
        }
        int best = 0;
        foreach (int v in arr) best = Math.Max(best, v);
        return best;
    }
}
'''

SOLUTIONS[1847] = r'''// LeetCode 1847 - Closest Room
// https://leetcode.com/problems/closest-room/

using System;
using System.Collections.Generic;

public class Solution {
    public int[] ClosestRoom(int[][] rooms, int[][] queries) {
        Array.Sort(rooms, (a, b) => a[1].CompareTo(b[1]));
        var indexed = new int[queries.Length][];
        for (int i = 0; i < queries.Length; i++) {
            indexed[i] = new[] { i, queries[i][0], queries[i][1] };
        }
        Array.Sort(indexed, (a, b) => b[2].CompareTo(a[2]));

        var available = new SortedSet<int>();
        int roomIndex = rooms.Length - 1;
        int[] answer = new int[queries.Length];
        Array.Fill(answer, -1);

        foreach (var query in indexed) {
            int queryIndex = query[0], preferred = query[1], minSize = query[2];
            while (roomIndex >= 0 && rooms[roomIndex][1] >= minSize) {
                available.Add(rooms[roomIndex][0]);
                roomIndex--;
            }
            if (available.Count == 0) continue;

            int bestId = -1, bestDist = int.MaxValue;
            var higherView = available.GetViewBetween(preferred, int.MaxValue);
            if (higherView.Count > 0) {
                bestId = higherView.Min;
                bestDist = Math.Abs(bestId - preferred);
            }
            if (preferred > int.MinValue) {
                var lowerView = available.GetViewBetween(int.MinValue, preferred);
                if (lowerView.Count > 0) {
                    int lower = lowerView.Max;
                    int dist = Math.Abs(lower - preferred);
                    if (dist < bestDist || (dist == bestDist && lower < bestId)) {
                        bestId = lower;
                    }
                }
            }
            answer[queryIndex] = bestId;
        }
        return answer;
    }
}
'''

SOLUTIONS[1848] = r'''// LeetCode 1848 - Minimum Distance to the Target Element
// https://leetcode.com/problems/minimum-distance-to-the-target-element/

using System;

public class Solution {
    public int GetMinDistance(int[] nums, int target, int start) {
        int best = nums.Length;
        for (int i = 0; i < nums.Length; i++) {
            if (nums[i] == target) best = Math.Min(best, Math.Abs(i - start));
        }
        return best;
    }
}
'''

SOLUTIONS[1849] = r'''// LeetCode 1849 - Splitting a String Into Descending Consecutive Values
// https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/

using System.Numerics;

public class Solution {
    public bool SplitString(string s) {
        return Dfs(s, 0, null, 0);
    }

    private bool Dfs(string s, int index, BigInteger? previous, int parts) {
        if (index == s.Length) return parts >= 2;
        for (int end = index + 1; end <= s.Length; end++) {
            var value = BigInteger.Parse(s.Substring(index, end - index));
            if (previous == null) {
                if (Dfs(s, end, value, parts + 1)) return true;
            } else if (value == previous.Value - 1) {
                if (Dfs(s, end, value, parts + 1)) return true;
            } else if (value > previous.Value - 1) {
                break;
            }
        }
        return false;
    }
}
'''

SOLUTIONS[1850] = r'''// LeetCode 1850 - Minimum Adjacent Swaps to Reach the Kth Smallest Number
// https://leetcode.com/problems/minimum-adjacent-swaps-to-reach-the-kth-smallest-number/

public class Solution {
    public int GetMinSwaps(string num, int k) {
        char[] target = num.ToCharArray();
        for (int t = 0; t < k; t++) NextPermutation(target);

        char[] source = num.ToCharArray();
        int swaps = 0;
        for (int i = 0; i < source.Length; i++) {
            if (source[i] == target[i]) continue;
            int j = i;
            while (source[j] != target[i]) j++;
            while (j > i) {
                (source[j], source[j - 1]) = (source[j - 1], source[j]);
                swaps++;
                j--;
            }
        }
        return swaps;
    }

    private void NextPermutation(char[] arr) {
        int i = arr.Length - 2;
        while (i >= 0 && arr[i] >= arr[i + 1]) i--;
        if (i < 0) {
            System.Array.Reverse(arr);
            return;
        }
        int j = arr.Length - 1;
        while (arr[j] <= arr[i]) j--;
        (arr[i], arr[j]) = (arr[j], arr[i]);
        System.Array.Reverse(arr, i + 1, arr.Length - i - 1);
    }
}
'''


def main() -> None:
    written = 0
    for num, folder in sorted(FOLDERS.items()):
        path = ROOT / folder / "Solution.cs"
        path.write_text(SOLUTIONS[num], encoding="utf-8", newline="\n")
        written += 1
        print(f"wrote {path.relative_to(ROOT)}")
    print(f"done: {written} files")


if __name__ == "__main__":
    main()
