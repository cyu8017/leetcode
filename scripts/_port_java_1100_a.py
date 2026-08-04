#!/usr/bin/env python3
"""Port Java solutions for folders 1100-1299. Writes solution.java from embedded ports."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

SOLUTIONS: dict[str, str] = {}

SOLUTIONS["1124_longest_well_performing_interval"] = r"""// LeetCode 1124 - Longest Well-Performing Interval
// https://leetcode.com/problems/longest-well-performing-interval/

import java.util.*;

class Solution {
    public int longestWPI(int[] hours) {
        int score = 0, ans = 0;
        Map<Integer, Integer> firstSeen = new HashMap<>();
        firstSeen.put(0, -1);
        for (int i = 0; i < hours.length; i++) {
            score += hours[i] > 8 ? 1 : -1;
            if (score > 0) ans = i + 1;
            else if (firstSeen.containsKey(score - 1)) {
                ans = Math.max(ans, i - firstSeen.get(score - 1));
            }
            firstSeen.putIfAbsent(score, i);
        }
        return ans;
    }
}
"""

SOLUTIONS["1125_smallest_sufficient_team"] = r"""// LeetCode 1125 - Smallest Sufficient Team
// https://leetcode.com/problems/smallest-sufficient-team/

import java.util.*;

class Solution {
    public int[] smallestSufficientTeam(String[] req_skills, List<List<String>> people) {
        Map<String, Integer> skillId = new HashMap<>();
        for (int i = 0; i < req_skills.length; i++) skillId.put(req_skills[i], i);
        int[] personMasks = new int[people.size()];
        for (int i = 0; i < people.size(); i++) {
            int mask = 0;
            for (String skill : people.get(i)) mask |= 1 << skillId.get(skill);
            personMasks[i] = mask;
        }
        int target = (1 << req_skills.length) - 1;
        int n = people.size();
        int[] dp = new int[1 << req_skills.length];
        Arrays.fill(dp, (1 << n) - 1);
        dp[0] = 0;
        for (int state = 0; state < dp.length; state++) {
            if (dp[state] == (1 << n) - 1 && state != 0) continue;
            for (int i = 0; i < n; i++) {
                int next = state | personMasks[i];
                if (Integer.bitCount(dp[next]) > Integer.bitCount(dp[state]) + 1) {
                    dp[next] = dp[state] | (1 << i);
                }
            }
        }
        int teamMask = dp[target];
        List<Integer> team = new ArrayList<>();
        for (int i = 0; i < n; i++) if (((teamMask >> i) & 1) == 1) team.add(i);
        int[] ans = new int[team.size()];
        for (int i = 0; i < team.size(); i++) ans[i] = team.get(i);
        return ans;
    }
}
"""

SOLUTIONS["1128_number_of_equivalent_domino_pairs"] = r"""// LeetCode 1128 - Number of Equivalent Domino Pairs
// https://leetcode.com/problems/number-of-equivalent-domino-pairs/

import java.util.*;

class Solution {
    public int numEquivDominoPairs(int[][] dominoes) {
        Map<Integer, Integer> count = new HashMap<>();
        int ans = 0;
        for (int[] d : dominoes) {
            int a = Math.min(d[0], d[1]), b = Math.max(d[0], d[1]);
            int key = a * 10 + b;
            int c = count.getOrDefault(key, 0);
            ans += c;
            count.put(key, c + 1);
        }
        return ans;
    }
}
"""

SOLUTIONS["1129_shortest_path_with_alternating_colors"] = r"""// LeetCode 1129 - Shortest Path with Alternating Colors
// https://leetcode.com/problems/shortest-path-with-alternating-colors/

import java.util.*;

class Solution {
    public int[] shortestAlternatingPaths(int n, int[][] redEdges, int[][] blueEdges) {
        List<Integer>[][] graph = new List[2][n];
        for (int c = 0; c < 2; c++) for (int i = 0; i < n; i++) graph[c][i] = new ArrayList<>();
        for (int[] e : redEdges) graph[0][e[0]].add(e[1]);
        for (int[] e : blueEdges) graph[1][e[0]].add(e[1]);
        int[] ans = new int[n];
        Arrays.fill(ans, -1);
        Queue<int[]> queue = new ArrayDeque<>();
        boolean[][] seen = new boolean[n][2];
        queue.offer(new int[]{0, 0, 0});
        queue.offer(new int[]{0, 1, 0});
        seen[0][0] = seen[0][1] = true;
        while (!queue.isEmpty()) {
            int[] cur = queue.poll();
            int node = cur[0], color = cur[1], dist = cur[2];
            if (ans[node] == -1) ans[node] = dist;
            int nextColor = 1 - color;
            for (int nxt : graph[color][node]) {
                if (!seen[nxt][nextColor]) {
                    seen[nxt][nextColor] = true;
                    queue.offer(new int[]{nxt, nextColor, dist + 1});
                }
            }
        }
        return ans;
    }
}
"""

SOLUTIONS["1130_minimum_cost_tree_from_leaf_values"] = r"""// LeetCode 1130 - Minimum Cost Tree From Leaf Values
// https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/

import java.util.*;

class Solution {
    public int mctFromLeafValues(int[] arr) {
        Deque<Integer> stack = new ArrayDeque<>();
        stack.push(Integer.MAX_VALUE);
        int ans = 0;
        for (int x : arr) {
            while (stack.peek() <= x) {
                int mid = stack.pop();
                ans += mid * Math.min(stack.peek(), x);
            }
            stack.push(x);
        }
        while (stack.size() > 2) {
            ans += stack.pop() * stack.peek();
        }
        return ans;
    }
}
"""

SOLUTIONS["1131_maximum_of_absolute_value_expression"] = r"""// LeetCode 1131 - Maximum of Absolute Value Expression
// https://leetcode.com/problems/maximum-of-absolute-value-expression/

class Solution {
    public int maxAbsValExpr(int[] arr1, int[] arr2) {
        int n = arr1.length, ans = 0;
        int[][] signs = {{1, 1}, {1, -1}, {-1, 1}, {-1, -1}};
        for (int[] s : signs) {
            int best = s[0] * arr1[0] + s[1] * arr2[0];
            for (int i = 1; i < n; i++) {
                int cur = s[0] * arr1[i] + s[1] * arr2[i] + i;
                ans = Math.max(ans, cur - best);
                best = Math.min(best, s[0] * arr1[i] + s[1] * arr2[i] + i);
            }
        }
        return ans;
    }
}
"""

SOLUTIONS["1133_largest_unique_number"] = r"""// LeetCode 1133 - Largest Unique Number
// https://leetcode.com/problems/largest-unique-number/

import java.util.*;

class Solution {
    public int largestUniqueNumber(int[] nums) {
        Map<Integer, Integer> count = new HashMap<>();
        for (int x : nums) count.merge(x, 1, Integer::sum);
        int ans = -1;
        for (Map.Entry<Integer, Integer> e : count.entrySet()) {
            if (e.getValue() == 1) ans = Math.max(ans, e.getKey());
        }
        return ans;
    }
}
"""

SOLUTIONS["1134_armstrong_number"] = r"""// LeetCode 1134 - Armstrong Number
// https://leetcode.com/problems/armstrong-number/

class Solution {
    public boolean isArmstrong(int n) {
        String digits = String.valueOf(n);
        int power = digits.length(), sum = 0;
        for (char d : digits.toCharArray()) {
            sum += (int) Math.pow(d - '0', power);
        }
        return n == sum;
    }
}
"""

SOLUTIONS["1135_connecting_cities_with_minimum_cost"] = r"""// LeetCode 1135 - Connecting Cities With Minimum Cost
// https://leetcode.com/problems/connecting-cities-with-minimum-cost/

import java.util.*;

class Solution {
    public int minimumCost(int n, int[][] connections) {
        int[] parent = new int[n + 1];
        for (int i = 0; i <= n; i++) parent[i] = i;
        Arrays.sort(connections, (a, b) -> Integer.compare(a[2], b[2]));
        int cost = 0, edges = 0;
        for (int[] e : connections) {
            if (union(parent, e[0], e[1])) {
                cost += e[2];
                edges++;
                if (edges == n - 1) return cost;
            }
        }
        return -1;
    }

    private int find(int[] parent, int x) {
        while (parent[x] != x) {
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    }

    private boolean union(int[] parent, int a, int b) {
        int ra = find(parent, a), rb = find(parent, b);
        if (ra == rb) return false;
        parent[rb] = ra;
        return true;
    }
}
"""


def main() -> None:
    written = 0
    for name, content in SOLUTIONS.items():
        path = ROOT / name / "solution.java"
        path.write_text(content.lstrip("\n") if False else content, encoding="utf-8", newline="\n")
        written += 1
        print(f"wrote {name}")
    print(f"done written={written}")


if __name__ == "__main__":
    main()
