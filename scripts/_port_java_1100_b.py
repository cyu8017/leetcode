#!/usr/bin/env python3
"""Port Java solutions batch B (1136-1165 area)."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOLUTIONS: dict[str, str] = {}

SOLUTIONS["1136_parallel_courses"] = r"""// LeetCode 1136 - Parallel Courses
// https://leetcode.com/problems/parallel-courses/

import java.util.*;

class Solution {
    public int minimumSemesters(int n, int[][] relations) {
        List<Integer>[] graph = new List[n + 1];
        for (int i = 1; i <= n; i++) graph[i] = new ArrayList<>();
        int[] indegree = new int[n + 1];
        for (int[] e : relations) {
            graph[e[0]].add(e[1]);
            indegree[e[1]]++;
        }
        Queue<Integer> queue = new ArrayDeque<>();
        for (int i = 1; i <= n; i++) if (indegree[i] == 0) queue.offer(i);
        int semesters = 0, taken = 0;
        while (!queue.isEmpty()) {
            semesters++;
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                int course = queue.poll();
                taken++;
                for (int nxt : graph[course]) {
                    if (--indegree[nxt] == 0) queue.offer(nxt);
                }
            }
        }
        return taken == n ? semesters : -1;
    }
}
"""

SOLUTIONS["1137_n_th_tribonacci_number"] = r"""// LeetCode 1137 - N-th Tribonacci Number
// https://leetcode.com/problems/n-th-tribonacci-number/

class Solution {
    public int tribonacci(int n) {
        if (n == 0) return 0;
        if (n <= 2) return 1;
        int a = 0, b = 1, c = 1;
        for (int i = 3; i <= n; i++) {
            int next = a + b + c;
            a = b; b = c; c = next;
        }
        return c;
    }
}
"""

SOLUTIONS["1138_alphabet_board_path"] = r"""// LeetCode 1138 - Alphabet Board Path
// https://leetcode.com/problems/alphabet-board-path/

class Solution {
    public String alphabetBoardPath(String target) {
        int row = 0, col = 0;
        StringBuilder ans = new StringBuilder();
        for (char ch : target.toCharArray()) {
            int r = (ch - 'a') / 5, c = (ch - 'a') % 5;
            // Move U/L before D/R to avoid falling off 'z'
            while (row > r) { ans.append('U'); row--; }
            while (col > c) { ans.append('L'); col--; }
            while (row < r) { ans.append('D'); row++; }
            while (col < c) { ans.append('R'); col++; }
            ans.append('!');
        }
        return ans.toString();
    }
}
"""

SOLUTIONS["1139_largest_1_bordered_square"] = r"""// LeetCode 1139 - Largest 1-Bordered Square
// https://leetcode.com/problems/largest-1-bordered-square/

class Solution {
    public int largest1BorderedSquare(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        int[][] left = new int[m][n], up = new int[m][n];
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (grid[r][c] == 1) {
                    left[r][c] = 1 + (c > 0 ? left[r][c - 1] : 0);
                    up[r][c] = 1 + (r > 0 ? up[r - 1][c] : 0);
                }
            }
        }
        int best = 0;
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (grid[r][c] == 0) continue;
                int limit = Math.min(left[r][c], up[r][c]);
                for (int size = limit; size > 0; size--) {
                    if (left[r - size + 1][c] >= size && up[r][c - size + 1] >= size) {
                        best = Math.max(best, size);
                        break;
                    }
                }
            }
        }
        return best * best;
    }
}
"""

SOLUTIONS["1140_stone_game_ii"] = r"""// LeetCode 1140 - Stone Game II
// https://leetcode.com/problems/stone-game-ii/

class Solution {
    public int stoneGameII(int[] piles) {
        int n = piles.length;
        int[] suffix = new int[n + 1];
        for (int i = n - 1; i >= 0; i--) suffix[i] = suffix[i + 1] + piles[i];
        int[][] memo = new int[n][n + 1];
        for (int[] row : memo) java.util.Arrays.fill(row, -1);
        return dfs(0, 1, piles, suffix, memo);
    }

    private int dfs(int i, int m, int[] piles, int[] suffix, int[][] memo) {
        int n = piles.length;
        if (i >= n) return 0;
        if (i + m >= n) return suffix[i];
        if (memo[i][m] != -1) return memo[i][m];
        int bestOpp = Integer.MAX_VALUE;
        for (int x = 1; x <= Math.min(2 * m, n - i); x++) {
            bestOpp = Math.min(bestOpp, dfs(i + x, Math.max(x, m), piles, suffix, memo));
        }
        return memo[i][m] = suffix[i] - bestOpp;
    }
}
"""

SOLUTIONS["1143_longest_common_subsequence"] = r"""// LeetCode 1143 - Longest Common Subsequence
// https://leetcode.com/problems/longest-common-subsequence/

class Solution {
    public int longestCommonSubsequence(String text1, String text2) {
        int m = text1.length(), n = text2.length();
        int[] dp = new int[n + 1];
        for (int i = 1; i <= m; i++) {
            int prev = 0;
            for (int j = 1; j <= n; j++) {
                int cur = dp[j];
                if (text1.charAt(i - 1) == text2.charAt(j - 1)) dp[j] = prev + 1;
                else dp[j] = Math.max(dp[j], dp[j - 1]);
                prev = cur;
            }
        }
        return dp[n];
    }
}
"""

SOLUTIONS["1144_decrease_elements_to_make_array_zigzag"] = r"""// LeetCode 1144 - Decrease Elements To Make Array Zigzag
// https://leetcode.com/problems/decrease-elements-to-make-array-zigzag/

class Solution {
    public int movesToMakeZigzag(int[] nums) {
        return Math.min(cost(nums, 0), cost(nums, 1));
    }

    private int cost(int[] nums, int start) {
        int ans = 0;
        for (int i = start; i < nums.length; i += 2) {
            int left = i > 0 ? nums[i - 1] : Integer.MAX_VALUE;
            int right = i + 1 < nums.length ? nums[i + 1] : Integer.MAX_VALUE;
            ans += Math.max(0, nums[i] - Math.min(left, right) + 1);
        }
        return ans;
    }
}
"""

SOLUTIONS["1145_binary_tree_coloring_game"] = r"""// LeetCode 1145 - Binary Tree Coloring Game
// https://leetcode.com/problems/binary-tree-coloring-game/

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

class Solution {
    private int left, right;

    public boolean btreeGameWinningMove(TreeNode root, int n, int x) {
        left = right = 0;
        dfs(root, x);
        return Math.max(Math.max(left, right), n - left - right - 1) > n / 2;
    }

    private int dfs(TreeNode node, int x) {
        if (node == null) return 0;
        int l = dfs(node.left, x), r = dfs(node.right, x);
        if (node.val == x) { left = l; right = r; }
        return l + r + 1;
    }
}
"""

SOLUTIONS["1146_snapshot_array"] = r"""// LeetCode 1146 - Snapshot Array
// https://leetcode.com/problems/snapshot-array/

import java.util.*;

class SnapshotArray {
    private int snapId;
    private final List<int[]>[] data;

    public SnapshotArray(int length) {
        snapId = 0;
        data = new List[length];
        for (int i = 0; i < length; i++) {
            data[i] = new ArrayList<>();
            data[i].add(new int[]{0, 0});
        }
    }

    public void set(int index, int val) {
        List<int[]> hist = data[index];
        int[] last = hist.get(hist.size() - 1);
        if (last[0] == snapId) last[1] = val;
        else hist.add(new int[]{snapId, val});
    }

    public int snap() {
        return snapId++;
    }

    public int get(int index, int snap_id) {
        List<int[]> hist = data[index];
        int lo = 0, hi = hist.size() - 1, ans = 0;
        while (lo <= hi) {
            int mid = (lo + hi) / 2;
            if (hist.get(mid)[0] <= snap_id) {
                ans = mid;
                lo = mid + 1;
            } else hi = mid - 1;
        }
        return hist.get(ans)[1];
    }
}
"""

SOLUTIONS["1147_longest_chunked_palindrome_decomposition"] = r"""// LeetCode 1147 - Longest Chunked Palindrome Decomposition
// https://leetcode.com/problems/longest-chunked-palindrome-decomposition/

class Solution {
    public int longestDecomposition(String text) {
        int n = text.length(), ans = 0, i = 0;
        while (i < n - i) {
            boolean found = false;
            for (int length = 1; length <= (n - 2 * i) / 2; length++) {
                if (text.substring(i, i + length).equals(text.substring(n - i - length, n - i))) {
                    ans += 2;
                    i += length;
                    found = true;
                    break;
                }
            }
            if (!found) {
                ans++;
                break;
            }
        }
        return ans;
    }
}
"""


def main() -> None:
    for name, content in SOLUTIONS.items():
        (ROOT / name / "solution.java").write_text(content, encoding="utf-8", newline="\n")
        print("wrote", name)
    print("done", len(SOLUTIONS))


if __name__ == "__main__":
    main()
