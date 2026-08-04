#!/usr/bin/env python3
"""Write Java solutions for LeetCode 1261-1299 (non-SQL stubs)."""
from __future__ import annotations

import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SOLUTIONS: dict[str, str] = {
    "1261_find_elements_in_a_contaminated_binary_tree": """// LeetCode 1261 - Find Elements in a Contaminated Binary Tree
// https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree/

import java.util.*;

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

class FindElements {
    private final Set<Integer> values = new HashSet<>();

    public FindElements(TreeNode root) {
        recover(root, 0);
    }

    private void recover(TreeNode node, int value) {
        if (node == null) return;
        node.val = value;
        values.add(value);
        recover(node.left, 2 * value + 1);
        recover(node.right, 2 * value + 2);
    }

    public boolean find(int target) {
        return values.contains(target);
    }
}
""",
    "1262_greatest_sum_divisible_by_three": """// LeetCode 1262 - Greatest Sum Divisible by Three
// https://leetcode.com/problems/greatest-sum-divisible-by-three/

class Solution {
    public int maxSumDivThree(int[] nums) {
        long impossible = -1_000_000_000_000_000_000L;
        long[] dp = {0, impossible, impossible};
        for (int value : nums) {
            long[] old = dp.clone();
            for (int total = 0; total < 3; total++) {
                if (old[total] != impossible) {
                    int remainder = (int) ((old[total] + value) % 3);
                    dp[remainder] = Math.max(dp[remainder], old[total] + value);
                }
            }
        }
        return (int) dp[0];
    }
}
""",
    "1263_minimum_moves_to_move_a_box_to_their_target_location": """// LeetCode 1263 - Minimum Moves to Move a Box to Their Target Location
// https://leetcode.com/problems/minimum-moves-to-move-a-box-to-their-target-location/

import java.util.*;

class Solution {
    public int minPushBox(char[][] grid) {
        int m = grid.length, n = grid[0].length;
        int[] box = null, player = null, target = null;
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (grid[r][c] == 'B') box = new int[] {r, c};
                else if (grid[r][c] == 'S') player = new int[] {r, c};
                else if (grid[r][c] == 'T') target = new int[] {r, c};
            }
        }

        int[][] dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        ArrayDeque<int[]> queue = new ArrayDeque<>();
        HashSet<Long> seen = new HashSet<>();
        queue.add(new int[] {box[0], box[1], player[0], player[1], 0});
        seen.add(stateKey(box[0], box[1], player[0], player[1], n));

        while (!queue.isEmpty()) {
            int[] cur = queue.poll();
            int br = cur[0], bc = cur[1], pr = cur[2], pc = cur[3], pushes = cur[4];
            if (br == target[0] && bc == target[1]) return pushes;
            Set<Integer> canReach = reachable(grid, m, n, pr, pc, br, bc);
            for (int[] d : dirs) {
                int sr = br - d[0], sc = bc - d[1];
                int nbr = br + d[0], nbc = bc + d[1];
                if (!canReach.contains(sr * n + sc)) continue;
                if (nbr < 0 || nbr >= m || nbc < 0 || nbc >= n || grid[nbr][nbc] == '#') continue;
                long key = stateKey(nbr, nbc, br, bc, n);
                if (seen.add(key)) queue.add(new int[] {nbr, nbc, br, bc, pushes + 1});
            }
        }
        return -1;
    }

    private long stateKey(int br, int bc, int pr, int pc, int n) {
        return ((long) br * n + bc) << 20 | (pr * n + pc);
    }

    private Set<Integer> reachable(char[][] grid, int m, int n, int pr, int pc, int br, int bc) {
        Set<Integer> seen = new HashSet<>();
        ArrayDeque<int[]> stack = new ArrayDeque<>();
        stack.push(new int[] {pr, pc});
        seen.add(pr * n + pc);
        int[][] dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        while (!stack.isEmpty()) {
            int[] cur = stack.pop();
            for (int[] d : dirs) {
                int nr = cur[0] + d[0], nc = cur[1] + d[1];
                int key = nr * n + nc;
                if (nr < 0 || nr >= m || nc < 0 || nc >= n || grid[nr][nc] == '#') continue;
                if (nr == br && nc == bc) continue;
                if (seen.add(key)) stack.push(new int[] {nr, nc});
            }
        }
        return seen;
    }
}
""",
    "1265_print_immutable_linked_list_in_reverse": """// LeetCode 1265 - Print Immutable Linked List in Reverse
// https://leetcode.com/problems/print-immutable-linked-list-in-reverse/

interface ImmutableListNode {
    void printValue();
    ImmutableListNode getNext();
}

class Solution {
    public void printLinkedListInReverse(ImmutableListNode head) {
        if (head == null) return;
        printLinkedListInReverse(head.getNext());
        head.printValue();
    }
}
""",
    "1266_minimum_time_visiting_all_points": """// LeetCode 1266 - Minimum Time Visiting All Points
// https://leetcode.com/problems/minimum-time-visiting-all-points/

class Solution {
    public int minTimeToVisitAllPoints(int[][] points) {
        int total = 0;
        for (int i = 1; i < points.length; i++) {
            total += Math.max(
                Math.abs(points[i][0] - points[i - 1][0]),
                Math.abs(points[i][1] - points[i - 1][1]));
        }
        return total;
    }
}
""",
    "1267_count_servers_that_communicate": """// LeetCode 1267 - Count Servers That Communicate
// https://leetcode.com/problems/count-servers-that-communicate/

class Solution {
    public int countServers(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        int[] rows = new int[m], cols = new int[n];
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

import java.util.*;

class Solution {
    public List<List<String>> suggestedProducts(String[] products, String searchWord) {
        Arrays.sort(products);
        List<List<String>> answer = new ArrayList<>();
        String prefix = "";
        for (char ch : searchWord.toCharArray()) {
            prefix += ch;
            int i = lowerBound(products, prefix);
            List<String> row = new ArrayList<>();
            for (int j = i; j < products.length && j < i + 3; j++) {
                if (products[j].startsWith(prefix)) row.add(products[j]);
                else break;
            }
            answer.add(row);
        }
        return answer;
    }

    private int lowerBound(String[] arr, String target) {
        int lo = 0, hi = arr.length;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (arr[mid].compareTo(target) < 0) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    }
}
""",
    "1269_number_of_ways_to_stay_in_the_same_place_after_some_steps": """// LeetCode 1269 - Number of Ways to Stay in the Same Place After Some Steps
// https://leetcode.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps/

class Solution {
    public int numWays(int steps, int arrLen) {
        int mod = 1_000_000_007;
        int width = Math.min(arrLen, steps / 2 + 1);
        int[] dp = new int[width];
        dp[0] = 1;
        for (int s = 0; s < steps; s++) {
            int[] next = new int[width];
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

import java.math.BigInteger;

class Solution {
    public String toHexspeak(String num) {
        BigInteger value = new BigInteger(num);
        String digits = "0123456789ABCDEF";
        StringBuilder out = new StringBuilder();
        while (value.signum() > 0) {
            int rem = value.mod(BigInteger.valueOf(16)).intValue();
            if (rem >= 2 && rem <= 9) return "ERROR";
            out.insert(0, digits.charAt(rem));
            value = value.divide(BigInteger.valueOf(16));
        }
        String result = out.length() == 0 ? "0" : out.toString();
        return result.replace('0', 'O').replace('1', 'I');
    }
}
""",
    "1272_remove_interval": """// LeetCode 1272 - Remove Interval
// https://leetcode.com/problems/remove-interval/

import java.util.*;

class Solution {
    public int[][] removeInterval(int[][] intervals, int[] toBeRemoved) {
        int left = toBeRemoved[0], right = toBeRemoved[1];
        List<int[]> answer = new ArrayList<>();
        for (int[] interval : intervals) {
            int start = interval[0], end = interval[1];
            if (end <= left || start >= right) {
                answer.add(new int[] {start, end});
            } else {
                if (start < left) answer.add(new int[] {start, left});
                if (end > right) answer.add(new int[] {right, end});
            }
        }
        return answer.toArray(new int[0][]);
    }
}
""",
    "1273_delete_tree_nodes": """// LeetCode 1273 - Delete Tree Nodes
// https://leetcode.com/problems/delete-tree-nodes/

import java.util.*;

class Solution {
    public int deleteTreeNodes(int nodes, int[] parent, int[] value) {
        List<Integer>[] children = new List[nodes];
        for (int i = 0; i < nodes; i++) children[i] = new ArrayList<>();
        for (int node = 1; node < nodes; node++) children[parent[node]].add(node);
        return dfs(0, children, value)[1];
    }

    private int[] dfs(int node, List<Integer>[] children, int[] value) {
        int total = value[node], count = 1;
        for (int child : children[node]) {
            int[] result = dfs(child, children, value);
            total += result[0];
            count += result[1];
        }
        return new int[] {total, total == 0 ? 0 : count};
    }
}
""",
    "1274_number_of_ships_in_a_rectangle": """// LeetCode 1274 - Number of Ships in a Rectangle
// https://leetcode.com/problems/number-of-ships-in-a-rectangle/

class Sea {
    public boolean hasShips(int[] topRight, int[] bottomLeft) {
        throw new UnsupportedOperationException();
    }
}

class Solution {
    public int countShips(Sea sea, int[] topRight, int[] bottomLeft) {
        int tx = topRight[0], ty = topRight[1];
        int bx = bottomLeft[0], by = bottomLeft[1];
        if (tx < bx || ty < by || !sea.hasShips(topRight, bottomLeft)) return 0;
        if (tx == bx && ty == by) return 1;
        int mx = (tx + bx) / 2, my = (ty + by) / 2;
        return countShips(sea, new int[] {mx, my}, bottomLeft)
            + countShips(sea, new int[] {tx, my}, new int[] {mx + 1, by})
            + countShips(sea, new int[] {mx, ty}, new int[] {bx, my + 1})
            + countShips(sea, topRight, new int[] {mx + 1, my + 1});
    }
}
""",
    "1275_find_winner_on_a_tic_tac_toe_game": """// LeetCode 1275 - Find Winner on a Tic Tac Toe Game
// https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/

import java.util.*;

class Solution {
    public String tictactoe(int[][] moves) {
        int[][] board = new int[3][3];
        for (int i = 0; i < moves.length; i++) {
            board[moves[i][0]][moves[i][1]] = i % 2 == 0 ? 1 : -1;
        }
        List<int[]> lines = new ArrayList<>();
        for (int i = 0; i < 3; i++) lines.add(board[i]);
        for (int c = 0; c < 3; c++) lines.add(new int[] {board[0][c], board[1][c], board[2][c]});
        lines.add(new int[] {board[0][0], board[1][1], board[2][2]});
        lines.add(new int[] {board[0][2], board[1][1], board[2][0]});
        for (int[] line : lines) {
            int sum = line[0] + line[1] + line[2];
            if (Math.abs(sum) == 3) return sum == 3 ? "A" : "B";
        }
        return moves.length == 9 ? "Draw" : "Pending";
    }
}
""",
    "1276_number_of_burgers_with_no_waste_of_ingredients": """// LeetCode 1276 - Number of Burgers with No Waste of Ingredients
// https://leetcode.com/problems/number-of-burgers-with-no-waste-of-ingredients/

class Solution {
    public int[] numOfBurgers(int tomatoSlices, int cheeseSlices) {
        if (tomatoSlices % 2 != 0) return new int[0];
        int jumbo = tomatoSlices / 2 - cheeseSlices;
        int small = cheeseSlices - jumbo;
        return jumbo >= 0 && small >= 0 ? new int[] {jumbo, small} : new int[0];
    }
}
""",
    "1277_count_square_submatrices_with_all_ones": """// LeetCode 1277 - Count Square Submatrices with All Ones
// https://leetcode.com/problems/count-square-submatrices-with-all-ones/

class Solution {
    public int countSquares(int[][] matrix) {
        int answer = 0;
        for (int r = 0; r < matrix.length; r++) {
            for (int c = 0; c < matrix[0].length; c++) {
                if (matrix[r][c] != 0 && r > 0 && c > 0) {
                    matrix[r][c] += Math.min(
                        matrix[r - 1][c],
                        Math.min(matrix[r][c - 1], matrix[r - 1][c - 1]));
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

class Solution {
    public int palindromePartition(String s, int k) {
        int n = s.length();
        int[][] cost = new int[n][n];
        for (int length = 2; length <= n; length++) {
            for (int i = 0; i <= n - length; i++) {
                int j = i + length - 1;
                cost[i][j] = (length > 2 ? cost[i + 1][j - 1] : 0) + (s.charAt(i) != s.charAt(j) ? 1 : 0);
            }
        }
        int inf = n + 1;
        int[][] dp = new int[k + 1][n + 1];
        for (int i = 0; i <= k; i++) {
            for (int j = 0; j <= n; j++) dp[i][j] = inf;
        }
        dp[0][0] = 0;
        for (int parts = 1; parts <= k; parts++) {
            for (int end = parts; end <= n; end++) {
                for (int start = parts - 1; start < end; start++) {
                    dp[parts][end] = Math.min(
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

class TrafficLight {
    private int greenRoad = 1;
    private final Object lock = new Object();

    public TrafficLight() {}

    public void carArrived(
            int carId,
            int roadId,
            int direction,
            Runnable turnGreen,
            Runnable crossCar) {
        synchronized (lock) {
            if (roadId != greenRoad) {
                turnGreen.run();
                greenRoad = roadId;
            }
            crossCar.run();
        }
    }
}
""",
    "1281_subtract_the_product_and_sum_of_digits_of_an_integer": """// LeetCode 1281 - Subtract the Product and Sum of Digits of an Integer
// https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/

class Solution {
    public int subtractProductAndSum(int n) {
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

import java.util.*;

class Solution {
    public List<List<Integer>> groupThePeople(int[] groupSizes) {
        Map<Integer, List<Integer>> pending = new HashMap<>();
        List<List<Integer>> answer = new ArrayList<>();
        for (int person = 0; person < groupSizes.length; person++) {
            int size = groupSizes[person];
            pending.computeIfAbsent(size, key -> new ArrayList<>()).add(person);
            if (pending.get(size).size() == size) {
                answer.add(pending.get(size));
                pending.put(size, new ArrayList<>());
            }
        }
        answer.sort(Comparator.comparingInt(List::size)
            .thenComparing(list -> list.toString()));
        return answer;
    }
}
""",
    "1283_find_the_smallest_divisor_given_a_threshold": """// LeetCode 1283 - Find the Smallest Divisor Given a Threshold
// https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/

class Solution {
    public int smallestDivisor(int[] nums, int threshold) {
        int lo = 1, hi = 0;
        for (int x : nums) hi = Math.max(hi, x);
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            long sum = 0;
            for (int x : nums) sum += (x + mid - 1) / mid;
            if (sum <= threshold) hi = mid;
            else lo = mid + 1;
        }
        return lo;
    }
}
""",
    "1284_minimum_number_of_flips_to_convert_binary_matrix_to_zero_matrix": """// LeetCode 1284 - Minimum Number of Flips to Convert Binary Matrix to Zero Matrix
// https://leetcode.com/problems/minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix/

import java.util.*;

class Solution {
    public int minFlips(int[][] mat) {
        int m = mat.length, n = mat[0].length;
        int start = 0;
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (mat[r][c] != 0) start |= 1 << (r * n + c);
            }
        }
        int[][] deltas = {{0, 0}, {1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        List<Integer> masks = new ArrayList<>();
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                int mask = 0;
                for (int[] d : deltas) {
                    int nr = r + d[0], nc = c + d[1];
                    if (nr >= 0 && nr < m && nc >= 0 && nc < n) mask ^= 1 << (nr * n + nc);
                }
                masks.add(mask);
            }
        }
        ArrayDeque<int[]> queue = new ArrayDeque<>();
        HashSet<Integer> seen = new HashSet<>();
        queue.add(new int[] {start, 0});
        seen.add(start);
        while (!queue.isEmpty()) {
            int[] cur = queue.poll();
            if (cur[0] == 0) return cur[1];
            for (int mask : masks) {
                int nxt = cur[0] ^ mask;
                if (seen.add(nxt)) queue.add(new int[] {nxt, cur[1] + 1});
            }
        }
        return -1;
    }
}
""",
    "1286_iterator_for_combination": """// LeetCode 1286 - Iterator for Combination
// https://leetcode.com/problems/iterator-for-combination/

import java.util.*;

class CombinationIterator {
    private final String[] items;
    private int index = 0;

    public CombinationIterator(String characters, int combinationLength) {
        List<String> built = new ArrayList<>();
        build(characters, combinationLength, 0, new char[combinationLength], 0, built);
        items = built.toArray(new String[0]);
    }

    public String next() {
        return items[index++];
    }

    public boolean hasNext() {
        return index < items.length;
    }

    private void build(String characters, int k, int start, char[] path, int depth, List<String> out) {
        if (depth == k) {
            out.add(new String(path));
            return;
        }
        for (int i = start; i < characters.length(); i++) {
            path[depth] = characters.charAt(i);
            build(characters, k, i + 1, path, depth + 1, out);
        }
    }
}
""",
    "1287_element_appearing_more_than_25_in_sorted_array": """// LeetCode 1287 - Element Appearing More Than 25% In Sorted Array
// https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/

class Solution {
    public int findSpecialInteger(int[] arr) {
        int n = arr.length;
        int threshold = n / 4;
        for (int idx : new int[] {n / 4, n / 2, 3 * n / 4}) {
            int value = arr[idx];
            int count = 0;
            for (int x : arr) if (x == value) count++;
            if (count > threshold) return value;
        }
        return arr[0];
    }
}
""",
    "1288_remove_covered_intervals": """// LeetCode 1288 - Remove Covered Intervals
// https://leetcode.com/problems/remove-covered-intervals/

import java.util.*;

class Solution {
    public int removeCoveredIntervals(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> a[0] != b[0] ? a[0] - b[0] : b[1] - a[1]);
        int answer = 0, farthest = -1;
        for (int[] interval : intervals) {
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

class Solution {
    public int minFallingPathSum(int[][] grid) {
        int[] dp = grid[0].clone();
        for (int rowIndex = 1; rowIndex < grid.length; rowIndex++) {
            int[] row = grid[rowIndex];
            int first = 0;
            for (int i = 1; i < dp.length; i++) {
                if (dp[i] < dp[first]) first = i;
            }
            int secondValue = Integer.MAX_VALUE;
            for (int i = 0; i < dp.length; i++) {
                if (i != first) secondValue = Math.min(secondValue, dp[i]);
            }
            if (dp.length == 1) secondValue = 0;
            int[] next = new int[dp.length];
            for (int i = 0; i < row.length; i++) {
                next[i] = row[i] + (i == first ? secondValue : dp[first]);
            }
            dp = next;
        }
        int best = dp[0];
        for (int value : dp) best = Math.min(best, value);
        return best;
    }
}
""",
    "1290_convert_binary_number_in_a_linked_list_to_integer": """// LeetCode 1290 - Convert Binary Number in a Linked List to Integer
// https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/

class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }
}

class Solution {
    public int getDecimalValue(ListNode head) {
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

import java.util.*;

class Solution {
    public List<Integer> sequentialDigits(int low, int high) {
        String digits = "123456789";
        List<Integer> answer = new ArrayList<>();
        for (int length = 2; length <= 9; length++) {
            for (int start = 0; start <= 9 - length; start++) {
                int value = Integer.parseInt(digits.substring(start, start + length));
                if (value >= low && value <= high) answer.add(value);
            }
        }
        return answer;
    }
}
""",
    "1292_maximum_side_length_of_a_square_with_sum_less_than_or_equal_to_threshold": """// LeetCode 1292 - Maximum Side Length of a Square with Sum Less than or Equal to Threshold
// https://leetcode.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/

class Solution {
    public int maxSideLength(int[][] mat, int threshold) {
        int m = mat.length, n = mat[0].length;
        int[][] prefix = new int[m + 1][n + 1];
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                prefix[r + 1][c + 1] = mat[r][c] + prefix[r][c + 1] + prefix[r + 1][c] - prefix[r][c];
            }
        }
        int lo = 0, hi = Math.min(m, n);
        while (lo < hi) {
            int mid = (lo + hi + 1) / 2;
            if (possible(prefix, m, n, mid, threshold)) lo = mid;
            else hi = mid - 1;
        }
        return lo;
    }

    private boolean possible(int[][] prefix, int m, int n, int size, int threshold) {
        for (int r = size; r <= m; r++) {
            for (int c = size; c <= n; c++) {
                int sum = prefix[r][c] - prefix[r - size][c] - prefix[r][c - size] + prefix[r - size][c - size];
                if (sum <= threshold) return true;
            }
        }
        return false;
    }
}
""",
    "1293_shortest_path_in_a_grid_with_obstacles_elimination": """// LeetCode 1293 - Shortest Path in a Grid with Obstacles Elimination
// https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/

import java.util.*;

class Solution {
    public int shortestPath(int[][] grid, int k) {
        int m = grid.length, n = grid[0].length;
        if (k >= m + n - 2) return m + n - 2;
        ArrayDeque<int[]> queue = new ArrayDeque<>();
        HashMap<Long, Integer> best = new HashMap<>();
        queue.add(new int[] {0, 0, k, 0});
        best.put(key(0, 0), k);
        int[][] dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        while (!queue.isEmpty()) {
            int[] cur = queue.poll();
            if (cur[0] == m - 1 && cur[1] == n - 1) return cur[3];
            for (int[] d : dirs) {
                int nr = cur[0] + d[0], nc = cur[1] + d[1];
                if (nr < 0 || nr >= m || nc < 0 || nc >= n) continue;
                int nxt = cur[2] - grid[nr][nc];
                if (nxt < 0) continue;
                long cell = key(nr, nc);
                if (best.containsKey(cell) && nxt <= best.get(cell)) continue;
                best.put(cell, nxt);
                queue.add(new int[] {nr, nc, nxt, cur[3] + 1});
            }
        }
        return -1;
    }

    private long key(int r, int c) {
        return ((long) r << 32) | (c & 0xffffffffL);
    }
}
""",
    "1295_find_numbers_with_even_number_of_digits": """// LeetCode 1295 - Find Numbers with Even Number of Digits
// https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

class Solution {
    public int findNumbers(int[] nums) {
        int count = 0;
        for (int value : nums) {
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

import java.util.*;

class Solution {
    public boolean isPossibleDivide(int[] nums, int k) {
        if (nums.length % k != 0) return false;
        TreeMap<Integer, Integer> counts = new TreeMap<>();
        for (int x : nums) counts.put(x, counts.getOrDefault(x, 0) + 1);
        while (!counts.isEmpty()) {
            int start = counts.firstKey();
            int amount = counts.get(start);
            if (amount == 0) {
                counts.remove(start);
                continue;
            }
            for (int value = start; value < start + k; value++) {
                if (!counts.containsKey(value) || counts.get(value) < amount) return false;
                counts.put(value, counts.get(value) - amount);
                if (counts.get(value) == 0) counts.remove(value);
            }
        }
        return true;
    }
}
""",
    "1297_maximum_number_of_occurrences_of_a_substring": """// LeetCode 1297 - Maximum Number of Occurrences of a Substring
// https://leetcode.com/problems/maximum-number-of-occurrences-of-a-substring/

import java.util.*;

class Solution {
    public int maxFreq(String s, int maxLetters, int minSize, int maxSize) {
        HashMap<String, Integer> counts = new HashMap<>();
        for (int i = 0; i + minSize <= s.length(); i++) {
            String sub = s.substring(i, i + minSize);
            HashSet<Character> seen = new HashSet<>();
            for (char ch : sub.toCharArray()) seen.add(ch);
            if (seen.size() <= maxLetters) {
                counts.put(sub, counts.getOrDefault(sub, 0) + 1);
            }
        }
        int best = 0;
        for (int freq : counts.values()) best = Math.max(best, freq);
        return best;
    }
}
""",
    "1298_maximum_candies_you_can_get_from_boxes": """// LeetCode 1298 - Maximum Candies You Can Get from Boxes
// https://leetcode.com/problems/maximum-candies-you-can-get-from-boxes/

import java.util.*;

class Solution {
    public int maxCandies(int[] status, int[] candies, int[][] keys, int[][] containedBoxes, int[] initialBoxes) {
        HashSet<Integer> owned = new HashSet<>();
        for (int box : initialBoxes) owned.add(box);
        HashSet<Integer> opened = new HashSet<>();
        ArrayDeque<Integer> queue = new ArrayDeque<>();
        for (int box : initialBoxes) {
            if (status[box] == 1) queue.add(box);
        }
        int total = 0;
        while (!queue.isEmpty()) {
            int box = queue.poll();
            if (opened.contains(box) || status[box] == 0) continue;
            opened.add(box);
            total += candies[box];
            for (int key : keys[box]) {
                status[key] = 1;
                if (owned.contains(key) && !opened.contains(key)) queue.add(key);
            }
            for (int child : containedBoxes[box]) {
                owned.add(child);
                if (status[child] == 1 && !opened.contains(child)) queue.add(child);
            }
        }
        return total;
    }
}
""",
    "1299_replace_elements_with_greatest_element_on_right_side": """// LeetCode 1299 - Replace Elements with Greatest Element on Right Side
// https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

class Solution {
    public int[] replaceElements(int[] arr) {
        int greatest = -1;
        for (int i = arr.length - 1; i >= 0; i--) {
            int current = arr[i];
            arr[i] = greatest;
            greatest = Math.max(greatest, current);
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
    return bool(re.search(r"void\s+solve\s*\(\s*\)\s*\{", content, re.IGNORECASE))


def main() -> None:
    written = []
    skipped_sql = []
    skipped_done = []
    for name, content in sorted(SOLUTIONS.items()):
        m = re.match(r"^(\d{4})_", name)
        if not m:
            continue
        num = int(m.group(1))
        if num < 1261 or num > 1299:
            continue
        folder = os.path.join(ROOT, name)
        if is_sql(folder):
            skipped_sql.append(name)
            continue
        out = os.path.join(folder, "Solution.java")
        if os.path.exists(out):
            existing = open(out, encoding="utf-8-sig").read()
            if not is_stub(existing):
                skipped_done.append(name)
                continue
        open(out, "w", encoding="utf-8", newline="\n").write(content)
        written.append(name)
    print(f"Wrote {len(written)} files")
    print(f"SQL skipped: {len(skipped_sql)}")
    print(f"Already implemented: {len(skipped_done)}")
    for n in written:
        print(n)


if __name__ == "__main__":
    main()
