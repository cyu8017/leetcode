#!/usr/bin/env python3
"""Port Java batch G: 1198-1210."""
from __future__ import annotations
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
S: dict[str, str] = {}

S["1198_find_smallest_common_element_in_all_rows"] = r"""// LeetCode 1198 - Find Smallest Common Element in All Rows
// https://leetcode.com/problems/find-smallest-common-element-in-all-rows/

import java.util.*;

class Solution {
    public int smallestCommonElement(int[][] mat) {
        Set<Integer> common = new HashSet<>();
        for (int x : mat[0]) common.add(x);
        for (int r = 1; r < mat.length; r++) {
            Set<Integer> row = new HashSet<>();
            for (int x : mat[r]) row.add(x);
            common.retainAll(row);
            if (common.isEmpty()) return -1;
        }
        int ans = Integer.MAX_VALUE;
        for (int x : common) ans = Math.min(ans, x);
        return ans;
    }
}
"""

S["1199_minimum_time_to_build_blocks"] = r"""// LeetCode 1199 - Minimum Time to Build Blocks
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
}
"""

S["1200_minimum_absolute_difference"] = r"""// LeetCode 1200 - Minimum Absolute Difference
// https://leetcode.com/problems/minimum-absolute-difference/

import java.util.*;

class Solution {
    public List<List<Integer>> minimumAbsDifference(int[] arr) {
        Arrays.sort(arr);
        int best = Integer.MAX_VALUE;
        for (int i = 0; i < arr.length - 1; i++) best = Math.min(best, arr[i + 1] - arr[i]);
        List<List<Integer>> ans = new ArrayList<>();
        for (int i = 0; i < arr.length - 1; i++) {
            if (arr[i + 1] - arr[i] == best) ans.add(Arrays.asList(arr[i], arr[i + 1]));
        }
        return ans;
    }
}
"""

S["1201_ugly_number_iii"] = r"""// LeetCode 1201 - Ugly Number III
// https://leetcode.com/problems/ugly-number-iii/

class Solution {
    public int nthUglyNumber(int n, int a, int b, int c) {
        long ab = lcm(a, b), ac = lcm(a, c), bc = lcm(b, c), abc = lcm(ab, c);
        long lo = 1, hi = 2_000_000_000L;
        while (lo < hi) {
            long mid = (lo + hi) / 2;
            if (count(mid, a, b, c, ab, ac, bc, abc) >= n) hi = mid;
            else lo = mid + 1;
        }
        return (int) lo;
    }
    private long count(long x, long a, long b, long c, long ab, long ac, long bc, long abc) {
        return x / a + x / b + x / c - x / ab - x / ac - x / bc + x / abc;
    }
    private long gcd(long x, long y) { return y == 0 ? x : gcd(y, x % y); }
    private long lcm(long x, long y) { return x / gcd(x, y) * y; }
}
"""

S["1202_smallest_string_with_swaps"] = r"""// LeetCode 1202 - Smallest String With Swaps
// https://leetcode.com/problems/smallest-string-with-swaps/

import java.util.*;

class Solution {
    public String smallestStringWithSwaps(String s, List<List<Integer>> pairs) {
        int n = s.length();
        int[] parent = new int[n];
        for (int i = 0; i < n; i++) parent[i] = i;
        for (List<Integer> p : pairs) {
            int ra = find(parent, p.get(0)), rb = find(parent, p.get(1));
            parent[ra] = rb;
        }
        Map<Integer, PriorityQueue<Character>> groups = new HashMap<>();
        for (int i = 0; i < n; i++) {
            groups.computeIfAbsent(find(parent, i), k -> new PriorityQueue<>()).offer(s.charAt(i));
        }
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) sb.append(groups.get(find(parent, i)).poll());
        return sb.toString();
    }
    private int find(int[] parent, int x) {
        while (parent[x] != x) { parent[x] = parent[parent[x]]; x = parent[x]; }
        return x;
    }
}
"""

S["1203_sort_items_by_groups_respecting_dependencies"] = r"""// LeetCode 1203 - Sort Items by Groups Respecting Dependencies
// https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/

import java.util.*;

class Solution {
    public int[] sortItems(int n, int m, int[] group, List<List<Integer>> beforeItems) {
        for (int i = 0; i < n; i++) {
            if (group[i] == -1) group[i] = m++;
        }
        List<Integer>[] itemGraph = new List[n];
        int[] itemIndeg = new int[n];
        for (int i = 0; i < n; i++) itemGraph[i] = new ArrayList<>();
        List<Integer>[] groupGraph = new List[m];
        int[] groupIndeg = new int[m];
        for (int i = 0; i < m; i++) groupGraph[i] = new ArrayList<>();
        Set<Long> seenGroupEdge = new HashSet<>();
        for (int v = 0; v < n; v++) {
            for (int u : beforeItems.get(v)) {
                itemGraph[u].add(v);
                itemIndeg[v]++;
                if (group[u] != group[v]) {
                    long key = ((long) group[u] << 32) | group[v];
                    if (seenGroupEdge.add(key)) {
                        groupGraph[group[u]].add(group[v]);
                        groupIndeg[group[v]]++;
                    }
                }
            }
        }
        List<Integer> items = topo(itemGraph, itemIndeg);
        List<Integer> groups = topo(groupGraph, groupIndeg);
        if (items.isEmpty() || groups.isEmpty()) return new int[0];
        List<Integer>[] buckets = new List[m];
        for (int i = 0; i < m; i++) buckets[i] = new ArrayList<>();
        for (int item : items) buckets[group[item]].add(item);
        List<Integer> ans = new ArrayList<>();
        for (int g : groups) ans.addAll(buckets[g]);
        int[] result = new int[ans.size()];
        for (int i = 0; i < ans.size(); i++) result[i] = ans.get(i);
        return result;
    }
    private List<Integer> topo(List<Integer>[] graph, int[] indeg) {
        Queue<Integer> q = new ArrayDeque<>();
        for (int i = 0; i < indeg.length; i++) if (indeg[i] == 0) q.offer(i);
        List<Integer> order = new ArrayList<>();
        while (!q.isEmpty()) {
            int u = q.poll();
            order.add(u);
            for (int v : graph[u]) if (--indeg[v] == 0) q.offer(v);
        }
        return order.size() == graph.length ? order : List.of();
    }
}
"""

S["1206_design_skiplist"] = r"""// LeetCode 1206 - Design Skiplist
// https://leetcode.com/problems/design-skiplist/

import java.util.*;

class Skiplist {
    private final List<Integer> values = new ArrayList<>();

    public Skiplist() {}

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
}
"""

S["1207_unique_number_of_occurrences"] = r"""// LeetCode 1207 - Unique Number of Occurrences
// https://leetcode.com/problems/unique-number-of-occurrences/

import java.util.*;

class Solution {
    public boolean uniqueOccurrences(int[] arr) {
        Map<Integer, Integer> count = new HashMap<>();
        for (int x : arr) count.merge(x, 1, Integer::sum);
        Set<Integer> seen = new HashSet<>();
        for (int c : count.values()) if (!seen.add(c)) return false;
        return true;
    }
}
"""

S["1208_get_equal_substrings_within_budget"] = r"""// LeetCode 1208 - Get Equal Substrings Within Budget
// https://leetcode.com/problems/get-equal-substrings-within-budget/

class Solution {
    public int equalSubstring(String s, String t, int maxCost) {
        int left = 0, cost = 0, answer = 0;
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
}
"""

S["1209_remove_all_adjacent_duplicates_in_string_ii"] = r"""// LeetCode 1209 - Remove All Adjacent Duplicates in String II
// https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/

import java.util.*;

class Solution {
    public String removeDuplicates(String s, int k) {
        Deque<int[]> stack = new ArrayDeque<>();
        for (char ch : s.toCharArray()) {
            if (!stack.isEmpty() && stack.peek()[0] == ch) stack.peek()[1]++;
            else stack.push(new int[]{ch, 1});
            if (stack.peek()[1] == k) stack.pop();
        }
        StringBuilder sb = new StringBuilder();
        List<int[]> list = new ArrayList<>(stack);
        Collections.reverse(list);
        for (int[] p : list) for (int i = 0; i < p[1]; i++) sb.append((char) p[0]);
        return sb.toString();
    }
}
"""

def main():
    for name, content in S.items():
        path = ROOT / name / "solution.java"
        cur = path.read_text(encoding="utf-8") if path.exists() else ""
        if "void solve()" in cur or len(cur.strip()) < 120:
            path.write_text(content, encoding="utf-8", newline="\n")
            print("wrote", name)
        else:
            print("skip", name)
    print("done", len(S))

if __name__ == "__main__":
    main()
