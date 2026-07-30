#!/usr/bin/env python3
"""Write Solution.cs for problems 1221-1260 (non-SQL)."""
from pathlib import Path

ROOT = Path(r"c:\Users\Charlie Yu\Documents\leetcode")

SOLUTIONS = {
    "1221_split_a_string_in_balanced_strings": '''// LeetCode 1221 - Split a String in Balanced Strings
// https://leetcode.com/problems/split-a-string-in-balanced-strings/

public class Solution {
    public int BalancedStringSplit(string s) {
        int balance = 0, answer = 0;
        foreach (char ch in s) {
            balance += ch == 'L' ? 1 : -1;
            if (balance == 0) answer++;
        }
        return answer;
    }
}
''',
    "1222_queens_that_can_attack_the_king": '''// LeetCode 1222 - Queens That Can Attack the King
// https://leetcode.com/problems/queens-that-can-attack-the-king/

using System.Collections.Generic;

public class Solution {
    public IList<IList<int>> QueensAttacktheKing(int[][] queens, int[] king) {
        var occupied = new HashSet<(int, int)>();
        foreach (var q in queens) occupied.Add((q[0], q[1]));
        var answer = new List<IList<int>>();
        int[] dirs = { -1, 0, 1 };
        foreach (int dr in dirs) {
            foreach (int dc in dirs) {
                if (dr == 0 && dc == 0) continue;
                int r = king[0] + dr, c = king[1] + dc;
                while (r >= 0 && r < 8 && c >= 0 && c < 8) {
                    if (occupied.Contains((r, c))) {
                        answer.Add(new int[] { r, c });
                        break;
                    }
                    r += dr;
                    c += dc;
                }
            }
        }
        return answer;
    }
}
''',
    "1223_dice_roll_simulation": '''// LeetCode 1223 - Dice Roll Simulation
// https://leetcode.com/problems/dice-roll-simulation/

using System.Collections.Generic;

public class Solution {
    public int DieSimulator(int n, int[] rollMax) {
        const int mod = 1_000_000_007;
        var dp = new List<int[]>();
        for (int j = 0; j < 6; j++) {
            var row = new int[rollMax[j] + 1];
            row[1] = 1;
            dp.Add(row);
        }
        for (int roll = 1; roll < n; roll++) {
            var totals = new int[6];
            for (int j = 0; j < 6; j++) {
                int sum = 0;
                for (int k = 1; k < dp[j].Length; k++) sum = (sum + dp[j][k]) % mod;
                totals[j] = sum;
            }
            var nxt = new List<int[]>();
            for (int j = 0; j < 6; j++) {
                var row = new int[rollMax[j] + 1];
                int allExcept = 0;
                for (int t = 0; t < 6; t++) {
                    if (t != j) allExcept = (allExcept + totals[t]) % mod;
                }
                row[1] = allExcept;
                for (int run = 2; run < row.Length; run++) {
                    row[run] = dp[j][run - 1];
                }
                nxt.Add(row);
            }
            dp = nxt;
        }
        int ans = 0;
        foreach (var row in dp) {
            for (int k = 1; k < row.Length; k++) ans = (ans + row[k]) % mod;
        }
        return ans;
    }
}
''',
    "1224_maximum_equal_frequency": '''// LeetCode 1224 - Maximum Equal Frequency
// https://leetcode.com/problems/maximum-equal-frequency/

using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int MaxEqualFreq(int[] nums) {
        var count = new Dictionary<int, int>();
        var frequencies = new Dictionary<int, int>();
        int answer = 0;
        for (int i = 0; i < nums.Length; i++) {
            int x = nums[i];
            count.TryGetValue(x, out int old);
            if (old > 0) {
                frequencies[old]--;
                if (frequencies[old] == 0) frequencies.Remove(old);
            }
            count[x] = old + 1;
            int nf = old + 1;
            frequencies[nf] = frequencies.GetValueOrDefault(nf) + 1;
            int high = frequencies.Keys.Max();
            if (high == 1
                || frequencies[high] * high + 1 == i + 1
                || (frequencies.GetValueOrDefault(high) == 1
                    && frequencies.GetValueOrDefault(high - 1) * (high - 1) + high == i + 1)) {
                answer = i + 1;
            }
        }
        return answer;
    }
}
''',
    "1226_the_dining_philosophers": '''// LeetCode 1226 - The Dining Philosophers
// https://leetcode.com/problems/the-dining-philosophers/

using System;

public class DiningPhilosophers {
    private readonly object[] forks = new object[5];

    public DiningPhilosophers() {
        for (int i = 0; i < 5; i++) forks[i] = new object();
    }

    public void WantsToEat(int philosopher, Action pickLeftFork, Action pickRightFork,
                           Action eat, Action putLeftFork, Action putRightFork) {
        int left = philosopher;
        int right = (philosopher + 1) % 5;
        int first = philosopher % 2 == 0 ? left : right;
        int second = philosopher % 2 == 0 ? right : left;
        lock (forks[first]) {
            lock (forks[second]) {
                pickLeftFork();
                pickRightFork();
                eat();
                putLeftFork();
                putRightFork();
            }
        }
    }
}
''',
    "1227_airplane_seat_assignment_probability": '''// LeetCode 1227 - Airplane Seat Assignment Probability
// https://leetcode.com/problems/airplane-seat-assignment-probability/

public class Solution {
    public double NthPersonGetsNthSeat(int n) {
        return n == 1 ? 1.0 : 0.5;
    }
}
''',
    "1228_missing_number_in_arithmetic_progression": '''// LeetCode 1228 - Missing Number In Arithmetic Progression
// https://leetcode.com/problems/missing-number-in-arithmetic-progression/

public class Solution {
    public int MissingNumber(int[] arr) {
        int difference = (arr[^1] - arr[0]) / arr.Length;
        for (int i = 1; i < arr.Length; i++) {
            int expected = arr[0] + i * difference;
            if (arr[i] != expected) return expected;
        }
        return arr[0];
    }
}
''',
    "1229_meeting_scheduler": '''// LeetCode 1229 - Meeting Scheduler
// https://leetcode.com/problems/meeting-scheduler/

using System;
using System.Collections.Generic;

public class Solution {
    public IList<int> MinAvailableDuration(int[][] slots1, int[][] slots2, int duration) {
        Array.Sort(slots1, (a, b) => a[0].CompareTo(b[0]));
        Array.Sort(slots2, (a, b) => a[0].CompareTo(b[0]));
        int i = 0, j = 0;
        while (i < slots1.Length && j < slots2.Length) {
            int start = Math.Max(slots1[i][0], slots2[j][0]);
            int end = Math.Min(slots1[i][1], slots2[j][1]);
            if (end - start >= duration) return new int[] { start, start + duration };
            if (slots1[i][1] < slots2[j][1]) i++;
            else j++;
        }
        return new int[0];
    }
}
''',
    "1230_toss_strange_coins": '''// LeetCode 1230 - Toss Strange Coins
// https://leetcode.com/problems/toss-strange-coins/

public class Solution {
    public double ProbabilityOfHeads(int[] prob, int target) {
        var dp = new double[target + 1];
        dp[0] = 1.0;
        foreach (double p in prob) {
            for (int heads = target; heads >= 0; heads--) {
                dp[heads] = dp[heads] * (1 - p) + (heads > 0 ? dp[heads - 1] * p : 0);
            }
        }
        return dp[target];
    }
}
''',
    "1231_divide_chocolate": '''// LeetCode 1231 - Divide Chocolate
// https://leetcode.com/problems/divide-chocolate/

using System.Linq;

public class Solution {
    public int MaximizeSweetness(int[] sweetness, int k) {
        int lo = 1, hi = sweetness.Sum() / (k + 1);
        while (lo <= hi) {
            int mid = (lo + hi) / 2;
            int pieces = 0, current = 0;
            foreach (int value in sweetness) {
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
''',
    "1232_check_if_it_is_a_straight_line": '''// LeetCode 1232 - Check If It Is a Straight Line
// https://leetcode.com/problems/check-if-it-is-a-straight-line/

public class Solution {
    public bool CheckStraightLine(int[][] coordinates) {
        int x0 = coordinates[0][0], y0 = coordinates[0][1];
        int dx = coordinates[1][0] - x0, dy = coordinates[1][1] - y0;
        for (int i = 2; i < coordinates.Length; i++) {
            int x = coordinates[i][0], y = coordinates[i][1];
            if ((x - x0) * dy != (y - y0) * dx) return false;
        }
        return true;
    }
}
''',
    "1233_remove_sub_folders_from_the_filesystem": '''// LeetCode 1233 - Remove Sub-Folders from the Filesystem
// https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/

using System.Collections.Generic;
using System.Linq;

public class Solution {
    public IList<string> RemoveSubfolders(string[] folder) {
        var answer = new List<string>();
        foreach (string path in folder.OrderBy(x => x)) {
            if (answer.Count == 0 || !path.StartsWith(answer[^1] + "/")) {
                answer.Add(path);
            }
        }
        return answer;
    }
}
''',
    "1234_replace_the_substring_for_balanced_string": '''// LeetCode 1234 - Replace the Substring for Balanced String
// https://leetcode.com/problems/replace-the-substring-for-balanced-string/

using System;
using System.Collections.Generic;

public class Solution {
    public int BalancedString(string s) {
        var count = new Dictionary<char, int>();
        foreach (char ch in s) count[ch] = count.GetValueOrDefault(ch) + 1;
        int limit = s.Length / 4;
        int n = s.Length, left = 0, answer = n;
        for (int right = 0; right < n; right++) {
            count[s[right]]--;
            while (left < n && Excess(count, limit) == 0) {
                answer = Math.Min(answer, right - left + 1);
                count[s[left]]++;
                left++;
            }
        }
        return answer;
    }

    private static int Excess(Dictionary<char, int> count, int limit) {
        int excess = 0;
        foreach (char c in "QWER") {
            if (count.GetValueOrDefault(c) > limit) excess++;
        }
        return excess;
    }
}
''',
    "1235_maximum_profit_in_job_scheduling": '''// LeetCode 1235 - Maximum Profit in Job Scheduling
// https://leetcode.com/problems/maximum-profit-in-job-scheduling/

using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int JobScheduling(int[] startTime, int[] endTime, int[] profit) {
        var jobs = new List<(int end, int start, int gain)>();
        for (int i = 0; i < startTime.Length; i++) {
            jobs.Add((endTime[i], startTime[i], profit[i]));
        }
        jobs.Sort((a, b) => a.end.CompareTo(b.end));
        var ends = new List<int> { 0 };
        var dp = new List<int> { 0 };
        foreach (var (end, start, gain) in jobs) {
            int idx = ends.BinarySearch(start);
            if (idx < 0) idx = ~idx - 1;
            ends.Add(end);
            dp.Add(Math.Max(dp[^1], dp[idx] + gain));
        }
        return dp[^1];
    }
}
''',
    "1236_web_crawler": '''// LeetCode 1236 - Web Crawler
// https://leetcode.com/problems/web-crawler/

using System;
using System.Collections.Generic;
using System.Linq;

public class HtmlParser {
    public virtual IList<string> GetUrls(string url) => new List<string>();
}

public class Solution {
    public IList<string> Crawl(string startUrl, HtmlParser htmlParser) {
        string host = new Uri(startUrl).Host;
        var seen = new HashSet<string> { startUrl };
        var stack = new Stack<string>();
        stack.Push(startUrl);
        while (stack.Count > 0) {
            string current = stack.Pop();
            foreach (string url in htmlParser.GetUrls(current)) {
                if (new Uri(url).Host == host && seen.Add(url)) {
                    stack.Push(url);
                }
            }
        }
        return seen.OrderBy(x => x).ToList();
    }
}
''',
    "1237_find_positive_integer_solution_for_a_given_equation": '''// LeetCode 1237 - Find Positive Integer Solution for a Given Equation
// https://leetcode.com/problems/find-positive-integer-solution-for-a-given-equation/

using System.Collections.Generic;

public class CustomFunction {
    public virtual int F(int x, int y) => 0;
}

public class Solution {
    public IList<IList<int>> FindSolution(CustomFunction customfunction, int z) {
        var answer = new List<IList<int>>();
        int x = 1, y = 1000;
        while (x <= 1000 && y >= 1) {
            int value = customfunction.F(x, y);
            if (value == z) {
                answer.Add(new int[] { x, y });
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
''',
    "1238_circular_permutation_in_binary_representation": '''// LeetCode 1238 - Circular Permutation in Binary Representation
// https://leetcode.com/problems/circular-permutation-in-binary-representation/

using System.Collections.Generic;

public class Solution {
    public IList<int> CircularPermutation(int n, int start) {
        var answer = new List<int>();
        for (int i = 0; i < (1 << n); i++) {
            answer.Add(start ^ i ^ (i >> 1));
        }
        return answer;
    }
}
''',
    "1239_maximum_length_of_a_concatenated_string_with_unique_characters": '''// LeetCode 1239 - Maximum Length of a Concatenated String with Unique Characters
// https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/

using System;
using System.Collections.Generic;

public class Solution {
    public int MaxLength(string[] arr) {
        var masks = new List<(int used, int length)> { (0, 0) };
        foreach (string word in arr) {
            int mask = 0;
            foreach (char ch in word) mask |= 1 << (ch - 'a');
            if (BitCount(mask) != word.Length) continue;
            var next = new List<(int, int)>(masks);
            foreach (var (used, length) in masks) {
                if ((used & mask) == 0) {
                    next.Add((used | mask, length + word.Length));
                }
            }
            masks = next;
        }
        int best = 0;
        foreach (var (_, length) in masks) best = Math.Max(best, length);
        return best;
    }

    private static int BitCount(int x) {
        int c = 0;
        while (x != 0) {
            c += x & 1;
            x >>= 1;
        }
        return c;
    }
}
''',
    "1240_tiling_a_rectangle_with_the_fewest_squares": '''// LeetCode 1240 - Tiling a Rectangle with the Fewest Squares
// https://leetcode.com/problems/tiling-a-rectangle-with-the-fewest-squares/

using System;
using System.Linq;

public class Solution {
    private int[] heights;
    private int best;

    public int TilingRectangle(int n, int m) {
        if (n > m) (n, m) = (m, n);
        heights = new int[m];
        best = n * m;
        Search(0);
        return best;
    }

    private void Search(int used) {
        if (used >= best) return;
        int low = heights.Min();
        if (low == heights.Length > 0 ? heights[0] + (heights.Length > 0 ? 0 : 0) : 0) { }
        low = heights.Min();
        int n = heights.Length > 0 ? Array.IndexOf(heights, low) >= 0 ? heights.Max(h => h) : 0 : 0;
        n = 0;
        foreach (int h in heights) if (h > n) n = h;
        // low is min height; n is max target row count from heights array length
        int maxRow = heights.Length == 0 ? 0 : heights.Max();
        low = heights.Min();
        if (low == maxRow) {
            best = used;
            return;
        }
        int left = Array.IndexOf(heights, low);
        int right = left;
        while (right < heights.Length && heights[right] == low) right++;
        int maxSize = Math.Min(maxRow - low, right - left);
        for (int size = maxSize; size >= 1; size--) {
            for (int i = left; i < left + size; i++) heights[i] = low + size;
            Search(used + 1);
            for (int i = left; i < left + size; i++) heights[i] = low;
        }
    }
}
''',
}

# Fix 1240 - I made a mess in the template above. Write it cleanly separately.
SOLUTIONS["1240_tiling_a_rectangle_with_the_fewest_squares"] = '''// LeetCode 1240 - Tiling a Rectangle with the Fewest Squares
// https://leetcode.com/problems/tiling-a-rectangle-with-the-fewest-squares/

using System;
using System.Linq;

public class Solution {
    private int[] heights;
    private int rowLimit;
    private int best;

    public int TilingRectangle(int n, int m) {
        if (n > m) (n, m) = (m, n);
        rowLimit = n;
        heights = new int[m];
        best = n * m;
        Search(0);
        return best;
    }

    private void Search(int used) {
        if (used >= best) return;
        int low = heights.Min();
        if (low == rowLimit) {
            best = used;
            return;
        }
        int left = Array.IndexOf(heights, low);
        int right = left;
        while (right < heights.Length && heights[right] == low) right++;
        int maxSize = Math.Min(rowLimit - low, right - left);
        for (int size = maxSize; size >= 1; size--) {
            for (int i = left; i < left + size; i++) heights[i] = low + size;
            Search(used + 1);
            for (int i = left; i < left + size; i++) heights[i] = low;
        }
    }
}
'''

SOLUTIONS.update({
    "1242_web_crawler_multithreaded": '''// LeetCode 1242 - Web Crawler Multithreaded
// https://leetcode.com/problems/web-crawler-multithreaded/

using System;
using System.Collections.Concurrent;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

public class HtmlParser {
    public virtual IList<string> GetUrls(string url) => new List<string>();
}

public class Solution {
    public IList<string> Crawl(string startUrl, HtmlParser htmlParser) {
        string host = new Uri(startUrl).Host;
        var seen = new ConcurrentDictionary<string, byte>();
        seen.TryAdd(startUrl, 0);
        var frontier = new List<string> { startUrl };
        while (frontier.Count > 0) {
            var next = new ConcurrentBag<string>();
            Parallel.ForEach(frontier, url => {
                foreach (string link in htmlParser.GetUrls(url)) {
                    if (new Uri(link).Host == host && seen.TryAdd(link, 0)) {
                        next.Add(link);
                    }
                }
            });
            frontier = next.ToList();
        }
        return seen.Keys.OrderBy(x => x).ToList();
    }
}
''',
    "1243_array_transformation": '''// LeetCode 1243 - Array Transformation
// https://leetcode.com/problems/array-transformation/

using System.Linq;

public class Solution {
    public IList<int> TransformArray(int[] arr) {
        while (true) {
            var nxt = arr.ToArray();
            for (int i = 1; i < arr.Length - 1; i++) {
                if (arr[i] < arr[i - 1] && arr[i] < arr[i + 1]) nxt[i]++;
                else if (arr[i] > arr[i - 1] && arr[i] > arr[i + 1]) nxt[i]--;
            }
            if (nxt.SequenceEqual(arr)) return arr.ToList();
            arr = nxt;
        }
    }
}
''',
    "1244_design_a_leaderboard": '''// LeetCode 1244 - Design A Leaderboard
// https://leetcode.com/problems/design-a-leaderboard/

using System.Collections.Generic;
using System.Linq;

public class Leaderboard {
    private readonly Dictionary<int, int> scores = new Dictionary<int, int>();

    public Leaderboard() {
    }

    public void AddScore(int playerId, int score) {
        scores[playerId] = scores.GetValueOrDefault(playerId) + score;
    }

    public int Top(int k) {
        return scores.Values.OrderByDescending(x => x).Take(k).Sum();
    }

    public void Reset(int playerId) {
        scores.Remove(playerId);
    }
}
''',
    "1245_tree_diameter": '''// LeetCode 1245 - Tree Diameter
// https://leetcode.com/problems/tree-diameter/

using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int TreeDiameter(int[][] edges) {
        if (edges.Length == 0) return 0;
        var graph = new Dictionary<int, List<int>>();
        foreach (var e in edges) {
            if (!graph.ContainsKey(e[0])) graph[e[0]] = new List<int>();
            if (!graph.ContainsKey(e[1])) graph[e[1]] = new List<int>();
            graph[e[0]].Add(e[1]);
            graph[e[1]].Add(e[0]);
        }
        (int node, int dist) Farthest(int start) {
            var q = new Queue<(int node, int dist)>();
            var seen = new HashSet<int> { start };
            q.Enqueue((start, 0));
            (int node, int dist) last = (start, 0);
            while (q.Count > 0) {
                last = q.Dequeue();
                foreach (int v in graph[last.node]) {
                    if (seen.Add(v)) q.Enqueue((v, last.dist + 1));
                }
            }
            return last;
        }
        int endpoint = Farthest(edges[0][0]).node;
        return Farthest(endpoint).dist;
    }
}
''',
    "1246_palindrome_removal": '''// LeetCode 1246 - Palindrome Removal
// https://leetcode.com/problems/palindrome-removal/

using System;

public class Solution {
    public int MinimumMoves(int[] arr) {
        int n = arr.Length;
        var dp = new int[n, n];
        for (int i = 0; i < n; i++) dp[i, i] = 1;
        for (int length = 2; length <= n; length++) {
            for (int i = 0; i <= n - length; i++) {
                int j = i + length - 1;
                dp[i, j] = 1 + dp[i + 1, j];
                if (arr[i] == arr[i + 1]) {
                    dp[i, j] = Math.Min(dp[i, j], 1 + (i + 2 <= j ? dp[i + 2, j] : 0));
                }
                for (int k = i + 2; k <= j; k++) {
                    if (arr[i] == arr[k]) {
                        dp[i, j] = Math.Min(dp[i, j],
                            dp[i + 1, k - 1] + (k < j ? dp[k + 1, j] : 0));
                    }
                }
            }
        }
        return dp[0, n - 1];
    }
}
''',
    "1247_minimum_swaps_to_make_strings_equal": '''// LeetCode 1247 - Minimum Swaps to Make Strings Equal
// https://leetcode.com/problems/minimum-swaps-to-make-strings-equal/

public class Solution {
    public int MinimumSwap(string s1, string s2) {
        int xy = 0, yx = 0;
        for (int i = 0; i < s1.Length; i++) {
            if (s1[i] == 'x' && s2[i] == 'y') xy++;
            if (s1[i] == 'y' && s2[i] == 'x') yx++;
        }
        if ((xy + yx) % 2 != 0) return -1;
        return xy / 2 + yx / 2 + 2 * (xy % 2);
    }
}
''',
    "1248_count_number_of_nice_subarrays": '''// LeetCode 1248 - Count Number of Nice Subarrays
// https://leetcode.com/problems/count-number-of-nice-subarrays/

using System.Collections.Generic;

public class Solution {
    public int NumberOfSubarrays(int[] nums, int k) {
        var frequency = new Dictionary<int, int> { [0] = 1 };
        int odd = 0, answer = 0;
        foreach (int x in nums) {
            odd += x & 1;
            if (frequency.TryGetValue(odd - k, out int cnt)) answer += cnt;
            frequency[odd] = frequency.GetValueOrDefault(odd) + 1;
        }
        return answer;
    }
}
''',
    "1249_minimum_remove_to_make_valid_parentheses": '''// LeetCode 1249 - Minimum Remove to Make Valid Parentheses
// https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

using System.Collections.Generic;
using System.Text;

public class Solution {
    public string MinRemoveToMakeValid(string s) {
        var chars = s.ToCharArray();
        var opens = new Stack<int>();
        for (int i = 0; i < chars.Length; i++) {
            if (chars[i] == '(') opens.Push(i);
            else if (chars[i] == ')') {
                if (opens.Count > 0) opens.Pop();
                else chars[i] = '\0';
            }
        }
        while (opens.Count > 0) chars[opens.Pop()] = '\0';
        var sb = new StringBuilder();
        foreach (char ch in chars) if (ch != '\0') sb.Append(ch);
        return sb.ToString();
    }
}
''',
    "1250_check_if_it_is_a_good_array": '''// LeetCode 1250 - Check If It Is a Good Array
// https://leetcode.com/problems/check-if-it-is-a-good-array/

public class Solution {
    public bool IsGoodArray(int[] nums) {
        int g = nums[0];
        for (int i = 1; i < nums.Length; i++) g = Gcd(g, nums[i]);
        return g == 1;
    }

    private static int Gcd(int a, int b) {
        while (b != 0) (a, b) = (b, a % b);
        return a;
    }
}
''',
    "1252_cells_with_odd_values_in_a_matrix": '''// LeetCode 1252 - Cells with Odd Values in a Matrix
// https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/

public class Solution {
    public int OddCells(int m, int n, int[][] indices) {
        var rows = new int[m];
        var cols = new int[n];
        foreach (var idx in indices) {
            rows[idx[0]] ^= 1;
            cols[idx[1]] ^= 1;
        }
        int answer = 0;
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if ((rows[r] ^ cols[c]) == 1) answer++;
            }
        }
        return answer;
    }
}
''',
    "1253_reconstruct_a_2_row_binary_matrix": '''// LeetCode 1253 - Reconstruct a 2-Row Binary Matrix
// https://leetcode.com/problems/reconstruct-a-2-row-binary-matrix/

using System.Collections.Generic;

public class Solution {
    public IList<IList<int>> ReconstructMatrix(int upper, int lower, int[] colsum) {
        var top = new int[colsum.Length];
        var bottom = new int[colsum.Length];
        for (int i = 0; i < colsum.Length; i++) {
            if (colsum[i] == 2) {
                top[i] = bottom[i] = 1;
                upper--;
                lower--;
            }
        }
        if (upper < 0 || lower < 0) return new List<IList<int>>();
        for (int i = 0; i < colsum.Length; i++) {
            if (colsum[i] == 1) {
                if (upper > 0) {
                    top[i] = 1;
                    upper--;
                } else if (lower > 0) {
                    bottom[i] = 1;
                    lower--;
                } else {
                    return new List<IList<int>>();
                }
            }
        }
        if (upper != 0 || lower != 0) return new List<IList<int>>();
        return new IList<int>[] { top, bottom };
    }
}
''',
    "1254_number_of_closed_islands": '''// LeetCode 1254 - Number of Closed Islands
// https://leetcode.com/problems/number-of-closed-islands/

using System.Collections.Generic;

public class Solution {
    public int ClosedIsland(int[][] grid) {
        int m = grid.Length, n = grid[0].Length, answer = 0;
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (grid[r][c] == 0 && Flood(grid, r, c)) answer++;
            }
        }
        return answer;
    }

    private static bool Flood(int[][] grid, int sr, int sc) {
        int m = grid.Length, n = grid[0].Length;
        var stack = new Stack<(int, int)>();
        stack.Push((sr, sc));
        grid[sr][sc] = 1;
        bool closed = true;
        while (stack.Count > 0) {
            var (r, c) = stack.Pop();
            if (r == 0 || r == m - 1 || c == 0 || c == n - 1) closed = false;
            int[] dr = { 1, -1, 0, 0 }, dc = { 0, 0, 1, -1 };
            for (int i = 0; i < 4; i++) {
                int nr = r + dr[i], nc = c + dc[i];
                if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] == 0) {
                    grid[nr][nc] = 1;
                    stack.Push((nr, nc));
                }
            }
        }
        return closed;
    }
}
''',
    "1255_maximum_score_words_formed_by_letters": '''// LeetCode 1255 - Maximum Score Words Formed by Letters
// https://leetcode.com/problems/maximum-score-words-formed-by-letters/

using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int MaxScoreWords(string[] words, char[] letters, int[] score) {
        var available = new Dictionary<char, int>();
        foreach (char ch in letters) available[ch] = available.GetValueOrDefault(ch) + 1;
        var counts = words.Select(w => {
            var c = new Dictionary<char, int>();
            foreach (char ch in w) c[ch] = c.GetValueOrDefault(ch) + 1;
            return c;
        }).ToArray();
        var values = words.Select(w => w.Sum(ch => score[ch - 'a'])).ToArray();

        int Dfs(int i) {
            if (i == words.Length) return 0;
            int best = Dfs(i + 1);
            if (CanUse(counts[i], available)) {
                Apply(counts[i], available, -1);
                best = Math.Max(best, values[i] + Dfs(i + 1));
                Apply(counts[i], available, 1);
            }
            return best;
        }
        return Dfs(0);
    }

    private static bool CanUse(Dictionary<char, int> need, Dictionary<char, int> available) {
        foreach (var kv in need) {
            if (available.GetValueOrDefault(kv.Key) < kv.Value) return false;
        }
        return true;
    }

    private static void Apply(Dictionary<char, int> need, Dictionary<char, int> available, int delta) {
        foreach (var kv in need) available[kv.Key] = available.GetValueOrDefault(kv.Key) + delta * kv.Value;
    }
}
''',
    "1256_encode_number": '''// LeetCode 1256 - Encode Number
// https://leetcode.com/problems/encode-number/

public class Solution {
    public string Encode(int num) {
        return Convert.ToString(num + 1, 2)[1..];
    }
}
''',
    "1257_smallest_common_region": '''// LeetCode 1257 - Smallest Common Region
// https://leetcode.com/problems/smallest-common-region/

using System.Collections.Generic;

public class Solution {
    public string FindSmallestRegion(string[][] regions, string region1, string region2) {
        var parent = new Dictionary<string, string>();
        foreach (var group in regions) {
            for (int i = 1; i < group.Length; i++) parent[group[i]] = group[0];
        }
        var ancestors = new HashSet<string>();
        while (!string.IsNullOrEmpty(region1)) {
            ancestors.Add(region1);
            parent.TryGetValue(region1, out region1);
        }
        while (!ancestors.Contains(region2)) {
            parent.TryGetValue(region2, out region2);
        }
        return region2;
    }
}
''',
    "1258_synonymous_sentences": '''// LeetCode 1258 - Synonymous Sentences
// https://leetcode.com/problems/synonymous-sentences/

using System.Collections.Generic;
using System.Linq;

public class Solution {
    public IList<string> GenerateSentences(IList<IList<string>> synonyms, string text) {
        var parent = new Dictionary<string, string>();
        string Find(string x) {
            if (!parent.ContainsKey(x)) parent[x] = x;
            if (parent[x] != x) parent[x] = Find(parent[x]);
            return parent[x];
        }
        foreach (var pair in synonyms) {
            string ra = Find(pair[0]), rb = Find(pair[1]);
            parent[ra] = rb;
        }
        var groups = new Dictionary<string, List<string>>();
        foreach (string word in parent.Keys.ToList()) {
            string root = Find(word);
            if (!groups.ContainsKey(root)) groups[root] = new List<string>();
            groups[root].Add(word);
        }
        foreach (var key in groups.Keys.ToList()) groups[key].Sort();

        var words = text.Split(' ');
        var choices = new List<List<string>>();
        foreach (string w in words) {
            if (parent.ContainsKey(w)) choices.Add(groups[Find(w)]);
            else choices.Add(new List<string> { w });
        }
        var answer = new List<string>();
        Dfs(choices, 0, new List<string>(), answer);
        return answer;
    }

    private static void Dfs(List<List<string>> choices, int idx, List<string> cur, List<string> answer) {
        if (idx == choices.Count) {
            answer.Add(string.Join(" ", cur));
            return;
        }
        foreach (string w in choices[idx]) {
            cur.Add(w);
            Dfs(choices, idx + 1, cur, answer);
            cur.RemoveAt(cur.Count - 1);
        }
    }
}
''',
    "1259_handshakes_that_dont_cross": '''// LeetCode 1259 - Handshakes That Don't Cross
// https://leetcode.com/problems/handshakes-that-dont-cross/

public class Solution {
    public int NumberOfWays(int numPeople) {
        const int mod = 1_000_000_007;
        var dp = new int[numPeople + 1];
        dp[0] = 1;
        for (int people = 2; people <= numPeople; people += 2) {
            long sum = 0;
            for (int left = 0; left < people; left += 2) {
                sum = (sum + (long)dp[left] * dp[people - 2 - left]) % mod;
            }
            dp[people] = (int)sum;
        }
        return dp[numPeople];
    }
}
''',
    "1260_shift_2d_grid": '''// LeetCode 1260 - Shift 2D Grid
// https://leetcode.com/problems/shift-2d-grid/

using System.Collections.Generic;
using System.Linq;

public class Solution {
    public IList<IList<int>> ShiftGrid(int[][] grid, int k) {
        int m = grid.Length, n = grid[0].Length;
        var flat = grid.SelectMany(row => row).ToList();
        k %= flat.Count;
        if (k > 0) {
            var tail = flat.GetRange(flat.Count - k, k);
            flat.RemoveRange(flat.Count - k, k);
            flat.InsertRange(0, tail);
        }
        var answer = new List<IList<int>>();
        for (int i = 0; i < m; i++) {
            answer.Add(flat.GetRange(i * n, n));
        }
        return answer;
    }
}
''',
})

SQL_SKIP = {
    "1225_report_contiguous_dates",
    "1241_number_of_comments_per_post",
    "1251_average_selling_price",
}

def main():
    written = []
    for name, content in SOLUTIONS.items():
        folder = ROOT / name
        if name in SQL_SKIP:
            continue
        path = folder / "Solution.cs"
        path.write_text(content, encoding="utf-8", newline="\n")
        written.append(name)
    print(f"Written: {len(written)}")
    for n in sorted(written):
        print(n)

if __name__ == "__main__":
    main()
