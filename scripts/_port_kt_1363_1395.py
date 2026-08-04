#!/usr/bin/env python3
"""Port Kotlin stubs for problems 1363-1395 (listed batch)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

SOLUTIONS: dict[str, str] = {}

SOLUTIONS["1363_largest_multiple_of_three"] = r"""// LeetCode 1363 - Largest Multiple of Three
// https://leetcode.com/problems/largest-multiple-of-three/

class Solution {
    fun largestMultipleOfThree(digits: IntArray): String {
        val cnt = IntArray(10)
        var rem = 0
        for (d in digits) {
            cnt[d]++
            rem += d
        }
        rem %= 3
        fun remove(r: Int, k0: Int): Boolean {
            var k = k0
            var d = r
            while (d < 10) {
                while (cnt[d] > 0 && k > 0) {
                    cnt[d]--
                    k--
                }
                if (k == 0) return true
                d += 3
            }
            return false
        }
        if (rem != 0 && !remove(rem, 1)) remove(3 - rem, 2)
        val sb = StringBuilder()
        for (d in 9 downTo 0) {
            repeat(cnt[d]) { sb.append(d) }
        }
        val s = sb.toString()
        return if (s.isNotEmpty() && s[0] == '0') "0" else s
    }
}
"""

SOLUTIONS["1365_how_many_numbers_are_smaller_than_the_current_number"] = r"""// LeetCode 1365 - How Many Numbers Are Smaller Than the Current Number
// https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

class Solution {
    fun smallerNumbersThanCurrent(nums: IntArray): IntArray {
        val sorted = nums.sorted()
        return IntArray(nums.size) { i -> sorted.indexOf(nums[i]) }
    }
}
"""

SOLUTIONS["1366_rank_teams_by_votes"] = r"""// LeetCode 1366 - Rank Teams by Votes
// https://leetcode.com/problems/rank-teams-by-votes/

class Solution {
    fun rankTeams(votes: Array<String>): String {
        val m = votes[0].length
        val count = mutableMapOf<Char, IntArray>()
        for (c in votes[0]) count[c] = IntArray(m)
        for (v in votes) {
            for (i in v.indices) count[v[i]]!![i]++
        }
        return count.keys.sortedWith(
            compareBy({ c: Char -> count[c]!!.map { -it } }, { c: Char -> c })
        ).joinToString("")
    }
}
"""

SOLUTIONS["1367_linked_list_in_binary_tree"] = r"""// LeetCode 1367 - Linked List in Binary Tree
// https://leetcode.com/problems/linked-list-in-binary-tree/

class ListNode(var `val`: Int) {
    var next: ListNode? = null
}

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun isSubPath(head: ListNode?, root: TreeNode?): Boolean {
        if (root == null) return false
        return match(head, root) || isSubPath(head, root.left) || isSubPath(head, root.right)
    }

    private fun match(a: ListNode?, b: TreeNode?): Boolean {
        if (a == null) return true
        if (b == null || a.`val` != b.`val`) return false
        return match(a.next, b.left) || match(a.next, b.right)
    }
}
"""

SOLUTIONS["1368_minimum_cost_to_make_at_least_one_valid_path_in_a_grid"] = r"""// LeetCode 1368 - Minimum Cost to Make at Least One Valid Path in a Grid
// https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/

class Solution {
    fun minCost(grid: Array<IntArray>): Int {
        val m = grid.size
        val n = grid[0].size
        val dist = Array(m) { IntArray(n) { 1_000_000_000 } }
        dist[0][0] = 0
        val dq = ArrayDeque<IntArray>()
        dq.add(intArrayOf(0, 0))
        val dirs = arrayOf(intArrayOf(0, 1), intArrayOf(0, -1), intArrayOf(1, 0), intArrayOf(-1, 0))
        while (dq.isNotEmpty()) {
            val cur = dq.removeFirst()
            val r = cur[0]
            val c = cur[1]
            for (k in dirs.indices) {
                val x = r + dirs[k][0]
                val y = c + dirs[k][1]
                if (x in 0 until m && y in 0 until n) {
                    val w = if (k + 1 != grid[r][c]) 1 else 0
                    val nd = dist[r][c] + w
                    if (nd < dist[x][y]) {
                        dist[x][y] = nd
                        if (w == 0) dq.addFirst(intArrayOf(x, y)) else dq.addLast(intArrayOf(x, y))
                    }
                }
            }
        }
        return dist[m - 1][n - 1]
    }
}
"""

SOLUTIONS["1370_increasing_decreasing_string"] = r"""// LeetCode 1370 - Increasing Decreasing String
// https://leetcode.com/problems/increasing-decreasing-string/

class Solution {
    fun sortString(s: String): String {
        val c = IntArray(26)
        for (ch in s) c[ch - 'a']++
        val out = StringBuilder()
        while (out.length < s.length) {
            for (i in 0 until 26) {
                if (c[i] > 0) {
                    out.append(('a' + i).toChar())
                    c[i]--
                }
            }
            for (i in 25 downTo 0) {
                if (c[i] > 0) {
                    out.append(('a' + i).toChar())
                    c[i]--
                }
            }
        }
        return out.toString()
    }
}
"""

SOLUTIONS["1371_find_the_longest_substring_containing_vowels_in_even_counts"] = r"""// LeetCode 1371 - Find the Longest Substring Containing Vowels in Even Counts
// https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/

class Solution {
    fun findTheLongestSubstring(s: String): Int {
        val first = mutableMapOf(0 to -1)
        var mask = 0
        var ans = 0
        val vowels = "aeiou"
        for (i in s.indices) {
            val idx = vowels.indexOf(s[i])
            if (idx >= 0) mask = mask xor (1 shl idx)
            if (mask in first) ans = maxOf(ans, i - first[mask]!!)
            else first[mask] = i
        }
        return ans
    }
}
"""

SOLUTIONS["1372_longest_zigzag_path_in_a_binary_tree"] = r"""// LeetCode 1372 - Longest ZigZag Path in a Binary Tree
// https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    private var ans = 0

    fun longestZigZag(root: TreeNode?): Int {
        ans = 0
        dfs(root)
        return ans
    }

    private fun dfs(node: TreeNode?): IntArray {
        if (node == null) return intArrayOf(-1, -1)
        val l = dfs(node.left)
        val r = dfs(node.right)
        val a = l[1] + 1
        val b = r[0] + 1
        ans = maxOf(ans, a, b)
        return intArrayOf(a, b)
    }
}
"""

SOLUTIONS["1373_maximum_sum_bst_in_binary_tree"] = r"""// LeetCode 1373 - Maximum Sum BST in Binary Tree
// https://leetcode.com/problems/maximum-sum-bst-in-binary-tree/

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    private var ans = 0

    fun maxSumBST(root: TreeNode?): Int {
        ans = 0
        dfs(root)
        return ans
    }

    // isBST, min, max, sum
    private fun dfs(node: TreeNode?): IntArray {
        if (node == null) return intArrayOf(1, Int.MAX_VALUE, Int.MIN_VALUE, 0)
        val left = dfs(node.left)
        val right = dfs(node.right)
        if (left[0] == 1 && right[0] == 1 && left[2] < node.`val` && node.`val` < right[1]) {
            val s = left[3] + right[3] + node.`val`
            ans = maxOf(ans, s)
            return intArrayOf(1, minOf(left[1], node.`val`), maxOf(right[2], node.`val`), s)
        }
        return intArrayOf(0, 0, 0, 0)
    }
}
"""

SOLUTIONS["1374_generate_a_string_with_characters_that_have_odd_counts"] = r"""// LeetCode 1374 - Generate a String With Characters That Have Odd Counts
// https://leetcode.com/problems/generate-a-string-with-characters-that-have-odd-counts/

class Solution {
    fun generateTheString(n: Int): String {
        return if (n % 2 == 1) "a".repeat(n) else "a".repeat(n - 1) + "b"
    }
}
"""

SOLUTIONS["1375_number_of_times_binary_string_is_prefix_aligned"] = r"""// LeetCode 1375 - Number of Times Binary String Is Prefix-Aligned
// https://leetcode.com/problems/number-of-times-binary-string-is-prefix-aligned/

class Solution {
    fun numTimesAllBlue(flips: IntArray): Int {
        var ans = 0
        var mx = 0
        for (i in flips.indices) {
            mx = maxOf(mx, flips[i])
            if (mx == i + 1) ans++
        }
        return ans
    }
}
"""

SOLUTIONS["1376_time_needed_to_inform_all_employees"] = r"""// LeetCode 1376 - Time Needed to Inform All Employees
// https://leetcode.com/problems/time-needed-to-inform-all-employees/

class Solution {
    fun numOfMinutes(n: Int, headID: Int, manager: IntArray, informTime: IntArray): Int {
        val children = Array(n) { mutableListOf<Int>() }
        for (i in manager.indices) {
            if (manager[i] != -1) children[manager[i]].add(i)
        }
        fun dfs(u: Int): Int {
            var best = 0
            for (v in children[u]) best = maxOf(best, dfs(v))
            return informTime[u] + best
        }
        return dfs(headID)
    }
}
"""

SOLUTIONS["1377_frog_position_after_t_seconds"] = r"""// LeetCode 1377 - Frog Position After T Seconds
// https://leetcode.com/problems/frog-position-after-t-seconds/

class Solution {
    fun frogPosition(n: Int, edges: Array<IntArray>, t: Int, target: Int): Double {
        val g = Array(n + 1) { mutableListOf<Int>() }
        for (e in edges) {
            g[e[0]].add(e[1])
            g[e[1]].add(e[0])
        }
        fun dfs(u: Int, p: Int, time: Int, prob: Double): Double {
            val kids = g[u].filter { it != p }
            if (time == t || kids.isEmpty()) return if (u == target) prob else 0.0
            var sum = 0.0
            for (v in kids) sum += dfs(v, u, time + 1, prob / kids.size)
            return sum
        }
        return dfs(1, 0, 0, 1.0)
    }
}
"""

SOLUTIONS["1379_find_a_corresponding_node_of_a_binary_tree_in_a_clone_of_that_tree"] = r"""// LeetCode 1379 - Find a Corresponding Node of a Binary Tree in a Clone of That Tree
// https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun getTargetCopy(original: TreeNode?, cloned: TreeNode?, target: TreeNode?): TreeNode? {
        if (original == null || cloned == null || target == null) return null
        val stack = ArrayDeque<Pair<TreeNode, TreeNode>>()
        stack.add(original to cloned)
        while (stack.isNotEmpty()) {
            val (a, b) = stack.removeLast()
            if (a === target || a.`val` == target.`val`) return b
            if (a.left != null) stack.add(a.left!! to b.left!!)
            if (a.right != null) stack.add(a.right!! to b.right!!)
        }
        return null
    }
}
"""

SOLUTIONS["1380_lucky_numbers_in_a_matrix"] = r"""// LeetCode 1380 - Lucky Numbers in a Matrix
// https://leetcode.com/problems/lucky-numbers-in-a-matrix/

class Solution {
    fun luckyNumbers(matrix: Array<IntArray>): List<Int> {
        val mins = matrix.map { it.min() }.toSet()
        val cols = matrix[0].indices
        val maxs = cols.map { c -> matrix.maxOf { row -> row[c] } }.toSet()
        return mins.intersect(maxs).toList()
    }
}
"""

SOLUTIONS["1381_design_a_stack_with_increment_operation"] = r"""// LeetCode 1381 - Design a Stack With Increment Operation
// https://leetcode.com/problems/design-a-stack-with-increment-operation/

class CustomStack(private val maxSize: Int) {
    private val a = mutableListOf<Int>()

    fun push(x: Int) {
        if (a.size < maxSize) a.add(x)
    }

    fun pop(): Int = if (a.isEmpty()) -1 else a.removeAt(a.lastIndex)

    fun increment(k: Int, `val`: Int) {
        val n = minOf(k, a.size)
        for (i in 0 until n) a[i] += `val`
    }
}
"""

SOLUTIONS["1382_balance_a_binary_search_tree"] = r"""// LeetCode 1382 - Balance a Binary Search Tree
// https://leetcode.com/problems/balance-a-binary-search-tree/

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun balanceBST(root: TreeNode?): TreeNode? {
        val nodes = mutableListOf<TreeNode>()
        fun walk(x: TreeNode?) {
            if (x == null) return
            walk(x.left)
            nodes.add(x)
            walk(x.right)
        }
        walk(root)
        fun build(l: Int, r: Int): TreeNode? {
            if (l >= r) return null
            val m = (l + r) / 2
            val x = nodes[m]
            x.left = build(l, m)
            x.right = build(m + 1, r)
            return x
        }
        return build(0, nodes.size)
    }
}
"""

SOLUTIONS["1383_maximum_performance_of_a_team"] = r"""// LeetCode 1383 - Maximum Performance of a Team
// https://leetcode.com/problems/maximum-performance-of-a-team/

class Solution {
    fun maxPerformance(n: Int, speed: IntArray, efficiency: IntArray, k: Int): Int {
        val engineers = efficiency.indices.map { i -> efficiency[i].toLong() to speed[i].toLong() }
            .sortedByDescending { it.first }
        val heap = java.util.PriorityQueue<Long>()
        var total = 0L
        var ans = 0L
        for ((e, s) in engineers) {
            heap.offer(s)
            total += s
            if (heap.size > k) total -= heap.poll()
            ans = maxOf(ans, total * e)
        }
        return (ans % 1_000_000_007L).toInt()
    }
}
"""

SOLUTIONS["1385_find_the_distance_value_between_two_arrays"] = r"""// LeetCode 1385 - Find the Distance Value Between Two Arrays
// https://leetcode.com/problems/find-the-distance-value-between-two-arrays/

class Solution {
    fun findTheDistanceValue(arr1: IntArray, arr2: IntArray, d: Int): Int {
        val b = arr2.sorted()
        var ans = 0
        for (x in arr1) {
            val i = b.binarySearch(x).let { if (it < 0) -it - 1 else it }
            val close = (i < b.size && kotlin.math.abs(b[i] - x) <= d) ||
                (i > 0 && kotlin.math.abs(b[i - 1] - x) <= d)
            if (!close) ans++
        }
        return ans
    }
}
"""

SOLUTIONS["1386_cinema_seat_allocation"] = r"""// LeetCode 1386 - Cinema Seat Allocation
// https://leetcode.com/problems/cinema-seat-allocation/

class Solution {
    fun maxNumberOfFamilies(n: Int, reservedSeats: Array<IntArray>): Int {
        val rows = mutableMapOf<Int, Int>()
        for (seat in reservedSeats) {
            val r = seat[0]
            val c = seat[1]
            if (c in 2..9) rows[r] = rows.getOrDefault(r, 0) or (1 shl (c - 2))
        }
        var ans = 2 * (n - rows.size)
        for (m in rows.values) {
            val left = m and 0b00001111 == 0
            val right = m and 0b11110000 == 0
            val middle = m and 0b00111100 == 0
            ans += if (left && right) 2 else if (left || right || middle) 1 else 0
        }
        return ans
    }
}
"""

SOLUTIONS["1387_sort_integers_by_the_power_value"] = r"""// LeetCode 1387 - Sort Integers by The Power Value
// https://leetcode.com/problems/sort-integers-by-the-power-value/

class Solution {
    private val memo = mutableMapOf<Int, Int>()

    fun getKth(lo: Int, hi: Int, k: Int): Int {
        return (lo..hi).sortedWith(compareBy({ power(it) }, { it }))[k - 1]
    }

    private fun power(x: Int): Int {
        memo[x]?.let { return it }
        val res = if (x == 1) 0 else 1 + power(if (x % 2 == 0) x / 2 else 3 * x + 1)
        memo[x] = res
        return res
    }
}
"""

SOLUTIONS["1388_pizza_with_3n_slices"] = r"""// LeetCode 1388 - Pizza With 3n Slices
// https://leetcode.com/problems/pizza-with-3n-slices/

class Solution {
    fun maxSizeSlices(slices: IntArray): Int {
        val k = slices.size / 3
        fun line(a: IntArray): Int {
            val dp = Array(a.size + 2) { IntArray(k + 1) }
            for (i in a.indices) {
                val x = a[i]
                val ii = i + 2
                for (j in 1..k) {
                    dp[ii][j] = maxOf(dp[ii - 1][j], dp[ii - 2][j - 1] + x)
                }
            }
            return dp[a.size + 1][k]
        }
        return maxOf(line(slices.copyOfRange(0, slices.size - 1)), line(slices.copyOfRange(1, slices.size)))
    }
}
"""

SOLUTIONS["1389_create_target_array_in_the_given_order"] = r"""// LeetCode 1389 - Create Target Array in the Given Order
// https://leetcode.com/problems/create-target-array-in-the-given-order/

class Solution {
    fun createTargetArray(nums: IntArray, index: IntArray): IntArray {
        val out = mutableListOf<Int>()
        for (i in nums.indices) out.add(index[i], nums[i])
        return out.toIntArray()
    }
}
"""

SOLUTIONS["1390_four_divisors"] = r"""// LeetCode 1390 - Four Divisors
// https://leetcode.com/problems/four-divisors/

class Solution {
    fun sumFourDivisors(nums: IntArray): Int {
        var ans = 0
        for (x in nums) {
            val ds = mutableSetOf<Int>()
            var d = 1
            while (d * d <= x) {
                if (x % d == 0) {
                    ds.add(d)
                    ds.add(x / d)
                }
                if (ds.size > 4) break
                d++
            }
            if (ds.size == 4) ans += ds.sum()
        }
        return ans
    }
}
"""

SOLUTIONS["1391_check_if_there_is_a_valid_path_in_a_grid"] = r"""// LeetCode 1391 - Check if There is a Valid Path in a Grid
// https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/

class Solution {
    fun hasValidPath(grid: Array<IntArray>): Boolean {
        val dirs = mapOf(
            1 to listOf(0 to -1, 0 to 1),
            2 to listOf(-1 to 0, 1 to 0),
            3 to listOf(0 to -1, 1 to 0),
            4 to listOf(0 to 1, 1 to 0),
            5 to listOf(0 to -1, -1 to 0),
            6 to listOf(0 to 1, -1 to 0),
        )
        val m = grid.size
        val n = grid[0].size
        val seen = mutableSetOf(0 to 0)
        val st = ArrayDeque<Pair<Int, Int>>()
        st.add(0 to 0)
        while (st.isNotEmpty()) {
            val (r, c) = st.removeLast()
            if (r == m - 1 && c == n - 1) return true
            for ((dr, dc) in dirs[grid[r][c]]!!) {
                val x = r + dr
                val y = c + dc
                if (x in 0 until m && y in 0 until n && (x to y) !in seen &&
                    (-dr to -dc) in dirs[grid[x][y]]!!
                ) {
                    seen.add(x to y)
                    st.add(x to y)
                }
            }
        }
        return false
    }
}
"""

SOLUTIONS["1392_longest_happy_prefix"] = r"""// LeetCode 1392 - Longest Happy Prefix
// https://leetcode.com/problems/longest-happy-prefix/

class Solution {
    fun longestPrefix(s: String): String {
        if (s.isEmpty()) return ""
        val pi = IntArray(s.length)
        for (i in 1 until s.length) {
            var j = pi[i - 1]
            while (j > 0 && s[i] != s[j]) j = pi[j - 1]
            if (s[i] == s[j]) j++
            pi[i] = j
        }
        return s.substring(0, pi.last())
    }
}
"""

SOLUTIONS["1394_find_lucky_integer_in_an_array"] = r"""// LeetCode 1394 - Find Lucky Integer in an Array
// https://leetcode.com/problems/find-lucky-integer-in-an-array/

class Solution {
    fun findLucky(arr: IntArray): Int {
        val cnt = mutableMapOf<Int, Int>()
        for (x in arr) cnt[x] = cnt.getOrDefault(x, 0) + 1
        var ans = -1
        for ((x, c) in cnt) if (x == c) ans = maxOf(ans, x)
        return ans
    }
}
"""

SOLUTIONS["1395_count_number_of_teams"] = r"""// LeetCode 1395 - Count Number of Teams
// https://leetcode.com/problems/count-number-of-teams/

class Solution {
    fun numTeams(rating: IntArray): Int {
        var ans = 0
        for (j in rating.indices) {
            val x = rating[j]
            var ll = 0
            var lg = 0
            for (i in 0 until j) {
                if (rating[i] < x) ll++ else lg++
            }
            var rg = 0
            var rl = 0
            for (i in j + 1 until rating.size) {
                if (rating[i] > x) rg++ else rl++
            }
            ans += ll * rg + lg * rl
        }
        return ans
    }
}
"""


def main() -> None:
    ported = 0
    failures: list[str] = []
    for folder, content in SOLUTIONS.items():
        path = ROOT / folder / "Solution.kt"
        if not path.parent.is_dir():
            failures.append(f"{folder}: missing folder")
            continue
        try:
            path.write_text(content.rstrip() + "\n", encoding="utf-8")
            ported += 1
            print(f"OK {folder}")
        except Exception as e:
            failures.append(f"{folder}: {e}")
            print(f"FAIL {folder}: {e}")
    stubs = []
    for folder in SOLUTIONS:
        text = (ROOT / folder / "Solution.kt").read_text(encoding="utf-8")
        if "fun solve()" in text:
            stubs.append(folder)
    print(f"\nported={ported} failures={len(failures)} still_stub={len(stubs)}")
    for f in failures:
        print(f"  FAIL {f}")
    for s in stubs:
        print(f"  STUB {s}")


if __name__ == "__main__":
    main()
