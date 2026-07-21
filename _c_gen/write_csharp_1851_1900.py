#!/usr/bin/env python3
"""Write C# solutions for LeetCode 1851-1900 (non-SQL)."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

SOLUTIONS: dict[int, str] = {}

SOLUTIONS[1851] = r'''// LeetCode 1851 - Minimum Interval to Include Each Query
// https://leetcode.com/problems/minimum-interval-to-include-each-query/

public class Solution {
    public int[] MinInterval(int[][] intervals, int[] queries) {
        Array.Sort(intervals, (a, b) => a[0].CompareTo(b[0]));
        var indexed = new (int idx, int query)[queries.Length];
        for (int i = 0; i < queries.Length; i++) {
            indexed[i] = (i, queries[i]);
        }
        Array.Sort(indexed, (a, b) => a.query.CompareTo(b.query));

        var heap = new PriorityQueue<(int size, int right), int>();
        var answer = new int[queries.Length];
        Array.Fill(answer, -1);
        int intervalIdx = 0;

        foreach (var (queryIdx, query) in indexed) {
            while (intervalIdx < intervals.Length && intervals[intervalIdx][0] <= query) {
                int left = intervals[intervalIdx][0];
                int right = intervals[intervalIdx][1];
                int size = right - left + 1;
                heap.Enqueue((size, right), size);
                intervalIdx++;
            }
            while (heap.Count > 0 && heap.Peek().right < query) {
                heap.Dequeue();
            }
            if (heap.Count > 0) {
                answer[queryIdx] = heap.Peek().size;
            }
        }
        return answer;
    }
}
'''

SOLUTIONS[1852] = r'''// LeetCode 1852 - Distinct Numbers in Each Subarray
// https://leetcode.com/problems/distinct-numbers-in-each-subarray/

public class Solution {
    public int[] DistinctNumbers(int[] nums, int k) {
        var counts = new Dictionary<int, int>();
        for (int i = 0; i < k; i++) {
            counts[nums[i]] = counts.GetValueOrDefault(nums[i]) + 1;
        }
        var result = new List<int> { counts.Count };
        int left = 0;
        for (int right = k; right < nums.Length; right++) {
            counts[nums[right]] = counts.GetValueOrDefault(nums[right]) + 1;
            int outgoing = nums[left];
            counts[outgoing]--;
            if (counts[outgoing] == 0) {
                counts.Remove(outgoing);
            }
            left++;
            result.Add(counts.Count);
        }
        return result.ToArray();
    }
}
'''

SOLUTIONS[1854] = r'''// LeetCode 1854 - Maximum Population Year
// https://leetcode.com/problems/maximum-population-year/

public class Solution {
    public int MaximumPopulation(int[][] logs) {
        var diff = new int[101];
        foreach (var log in logs) {
            diff[log[0] - 1950]++;
            diff[log[1] - 1950]--;
        }
        int bestYear = 1950;
        int bestPopulation = 0;
        int population = 0;
        for (int offset = 0; offset < 101; offset++) {
            population += diff[offset];
            if (population > bestPopulation) {
                bestPopulation = population;
                bestYear = 1950 + offset;
            }
        }
        return bestYear;
    }
}
'''

SOLUTIONS[1855] = r'''// LeetCode 1855 - Maximum Distance Between a Pair of Values
// https://leetcode.com/problems/maximum-distance-between-a-pair-of-values/

public class Solution {
    public int MaxDistance(int[] nums1, int[] nums2) {
        int answer = 0;
        int j = 0;
        for (int i = 0; i < nums1.Length; i++) {
            while (j < nums2.Length && nums1[i] <= nums2[j]) {
                j++;
            }
            answer = Math.Max(answer, j - i - 1);
        }
        return answer;
    }
}
'''

SOLUTIONS[1856] = r'''// LeetCode 1856 - Maximum Subarray Min-Product
// https://leetcode.com/problems/maximum-subarray-min-product/

public class Solution {
    public int MaxSumMinProduct(int[] nums) {
        const int mod = 1_000_000_007;
        int n = nums.Length;
        var prefix = new long[n + 1];
        for (int i = 0; i < n; i++) {
            prefix[i + 1] = prefix[i] + nums[i];
        }

        var leftBound = new int[n];
        var stack = new List<int>();
        for (int i = 0; i < n; i++) {
            while (stack.Count > 0 && nums[stack[^1]] >= nums[i]) {
                stack.RemoveAt(stack.Count - 1);
            }
            leftBound[i] = stack.Count == 0 ? -1 : stack[^1];
            stack.Add(i);
        }

        var rightBound = new int[n];
        stack.Clear();
        for (int i = n - 1; i >= 0; i--) {
            while (stack.Count > 0 && nums[stack[^1]] >= nums[i]) {
                stack.RemoveAt(stack.Count - 1);
            }
            rightBound[i] = stack.Count == 0 ? n : stack[^1];
            stack.Add(i);
        }

        long best = 0;
        for (int i = 0; i < n; i++) {
            long total = prefix[rightBound[i]] - prefix[leftBound[i] + 1];
            best = Math.Max(best, total * nums[i]);
        }
        return (int)(best % mod);
    }
}
'''

SOLUTIONS[1857] = r'''// LeetCode 1857 - Largest Color Value in a Directed Graph
// https://leetcode.com/problems/largest-color-value-in-a-directed-graph/

public class Solution {
    public int LargestPathValue(string colors, int[][] edges) {
        int n = colors.Length;
        var indegree = new int[n];
        var adjacency = new List<int>[n];
        for (int i = 0; i < n; i++) {
            adjacency[i] = new List<int>();
        }
        foreach (var edge in edges) {
            adjacency[edge[0]].Add(edge[1]);
            indegree[edge[1]]++;
        }

        var queue = new Queue<int>();
        for (int node = 0; node < n; node++) {
            if (indegree[node] == 0) {
                queue.Enqueue(node);
            }
        }

        var dp = new int[n][];
        for (int node = 0; node < n; node++) {
            dp[node] = new int[26];
            dp[node][colors[node] - 'a'] = 1;
        }

        int processed = 0;
        int answer = 0;
        while (queue.Count > 0) {
            int node = queue.Dequeue();
            processed++;
            foreach (int value in dp[node]) {
                answer = Math.Max(answer, value);
            }
            foreach (int neighbor in adjacency[node]) {
                int neighborColor = colors[neighbor] - 'a';
                for (int colorIndex = 0; colorIndex < 26; colorIndex++) {
                    int candidate = dp[node][colorIndex];
                    if (colorIndex == neighborColor) {
                        candidate++;
                    }
                    if (candidate > dp[neighbor][colorIndex]) {
                        dp[neighbor][colorIndex] = candidate;
                    }
                }
                indegree[neighbor]--;
                if (indegree[neighbor] == 0) {
                    queue.Enqueue(neighbor);
                }
            }
        }
        return processed == n ? answer : -1;
    }
}
'''

SOLUTIONS[1858] = r'''// LeetCode 1858 - Longest Word With All Prefixes
// https://leetcode.com/problems/longest-word-with-all-prefixes/

public class Solution {
    public string LongestWord(string[] words) {
        var wordSet = new HashSet<string>(words);
        string best = "";
        foreach (string word in words) {
            bool valid = true;
            for (int len = word.Length; len > 0; len--) {
                if (!wordSet.Contains(word.Substring(0, len))) {
                    valid = false;
                    break;
                }
            }
            if (valid && (word.Length > best.Length || (word.Length == best.Length && string.CompareOrdinal(word, best) < 0))) {
                best = word;
            }
        }
        return best;
    }
}
'''

SOLUTIONS[1859] = r'''// LeetCode 1859 - Sorting the Sentence
// https://leetcode.com/problems/sorting-the-sentence/

public class Solution {
    public string SortSentence(string s) {
        string[] tokens = s.Split(' ');
        var ordered = new string[tokens.Length];
        foreach (string token in tokens) {
            int position = token[^1] - '1';
            ordered[position] = token.Substring(0, token.Length - 1);
        }
        return string.Join(" ", ordered);
    }
}
'''

SOLUTIONS[1860] = r'''// LeetCode 1860 - Incremental Memory Leak
// https://leetcode.com/problems/incremental-memory-leak/

public class Solution {
    public int[] MemLeak(int memory1, int memory2) {
        int m1 = memory1;
        int m2 = memory2;
        int second = 1;
        while (m1 >= second || m2 >= second) {
            if (m1 >= m2) {
                m1 -= second;
            } else {
                m2 -= second;
            }
            second++;
        }
        return new[] { second, m1, m2 };
    }
}
'''

SOLUTIONS[1861] = r'''// LeetCode 1861 - Rotating the Box
// https://leetcode.com/problems/rotating-the-box/

public class Solution {
    public char[][] RotateTheBox(char[][] boxGrid) {
        int m = boxGrid.Length;
        int n = boxGrid[0].Length;
        var rotated = new char[n][];
        for (int i = 0; i < n; i++) {
            rotated[i] = new char[m];
            for (int j = 0; j < m; j++) {
                rotated[i][j] = '.';
            }
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                rotated[i][j] = boxGrid[m - 1 - j][i];
            }
        }
        for (int col = 0; col < m; col++) {
            int row = n - 1;
            for (int i = n - 1; i >= 0; i--) {
                if (rotated[i][col] == '*') {
                    row = i - 1;
                } else if (rotated[i][col] == '#') {
                    rotated[i][col] = '.';
                    rotated[row][col] = '#';
                    row--;
                }
            }
        }
        return rotated;
    }
}
'''

SOLUTIONS[1862] = r'''// LeetCode 1862 - Sum of Floored Pairs
// https://leetcode.com/problems/sum-of-floored-pairs/

public class Solution {
    public int SumOfFlooredPairs(int[] nums) {
        const int mod = 1_000_000_007;
        int maxVal = 0;
        foreach (int num in nums) {
            maxVal = Math.Max(maxVal, num);
        }
        var count = new int[maxVal + 1];
        foreach (int num in nums) {
            count[num]++;
        }

        var prefix = new int[maxVal + 1];
        prefix[0] = count[0];
        for (int value = 1; value <= maxVal; value++) {
            prefix[value] = prefix[value - 1] + count[value];
        }

        long answer = 0;
        for (int divisor = 1; divisor <= maxVal; divisor++) {
            if (count[divisor] == 0) {
                continue;
            }
            int quotient = 1;
            while ((long)quotient * divisor <= maxVal) {
                int low = quotient * divisor;
                int high = Math.Min((quotient + 1) * divisor - 1, maxVal);
                int matches = prefix[high] - (low > 0 ? prefix[low - 1] : 0);
                answer = (answer + (long)count[divisor] * matches * quotient) % mod;
                quotient++;
            }
        }
        return (int)answer;
    }
}
'''

SOLUTIONS[1863] = r'''// LeetCode 1863 - Sum of All Subset XOR Totals
// https://leetcode.com/problems/sum-of-all-subset-xor-totals/

public class Solution {
    public int SubsetXORSum(int[] nums) {
        int bits = 0;
        foreach (int num in nums) {
            bits |= num;
        }
        int total = 0;
        for (int bit = 1; bit <= bits; bit <<= 1) {
            if ((bits & bit) != 0) {
                total += bit;
            }
        }
        return total << (nums.Length - 1);
    }
}
'''

SOLUTIONS[1864] = r'''// LeetCode 1864 - Minimum Number of Swaps to Make the Binary String Alternating
// https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-binary-string-alternating/

public class Solution {
    public int MinSwaps(string s) {
        int zeros = 0;
        foreach (char ch in s) {
            if (ch == '0') {
                zeros++;
            }
        }
        int ones = s.Length - zeros;
        if (Math.Abs(zeros - ones) > 1) {
            return -1;
        }

        int Mismatches(char start) {
            int count = 0;
            for (int i = 0; i < s.Length; i++) {
                char expected = i % 2 == 0 ? start : (start == '0' ? '1' : '0');
                if (s[i] != expected) {
                    count++;
                }
            }
            return count / 2;
        }

        if (zeros == ones) {
            return Math.Min(Mismatches('0'), Mismatches('1'));
        }
        return zeros > ones ? Mismatches('0') : Mismatches('1');
    }
}
'''

SOLUTIONS[1865] = r'''// LeetCode 1865 - Finding Pairs With a Certain Sum
// https://leetcode.com/problems/finding-pairs-with-a-certain-sum/

public class FindSumPairs {
    private readonly int[] nums1;
    private readonly int[] nums2;
    private readonly Dictionary<int, int> counts = new();

    public FindSumPairs(int[] nums1, int[] nums2) {
        this.nums1 = nums1;
        this.nums2 = (int[])nums2.Clone();
        foreach (int num in this.nums2) {
            counts[num] = counts.GetValueOrDefault(num) + 1;
        }
    }

    public void Add(int index, int val) {
        counts[nums2[index]]--;
        nums2[index] += val;
        counts[nums2[index]] = counts.GetValueOrDefault(nums2[index]) + 1;
    }

    public int Count(int tot) {
        int answer = 0;
        foreach (int num in nums1) {
            answer += counts.GetValueOrDefault(tot - num);
        }
        return answer;
    }
}
'''

SOLUTIONS[1866] = r'''// LeetCode 1866 - Number of Ways to Rearrange Sticks With K Sticks Visible
// https://leetcode.com/problems/number-of-ways-to-rearrange-sticks-with-k-sticks-visible/

public class Solution {
    public int RearrangeSticks(int n, int k) {
        const int mod = 1_000_000_007;
        if (k == 0 || k > n) {
            return 0;
        }
        var dp = new long[n + 1, n + 1];
        dp[1, 1] = 1;
        for (int sticks = 2; sticks <= n; sticks++) {
            dp[sticks, 1] = (sticks - 1) * dp[sticks - 1, 1] % mod;
            for (int visible = 2; visible <= sticks; visible++) {
                dp[sticks, visible] = (dp[sticks - 1, visible - 1] + (sticks - 1) * dp[sticks - 1, visible]) % mod;
            }
        }
        return (int)dp[n, k];
    }
}
'''

SOLUTIONS[1868] = r'''// LeetCode 1868 - Product of Two Run-Length Encoded Arrays
// https://leetcode.com/problems/product-of-two-run-length-encoded-arrays/

public class Solution {
    public int[][] FindRLEArray(int[][] encoded1, int[][] encoded2) {
        var result = new List<int[]>();
        int i = 0;
        int j = 0;
        int rem1 = encoded1[0][1];
        int rem2 = encoded2[0][1];

        while (i < encoded1.Length) {
            int take = Math.Min(rem1, rem2);
            int value = encoded1[i][0] * encoded2[j][0];
            if (result.Count > 0 && result[^1][0] == value) {
                result[^1][1] += take;
            } else {
                result.Add(new[] { value, take });
            }
            rem1 -= take;
            rem2 -= take;
            if (rem1 == 0) {
                i++;
                if (i < encoded1.Length) {
                    rem1 = encoded1[i][1];
                }
            }
            if (rem2 == 0) {
                j++;
                if (j < encoded2.Length) {
                    rem2 = encoded2[j][1];
                }
            }
        }
        return result.ToArray();
    }
}
'''

SOLUTIONS[1869] = r'''// LeetCode 1869 - Longer Contiguous Segments of Ones than Zeros
// https://leetcode.com/problems/longer-contiguous-segments-of-ones-than-zeros/

public class Solution {
    public bool CheckZeroOnes(string s) {
        int maxZeros = 0;
        int maxOnes = 0;
        int zeros = 0;
        int ones = 0;
        foreach (char ch in s) {
            if (ch == '0') {
                zeros++;
                ones = 0;
                maxZeros = Math.Max(maxZeros, zeros);
            } else {
                ones++;
                zeros = 0;
                maxOnes = Math.Max(maxOnes, ones);
            }
        }
        return maxOnes > maxZeros;
    }
}
'''

SOLUTIONS[1870] = r'''// LeetCode 1870 - Minimum Speed to Arrive on Time
// https://leetcode.com/problems/minimum-speed-to-arrive-on-time/

public class Solution {
    public int MinSpeedOnTime(int[] dist, double hour) {
        int n = dist.Length;
        if (n - 1 >= hour) {
            return -1;
        }

        bool CanArrive(int speed) {
            double time = 0;
            for (int i = 0; i < n - 1; i++) {
                time += (dist[i] + speed - 1) / speed;
            }
            time += (double)dist[n - 1] / speed;
            return time <= hour;
        }

        if (!CanArrive(10_000_000)) {
            return -1;
        }
        int lo = 1;
        int hi = 10_000_000;
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (CanArrive(mid)) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        return lo;
    }
}
'''

SOLUTIONS[1871] = r'''// LeetCode 1871 - Jump Game VII
// https://leetcode.com/problems/jump-game-vii/

public class Solution {
    public bool CanReach(string s, int minJump, int maxJump) {
        int n = s.Length;
        var reachable = new bool[n];
        reachable[0] = true;
        var prefix = new int[n + 1];
        for (int i = 0; i < n; i++) {
            if (i > 0 && s[i] == '0') {
                int left = Math.Max(0, i - maxJump);
                int right = i - minJump;
                if (right >= left && prefix[right + 1] - prefix[left] > 0) {
                    reachable[i] = true;
                }
            }
            prefix[i + 1] = prefix[i] + (reachable[i] ? 1 : 0);
        }
        return reachable[n - 1];
    }
}
'''

SOLUTIONS[1872] = r'''// LeetCode 1872 - Stone Game VIII
// https://leetcode.com/problems/stone-game-viii/

public class Solution {
    public int StoneGameVIII(int[] stones) {
        int n = stones.Length;
        for (int i = 1; i < n; i++) {
            stones[i] += stones[i - 1];
        }
        int score = stones[n - 1];
        for (int i = n - 2; i >= 1; i--) {
            score = Math.Max(stones[i] - score, score);
        }
        return score;
    }
}
'''

SOLUTIONS[1874] = r'''// LeetCode 1874 - Minimize Product Sum of Two Arrays
// https://leetcode.com/problems/minimize-product-sum-of-two-arrays/

public class Solution {
    public int MinProductSum(int[] nums1, int[] nums2) {
        Array.Sort(nums1);
        Array.Sort(nums2);
        int answer = 0;
        for (int i = 0; i < nums1.Length; i++) {
            answer += nums1[i] * nums2[nums2.Length - 1 - i];
        }
        return answer;
    }
}
'''

SOLUTIONS[1876] = r'''// LeetCode 1876 - Substrings of Size Three with Distinct Characters
// https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/

public class Solution {
    public int CountGoodSubstrings(string s) {
        if (s.Length < 3) {
            return 0;
        }
        int count = 0;
        for (int i = 0; i < s.Length - 2; i++) {
            char a = s[i], b = s[i + 1], c = s[i + 2];
            if (a != b && b != c && a != c) {
                count++;
            }
        }
        return count;
    }
}
'''

SOLUTIONS[1877] = r'''// LeetCode 1877 - Minimize Maximum Pair Sum in Array
// https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/

public class Solution {
    public int MinPairSum(int[] nums) {
        Array.Sort(nums);
        int best = 0;
        for (int i = 0; i < nums.Length / 2; i++) {
            best = Math.Max(best, nums[i] + nums[nums.Length - 1 - i]);
        }
        return best;
    }
}
'''

SOLUTIONS[1878] = r'''// LeetCode 1878 - Get Biggest Three Rhombus Sums in a Grid
// https://leetcode.com/problems/get-biggest-three-rhombus-sums-in-a-grid/

public class Solution {
    public int[] GetBiggestThree(int[][] grid) {
        int m = grid.Length;
        int n = grid[0].Length;
        var s1 = new int[m + 1][];
        var s2 = new int[m + 1][];
        for (int i = 0; i <= m; i++) {
            s1[i] = new int[n + 2];
            s2[i] = new int[n + 2];
        }

        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                int value = grid[i - 1][j - 1];
                s1[i][j] = s1[i - 1][j - 1] + value;
                s2[i][j] = s2[i - 1][j + 1] + value;
            }
        }

        var rhombusSums = new HashSet<int>();
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                int value = grid[i - 1][j - 1];
                int limit = Math.Min(Math.Min(i - 1, m - i), Math.Min(j - 1, n - j));
                rhombusSums.Add(value);
                for (int k = 1; k <= limit; k++) {
                    int a = s1[i + k][j] - s1[i][j - k];
                    int b = s1[i][j + k] - s1[i - k][j];
                    int c = s2[i][j - k] - s2[i - k][j];
                    int d = s2[i + k][j] - s2[i][j + k];
                    rhombusSums.Add(a + b + c + d - grid[i + k - 1][j - 1] + grid[i - k - 1][j - 1]);
                }
            }
        }

        var sorted = rhombusSums.ToArray();
        Array.Sort(sorted, (x, y) => y.CompareTo(x));
        int take = Math.Min(3, sorted.Length);
        var answer = new int[take];
        Array.Copy(sorted, answer, take);
        return answer;
    }
}
'''

SOLUTIONS[1879] = r'''// LeetCode 1879 - Minimum XOR Sum of Two Arrays
// https://leetcode.com/problems/minimum-xor-sum-of-two-arrays/

public class Solution {
    public int MinimumXORSum(int[] nums1, int[] nums2) {
        int n = nums1.Length;
        var dp = new int[1 << n];
        Array.Fill(dp, int.MaxValue / 2);
        dp[0] = 0;
        for (int mask = 0; mask < (1 << n); mask++) {
            int i = BitCount(mask);
            if (i >= n) {
                continue;
            }
            for (int j = 0; j < n; j++) {
                if ((mask & (1 << j)) == 0) {
                    int nextMask = mask | (1 << j);
                    int cost = dp[mask] + (nums1[i] ^ nums2[j]);
                    if (cost < dp[nextMask]) {
                        dp[nextMask] = cost;
                    }
                }
            }
        }
        return dp[(1 << n) - 1];
    }

    private static int BitCount(int value) {
        int count = 0;
        while (value != 0) {
            count += value & 1;
            value >>= 1;
        }
        return count;
    }
}
'''

SOLUTIONS[1880] = r'''// LeetCode 1880 - Check if Word Equals Summation of Two Words
// https://leetcode.com/problems/check-if-word-equals-summation-of-two-words/

public class Solution {
    public bool IsSumEqual(string firstWord, string secondWord, string targetWord) {
        return Value(firstWord) + Value(secondWord) == Value(targetWord);
    }

    private static int Value(string word) {
        int result = 0;
        foreach (char ch in word) {
            result = result * 10 + (ch - 'a');
        }
        return result;
    }
}
'''

SOLUTIONS[1881] = r'''// LeetCode 1881 - Maximum Value after Insertion
// https://leetcode.com/problems/maximum-value-after-insertion/

public class Solution {
    public string MaxValue(string n, int x) {
        bool neg = n[0] == '-';
        int start = neg ? 1 : 0;
        for (int i = start; i < n.Length; i++) {
            int d = n[i] - '0';
            if (neg) {
                if (d > x) {
                    return n.Substring(0, i) + x + n.Substring(i);
                }
            } else if (d < x) {
                return n.Substring(0, i) + x + n.Substring(i);
            }
        }
        return n + x;
    }
}
'''

SOLUTIONS[1882] = r'''// LeetCode 1882 - Process Tasks Using Servers
// https://leetcode.com/problems/process-tasks-using-servers/

public class Solution {
    public int[] AssignTasks(int[] servers, int[] tasks) {
        var available = new PriorityQueue<(int weight, int index), (int weight, int index)>();
        for (int index = 0; index < servers.Length; index++) {
            available.Enqueue((servers[index], index), (servers[index], index));
        }
        var busy = new PriorityQueue<(long finish, int weight, int index), (long finish, int weight, int index)>();
        var answer = new int[tasks.Length];
        long time = 0;

        for (int moment = 0; moment < tasks.Length; moment++) {
            int task = tasks[moment];
            time = Math.Max(time, moment);
            while (busy.Count > 0 && busy.Peek().finish <= time) {
                var (_, weight, index) = busy.Dequeue();
                available.Enqueue((weight, index), (weight, index));
            }
            while (available.Count == 0) {
                time = busy.Peek().finish;
                while (busy.Count > 0 && busy.Peek().finish <= time) {
                    var (_, weight, index) = busy.Dequeue();
                    available.Enqueue((weight, index), (weight, index));
                }
            }
            var (w, idx) = available.Dequeue();
            busy.Enqueue((time + task, w, idx), (time + task, w, idx));
            answer[moment] = idx;
        }
        return answer;
    }
}
'''

SOLUTIONS[1883] = r'''// LeetCode 1883 - Minimum Skips to Arrive at Meeting On Time
// https://leetcode.com/problems/minimum-skips-to-arrive-at-meeting-on-time/

public class Solution {
    public int MinSkips(int[] dist, int speed, int hoursBefore) {
        long limit = (long)hoursBefore * speed;
        int n = dist.Length;
        const long INF = long.MaxValue / 4;
        var dp = new long[n + 1];
        Array.Fill(dp, INF);
        dp[0] = 0;

        foreach (int road in dist) {
            var nxt = new long[n + 1];
            Array.Fill(nxt, INF);
            for (int skips = 0; skips < n; skips++) {
                if (dp[skips] >= INF) {
                    continue;
                }
                long ceiled = ((dp[skips] + road + speed - 1) / speed) * speed;
                nxt[skips] = Math.Min(nxt[skips], ceiled);
                nxt[skips + 1] = Math.Min(nxt[skips + 1], dp[skips] + road);
            }
            dp = nxt;
        }

        for (int skips = 0; skips <= n; skips++) {
            if (dp[skips] <= limit) {
                return skips;
            }
        }
        return -1;
    }
}
'''

SOLUTIONS[1884] = r'''// LeetCode 1884 - Egg Drop With 2 Eggs and N Floors
// https://leetcode.com/problems/egg-drop-with-2-eggs-and-n-floors/

public class Solution {
    public int TwoEggDrop(int n) {
        int moves = 0;
        int covered = 0;
        while (covered < n) {
            moves++;
            covered += moves;
        }
        return moves;
    }
}
'''

SOLUTIONS[1885] = r'''// LeetCode 1885 - Count Pairs in Two Arrays
// https://leetcode.com/problems/count-pairs-in-two-arrays/

public class Solution {
    public long CountPairs(int[] nums1, int[] nums2) {
        int n = nums1.Length;
        var diff = new int[n];
        for (int i = 0; i < n; i++) {
            diff[i] = nums1[i] - nums2[i];
        }
        Array.Sort(diff);
        long answer = 0;
        for (int i = 0; i < n; i++) {
            int target = -diff[i];
            int lo = i + 1;
            int hi = n;
            while (lo < hi) {
                int mid = lo + (hi - lo) / 2;
                if (diff[mid] <= target) {
                    lo = mid + 1;
                } else {
                    hi = mid;
                }
            }
            answer += n - lo;
        }
        return answer;
    }
}
'''

SOLUTIONS[1886] = r'''// LeetCode 1886 - Determine Whether Matrix Can Be Obtained By Rotation
// https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/

public class Solution {
    public bool FindRotation(int[][] mat, int[][] target) {
        int[][] current = mat;
        for (int r = 0; r < 4; r++) {
            if (Same(current, target)) {
                return true;
            }
            current = Rotate(current);
        }
        return false;
    }

    private static bool Same(int[][] a, int[][] b) {
        for (int i = 0; i < a.Length; i++) {
            for (int j = 0; j < a[i].Length; j++) {
                if (a[i][j] != b[i][j]) {
                    return false;
                }
            }
        }
        return true;
    }

    private static int[][] Rotate(int[][] mat) {
        int n = mat.Length;
        var next = new int[n][];
        for (int i = 0; i < n; i++) {
            next[i] = new int[n];
            for (int j = 0; j < n; j++) {
                next[i][j] = mat[n - 1 - j][i];
            }
        }
        return next;
    }
}
'''

SOLUTIONS[1887] = r'''// LeetCode 1887 - Reduction Operations to Make the Array Elements Equal
// https://leetcode.com/problems/reduction-operations-to-make-the-array-elements-equal/

public class Solution {
    public int ReductionOperations(int[] nums) {
        Array.Sort(nums);
        int answer = 0;
        int rank = 0;
        for (int i = 1; i < nums.Length; i++) {
            if (nums[i] != nums[i - 1]) {
                rank++;
            }
            answer += rank;
        }
        return answer;
    }
}
'''

SOLUTIONS[1888] = r'''// LeetCode 1888 - Minimum Number of Flips to Make the Binary String Alternating
// https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/

public class Solution {
    public int MinFlips(string s) {
        int n = s.Length;
        string doubled = s + s;
        int alt0 = 0;
        int alt1 = 0;
        for (int i = 0; i < n; i++) {
            char expect0 = i % 2 == 0 ? '0' : '1';
            char expect1 = i % 2 == 0 ? '1' : '0';
            if (doubled[i] != expect0) {
                alt0++;
            }
            if (doubled[i] != expect1) {
                alt1++;
            }
        }
        int answer = Math.Min(alt0, alt1);
        for (int i = 0; i < n; i++) {
            char expect0i = i % 2 == 0 ? '0' : '1';
            char expect0n = (i + n) % 2 == 0 ? '0' : '1';
            if (doubled[i] != expect0i) {
                alt0--;
            }
            if (doubled[i + n] != expect0n) {
                alt0++;
            }

            char expect1i = i % 2 == 0 ? '1' : '0';
            char expect1n = (i + n) % 2 == 0 ? '1' : '0';
            if (doubled[i] != expect1i) {
                alt1--;
            }
            if (doubled[i + n] != expect1n) {
                alt1++;
            }

            answer = Math.Min(answer, Math.Min(alt0, alt1));
        }
        return answer;
    }
}
'''

SOLUTIONS[1889] = r'''// LeetCode 1889 - Minimum Space Wasted From Packaging
// https://leetcode.com/problems/minimum-space-wasted-from-packaging/

public class Solution {
    public int MinWastedSpace(int[] packages, int[][] boxes) {
        Array.Sort(packages);
        var prefix = new long[packages.Length];
        prefix[0] = packages[0];
        for (int i = 1; i < packages.Length; i++) {
            prefix[i] = prefix[i - 1] + packages[i];
        }

        long answer = long.MaxValue;
        foreach (int[] supplier in boxes) {
            var sortedBoxes = (int[])supplier.Clone();
            Array.Sort(sortedBoxes);
            int start = 0;
            long wasted = 0;
            bool ok = true;
            foreach (int box in sortedBoxes) {
                if (!ok) {
                    break;
                }
                int lo = start;
                int hi = packages.Length;
                while (lo < hi) {
                    int mid = lo + (hi - lo) / 2;
                    if (packages[mid] <= box) {
                        lo = mid + 1;
                    } else {
                        hi = mid;
                    }
                }
                int end = lo;
                if (end != start) {
                    long packageSum = prefix[end - 1] - (start > 0 ? prefix[start - 1] : 0L);
                    wasted += (long)box * (end - start) - packageSum;
                    start = end;
                }
            }
            if (start == packages.Length) {
                answer = Math.Min(answer, wasted);
            }
        }
        return answer == long.MaxValue ? -1 : (int)(answer % 1_000_000_007L);
    }
}
'''

SOLUTIONS[1891] = r'''// LeetCode 1891 - Cutting Ribbons
// https://leetcode.com/problems/cutting-ribbons/

public class Solution {
    public int MaxLength(int[] ribbons, int k) {
        bool Can(int length) {
            long total = 0;
            foreach (int ribbon in ribbons) {
                total += ribbon / length;
                if (total >= k) {
                    return true;
                }
            }
            return total >= k;
        }

        int lo = 1;
        int hi = 0;
        foreach (int ribbon in ribbons) {
            hi = Math.Max(hi, ribbon);
        }
        while (lo < hi) {
            int mid = lo + (hi - lo + 1) / 2;
            if (Can(mid)) {
                lo = mid;
            } else {
                hi = mid - 1;
            }
        }
        return Can(lo) ? lo : 0;
    }
}
'''

SOLUTIONS[1893] = r'''// LeetCode 1893 - Check if All the Integers in a Range Are Covered
// https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/

public class Solution {
    public bool IsCovered(int[][] ranges, int left, int right) {
        var covered = new bool[51];
        foreach (var r in ranges) {
            for (int value = r[0]; value <= r[1]; value++) {
                covered[value] = true;
            }
        }
        for (int value = left; value <= right; value++) {
            if (!covered[value]) {
                return false;
            }
        }
        return true;
    }
}
'''

SOLUTIONS[1894] = r'''// LeetCode 1894 - Find the Student that Will Replace the Chalk
// https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/

public class Solution {
    public int ChalkReplacer(int[] chalk, int k) {
        long sum = 0;
        foreach (int c in chalk) {
            sum += c;
        }
        long remaining = k % sum;
        for (int index = 0; index < chalk.Length; index++) {
            if (remaining < chalk[index]) {
                return index;
            }
            remaining -= chalk[index];
        }
        return 0;
    }
}
'''

SOLUTIONS[1895] = r'''// LeetCode 1895 - Largest Magic Square
// https://leetcode.com/problems/largest-magic-square/

public class Solution {
    public int LargestMagicSquare(int[][] grid) {
        int rows = grid.Length;
        int cols = grid[0].Length;
        var rowPrefix = new int[rows][];
        var colPrefix = new int[cols][];
        for (int i = 0; i < rows; i++) {
            rowPrefix[i] = new int[cols + 1];
        }
        for (int j = 0; j < cols; j++) {
            colPrefix[j] = new int[rows + 1];
        }
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                rowPrefix[i][j + 1] = rowPrefix[i][j] + grid[i][j];
                colPrefix[j][i + 1] = colPrefix[j][i] + grid[i][j];
            }
        }

        int RowSum(int row, int colStart, int colEnd) =>
            rowPrefix[row][colEnd + 1] - rowPrefix[row][colStart];

        int ColSum(int col, int rowStart, int rowEnd) =>
            colPrefix[col][rowEnd + 1] - colPrefix[col][rowStart];

        bool IsMagic(int rowStart, int colStart, int size) {
            int target = RowSum(rowStart, colStart, colStart + size - 1);
            for (int row = rowStart; row < rowStart + size; row++) {
                if (RowSum(row, colStart, colStart + size - 1) != target) {
                    return false;
                }
            }
            for (int col = colStart; col < colStart + size; col++) {
                if (ColSum(col, rowStart, rowStart + size - 1) != target) {
                    return false;
                }
            }
            int diag1 = 0;
            int diag2 = 0;
            for (int offset = 0; offset < size; offset++) {
                diag1 += grid[rowStart + offset][colStart + offset];
                diag2 += grid[rowStart + offset][colStart + size - 1 - offset];
            }
            return diag1 == target && diag2 == target;
        }

        for (int size = Math.Min(rows, cols); size >= 1; size--) {
            for (int rowStart = 0; rowStart <= rows - size; rowStart++) {
                for (int colStart = 0; colStart <= cols - size; colStart++) {
                    if (IsMagic(rowStart, colStart, size)) {
                        return size;
                    }
                }
            }
        }
        return 1;
    }
}
'''

SOLUTIONS[1896] = r'''// LeetCode 1896 - Minimum Cost to Change the Final Value of Expression
// https://leetcode.com/problems/minimum-cost-to-change-the-final-value-of-expression/

public class Solution {
    private string expression = "";
    private int index;

    public int MinOperationsToFlip(string expression) {
        this.expression = expression;
        index = 0;
        int[] node = ParseExpr();
        return node[0] == 0 ? node[2] : node[1];
    }

    private static int[] Combine(int[] left, char op, int[] right) {
        int leftVal = left[0], leftToZero = left[1], leftToOne = left[2];
        int rightVal = right[0], rightToZero = right[1], rightToOne = right[2];
        if (op == '&') {
            int andVal = leftVal & rightVal;
            int andToZero = Math.Min(leftToZero, leftToOne + rightToZero);
            int andToOne = leftToOne + rightToOne;
            int orToZero = leftToZero + rightToZero;
            int orToOne = Math.Min(leftToOne, Math.Min(leftToZero + rightToOne, rightToZero + leftToOne));
            return new[] { andVal, Math.Min(andToZero, 1 + orToZero), Math.Min(andToOne, 1 + orToOne) };
        } else {
            int orVal = leftVal | rightVal;
            int orToZero = leftToZero + rightToZero;
            int orToOne = Math.Min(leftToOne, Math.Min(leftToZero + rightToOne, rightToZero + leftToOne));
            int andToZero = Math.Min(leftToZero, leftToOne + rightToZero);
            int andToOne = leftToOne + rightToOne;
            return new[] { orVal, Math.Min(orToZero, 1 + andToZero), Math.Min(orToOne, 1 + andToOne) };
        }
    }

    private int[] ParseFactor() {
        if (expression[index] == '0' || expression[index] == '1') {
            int value = expression[index] - '0';
            index++;
            return new[] { value, value == 0 ? 0 : 1, value == 0 ? 1 : 0 };
        }
        index++;
        int[] node = ParseExpr();
        index++;
        return node;
    }

    private int[] ParseExpr() {
        int[] node = ParseFactor();
        while (index < expression.Length && (expression[index] == '&' || expression[index] == '|')) {
            char op = expression[index];
            index++;
            node = Combine(node, op, ParseFactor());
        }
        return node;
    }
}
'''

SOLUTIONS[1897] = r'''// LeetCode 1897 - Redistribute Characters to Make All Strings Equal
// https://leetcode.com/problems/redistribute-characters-to-make-all-strings-equal/

public class Solution {
    public bool MakeEqual(string[] words) {
        var counts = new int[26];
        foreach (string word in words) {
            foreach (char ch in word) {
                counts[ch - 'a']++;
            }
        }
        int n = words.Length;
        foreach (int count in counts) {
            if (count % n != 0) {
                return false;
            }
        }
        return true;
    }
}
'''

SOLUTIONS[1898] = r'''// LeetCode 1898 - Maximum Number of Removable Characters
// https://leetcode.com/problems/maximum-number-of-removable-characters/

public class Solution {
    public int MaximumRemovals(string s, string p, int[] removable) {
        bool StillSubsequence(int k) {
            var removed = new HashSet<int>();
            for (int i = 0; i < k; i++) {
                removed.Add(removable[i]);
            }
            int index = 0;
            for (int position = 0; position < s.Length; position++) {
                if (removed.Contains(position)) {
                    continue;
                }
                if (index < p.Length && s[position] == p[index]) {
                    index++;
                }
            }
            return index == p.Length;
        }

        int lo = 0;
        int hi = removable.Length;
        while (lo < hi) {
            int mid = lo + (hi - lo + 1) / 2;
            if (StillSubsequence(mid)) {
                lo = mid;
            } else {
                hi = mid - 1;
            }
        }
        return lo;
    }
}
'''

SOLUTIONS[1899] = r'''// LeetCode 1899 - Merge Triplets to Form Target Triplet
// https://leetcode.com/problems/merge-triplets-to-form-target-triplet/

public class Solution {
    public bool MergeTriplets(int[][] triplets, int[] target) {
        var merged = new int[3];
        foreach (var t in triplets) {
            if (t[0] <= target[0] && t[1] <= target[1] && t[2] <= target[2]) {
                merged[0] = Math.Max(merged[0], t[0]);
                merged[1] = Math.Max(merged[1], t[1]);
                merged[2] = Math.Max(merged[2], t[2]);
            }
        }
        return merged[0] == target[0] && merged[1] == target[1] && merged[2] == target[2];
    }
}
'''

SOLUTIONS[1900] = r'''// LeetCode 1900 - The Earliest and Latest Rounds Where Players Compete
// https://leetcode.com/problems/the-earliest-and-latest-rounds-where-players-compete/

public class Solution {
    private int first;
    private int second;
    private readonly Dictionary<string, int[]> memo = new();

    public int[] EarliestAndLatest(int n, int firstPlayer, int secondPlayer) {
        first = firstPlayer;
        second = secondPlayer;
        memo.Clear();
        var players = new List<int>();
        for (int i = 1; i <= n; i++) {
            players.Add(i);
        }
        return Dfs(players);
    }

    private int[] Dfs(List<int> players) {
        string key = string.Join(",", players);
        if (memo.TryGetValue(key, out int[]? cached)) {
            return cached;
        }

        int count = players.Count;
        int firstIndex = players.IndexOf(first);
        int secondIndex = players.IndexOf(second);
        if (firstIndex + secondIndex == count - 1) {
            var result = new[] { 1, 1 };
            memo[key] = result;
            return result;
        }

        var choices = new List<List<int>>();
        for (int index = 0; index < count / 2; index++) {
            int left = players[index];
            int right = players[count - 1 - index];
            if (left == first || left == second) {
                choices.Add(new List<int> { left });
            } else if (right == first || right == second) {
                choices.Add(new List<int> { right });
            } else {
                choices.Add(new List<int> { left, right });
            }
        }
        if (count % 2 == 1) {
            choices.Add(new List<int> { players[count / 2] });
        }

        int earliest = int.MaxValue / 2;
        int latest = 0;
        var picks = new List<int>();

        void Explore(int i) {
            if (i == choices.Count) {
                var winners = new List<int>(picks);
                winners.Sort();
                int[] next = Dfs(winners);
                earliest = Math.Min(earliest, next[0] + 1);
                latest = Math.Max(latest, next[1] + 1);
                return;
            }
            foreach (int pick in choices[i]) {
                picks.Add(pick);
                Explore(i + 1);
                picks.RemoveAt(picks.Count - 1);
            }
        }

        Explore(0);
        var answer = new[] { earliest, latest };
        memo[key] = answer;
        return answer;
    }
}
'''


def main() -> None:
    skip = {1853, 1867, 1873, 1875, 1890, 1892}
    written = []
    for num, content in sorted(SOLUTIONS.items()):
        if num in skip:
            continue
        folders = list(ROOT.glob(f"{num:04d}_*"))
        if not folders:
            raise SystemExit(f"Missing folder for {num}")
        path = folders[0] / "Solution.cs"
        path.write_text(content.lstrip("\n"), encoding="utf-8", newline="\n")
        written.append(folders[0].name)
    print(f"Wrote {len(written)} Solution.cs files")
    for name in written:
        print(f"  {name}")


if __name__ == "__main__":
    main()
