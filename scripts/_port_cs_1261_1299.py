#!/usr/bin/env python3
"""Write C# solutions for LeetCode 1261-1299 (non-SQL stubs)."""
from __future__ import annotations

import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SOLUTIONS: dict[str, str] = {
    "1261_find_elements_in_a_contaminated_binary_tree": """// LeetCode 1261 - Find Elements in a Contaminated Binary Tree
// https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree/

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

public class FindElements {
    private readonly HashSet<int> values = new HashSet<int>();

    public FindElements(TreeNode root) {
        void Recover(TreeNode node, int value) {
            if (node == null) return;
            node.val = value;
            values.Add(value);
            Recover(node.left, 2 * value + 1);
            Recover(node.right, 2 * value + 2);
        }
        Recover(root, 0);
    }

    public bool Find(int target) {
        return values.Contains(target);
    }
}
""",
    "1262_greatest_sum_divisible_by_three": """// LeetCode 1262 - Greatest Sum Divisible by Three
// https://leetcode.com/problems/greatest-sum-divisible-by-three/

public class Solution {
    public int MaxSumDivThree(int[] nums) {
        const long impossible = -1000000000000000000L;
        long[] dp = { 0, impossible, impossible };
        foreach (int value in nums) {
            long[] old = (long[])dp.Clone();
            for (int total = 0; total < 3; total++) {
                if (old[total] != impossible) {
                    int remainder = (int)((old[total] + value) % 3);
                    dp[remainder] = System.Math.Max(dp[remainder], old[total] + value);
                }
            }
        }
        return (int)dp[0];
    }
}
""",
    "1263_minimum_moves_to_move_a_box_to_their_target_location": """// LeetCode 1263 - Minimum Moves to Move a Box to Their Target Location
// https://leetcode.com/problems/minimum-moves-to-move-a-box-to-their-target-location/

using System.Collections.Generic;

public class Solution {
    public int MinPushBox(char[][] grid) {
        int m = grid.Length, n = grid[0].Length;
        int[] box = null, player = null, target = null;
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (grid[r][c] == 'B') box = new[] { r, c };
                else if (grid[r][c] == 'S') player = new[] { r, c };
                else if (grid[r][c] == 'T') target = new[] { r, c };
            }
        }

        HashSet<int> Reachable(int[] start, int[] blocked) {
            var seen = new HashSet<int> { start[0] * n + start[1] };
            var stack = new Stack<int[]>();
            stack.Push(start);
            while (stack.Count > 0) {
                var cur = stack.Pop();
                foreach (var d in new[] { new[] { 1, 0 }, new[] { -1, 0 }, new[] { 0, 1 }, new[] { 0, -1 } }) {
                    int nr = cur[0] + d[0], nc = cur[1] + d[1];
                    int key = nr * n + nc;
                    if (nr < 0 || nr >= m || nc < 0 || nc >= n || grid[nr][nc] == '#') continue;
                    if (blocked != null && nr == blocked[0] && nc == blocked[1]) continue;
                    if (seen.Add(key)) stack.Push(new[] { nr, nc });
                }
            }
            return seen;
        }

        var queue = new Queue<(int[] box, int[] player, int pushes)>();
        var seenStates = new HashSet<long>();
        long StateKey(int[] b, int[] p) => ((long)b[0] * n + b[1]) << 20 | (p[0] * n + p[1]);
        queue.Enqueue((box, player, 0));
        seenStates.Add(StateKey(box, player));
        int[][] dirs = { new[] { 1, 0 }, new[] { -1, 0 }, new[] { 0, 1 }, new[] { 0, -1 } };

        while (queue.Count > 0) {
            var (b, p, pushes) = queue.Dequeue();
            if (b[0] == target[0] && b[1] == target[1]) return pushes;
            var canReach = Reachable(p, b);
            foreach (var d in dirs) {
                int[] stand = { b[0] - d[0], b[1] - d[1] };
                int[] nb = { b[0] + d[0], b[1] + d[1] };
                if (!canReach.Contains(stand[0] * n + stand[1])) continue;
                if (nb[0] < 0 || nb[0] >= m || nb[1] < 0 || nb[1] >= n || grid[nb[0]][nb[1]] == '#') continue;
                long key = StateKey(nb, b);
                if (seenStates.Add(key)) queue.Enqueue((nb, b, pushes + 1));
            }
        }
        return -1;
    }
}
""",
    "1265_print_immutable_linked_list_in_reverse": """// LeetCode 1265 - Print Immutable Linked List in Reverse
// https://leetcode.com/problems/print-immutable-linked-list-in-reverse/

public class ImmutableListNode {
    public virtual void PrintValue() { }
    public virtual ImmutableListNode GetNext() { return null; }
}

public class Solution {
    public void PrintLinkedListInReverse(ImmutableListNode head) {
        if (head == null) return;
        PrintLinkedListInReverse(head.GetNext());
        head.PrintValue();
    }
}
""",
    "1266_minimum_time_visiting_all_points": """// LeetCode 1266 - Minimum Time Visiting All Points
// https://leetcode.com/problems/minimum-time-visiting-all-points/

public class Solution {
    public int MinTimeToVisitAllPoints(int[][] points) {
        int total = 0;
        for (int i = 1; i < points.Length; i++) {
            total += System.Math.Max(
                System.Math.Abs(points[i][0] - points[i - 1][0]),
                System.Math.Abs(points[i][1] - points[i - 1][1]));
        }
        return total;
    }
}
""",
    "1267_count_servers_that_communicate": """// LeetCode 1267 - Count Servers That Communicate
// https://leetcode.com/problems/count-servers-that-communicate/

public class Solution {
    public int CountServers(int[][] grid) {
        int m = grid.Length, n = grid[0].Length;
        var rows = new int[m];
        var cols = new int[n];
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (grid[r][c] == 1) {
                    rows[r]++;
                    cols[c]++;
                }
            }
        }
        int count = 0;
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (grid[r][c] == 1 && (rows[r] > 1 || cols[c] > 1)) count++;
            }
        }
        return count;
    }
}
""",
    "1268_search_suggestions_system": """// LeetCode 1268 - Search Suggestions System
// https://leetcode.com/problems/search-suggestions-system/

using System.Collections.Generic;
using System.Linq;

public class Solution {
    public IList<IList<string>> SuggestedProducts(string[] products, string searchWord) {
        System.Array.Sort(products);
        var answer = new List<IList<string>>();
        string prefix = "";
        foreach (char ch in searchWord) {
            prefix += ch;
            int i = LowerBound(products, prefix);
            var row = new List<string>();
            for (int j = i; j < products.Length && j < i + 3; j++) {
                if (products[j].StartsWith(prefix)) row.Add(products[j]);
                else break;
            }
            answer.Add(row);
        }
        return answer;
    }

    private static int LowerBound(string[] arr, string target) {
        int lo = 0, hi = arr.Length;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (string.CompareOrdinal(arr[mid], target) < 0) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    }
}
""",
    "1269_number_of_ways_to_stay_in_the_same_place_after_some_steps": """// LeetCode 1269 - Number of Ways to Stay in the Same Place After Some Steps
// https://leetcode.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps/

public class Solution {
    public int NumWays(int steps, int arrLen) {
        const int mod = 1_000_000_007;
        int width = System.Math.Min(arrLen, steps / 2 + 1);
        var dp = new int[width];
        dp[0] = 1;
        for (int s = 0; s < steps; s++) {
            var next = new int[width];
            for (int i = 0; i < width; i++) {
                next[i] = dp[i];
                if (i > 0) next[i] = (next[i] + dp[i - 1]) % mod;
                if (i + 1 < width) next[i] = (next[i] + dp[i + 1]) % mod;
            }
            dp = next;
        }
        return dp[0];
    }
}
""",
    "1271_hexspeak": """// LeetCode 1271 - Hexspeak
// https://leetcode.com/problems/hexspeak/

public class Solution {
    public string ToHexspeak(string num) {
        long value = long.Parse(num);
        const string digits = "0123456789ABCDEF";
        var outChars = new System.Text.StringBuilder();
        while (value > 0) {
            int rem = (int)(value % 16);
            if (rem >= 2 && rem <= 9) return "ERROR";
            outChars.Insert(0, digits[rem]);
            value /= 16;
        }
        string result = outChars.Length == 0 ? "0" : outChars.ToString();
        return result.Replace('0', 'O').Replace('1', 'I');
    }
}
""",
    "1272_remove_interval": """// LeetCode 1272 - Remove Interval
// https://leetcode.com/problems/remove-interval/

using System.Collections.Generic;

public class Solution {
    public int[][] RemoveInterval(int[][] intervals, int[] toBeRemoved) {
        int left = toBeRemoved[0], right = toBeRemoved[1];
        var answer = new List<int[]>();
        foreach (var interval in intervals) {
            int start = interval[0], end = interval[1];
            if (end <= left || start >= right) {
                answer.Add(new[] { start, end });
            } else {
                if (start < left) answer.Add(new[] { start, left });
                if (end > right) answer.Add(new[] { right, end });
            }
        }
        return answer.ToArray();
    }
}
""",
    "1273_delete_tree_nodes": """// LeetCode 1273 - Delete Tree Nodes
// https://leetcode.com/problems/delete-tree-nodes/

using System.Collections.Generic;

public class Solution {
    public int DeleteTreeNodes(int nodes, int[] parent, int[] value) {
        var children = new List<int>[nodes];
        for (int i = 0; i < nodes; i++) children[i] = new List<int>();
        for (int node = 1; node < nodes; node++) children[parent[node]].Add(node);

        (int total, int count) Dfs(int node) {
            int total = value[node], count = 1;
            foreach (int child in children[node]) {
                var (childSum, childCount) = Dfs(child);
                total += childSum;
                count += childCount;
            }
            return (total, total == 0 ? 0 : count);
        }
        return Dfs(0).count;
    }
}
""",
    "1274_number_of_ships_in_a_rectangle": """// LeetCode 1274 - Number of Ships in a Rectangle
// https://leetcode.com/problems/number-of-ships-in-a-rectangle/

public class Point {
    public int x;
    public int y;
    public Point() { }
    public Point(int x, int y) {
        this.x = x;
        this.y = y;
    }
}

public class Sea {
    public bool HasShips(Point topRight, Point bottomLeft) {
        throw new System.NotImplementedException();
    }
}

public class Solution {
    public int CountShips(Sea sea, Point topRight, Point bottomLeft) {
        if (topRight.x < bottomLeft.x || topRight.y < bottomLeft.y) return 0;
        if (!sea.HasShips(topRight, bottomLeft)) return 0;
        if (topRight.x == bottomLeft.x && topRight.y == bottomLeft.y) return 1;
        int mx = (topRight.x + bottomLeft.x) / 2;
        int my = (topRight.y + bottomLeft.y) / 2;
        return CountShips(sea, new Point(mx, my), bottomLeft)
            + CountShips(sea, new Point(topRight.x, my), new Point(mx + 1, bottomLeft.y))
            + CountShips(sea, new Point(mx, topRight.y), new Point(bottomLeft.x, my + 1))
            + CountShips(sea, topRight, new Point(mx + 1, my + 1));
    }
}
""",
    "1275_find_winner_on_a_tic_tac_toe_game": """// LeetCode 1275 - Find Winner on a Tic Tac Toe Game
// https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/

public class Solution {
    public string Tictactoe(int[][] moves) {
        int[][] board = {
            new[] { 0, 0, 0 },
            new[] { 0, 0, 0 },
            new[] { 0, 0, 0 },
        };
        for (int i = 0; i < moves.Length; i++) {
            int r = moves[i][0], c = moves[i][1];
            board[r][c] = i % 2 == 0 ? 1 : -1;
        }
        var lines = new System.Collections.Generic.List<int[]>();
        for (int i = 0; i < 3; i++) lines.Add(board[i]);
        for (int c = 0; c < 3; c++) lines.Add(new[] { board[0][c], board[1][c], board[2][c] });
        lines.Add(new[] { board[0][0], board[1][1], board[2][2] });
        lines.Add(new[] { board[0][2], board[1][1], board[2][0] });
        foreach (var line in lines) {
            int sum = line[0] + line[1] + line[2];
            if (System.Math.Abs(sum) == 3) return sum == 3 ? "A" : "B";
        }
        return moves.Length == 9 ? "Draw" : "Pending";
    }
}
""",
    "1276_number_of_burgers_with_no_waste_of_ingredients": """// LeetCode 1276 - Number of Burgers with No Waste of Ingredients
// https://leetcode.com/problems/number-of-burgers-with-no-waste-of-ingredients/

public class Solution {
    public int[] NumOfBurgers(int tomatoSlices, int cheeseSlices) {
        if (tomatoSlices % 2 != 0) return new int[0];
        int jumbo = tomatoSlices / 2 - cheeseSlices;
        int small = cheeseSlices - jumbo;
        return jumbo >= 0 && small >= 0 ? new[] { jumbo, small } : new int[0];
    }
}
""",
    "1277_count_square_submatrices_with_all_ones": """// LeetCode 1277 - Count Square Submatrices with All Ones
// https://leetcode.com/problems/count-square-submatrices-with-all-ones/

public class Solution {
    public int CountSquares(int[][] matrix) {
        int answer = 0;
        for (int r = 0; r < matrix.Length; r++) {
            for (int c = 0; c < matrix[0].Length; c++) {
                if (matrix[r][c] != 0 && r > 0 && c > 0) {
                    matrix[r][c] += System.Math.Min(
                        matrix[r - 1][c],
                        System.Math.Min(matrix[r][c - 1], matrix[r - 1][c - 1]));
                }
                answer += matrix[r][c];
            }
        }
        return answer;
    }
}
""",
    "1278_palindrome_partitioning_iii": """// LeetCode 1278 - Palindrome Partitioning III
// https://leetcode.com/problems/palindrome-partitioning-iii/

public class Solution {
    public int PalindromePartition(string s, int k) {
        int n = s.Length;
        var cost = new int[n][];
        for (int i = 0; i < n; i++) cost[i] = new int[n];
        for (int length = 2; length <= n; length++) {
            for (int i = 0; i <= n - length; i++) {
                int j = i + length - 1;
                cost[i][j] = (length > 2 ? cost[i + 1][j - 1] : 0) + (s[i] != s[j] ? 1 : 0);
            }
        }
        int inf = n + 1;
        var dp = new int[k + 1][];
        for (int i = 0; i <= k; i++) {
            dp[i] = new int[n + 1];
            for (int j = 0; j <= n; j++) dp[i][j] = inf;
        }
        dp[0][0] = 0;
        for (int parts = 1; parts <= k; parts++) {
            for (int end = parts; end <= n; end++) {
                for (int start = parts - 1; start < end; start++) {
                    dp[parts][end] = System.Math.Min(
                        dp[parts][end],
                        dp[parts - 1][start] + cost[start][end - 1]);
                }
            }
        }
        return dp[k][n];
    }
}
""",
    "1279_traffic_light_controlled_intersection": """// LeetCode 1279 - Traffic Light Controlled Intersection
// https://leetcode.com/problems/traffic-light-controlled-intersection/

using System;

public class TrafficLight {
    private int greenRoad = 1;
    private readonly object gate = new object();

    public void CarArrived(
        int carId,
        int roadId,
        int direction,
        Action turnGreen,
        Action crossCar) {
        lock (gate) {
            if (roadId != greenRoad) {
                turnGreen();
                greenRoad = roadId;
            }
            crossCar();
        }
    }
}
""",
    "1281_subtract_the_product_and_sum_of_digits_of_an_integer": """// LeetCode 1281 - Subtract the Product and Sum of Digits of an Integer
// https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/

public class Solution {
    public int SubtractProductAndSum(int n) {
        int product = 1, total = 0;
        while (n > 0) {
            int digit = n % 10;
            product *= digit;
            total += digit;
            n /= 10;
        }
        return product - total;
    }
}
""",
    "1282_group_the_people_given_the_group_size_they_belong_to": """// LeetCode 1282 - Group the People Given the Group Size They Belong To
// https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/

using System.Collections.Generic;
using System.Linq;

public class Solution {
    public IList<IList<int>> GroupThePeople(int[] groupSizes) {
        var pending = new Dictionary<int, List<int>>();
        var answer = new List<IList<int>>();
        for (int person = 0; person < groupSizes.Length; person++) {
            int size = groupSizes[person];
            if (!pending.ContainsKey(size)) pending[size] = new List<int>();
            pending[size].Add(person);
            if (pending[size].Count == size) {
                answer.Add(pending[size]);
                pending[size] = new List<int>();
            }
        }
        return answer
            .OrderBy(group => group.Count)
            .ThenBy(group => string.Join(",", group))
            .ToList();
    }
}
""",
    "1283_find_the_smallest_divisor_given_a_threshold": """// LeetCode 1283 - Find the Smallest Divisor Given a Threshold
// https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/

using System.Linq;

public class Solution {
    public int SmallestDivisor(int[] nums, int threshold) {
        int lo = 1, hi = nums.Max();
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            long sum = 0;
            foreach (int x in nums) sum += (x + mid - 1) / mid;
            if (sum <= threshold) hi = mid;
            else lo = mid + 1;
        }
        return lo;
    }
}
""",
    "1284_minimum_number_of_flips_to_convert_binary_matrix_to_zero_matrix": """// LeetCode 1284 - Minimum Number of Flips to Convert Binary Matrix to Zero Matrix
// https://leetcode.com/problems/minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix/

using System.Collections.Generic;

public class Solution {
    public int MinFlips(int[][] mat) {
        int m = mat.Length, n = mat[0].Length;
        int start = 0;
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (mat[r][c] != 0) start |= 1 << (r * n + c);
            }
        }
        var masks = new List<int>();
        int[][] deltas = { new[] { 0, 0 }, new[] { 1, 0 }, new[] { -1, 0 }, new[] { 0, 1 }, new[] { 0, -1 } };
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                int mask = 0;
                foreach (var d in deltas) {
                    int nr = r + d[0], nc = c + d[1];
                    if (nr >= 0 && nr < m && nc >= 0 && nc < n) mask ^= 1 << (nr * n + nc);
                }
                masks.Add(mask);
            }
        }
        var queue = new Queue<(int state, int distance)>();
        var seen = new HashSet<int> { start };
        queue.Enqueue((start, 0));
        while (queue.Count > 0) {
            var (state, distance) = queue.Dequeue();
            if (state == 0) return distance;
            foreach (int mask in masks) {
                int nxt = state ^ mask;
                if (seen.Add(nxt)) queue.Enqueue((nxt, distance + 1));
            }
        }
        return -1;
    }
}
""",
    "1286_iterator_for_combination": """// LeetCode 1286 - Iterator for Combination
// https://leetcode.com/problems/iterator-for-combination/

using System.Collections.Generic;
using System.Linq;

public class CombinationIterator {
    private readonly string[] items;
    private int index = 0;

    public CombinationIterator(string characters, int combinationLength) {
        items = BuildCombinations(characters, combinationLength);
    }

    public string Next() {
        return items[index++];
    }

    public bool HasNext() {
        return index < items.Length;
    }

    private static string[] BuildCombinations(string characters, int k) {
        var result = new List<string>();
        void Dfs(int start, char[] path, int depth) {
            if (depth == k) {
                result.Add(new string(path, 0, k));
                return;
            }
            for (int i = start; i < characters.Length; i++) {
                path[depth] = characters[i];
                Dfs(i + 1, path, depth + 1);
            }
        }
        Dfs(0, new char[k], 0);
        return result.ToArray();
    }
}
""",
    "1287_element_appearing_more_than_25_in_sorted_array": """// LeetCode 1287 - Element Appearing More Than 25% In Sorted Array
// https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/

public class Solution {
    public int FindSpecialInteger(int[] arr) {
        int n = arr.Length;
        int threshold = n / 4;
        foreach (int idx in new[] { n / 4, n / 2, 3 * n / 4 }) {
            int value = arr[idx];
            int count = 0;
            foreach (int x in arr) if (x == value) count++;
            if (count > threshold) return value;
        }
        return arr[0];
    }
}
""",
    "1288_remove_covered_intervals": """// LeetCode 1288 - Remove Covered Intervals
// https://leetcode.com/problems/remove-covered-intervals/

using System.Linq;

public class Solution {
    public int RemoveCoveredIntervals(int[][] intervals) {
        var sorted = intervals
            .OrderBy(x => x[0])
            .ThenByDescending(x => x[1])
            .ToArray();
        int answer = 0, farthest = -1;
        foreach (var interval in sorted) {
            if (interval[1] > farthest) {
                answer++;
                farthest = interval[1];
            }
        }
        return answer;
    }
}
""",
    "1289_minimum_falling_path_sum_ii": """// LeetCode 1289 - Minimum Falling Path Sum II
// https://leetcode.com/problems/minimum-falling-path-sum-ii/

using System.Linq;

public class Solution {
    public int MinFallingPathSum(int[][] grid) {
        var dp = (int[])grid[0].Clone();
        for (int rowIndex = 1; rowIndex < grid.Length; rowIndex++) {
            int[] row = grid[rowIndex];
            int first = 0;
            for (int i = 1; i < dp.Length; i++) {
                if (dp[i] < dp[first]) first = i;
            }
            int secondValue = int.MaxValue;
            for (int i = 0; i < dp.Length; i++) {
                if (i != first) secondValue = System.Math.Min(secondValue, dp[i]);
            }
            if (dp.Length == 1) secondValue = 0;
            var next = new int[dp.Length];
            for (int i = 0; i < row.Length; i++) {
                next[i] = row[i] + (i == first ? secondValue : dp[first]);
            }
            dp = next;
        }
        return dp.Min();
    }
}
""",
    "1290_convert_binary_number_in_a_linked_list_to_integer": """// LeetCode 1290 - Convert Binary Number in a Linked List to Integer
// https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/

public class ListNode {
    public int val;
    public ListNode next;
    public ListNode(int val = 0, ListNode next = null) {
        this.val = val;
        this.next = next;
    }
}

public class Solution {
    public int GetDecimalValue(ListNode head) {
        int value = 0;
        while (head != null) {
            value = value * 2 + head.val;
            head = head.next;
        }
        return value;
    }
}
""",
    "1291_sequential_digits": """// LeetCode 1291 - Sequential Digits
// https://leetcode.com/problems/sequential-digits/

using System.Collections.Generic;

public class Solution {
    public IList<int> SequentialDigits(int low, int high) {
        const string digits = "123456789";
        var answer = new List<int>();
        for (int length = 2; length <= 9; length++) {
            for (int start = 0; start <= 9 - length; start++) {
                int value = int.Parse(digits.Substring(start, length));
                if (value >= low && value <= high) answer.Add(value);
            }
        }
        return answer;
    }
}
""",
    "1292_maximum_side_length_of_a_square_with_sum_less_than_or_equal_to_threshold": """// LeetCode 1292 - Maximum Side Length of a Square with Sum Less than or Equal to Threshold
// https://leetcode.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/

public class Solution {
    public int MaxSideLength(int[][] mat, int threshold) {
        int m = mat.Length, n = mat[0].Length;
        var prefix = new int[m + 1][];
        for (int i = 0; i <= m; i++) prefix[i] = new int[n + 1];
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                prefix[r + 1][c + 1] = mat[r][c] + prefix[r][c + 1] + prefix[r + 1][c] - prefix[r][c];
            }
        }
        bool Possible(int size) {
            for (int r = size; r <= m; r++) {
                for (int c = size; c <= n; c++) {
                    int sum = prefix[r][c] - prefix[r - size][c] - prefix[r][c - size] + prefix[r - size][c - size];
                    if (sum <= threshold) return true;
                }
            }
            return false;
        }
        int lo = 0, hi = System.Math.Min(m, n);
        while (lo < hi) {
            int mid = (lo + hi + 1) / 2;
            if (Possible(mid)) lo = mid;
            else hi = mid - 1;
        }
        return lo;
    }
}
""",
    "1293_shortest_path_in_a_grid_with_obstacles_elimination": """// LeetCode 1293 - Shortest Path in a Grid with Obstacles Elimination
// https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/

using System.Collections.Generic;

public class Solution {
    public int ShortestPath(int[][] grid, int k) {
        int m = grid.Length, n = grid[0].Length;
        if (k >= m + n - 2) return m + n - 2;
        var queue = new Queue<(int r, int c, int remaining, int distance)>();
        var best = new Dictionary<(int, int), int> { [(0, 0)] = k };
        queue.Enqueue((0, 0, k, 0));
        int[][] dirs = { new[] { 1, 0 }, new[] { -1, 0 }, new[] { 0, 1 }, new[] { 0, -1 } };
        while (queue.Count > 0) {
            var (r, c, remaining, distance) = queue.Dequeue();
            if (r == m - 1 && c == n - 1) return distance;
            foreach (var d in dirs) {
                int nr = r + d[0], nc = c + d[1];
                if (nr < 0 || nr >= m || nc < 0 || nc >= n) continue;
                int nxt = remaining - grid[nr][nc];
                if (nxt < 0) continue;
                if (best.TryGetValue((nr, nc), out int prev) && nxt <= prev) continue;
                best[(nr, nc)] = nxt;
                queue.Enqueue((nr, nc, nxt, distance + 1));
            }
        }
        return -1;
    }
}
""",
    "1295_find_numbers_with_even_number_of_digits": """// LeetCode 1295 - Find Numbers with Even Number of Digits
// https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

public class Solution {
    public int FindNumbers(int[] nums) {
        int count = 0;
        foreach (int value in nums) {
            int digits = value == 0 ? 1 : 0;
            int x = value;
            while (x > 0) {
                digits++;
                x /= 10;
            }
            if (digits % 2 == 0) count++;
        }
        return count;
    }
}
""",
    "1296_divide_array_in_sets_of_k_consecutive_numbers": """// LeetCode 1296 - Divide Array in Sets of K Consecutive Numbers
// https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/

using System.Collections.Generic;
using System.Linq;

public class Solution {
    public bool IsPossibleDivide(int[] nums, int k) {
        if (nums.Length % k != 0) return false;
        var counts = new SortedDictionary<int, int>();
        foreach (int x in nums) {
            if (!counts.ContainsKey(x)) counts[x] = 0;
            counts[x]++;
        }
        foreach (int start in counts.Keys.ToList()) {
            int amount = counts[start];
            if (amount == 0) continue;
            for (int value = start; value < start + k; value++) {
                if (!counts.TryGetValue(value, out int have) || have < amount) return false;
                counts[value] = have - amount;
            }
        }
        return true;
    }
}
""",
    "1297_maximum_number_of_occurrences_of_a_substring": """// LeetCode 1297 - Maximum Number of Occurrences of a Substring
// https://leetcode.com/problems/maximum-number-of-occurrences-of-a-substring/

using System.Collections.Generic;

public class Solution {
    public int MaxFreq(string s, int maxLetters, int minSize, int maxSize) {
        var counts = new Dictionary<string, int>();
        for (int i = 0; i + minSize <= s.Length; i++) {
            string sub = s.Substring(i, minSize);
            var seen = new HashSet<char>();
            foreach (char ch in sub) seen.Add(ch);
            if (seen.Count <= maxLetters) {
                if (!counts.ContainsKey(sub)) counts[sub] = 0;
                counts[sub]++;
            }
        }
        int best = 0;
        foreach (var kv in counts) best = System.Math.Max(best, kv.Value);
        return best;
    }
}
""",
    "1298_maximum_candies_you_can_get_from_boxes": """// LeetCode 1298 - Maximum Candies You Can Get from Boxes
// https://leetcode.com/problems/maximum-candies-you-can-get-from-boxes/

using System.Collections.Generic;

public class Solution {
    public int MaxCandies(int[] status, int[] candies, int[][] keys, int[][] containedBoxes, int[] initialBoxes) {
        var owned = new HashSet<int>(initialBoxes);
        var opened = new HashSet<int>();
        var queue = new Queue<int>();
        foreach (int box in initialBoxes) {
            if (status[box] == 1) queue.Enqueue(box);
        }
        int total = 0;
        while (queue.Count > 0) {
            int box = queue.Dequeue();
            if (opened.Contains(box) || status[box] == 0) continue;
            opened.Add(box);
            total += candies[box];
            foreach (int key in keys[box]) {
                status[key] = 1;
                if (owned.Contains(key) && !opened.Contains(key)) queue.Enqueue(key);
            }
            foreach (int child in containedBoxes[box]) {
                owned.Add(child);
                if (status[child] == 1 && !opened.Contains(child)) queue.Enqueue(child);
            }
        }
        return total;
    }
}
""",
    "1299_replace_elements_with_greatest_element_on_right_side": """// LeetCode 1299 - Replace Elements with Greatest Element on Right Side
// https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

public class Solution {
    public int[] ReplaceElements(int[] arr) {
        int greatest = -1;
        for (int i = arr.Length - 1; i >= 0; i--) {
            int current = arr[i];
            arr[i] = greatest;
            greatest = System.Math.Max(greatest, current);
        }
        return arr;
    }
}
""",
}


def is_sql(folder: str) -> bool:
    for cfg in ("tests/cases.json", "tests/config.json"):
        p = os.path.join(folder, cfg)
        if os.path.exists(p):
            try:
                if json.load(open(p, encoding="utf-8")).get("kind") == "sql":
                    return True
            except Exception:
                pass
    return False


def is_stub(content: str) -> bool:
    return bool(re.search(r"void\s+Solve\s*\(\s*\)\s*\{", content))


def main() -> None:
    written = []
    for name, content in sorted(SOLUTIONS.items()):
        m = re.match(r"^(\d{4})_", name)
        if not m:
            continue
        num = int(m.group(1))
        if num < 1261 or num > 1299:
            continue
        folder = os.path.join(ROOT, name)
        if is_sql(folder):
            continue
        out = os.path.join(folder, "Solution.cs")
        open(out, "w", encoding="utf-8", newline="\n").write(content)
        written.append(name)
    print(f"Wrote {len(written)} files")
    for n in written:
        print(n)


if __name__ == "__main__":
    main()
