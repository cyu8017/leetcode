#!/usr/bin/env python3
"""Port Java batch D: 1162-1190."""
from __future__ import annotations
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
S: dict[str, str] = {}

S["1162_as_far_from_land_as_possible"] = r"""// LeetCode 1162 - As Far from Land as Possible
// https://leetcode.com/problems/as-far-from-land-as-possible/

import java.util.*;

class Solution {
    public int maxDistance(int[][] grid) {
        int n = grid.length;
        Queue<int[]> queue = new ArrayDeque<>();
        for (int r = 0; r < n; r++)
            for (int c = 0; c < n; c++)
                if (grid[r][c] == 1) queue.offer(new int[]{r, c});
        if (queue.isEmpty() || queue.size() == n * n) return -1;
        int dist = -1;
        int[][] dirs = {{1,0},{-1,0},{0,1},{0,-1}};
        while (!queue.isEmpty()) {
            dist++;
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                int[] cur = queue.poll();
                for (int[] d : dirs) {
                    int nr = cur[0] + d[0], nc = cur[1] + d[1];
                    if (nr >= 0 && nr < n && nc >= 0 && nc < n && grid[nr][nc] == 0) {
                        grid[nr][nc] = 1;
                        queue.offer(new int[]{nr, nc});
                    }
                }
            }
        }
        return dist;
    }
}
"""

S["1163_last_substring_in_lexicographical_order"] = r"""// LeetCode 1163 - Last Substring in Lexicographical Order
// https://leetcode.com/problems/last-substring-in-lexicographical-order/

class Solution {
    public String lastSubstring(String s) {
        int i = 0, j = 1, k = 0, n = s.length();
        while (j + k < n) {
            if (s.charAt(i + k) == s.charAt(j + k)) { k++; continue; }
            if (s.charAt(i + k) > s.charAt(j + k)) j = j + k + 1;
            else { i = Math.max(i + k + 1, j); j = i + 1; }
            k = 0;
        }
        return s.substring(i);
    }
}
"""

S["1165_single_row_keyboard"] = r"""// LeetCode 1165 - Single-Row Keyboard
// https://leetcode.com/problems/single-row-keyboard/

class Solution {
    public int calculateTime(String keyboard, String word) {
        int[] pos = new int[26];
        for (int i = 0; i < keyboard.length(); i++) pos[keyboard.charAt(i) - 'a'] = i;
        int ans = 0, prev = 0;
        for (char ch : word.toCharArray()) {
            ans += Math.abs(pos[ch - 'a'] - prev);
            prev = pos[ch - 'a'];
        }
        return ans;
    }
}
"""

S["1166_design_file_system"] = r"""// LeetCode 1166 - Design File System
// https://leetcode.com/problems/design-file-system/

import java.util.*;

class FileSystem {
    private final Map<String, Integer> paths = new HashMap<>();

    public FileSystem() {
        paths.put("", -1);
    }

    public boolean createPath(String path, int value) {
        if (paths.containsKey(path)) return false;
        int idx = path.lastIndexOf('/');
        String parent = path.substring(0, idx);
        if (!paths.containsKey(parent)) return false;
        paths.put(path, value);
        return true;
    }

    public int get(String path) {
        return paths.getOrDefault(path, -1);
    }
}
"""

S["1167_minimum_cost_to_connect_sticks"] = r"""// LeetCode 1167 - Minimum Cost to Connect Sticks
// https://leetcode.com/problems/minimum-cost-to-connect-sticks/

import java.util.*;

class Solution {
    public int connectSticks(int[] sticks) {
        if (sticks.length <= 1) return 0;
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for (int s : sticks) pq.offer(s);
        int ans = 0;
        while (pq.size() > 1) {
            int cost = pq.poll() + pq.poll();
            ans += cost;
            pq.offer(cost);
        }
        return ans;
    }
}
"""

S["1168_optimize_water_distribution_in_a_village"] = r"""// LeetCode 1168 - Optimize Water Distribution in a Village
// https://leetcode.com/problems/optimize-water-distribution-in-a-village/

import java.util.*;

class Solution {
    public int minCostToSupplyWater(int n, int[] wells, int[][] pipes) {
        int[] parent = new int[n + 1];
        for (int i = 0; i <= n; i++) parent[i] = i;
        List<int[]> edges = new ArrayList<>();
        for (int i = 0; i < wells.length; i++) edges.add(new int[]{0, i + 1, wells[i]});
        for (int[] p : pipes) edges.add(p);
        edges.sort((a, b) -> Integer.compare(a[2], b[2]));
        int ans = 0;
        for (int[] e : edges) {
            int ra = find(parent, e[0]), rb = find(parent, e[1]);
            if (ra == rb) continue;
            parent[rb] = ra;
            ans += e[2];
        }
        return ans;
    }
    private int find(int[] parent, int x) {
        while (parent[x] != x) { parent[x] = parent[parent[x]]; x = parent[x]; }
        return x;
    }
}
"""

S["1169_invalid_transactions"] = r"""// LeetCode 1169 - Invalid Transactions
// https://leetcode.com/problems/invalid-transactions/

import java.util.*;

class Solution {
    public List<String> invalidTransactions(String[] transactions) {
        int n = transactions.length;
        String[] name = new String[n];
        int[] time = new int[n], amount = new int[n];
        String[] city = new String[n];
        for (int i = 0; i < n; i++) {
            String[] p = transactions[i].split(",");
            name[i] = p[0]; time[i] = Integer.parseInt(p[1]);
            amount[i] = Integer.parseInt(p[2]); city[i] = p[3];
        }
        Set<String> invalid = new LinkedHashSet<>();
        for (int i = 0; i < n; i++) {
            if (amount[i] > 1000) invalid.add(transactions[i]);
            for (int j = 0; j < n; j++) {
                if (i != j && name[i].equals(name[j]) && !city[i].equals(city[j]) && Math.abs(time[i] - time[j]) <= 60) {
                    invalid.add(transactions[i]);
                    invalid.add(transactions[j]);
                }
            }
        }
        return new ArrayList<>(invalid);
    }
}
"""

S["1170_compare_strings_by_frequency_of_the_smallest_character"] = r"""// LeetCode 1170 - Compare Strings by Frequency of the Smallest Character
// https://leetcode.com/problems/compare-strings-by-frequency-of-the-smallest-character/

import java.util.*;

class Solution {
    public int[] numSmallerByFrequency(String[] queries, String[] words) {
        int[] freqs = new int[words.length];
        for (int i = 0; i < words.length; i++) freqs[i] = f(words[i]);
        Arrays.sort(freqs);
        int[] ans = new int[queries.length];
        for (int i = 0; i < queries.length; i++) {
            int fq = f(queries[i]);
            int lo = 0, hi = freqs.length;
            while (lo < hi) {
                int mid = (lo + hi) / 2;
                if (freqs[mid] <= fq) lo = mid + 1; else hi = mid;
            }
            ans[i] = freqs.length - lo;
        }
        return ans;
    }
    private int f(String s) {
        char min = 'z';
        for (char c : s.toCharArray()) if (c < min) min = c;
        int cnt = 0;
        for (char c : s.toCharArray()) if (c == min) cnt++;
        return cnt;
    }
}
"""

S["1171_remove_zero_sum_consecutive_nodes_from_linked_list"] = r"""// LeetCode 1171 - Remove Zero Sum Consecutive Nodes from Linked List
// https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/

import java.util.*;

class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

class Solution {
    public ListNode removeZeroSumSublists(ListNode head) {
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        Map<Integer, ListNode> seen = new HashMap<>();
        int prefix = 0;
        for (ListNode node = dummy; node != null; node = node.next) {
            prefix += node.val;
            seen.put(prefix, node);
        }
        prefix = 0;
        for (ListNode node = dummy; node != null; node = node.next) {
            prefix += node.val;
            node.next = seen.get(prefix).next;
        }
        return dummy.next;
    }
}
"""

S["1172_dinner_plate_stacks"] = r"""// LeetCode 1172 - Dinner Plate Stacks
// https://leetcode.com/problems/dinner-plate-stacks/

import java.util.*;

class DinnerPlates {
    private final int capacity;
    private final List<Deque<Integer>> stacks = new ArrayList<>();
    private final PriorityQueue<Integer> available = new PriorityQueue<>();

    public DinnerPlates(int capacity) {
        this.capacity = capacity;
    }

    public void push(int val) {
        while (!available.isEmpty() && (available.peek() >= stacks.size() || stacks.get(available.peek()).size() == capacity)) {
            available.poll();
        }
        if (available.isEmpty()) {
            stacks.add(new ArrayDeque<>());
            available.offer(stacks.size() - 1);
        }
        int idx = available.peek();
        stacks.get(idx).push(val);
        if (stacks.get(idx).size() == capacity) available.poll();
    }

    public int pop() {
        while (!stacks.isEmpty() && stacks.get(stacks.size() - 1).isEmpty()) stacks.remove(stacks.size() - 1);
        return stacks.isEmpty() ? -1 : popAtStack(stacks.size() - 1);
    }

    public int popAtStack(int index) {
        if (index < 0 || index >= stacks.size() || stacks.get(index).isEmpty()) return -1;
        if (stacks.get(index).size() == capacity) available.offer(index);
        return stacks.get(index).pop();
    }
}
"""

def main():
    for name, content in S.items():
        (ROOT / name / "solution.java").write_text(content, encoding="utf-8", newline="\n")
        print("wrote", name)
    print("done", len(S))

if __name__ == "__main__":
    main()
