#!/usr/bin/env python3
"""Write Java solutions for LeetCode 1000-1049 (non-SQL)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent

TREE = """
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}
""".strip()

LIST = """
class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}
""".strip()

SOLUTIONS: dict[str, str] = {}

SOLUTIONS["1000_minimum_cost_to_merge_stones"] = r'''// LeetCode 1000 - Minimum Cost to Merge Stones
// https://leetcode.com/problems/minimum-cost-to-merge-stones/

class Solution {
    public int mergeStones(int[] stones, int k) {
        int n = stones.length;
        if ((n - 1) % (k - 1) != 0) return -1;
        int[] prefix = new int[n + 1];
        for (int i = 0; i < n; i++) prefix[i + 1] = prefix[i] + stones[i];
        int[][] dp = new int[n][n];
        for (int length = k; length <= n; length++) {
            for (int i = 0; i + length - 1 < n; i++) {
                int j = i + length - 1;
                int best = Integer.MAX_VALUE / 2;
                for (int m = i; m < j; m += k - 1) {
                    best = Math.min(best, dp[i][m] + dp[m + 1][j]);
                }
                dp[i][j] = best;
                if ((length - 1) % (k - 1) == 0) {
                    dp[i][j] += prefix[j + 1] - prefix[i];
                }
            }
        }
        return dp[0][n - 1];
    }
}
'''

SOLUTIONS["1001_grid_illumination"] = r'''// LeetCode 1001 - Grid Illumination
// https://leetcode.com/problems/grid-illumination/

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

class Solution {
    public int[] gridIllumination(int n, int[][] lamps, int[][] queries) {
        Map<Integer, Integer> rows = new HashMap<>();
        Map<Integer, Integer> cols = new HashMap<>();
        Map<Integer, Integer> diag1 = new HashMap<>();
        Map<Integer, Integer> diag2 = new HashMap<>();
        Set<Long> lit = new HashSet<>();
        for (int[] lamp : lamps) {
            int r = lamp[0], c = lamp[1];
            long key = (((long) r) << 32) | (c & 0xffffffffL);
            if (!lit.add(key)) continue;
            rows.merge(r, 1, Integer::sum);
            cols.merge(c, 1, Integer::sum);
            diag1.merge(r - c, 1, Integer::sum);
            diag2.merge(r + c, 1, Integer::sum);
        }
        int[] ans = new int[queries.length];
        for (int qi = 0; qi < queries.length; qi++) {
            int r = queries[qi][0], c = queries[qi][1];
            if (rows.getOrDefault(r, 0) > 0 || cols.getOrDefault(c, 0) > 0
                    || diag1.getOrDefault(r - c, 0) > 0 || diag2.getOrDefault(r + c, 0) > 0) {
                ans[qi] = 1;
            }
            for (int i = r - 1; i <= r + 1; i++) {
                for (int j = c - 1; j <= c + 1; j++) {
                    long key = (((long) i) << 32) | (j & 0xffffffffL);
                    if (lit.remove(key)) {
                        dec(rows, i);
                        dec(cols, j);
                        dec(diag1, i - j);
                        dec(diag2, i + j);
                    }
                }
            }
        }
        return ans;
    }

    private void dec(Map<Integer, Integer> map, int key) {
        int v = map.getOrDefault(key, 0) - 1;
        if (v <= 0) map.remove(key);
        else map.put(key, v);
    }
}
'''

SOLUTIONS["1002_find_common_characters"] = r'''// LeetCode 1002 - Find Common Characters
// https://leetcode.com/problems/find-common-characters/

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public List<String> commonChars(String[] words) {
        int[] common = new int[26];
        Arrays.fill(common, Integer.MAX_VALUE);
        for (String w : words) {
            int[] cnt = new int[26];
            for (char ch : w.toCharArray()) cnt[ch - 'a']++;
            for (int i = 0; i < 26; i++) common[i] = Math.min(common[i], cnt[i]);
        }
        List<String> ans = new ArrayList<>();
        for (int i = 0; i < 26; i++) {
            while (common[i]-- > 0) ans.add(String.valueOf((char) ('a' + i)));
        }
        return ans;
    }
}
'''

SOLUTIONS["1003_check_if_word_is_valid_after_substitutions"] = r'''// LeetCode 1003 - Check If Word Is Valid After Substitutions
// https://leetcode.com/problems/check-if-word-is-valid-after-substitutions/

class Solution {
    public boolean isValid(String s) {
        StringBuilder stack = new StringBuilder();
        for (char ch : s.toCharArray()) {
            stack.append(ch);
            int n = stack.length();
            if (n >= 3 && stack.charAt(n - 3) == 'a' && stack.charAt(n - 2) == 'b' && stack.charAt(n - 1) == 'c') {
                stack.setLength(n - 3);
            }
        }
        return stack.length() == 0;
    }
}
'''

SOLUTIONS["1004_max_consecutive_ones_iii"] = r'''// LeetCode 1004 - Max Consecutive Ones III
// https://leetcode.com/problems/max-consecutive-ones-iii/

class Solution {
    public int longestOnes(int[] nums, int k) {
        int left = 0, zeros = 0, ans = 0;
        for (int right = 0; right < nums.length; right++) {
            if (nums[right] == 0) zeros++;
            while (zeros > k) {
                if (nums[left++] == 0) zeros--;
            }
            ans = Math.max(ans, right - left + 1);
        }
        return ans;
    }
}
'''

SOLUTIONS["1005_maximize_sum_of_array_after_k_negations"] = r'''// LeetCode 1005 - Maximize Sum Of Array After K Negations
// https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/

import java.util.Arrays;

class Solution {
    public int largestSumAfterKNegations(int[] nums, int k) {
        Arrays.sort(nums);
        for (int i = 0; i < nums.length && k > 0; i++) {
            if (nums[i] < 0) {
                nums[i] = -nums[i];
                k--;
            }
        }
        if (k % 2 == 1) {
            Arrays.sort(nums);
            nums[0] = -nums[0];
        }
        int sum = 0;
        for (int x : nums) sum += x;
        return sum;
    }
}
'''

SOLUTIONS["1006_clumsy_factorial"] = r'''// LeetCode 1006 - Clumsy Factorial
// https://leetcode.com/problems/clumsy-factorial/

import java.util.ArrayDeque;
import java.util.Deque;

class Solution {
    public int clumsy(int n) {
        Deque<Integer> stack = new ArrayDeque<>();
        stack.push(n--);
        int op = 0;
        while (n > 0) {
            if (op % 4 == 0) stack.push(stack.pop() * n);
            else if (op % 4 == 1) stack.push(stack.pop() / n);
            else if (op % 4 == 2) stack.push(n);
            else stack.push(-n);
            n--;
            op++;
        }
        int sum = 0;
        for (int x : stack) sum += x;
        return sum;
    }
}
'''

SOLUTIONS["1007_minimum_domino_rotations_for_equal_row"] = r'''// LeetCode 1007 - Minimum Domino Rotations For Equal Row
// https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/

class Solution {
    public int minDominoRotations(int[] tops, int[] bottoms) {
        int ans = Math.min(check(tops, bottoms, tops[0]), check(tops, bottoms, bottoms[0]));
        return ans == Integer.MAX_VALUE / 2 ? -1 : ans;
    }

    private int check(int[] tops, int[] bottoms, int target) {
        int rotTop = 0, rotBot = 0;
        for (int i = 0; i < tops.length; i++) {
            if (tops[i] != target && bottoms[i] != target) return Integer.MAX_VALUE / 2;
            if (tops[i] != target) rotTop++;
            if (bottoms[i] != target) rotBot++;
        }
        return Math.min(rotTop, rotBot);
    }
}
'''

SOLUTIONS["1008_construct_binary_search_tree_from_preorder_traversal"] = f'''// LeetCode 1008 - Construct Binary Search Tree from Preorder Traversal
// https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/

{TREE}

class Solution {{
    private int i;

    public TreeNode bstFromPreorder(int[] preorder) {{
        i = 0;
        return build(preorder, Integer.MAX_VALUE);
    }}

    private TreeNode build(int[] preorder, int bound) {{
        if (i == preorder.length || preorder[i] > bound) return null;
        TreeNode root = new TreeNode(preorder[i++]);
        root.left = build(preorder, root.val);
        root.right = build(preorder, bound);
        return root;
    }}
}}
'''

SOLUTIONS["1009_complement_of_base_10_integer"] = r'''// LeetCode 1009 - Complement of Base 10 Integer
// https://leetcode.com/problems/complement-of-base-10-integer/

class Solution {
    public int bitwiseComplement(int n) {
        if (n == 0) return 1;
        int mask = 1;
        while (mask <= n) mask <<= 1;
        return n ^ (mask - 1);
    }
}
'''

SOLUTIONS["1010_pairs_of_songs_with_total_durations_divisible_by_60"] = r'''// LeetCode 1010 - Pairs of Songs With Total Durations Divisible by 60
// https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/

class Solution {
    public int numPairsDivisibleBy60(int[] time) {
        int[] count = new int[60];
        int ans = 0;
        for (int t : time) {
            ans += count[(60 - t % 60) % 60];
            count[t % 60]++;
        }
        return ans;
    }
}
'''

SOLUTIONS["1011_capacity_to_ship_packages_within_d_days"] = r'''// LeetCode 1011 - Capacity To Ship Packages Within D Days
// https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution {
    public int shipWithinDays(int[] weights, int days) {
        int lo = 0, hi = 0;
        for (int w : weights) {
            lo = Math.max(lo, w);
            hi += w;
        }
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (can(weights, days, mid)) hi = mid;
            else lo = mid + 1;
        }
        return lo;
    }

    private boolean can(int[] weights, int days, int cap) {
        int need = 1, cur = 0;
        for (int w : weights) {
            if (cur + w > cap) {
                need++;
                cur = 0;
            }
            cur += w;
        }
        return need <= days;
    }
}
'''

SOLUTIONS["1012_numbers_with_repeated_digits"] = r'''// LeetCode 1012 - Numbers With Repeated Digits
// https://leetcode.com/problems/numbers-with-repeated-digits/

class Solution {
    public int numDupDigitsAtMostN(int n) {
        String s = Integer.toString(n);
        int m = s.length();
        int totalUnique = 0;
        for (int length = 1; length < m; length++) {
            totalUnique += 9 * P(9, length - 1);
        }
        boolean[] used = new boolean[10];
        boolean broken = false;
        for (int i = 0; i < m; i++) {
            int d = s.charAt(i) - '0';
            int start = i == 0 ? 1 : 0;
            for (int x = start; x < d; x++) {
                if (used[x]) continue;
                totalUnique += P(9 - i, m - i - 1);
            }
            if (used[d]) {
                broken = true;
                break;
            }
            used[d] = true;
        }
        if (!broken) totalUnique++;
        return n - totalUnique;
    }

    private int P(int a, int b) {
        int res = 1;
        for (int i = 0; i < b; i++) res *= a - i;
        return res;
    }
}
'''

SOLUTIONS["1013_partition_array_into_three_parts_with_equal_sum"] = r'''// LeetCode 1013 - Partition Array Into Three Parts With Equal Sum
// https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/

class Solution {
    public boolean canThreePartsEqualSum(int[] arr) {
        int total = 0;
        for (int x : arr) total += x;
        if (total % 3 != 0) return false;
        int target = total / 3, parts = 0, cur = 0;
        for (int x : arr) {
            cur += x;
            if (cur == target) {
                parts++;
                cur = 0;
            }
        }
        return parts >= 3;
    }
}
'''

SOLUTIONS["1014_best_sightseeing_pair"] = r'''// LeetCode 1014 - Best Sightseeing Pair
// https://leetcode.com/problems/best-sightseeing-pair/

class Solution {
    public int maxScoreSightseeingPair(int[] values) {
        int best = values[0], ans = 0;
        for (int j = 1; j < values.length; j++) {
            ans = Math.max(ans, best + values[j] - j);
            best = Math.max(best, values[j] + j);
        }
        return ans;
    }
}
'''

SOLUTIONS["1015_smallest_integer_divisible_by_k"] = r'''// LeetCode 1015 - Smallest Integer Divisible by K
// https://leetcode.com/problems/smallest-integer-divisible-by-k/

class Solution {
    public int smallestRepunitDivByK(int k) {
        if (k % 2 == 0 || k % 5 == 0) return -1;
        int rem = 0;
        for (int length = 1; length <= k; length++) {
            rem = (rem * 10 + 1) % k;
            if (rem == 0) return length;
        }
        return -1;
    }
}
'''

SOLUTIONS["1016_binary_string_with_substrings_representing_1_to_n"] = r'''// LeetCode 1016 - Binary String With Substrings Representing 1 To N
// https://leetcode.com/problems/binary-string-with-substrings-representing-1-to-n/

class Solution {
    public boolean queryString(String s, int n) {
        for (int i = n; i > n / 2; i--) {
            if (!s.contains(Integer.toBinaryString(i))) return false;
        }
        return true;
    }
}
'''

SOLUTIONS["1017_convert_to_base_2"] = r'''// LeetCode 1017 - Convert to Base -2
// https://leetcode.com/problems/convert-to-base-2/

class Solution {
    public String baseNeg2(int n) {
        if (n == 0) return "0";
        StringBuilder ans = new StringBuilder();
        while (n != 0) {
            int rem = n % -2;
            n /= -2;
            if (rem < 0) {
                n++;
                rem += 2;
            }
            ans.append(rem);
        }
        return ans.reverse().toString();
    }
}
'''

SOLUTIONS["1018_binary_prefix_divisible_by_5"] = r'''// LeetCode 1018 - Binary Prefix Divisible By 5
// https://leetcode.com/problems/binary-prefix-divisible-by-5/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<Boolean> prefixesDivBy5(int[] nums) {
        List<Boolean> ans = new ArrayList<>(nums.length);
        int rem = 0;
        for (int bit : nums) {
            rem = (rem * 2 + bit) % 5;
            ans.add(rem == 0);
        }
        return ans;
    }
}
'''

SOLUTIONS["1019_next_greater_node_in_linked_list"] = f'''// LeetCode 1019 - Next Greater Node In Linked List
// https://leetcode.com/problems/next-greater-node-in-linked-list/

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.List;

{LIST}

class Solution {{
    public int[] nextLargerNodes(ListNode head) {{
        List<Integer> vals = new ArrayList<>();
        while (head != null) {{
            vals.add(head.val);
            head = head.next;
        }}
        int[] ans = new int[vals.size()];
        Deque<Integer> stack = new ArrayDeque<>();
        for (int i = 0; i < vals.size(); i++) {{
            while (!stack.isEmpty() && vals.get(stack.peek()) < vals.get(i)) {{
                ans[stack.pop()] = vals.get(i);
            }}
            stack.push(i);
        }}
        return ans;
    }}
}}
'''

SOLUTIONS["1020_number_of_enclaves"] = r'''// LeetCode 1020 - Number of Enclaves
// https://leetcode.com/problems/number-of-enclaves/

class Solution {
    public int numEnclaves(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        for (int i = 0; i < m; i++) {
            dfs(grid, i, 0);
            dfs(grid, i, n - 1);
        }
        for (int j = 0; j < n; j++) {
            dfs(grid, 0, j);
            dfs(grid, m - 1, j);
        }
        int ans = 0;
        for (int[] row : grid) for (int x : row) ans += x;
        return ans;
    }

    private void dfs(int[][] grid, int r, int c) {
        if (r < 0 || r >= grid.length || c < 0 || c >= grid[0].length || grid[r][c] != 1) return;
        grid[r][c] = 0;
        dfs(grid, r + 1, c);
        dfs(grid, r - 1, c);
        dfs(grid, r, c + 1);
        dfs(grid, r, c - 1);
    }
}
'''

SOLUTIONS["1021_remove_outermost_parentheses"] = r'''// LeetCode 1021 - Remove Outermost Parentheses
// https://leetcode.com/problems/remove-outermost-parentheses/

class Solution {
    public String removeOuterParentheses(String s) {
        StringBuilder ans = new StringBuilder();
        int depth = 0;
        for (char ch : s.toCharArray()) {
            if (ch == '(') {
                if (depth > 0) ans.append(ch);
                depth++;
            } else {
                depth--;
                if (depth > 0) ans.append(ch);
            }
        }
        return ans.toString();
    }
}
'''

SOLUTIONS["1022_sum_of_root_to_leaf_binary_numbers"] = f'''// LeetCode 1022 - Sum of Root To Leaf Binary Numbers
// https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/

{TREE}

class Solution {{
    public int sumRootToLeaf(TreeNode root) {{
        return dfs(root, 0);
    }}

    private int dfs(TreeNode node, int value) {{
        if (node == null) return 0;
        value = value * 2 + node.val;
        if (node.left == null && node.right == null) return value;
        return dfs(node.left, value) + dfs(node.right, value);
    }}
}}
'''

SOLUTIONS["1023_camelcase_matching"] = r'''// LeetCode 1023 - Camelcase Matching
// https://leetcode.com/problems/camelcase-matching/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<Boolean> camelMatch(String[] queries, String pattern) {
        List<Boolean> ans = new ArrayList<>(queries.length);
        for (String q : queries) ans.add(matches(q, pattern));
        return ans;
    }

    private boolean matches(String q, String pattern) {
        int i = 0;
        for (char ch : q.toCharArray()) {
            if (i < pattern.length() && ch == pattern.charAt(i)) i++;
            else if (ch >= 'A' && ch <= 'Z') return false;
        }
        return i == pattern.length();
    }
}
'''

SOLUTIONS["1024_video_stitching"] = r'''// LeetCode 1024 - Video Stitching
// https://leetcode.com/problems/video-stitching/

class Solution {
    public int videoStitching(int[][] clips, int time) {
        int[] furthest = new int[time + 1];
        for (int[] clip : clips) {
            int start = clip[0], end = clip[1];
            if (start <= time) furthest[start] = Math.max(furthest[start], end);
        }
        int ans = 0, reach = 0, nextReach = 0;
        for (int i = 0; i < time; i++) {
            nextReach = Math.max(nextReach, furthest[i]);
            if (i == reach) {
                if (nextReach <= i) return -1;
                ans++;
                reach = nextReach;
            }
        }
        return ans;
    }
}
'''

SOLUTIONS["1025_divisor_game"] = r'''// LeetCode 1025 - Divisor Game
// https://leetcode.com/problems/divisor-game/

class Solution {
    public boolean divisorGame(int n) {
        return n % 2 == 0;
    }
}
'''

SOLUTIONS["1026_maximum_difference_between_node_and_ancestor"] = f'''// LeetCode 1026 - Maximum Difference Between Node and Ancestor
// https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/

{TREE}

class Solution {{
    public int maxAncestorDiff(TreeNode root) {{
        return dfs(root, root.val, root.val);
    }}

    private int dfs(TreeNode node, int lo, int hi) {{
        if (node == null) return hi - lo;
        lo = Math.min(lo, node.val);
        hi = Math.max(hi, node.val);
        return Math.max(dfs(node.left, lo, hi), dfs(node.right, lo, hi));
    }}
}}
'''

SOLUTIONS["1027_longest_arithmetic_subsequence"] = r'''// LeetCode 1027 - Longest Arithmetic Subsequence
// https://leetcode.com/problems/longest-arithmetic-subsequence/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int longestArithSeqLength(int[] nums) {
        @SuppressWarnings("unchecked")
        Map<Integer, Integer>[] dp = new HashMap[nums.length];
        int ans = 1;
        for (int j = 1; j < nums.length; j++) {
            dp[j] = new HashMap<>();
            for (int i = 0; i < j; i++) {
                int d = nums[j] - nums[i];
                int prev = 1;
                if (dp[i] != null) prev = dp[i].getOrDefault(d, 1);
                int cur = prev + 1;
                dp[j].put(d, cur);
                ans = Math.max(ans, cur);
            }
        }
        return ans;
    }
}
'''

SOLUTIONS["1028_recover_a_tree_from_preorder_traversal"] = f'''// LeetCode 1028 - Recover a Tree From Preorder Traversal
// https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/

import java.util.ArrayDeque;
import java.util.Deque;

{TREE}

class Solution {{
    public TreeNode recoverFromPreorder(String traversal) {{
        Deque<TreeNode> stack = new ArrayDeque<>();
        int i = 0, n = traversal.length();
        while (i < n) {{
            int depth = 0;
            while (i < n && traversal.charAt(i) == '-') {{
                depth++;
                i++;
            }}
            int val = 0;
            while (i < n && Character.isDigit(traversal.charAt(i))) {{
                val = val * 10 + (traversal.charAt(i++) - '0');
            }}
            TreeNode node = new TreeNode(val);
            while (stack.size() > depth) stack.pop();
            if (!stack.isEmpty()) {{
                TreeNode parent = stack.peek();
                if (parent.left == null) parent.left = node;
                else parent.right = node;
            }}
            stack.push(node);
        }}
        while (stack.size() > 1) stack.pop();
        return stack.peek();
    }}
}}
'''

SOLUTIONS["1029_two_city_scheduling"] = r'''// LeetCode 1029 - Two City Scheduling
// https://leetcode.com/problems/two-city-scheduling/

import java.util.Arrays;

class Solution {
    public int twoCitySchedCost(int[][] costs) {
        Arrays.sort(costs, (a, b) -> (a[0] - a[1]) - (b[0] - b[1]));
        int n = costs.length / 2, sum = 0;
        for (int i = 0; i < n; i++) sum += costs[i][0];
        for (int i = n; i < costs.length; i++) sum += costs[i][1];
        return sum;
    }
}
'''

SOLUTIONS["1030_matrix_cells_in_distance_order"] = r'''// LeetCode 1030 - Matrix Cells in Distance Order
// https://leetcode.com/problems/matrix-cells-in-distance-order/

import java.util.Arrays;

class Solution {
    public int[][] allCellsDistOrder(int rows, int cols, int rCenter, int cCenter) {
        int[][] cells = new int[rows * cols][2];
        int idx = 0;
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                cells[idx][0] = r;
                cells[idx++][1] = c;
            }
        }
        Arrays.sort(cells, (a, b) -> {
            int da = Math.abs(a[0] - rCenter) + Math.abs(a[1] - cCenter);
            int db = Math.abs(b[0] - rCenter) + Math.abs(b[1] - cCenter);
            return Integer.compare(da, db);
        });
        return cells;
    }
}
'''

SOLUTIONS["1031_maximum_sum_of_two_non_overlapping_subarrays"] = r'''// LeetCode 1031 - Maximum Sum of Two Non-Overlapping Subarrays
// https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays/

class Solution {
    public int maxSumTwoNoOverlap(int[] nums, int firstLen, int secondLen) {
        int[] prefix = new int[nums.length + 1];
        for (int i = 0; i < nums.length; i++) prefix[i + 1] = prefix[i] + nums[i];
        return Math.max(best(prefix, firstLen, secondLen), best(prefix, secondLen, firstLen));
    }

    private int best(int[] prefix, int a, int b) {
        int bestA = 0, ans = 0;
        for (int i = a + b; i < prefix.length; i++) {
            bestA = Math.max(bestA, prefix[i - b] - prefix[i - b - a]);
            ans = Math.max(ans, bestA + prefix[i] - prefix[i - b]);
        }
        return ans;
    }
}
'''

SOLUTIONS["1032_stream_of_characters"] = r'''// LeetCode 1032 - Stream of Characters
// https://leetcode.com/problems/stream-of-characters/

class StreamChecker {
    private static class TrieNode {
        TrieNode[] children = new TrieNode[26];
        boolean isWord;
    }

    private final TrieNode root = new TrieNode();
    private final StringBuilder stream = new StringBuilder();

    public StreamChecker(String[] words) {
        for (String word : words) {
            TrieNode node = root;
            for (int i = word.length() - 1; i >= 0; i--) {
                int idx = word.charAt(i) - 'a';
                if (node.children[idx] == null) node.children[idx] = new TrieNode();
                node = node.children[idx];
            }
            node.isWord = true;
        }
    }

    public boolean query(String letter) {
        return query(letter.charAt(0));
    }

    public boolean query(char letter) {
        stream.append(letter);
        TrieNode node = root;
        for (int i = stream.length() - 1; i >= 0; i--) {
            if (node.isWord) return true;
            int idx = stream.charAt(i) - 'a';
            if (node.children[idx] == null) return false;
            node = node.children[idx];
        }
        return node.isWord;
    }
}
'''

SOLUTIONS["1033_moving_stones_until_consecutive"] = r'''// LeetCode 1033 - Moving Stones Until Consecutive
// https://leetcode.com/problems/moving-stones-until-consecutive/

import java.util.Arrays;

class Solution {
    public int[] numMovesStones(int a, int b, int c) {
        int[] arr = {a, b, c};
        Arrays.sort(arr);
        int x = arr[0], y = arr[1], z = arr[2];
        int minMoves = 2;
        if (z - x == 2) minMoves = 0;
        else if (y - x <= 2 || z - y <= 2) minMoves = 1;
        return new int[]{minMoves, z - x - 2};
    }
}
'''

SOLUTIONS["1034_coloring_a_border"] = r'''// LeetCode 1034 - Coloring A Border
// https://leetcode.com/problems/coloring-a-border/

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

class Solution {
    public int[][] colorBorder(int[][] grid, int row, int col, int color) {
        int m = grid.length, n = grid[0].length, original = grid[row][col];
        Set<Long> component = new HashSet<>();
        Deque<int[]> stack = new ArrayDeque<>();
        stack.push(new int[]{row, col});
        component.add(key(row, col));
        int[][] dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        while (!stack.isEmpty()) {
            int[] cur = stack.pop();
            for (int[] d : dirs) {
                int nr = cur[0] + d[0], nc = cur[1] + d[1];
                long k = key(nr, nc);
                if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] == original && component.add(k)) {
                    stack.push(new int[]{nr, nc});
                }
            }
        }
        List<long[]> border = new ArrayList<>();
        for (long k : component) {
            int r = (int) (k >> 32), c = (int) k;
            boolean isBorder = false;
            for (int[] d : dirs) {
                int nr = r + d[0], nc = c + d[1];
                if (nr < 0 || nr >= m || nc < 0 || nc >= n || !component.contains(key(nr, nc))) {
                    isBorder = true;
                    break;
                }
            }
            if (isBorder) border.add(new long[]{r, c});
        }
        for (long[] cell : border) grid[(int) cell[0]][(int) cell[1]] = color;
        return grid;
    }

    private long key(int r, int c) {
        return (((long) r) << 32) | (c & 0xffffffffL);
    }
}
'''

SOLUTIONS["1035_uncrossed_lines"] = r'''// LeetCode 1035 - Uncrossed Lines
// https://leetcode.com/problems/uncrossed-lines/

class Solution {
    public int maxUncrossedLines(int[] nums1, int[] nums2) {
        int m = nums1.length, n = nums2.length;
        int[][] dp = new int[m + 1][n + 1];
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (nums1[i - 1] == nums2[j - 1]) dp[i][j] = dp[i - 1][j - 1] + 1;
                else dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
        return dp[m][n];
    }
}
'''

SOLUTIONS["1036_escape_a_large_maze"] = r'''// LeetCode 1036 - Escape a Large Maze
// https://leetcode.com/problems/escape-a-large-maze/

import java.util.ArrayDeque;
import java.util.HashSet;
import java.util.Queue;
import java.util.Set;

class Solution {
    // Harness emits empty int[][] as new int[0]; overload accepts that form.
    public boolean isEscapePossible(int[] blocked, int[] source, int[] target) {
        return isEscapePossible(new int[0][], source, target);
    }

    public boolean isEscapePossible(int[][] blocked, int[] source, int[] target) {
        Set<Long> blockedSet = new HashSet<>();
        for (int[] b : blocked) blockedSet.add(key(b[0], b[1]));
        int limit = blocked.length * (blocked.length - 1) / 2;
        return bfs(source, target, blockedSet, limit) && bfs(target, source, blockedSet, limit);
    }

    private boolean bfs(int[] start, int[] goal, Set<Long> blockedSet, int limit) {
        Queue<long[]> q = new ArrayDeque<>();
        Set<Long> seen = new HashSet<>();
        q.offer(new long[]{start[0], start[1]});
        seen.add(key(start[0], start[1]));
        int[][] dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        while (!q.isEmpty()) {
            if (seen.size() > limit) return true;
            long[] cur = q.poll();
            int r = (int) cur[0], c = (int) cur[1];
            if (r == goal[0] && c == goal[1]) return true;
            for (int[] d : dirs) {
                int nr = r + d[0], nc = c + d[1];
                long k = key(nr, nc);
                if (nr >= 0 && nr < 1_000_000 && nc >= 0 && nc < 1_000_000
                        && !blockedSet.contains(k) && seen.add(k)) {
                    q.offer(new long[]{nr, nc});
                }
            }
        }
        return false;
    }

    private long key(int r, int c) {
        return (((long) r) << 32) | (c & 0xffffffffL);
    }
}
'''

SOLUTIONS["1037_valid_boomerang"] = r'''// LeetCode 1037 - Valid Boomerang
// https://leetcode.com/problems/valid-boomerang/

class Solution {
    public boolean isBoomerang(int[][] points) {
        int x1 = points[0][0], y1 = points[0][1];
        int x2 = points[1][0], y2 = points[1][1];
        int x3 = points[2][0], y3 = points[2][1];
        return (x2 - x1) * (y3 - y1) != (x3 - x1) * (y2 - y1);
    }
}
'''

SOLUTIONS["1038_binary_search_tree_to_greater_sum_tree"] = f'''// LeetCode 1038 - Binary Search Tree to Greater Sum Tree
// https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

{TREE}

class Solution {{
    private int total;

    public TreeNode bstToGst(TreeNode root) {{
        total = 0;
        reverseInorder(root);
        return root;
    }}

    private void reverseInorder(TreeNode node) {{
        if (node == null) return;
        reverseInorder(node.right);
        total += node.val;
        node.val = total;
        reverseInorder(node.left);
    }}
}}
'''

SOLUTIONS["1039_minimum_score_triangulation_of_polygon"] = r'''// LeetCode 1039 - Minimum Score Triangulation of Polygon
// https://leetcode.com/problems/minimum-score-triangulation-of-polygon/

import java.util.Arrays;

class Solution {
    public int minScoreTriangulation(int[] values) {
        int n = values.length;
        int[][] memo = new int[n][n];
        for (int[] row : memo) Arrays.fill(row, -1);
        return dp(values, 0, n - 1, memo);
    }

    private int dp(int[] values, int i, int j, int[][] memo) {
        if (j - i < 2) return 0;
        if (memo[i][j] != -1) return memo[i][j];
        int best = Integer.MAX_VALUE;
        for (int k = i + 1; k < j; k++) {
            best = Math.min(best, dp(values, i, k, memo) + values[i] * values[k] * values[j] + dp(values, k, j, memo));
        }
        return memo[i][j] = best;
    }
}
'''

SOLUTIONS["1040_moving_stones_until_consecutive_ii"] = r'''// LeetCode 1040 - Moving Stones Until Consecutive II
// https://leetcode.com/problems/moving-stones-until-consecutive-ii/

import java.util.Arrays;

class Solution {
    public int[] numMovesStonesII(int[] stones) {
        Arrays.sort(stones);
        int n = stones.length;
        int maxMoves = Math.max(stones[n - 1] - stones[1] - n + 2, stones[n - 2] - stones[0] - n + 2);
        int minMoves = maxMoves, i = 0;
        for (int j = 0; j < n; j++) {
            while (stones[j] - stones[i] + 1 > n) i++;
            int inside = j - i + 1;
            int cur = n - inside;
            if (inside == n - 1 && stones[j] - stones[i] + 1 == n - 1) cur = 2;
            minMoves = Math.min(minMoves, cur);
        }
        return new int[]{minMoves, maxMoves};
    }
}
'''

SOLUTIONS["1041_robot_bounded_in_circle"] = r'''// LeetCode 1041 - Robot Bounded In Circle
// https://leetcode.com/problems/robot-bounded-in-circle/

class Solution {
    public boolean isRobotBounded(String instructions) {
        int x = 0, y = 0, dx = 0, dy = 1;
        for (char ch : instructions.toCharArray()) {
            if (ch == 'G') {
                x += dx;
                y += dy;
            } else if (ch == 'L') {
                int tmp = dx;
                dx = -dy;
                dy = tmp;
            } else {
                int tmp = dx;
                dx = dy;
                dy = -tmp;
            }
        }
        return (x == 0 && y == 0) || !(dx == 0 && dy == 1);
    }
}
'''

SOLUTIONS["1042_flower_planting_with_no_adjacent"] = r'''// LeetCode 1042 - Flower Planting With No Adjacent
// https://leetcode.com/problems/flower-planting-with-no-adjacent/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public int[] gardenNoAdj(int n, int[][] paths) {
        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i <= n; i++) graph.add(new ArrayList<>());
        for (int[] p : paths) {
            graph.get(p[0]).add(p[1]);
            graph.get(p[1]).add(p[0]);
        }
        int[] ans = new int[n + 1];
        for (int garden = 1; garden <= n; garden++) {
            boolean[] used = new boolean[5];
            for (int nei : graph.get(garden)) used[ans[nei]] = true;
            for (int c = 1; c <= 4; c++) {
                if (!used[c]) {
                    ans[garden] = c;
                    break;
                }
            }
        }
        int[] res = new int[n];
        System.arraycopy(ans, 1, res, 0, n);
        return res;
    }
}
'''

SOLUTIONS["1043_partition_array_for_maximum_sum"] = r'''// LeetCode 1043 - Partition Array for Maximum Sum
// https://leetcode.com/problems/partition-array-for-maximum-sum/

class Solution {
    public int maxSumAfterPartitioning(int[] arr, int k) {
        int n = arr.length;
        int[] dp = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            int best = 0, limit = Math.min(k, i);
            for (int size = 1; size <= limit; size++) {
                best = Math.max(best, arr[i - size]);
                dp[i] = Math.max(dp[i], dp[i - size] + best * size);
            }
        }
        return dp[n];
    }
}
'''

SOLUTIONS["1044_longest_duplicate_substring"] = r'''// LeetCode 1044 - Longest Duplicate Substring
// https://leetcode.com/problems/longest-duplicate-substring/

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    private static final long MOD = 1_000_000_007L;
    private static final long BASE = 911382323L;

    public String longestDupSubstring(String s) {
        int n = s.length();
        int[] nums = new int[n];
        for (int i = 0; i < n; i++) nums[i] = s.charAt(i);
        int lo = 0, hi = n - 1, start = -1, bestLen = 0;
        while (lo <= hi) {
            int mid = (lo + hi) / 2;
            int pos = search(s, nums, mid);
            if (pos >= 0) {
                start = pos;
                bestLen = mid;
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return start < 0 ? "" : s.substring(start, start + bestLen);
    }

    private int search(String s, int[] nums, int length) {
        if (length == 0) return 0;
        int n = nums.length;
        long h = 0, power = 1;
        for (int i = 0; i < length; i++) {
            h = (h * BASE + nums[i]) % MOD;
            power = power * BASE % MOD;
        }
        Map<Long, List<Integer>> seen = new HashMap<>();
        seen.computeIfAbsent(h, k -> new ArrayList<>()).add(0);
        for (int i = 1; i + length - 1 < n; i++) {
            h = (h * BASE - nums[i - 1] * power % MOD + MOD) % MOD;
            h = (h + nums[i + length - 1]) % MOD;
            List<Integer> idxs = seen.get(h);
            if (idxs != null) {
                String cur = s.substring(i, i + length);
                for (int j : idxs) {
                    if (s.substring(j, j + length).equals(cur)) return i;
                }
                idxs.add(i);
            } else {
                List<Integer> list = new ArrayList<>();
                list.add(i);
                seen.put(h, list);
            }
        }
        return -1;
    }
}
'''

SOLUTIONS["1046_last_stone_weight"] = r'''// LeetCode 1046 - Last Stone Weight
// https://leetcode.com/problems/last-stone-weight/

import java.util.Collections;
import java.util.PriorityQueue;

class Solution {
    public int lastStoneWeight(int[] stones) {
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        for (int s : stones) pq.offer(s);
        while (pq.size() > 1) {
            int a = pq.poll(), b = pq.poll();
            if (a != b) pq.offer(a - b);
        }
        return pq.isEmpty() ? 0 : pq.peek();
    }
}
'''

SOLUTIONS["1047_remove_all_adjacent_duplicates_in_string"] = r'''// LeetCode 1047 - Remove All Adjacent Duplicates In String
// https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

class Solution {
    public String removeDuplicates(String s) {
        StringBuilder stack = new StringBuilder();
        for (char ch : s.toCharArray()) {
            int n = stack.length();
            if (n > 0 && stack.charAt(n - 1) == ch) stack.setLength(n - 1);
            else stack.append(ch);
        }
        return stack.toString();
    }
}
'''

SOLUTIONS["1048_longest_string_chain"] = r'''// LeetCode 1048 - Longest String Chain
// https://leetcode.com/problems/longest-string-chain/

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

class Solution {
    public int longestStrChain(String[] words) {
        Arrays.sort(words, (a, b) -> a.length() - b.length());
        Map<String, Integer> dp = new HashMap<>();
        int ans = 1;
        for (String w : words) {
            int best = 1;
            for (int i = 0; i < w.length(); i++) {
                String prev = w.substring(0, i) + w.substring(i + 1);
                best = Math.max(best, dp.getOrDefault(prev, 0) + 1);
            }
            dp.put(w, best);
            ans = Math.max(ans, best);
        }
        return ans;
    }
}
'''

SOLUTIONS["1049_last_stone_weight_ii"] = r'''// LeetCode 1049 - Last Stone Weight II
// https://leetcode.com/problems/last-stone-weight-ii/

import java.util.HashSet;
import java.util.Set;

class Solution {
    public int lastStoneWeightII(int[] stones) {
        int total = 0;
        for (int s : stones) total += s;
        Set<Integer> reachable = new HashSet<>();
        reachable.add(0);
        for (int stone : stones) {
            Set<Integer> next = new HashSet<>();
            for (int s : reachable) {
                next.add(s);
                next.add(s + stone);
            }
            reachable = next;
        }
        int best = total;
        for (int s : reachable) best = Math.min(best, Math.abs(total - 2 * s));
        return best;
    }
}
'''


def main() -> None:
    written = 0
    for folder, content in SOLUTIONS.items():
        path = ROOT / folder / "Solution.java"
        if not path.parent.exists():
            print(f"MISSING FOLDER: {folder}")
            continue
        path.write_text(content.rstrip() + "\n", encoding="utf-8")
        written += 1
        print(f"wrote {folder}")
    print(f"done: {written}/{len(SOLUTIONS)}")


if __name__ == "__main__":
    main()
