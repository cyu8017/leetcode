#!/usr/bin/env python3
"""Write Solution.kt for problems 1650-1699 (non-SQL)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent

SOLUTIONS: dict[str, str] = {}

SOLUTIONS["1650_lowest_common_ancestor_of_a_binary_tree_iii"] = r'''// LeetCode 1650 - Lowest Common Ancestor of a Binary Tree III
// https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/

class Node(var `val`: Int = 0) {
    var left: Node? = null
    var right: Node? = null
    var parent: Node? = null
}

class Solution {
    fun lowestCommonAncestor(p: Node?, q: Node?): Node? {
        var a = p
        var b = q
        while (a !== b) {
            a = if (a != null) a.parent else q
            b = if (b != null) b.parent else p
        }
        return a
    }
}
'''

SOLUTIONS["1652_defuse_the_bomb"] = r'''// LeetCode 1652 - Defuse the Bomb
// https://leetcode.com/problems/defuse-the-bomb/

class Solution {
    fun decrypt(code: IntArray, k: Int): IntArray {
        val n = code.size
        if (k == 0) return IntArray(n)
        val a = IntArray(n * 2) { code[it % n] }
        val ans = IntArray(n)
        for (i in 0 until n) {
            ans[i] = if (k > 0) {
                (i + 1 until i + k + 1).sumOf { a[it] }
            } else {
                (i + n + k until i + n).sumOf { a[it] }
            }
        }
        return ans
    }
}
'''

SOLUTIONS["1653_minimum_deletions_to_make_string_balanced"] = r'''// LeetCode 1653 - Minimum Deletions to Make String Balanced
// https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/

class Solution {
    fun minimumDeletions(s: String): Int {
        var b = 0
        var ans = 0
        for (c in s) {
            if (c == 'b') b++
            else ans = minOf(ans + 1, b)
        }
        return ans
    }
}
'''

SOLUTIONS["1654_minimum_jumps_to_reach_home"] = r'''// LeetCode 1654 - Minimum Jumps to Reach Home
// https://leetcode.com/problems/minimum-jumps-to-reach-home/

class Solution {
    fun minimumJumps(forbidden: IntArray, a: Int, b: Int, x: Int): Int {
        val bad = forbidden.toHashSet()
        val limit = maxOf(x, forbidden.maxOrNull() ?: 0) + a + b
        val q = ArrayDeque<IntArray>()
        q.add(intArrayOf(0, 0, 0))
        val seen = HashSet<Long>()
        seen.add(0L)
        while (q.isNotEmpty()) {
            val cur = q.removeFirst()
            val p = cur[0]
            val d = cur[1]
            val back = cur[2] == 1
            if (p == x) return d
            val candidates = listOf(p + a to false, p - b to true)
            for ((np, nb) in candidates) {
                if (np < 0 || np > limit || np in bad) continue
                if (back && nb) continue
                val key = (np.toLong() shl 1) or (if (nb) 1L else 0L)
                if (key in seen) continue
                seen.add(key)
                q.add(intArrayOf(np, d + 1, if (nb) 1 else 0))
            }
        }
        return -1
    }
}
'''

SOLUTIONS["1655_distribute_repeating_integers"] = r'''// LeetCode 1655 - Distribute Repeating Integers
// https://leetcode.com/problems/distribute-repeating-integers/

class Solution {
    fun canDistribute(nums: IntArray, quantity: IntArray): Boolean {
        val freq = HashMap<Int, Int>()
        for (x in nums) freq[x] = (freq[x] ?: 0) + 1
        val cnt = freq.values.toList()
        quantity.sortDescending()
        val m = quantity.size
        val sums = IntArray(1 shl m)
        for (mask in 1 until (1 shl m)) {
            val bit = mask and -mask
            sums[mask] = sums[mask xor bit] + quantity[Integer.numberOfTrailingZeros(bit)]
        }
        var dp = hashSetOf(0)
        for (c in cnt) {
            val nxt = HashSet(dp)
            for (mask in dp) {
                val left = ((1 shl m) - 1) xor mask
                var sub = left
                while (sub > 0) {
                    if (sums[sub] <= c) nxt.add(mask or sub)
                    sub = (sub - 1) and left
                }
            }
            dp = nxt
        }
        return ((1 shl m) - 1) in dp
    }
}
'''

SOLUTIONS["1656_design_an_ordered_stream"] = r'''// LeetCode 1656 - Design an Ordered Stream
// https://leetcode.com/problems/design-an-ordered-stream/

class OrderedStream(n: Int) {
    private val a = arrayOfNulls<String>(n + 1)
    private var p = 1

    fun insert(idKey: Int, value: String): List<String> {
        a[idKey] = value
        val out = mutableListOf<String>()
        while (p < a.size && a[p] != null) {
            out.add(a[p]!!)
            p++
        }
        return out
    }
}
'''

SOLUTIONS["1657_determine_if_two_strings_are_close"] = r'''// LeetCode 1657 - Determine if Two Strings Are Close
// https://leetcode.com/problems/determine-if-two-strings-are-close/

class Solution {
    fun closeStrings(word1: String, word2: String): Boolean {
        if (word1.length != word2.length) return false
        val a = IntArray(26)
        val b = IntArray(26)
        for (c in word1) a[c - 'a']++
        for (c in word2) b[c - 'a']++
        for (i in 0 until 26) {
            if ((a[i] == 0) != (b[i] == 0)) return false
        }
        a.sort()
        b.sort()
        return a.contentEquals(b)
    }
}
'''

SOLUTIONS["1658_minimum_operations_to_reduce_x_to_zero"] = r'''// LeetCode 1658 - Minimum Operations to Reduce X to Zero
// https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/

class Solution {
    fun minOperations(nums: IntArray, x: Int): Int {
        val target = nums.sum() - x
        if (target < 0) return -1
        var best = -1
        var left = 0
        var cur = 0
        for (right in nums.indices) {
            cur += nums[right]
            while (cur > target) {
                cur -= nums[left]
                left++
            }
            if (cur == target) best = maxOf(best, right - left + 1)
        }
        return if (best < 0) -1 else nums.size - best
    }
}
'''

SOLUTIONS["1659_maximize_grid_happiness"] = r'''// LeetCode 1659 - Maximize Grid Happiness
// https://leetcode.com/problems/maximize-grid-happiness/

class Solution {
    fun getMaxGridHappiness(m: Int, n: Int, introvertsCount: Int, extrovertsCount: Int): Int {
        var states = 1
        repeat(n) { states *= 3 }
        val cells = Array(states) { IntArray(n) }
        val intro = IntArray(states)
        val extro = IntArray(states)
        val row = IntArray(states)
        for (s in 0 until states) {
            var x = s
            for (j in 0 until n) {
                cells[s][j] = x % 3
                x /= 3
            }
            var value = 0
            for (j in 0 until n) {
                when (cells[s][j]) {
                    1 -> { intro[s]++; value += 120 }
                    2 -> { extro[s]++; value += 40 }
                }
            }
            for (j in 1 until n) value += pair(cells[s][j - 1], cells[s][j])
            row[s] = value
        }
        val compat = Array(states) { IntArray(states) }
        for (a in 0 until states) {
            for (b in 0 until states) {
                var v = 0
                for (j in 0 until n) v += pair(cells[a][j], cells[b][j])
                compat[a][b] = v
            }
        }
        val memo = IntArray((m + 1) * states * (introvertsCount + 1) * (extrovertsCount + 1)) { -1 }
        fun dfs(r: Int, prev: Int, i: Int, e: Int): Int {
            if (r == m) return 0
            val id = (((r * states + prev) * (introvertsCount + 1) + i) * (extrovertsCount + 1)) + e
            if (memo[id] >= 0) return memo[id]
            var best = 0
            for (s in 0 until states) {
                if (intro[s] > i || extro[s] > e) continue
                best = maxOf(best, row[s] + compat[prev][s] + dfs(r + 1, s, i - intro[s], e - extro[s]))
            }
            memo[id] = best
            return best
        }
        return dfs(0, 0, introvertsCount, extrovertsCount)
    }

    private fun pair(a: Int, b: Int): Int {
        if (a == 0 || b == 0) return 0
        val va = if (a == 1) -30 else 20
        val vb = if (b == 1) -30 else 20
        return va + vb
    }
}
'''

SOLUTIONS["1660_correct_a_binary_tree"] = r'''// LeetCode 1660 - Correct a Binary Tree
// https://leetcode.com/problems/correct-a-binary-tree/

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun correctBinaryTree(root: TreeNode?): TreeNode? {
        val seen = HashSet<TreeNode>()
        fun dfs(node: TreeNode?): TreeNode? {
            if (node == null) return null
            if (node.right != null && node.right in seen) return null
            seen.add(node)
            node.right = dfs(node.right)
            node.left = dfs(node.left)
            return node
        }
        return dfs(root)
    }
}
'''

SOLUTIONS["1662_check_if_two_string_arrays_are_equivalent"] = r'''// LeetCode 1662 - Check If Two String Arrays are Equivalent
// https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/

class Solution {
    fun arrayStringsAreEqual(word1: Array<String>, word2: Array<String>): Boolean {
        return word1.joinToString("") == word2.joinToString("")
    }
}
'''

SOLUTIONS["1663_smallest_string_with_a_given_numeric_value"] = r'''// LeetCode 1663 - Smallest String With A Given Numeric Value
// https://leetcode.com/problems/smallest-string-with-a-given-numeric-value/

class Solution {
    fun getSmallestString(n: Int, k: Int): String {
        val a = CharArray(n) { 'a' }
        var rem = k - n
        for (i in n - 1 downTo 0) {
            val d = minOf(25, rem)
            a[i] = ('a'.code + d).toChar()
            rem -= d
        }
        return String(a)
    }
}
'''

SOLUTIONS["1664_ways_to_make_a_fair_array"] = r'''// LeetCode 1664 - Ways to Make a Fair Array
// https://leetcode.com/problems/ways-to-make-a-fair-array/

class Solution {
    fun waysToMakeFair(nums: IntArray): Int {
        var te = 0
        var to = 0
        for (i in nums.indices) {
            if (i % 2 == 0) te += nums[i] else to += nums[i]
        }
        var le = 0
        var lo = 0
        var ans = 0
        for (i in nums.indices) {
            val x = nums[i]
            if (i % 2 == 1) to -= x else te -= x
            if (le + to == lo + te) ans++
            if (i % 2 == 1) lo += x else le += x
        }
        return ans
    }
}
'''

SOLUTIONS["1665_minimum_initial_energy_to_finish_tasks"] = r'''// LeetCode 1665 - Minimum Initial Energy to Finish Tasks
// https://leetcode.com/problems/minimum-initial-energy-to-finish-tasks/

class Solution {
    fun minimumEffort(tasks: Array<IntArray>): Int {
        tasks.sortByDescending { it[1] - it[0] }
        var energy = 0
        var spent = 0
        for (t in tasks) {
            energy = maxOf(energy, spent + t[1])
            spent += t[0]
        }
        return energy
    }
}
'''

SOLUTIONS["1666_change_the_root_of_a_binary_tree"] = r'''// LeetCode 1666 - Change the Root of a Binary Tree
// https://leetcode.com/problems/change-the-root-of-a-binary-tree/

class Node(var `val`: Int = 0) {
    var left: Node? = null
    var right: Node? = null
    var parent: Node? = null
}

class Solution {
    fun flipBinaryTree(root: Node?, leaf: Node?): Node? {
        var node = leaf
        while (node !== root) {
            val parent = node!!.parent!!
            if (parent.left === node) parent.left = null else parent.right = null
            val originalLeft = node.left
            node.left = parent
            if (originalLeft != null) node.right = originalLeft
            node = parent
        }
        fun fixParent(cur: Node?, parent: Node?) {
            if (cur == null) return
            cur.parent = parent
            fixParent(cur.left, cur)
            fixParent(cur.right, cur)
        }
        fixParent(leaf, null)
        return leaf
    }
}
'''

SOLUTIONS["1668_maximum_repeating_substring"] = r'''// LeetCode 1668 - Maximum Repeating Substring
// https://leetcode.com/problems/maximum-repeating-substring/

class Solution {
    fun maxRepeating(sequence: String, word: String): Int {
        var k = 0
        while (word.repeat(k + 1) in sequence) k++
        return k
    }
}
'''

SOLUTIONS["1669_merge_in_between_linked_lists"] = r'''// LeetCode 1669 - Merge In Between Linked Lists
// https://leetcode.com/problems/merge-in-between-linked-lists/

class ListNode(var `val`: Int = 0) {
    var next: ListNode? = null
}

class Solution {
    fun mergeInBetween(list1: ListNode?, a: Int, b: Int, list2: ListNode?): ListNode? {
        var pre = list1
        repeat(a - 1) { pre = pre!!.next }
        var post = pre
        repeat(b - a + 2) { post = post!!.next }
        pre!!.next = list2
        while (pre!!.next != null) pre = pre.next
        pre!!.next = post
        return list1
    }
}
'''

SOLUTIONS["1670_design_front_middle_back_queue"] = r'''// LeetCode 1670 - Design Front Middle Back Queue
// https://leetcode.com/problems/design-front-middle-back-queue/

class FrontMiddleBackQueue {
    private val l = ArrayDeque<Int>()
    private val r = ArrayDeque<Int>()

    private fun bal() {
        while (l.size > r.size + 1) r.addFirst(l.removeLast())
        while (r.size > l.size) l.addLast(r.removeFirst())
    }

    fun pushFront(`val`: Int) {
        l.addFirst(`val`)
        bal()
    }

    fun pushMiddle(`val`: Int) {
        if (l.size > r.size) r.addFirst(l.removeLast())
        l.addLast(`val`)
    }

    fun pushBack(`val`: Int) {
        r.addLast(`val`)
        bal()
    }

    fun popFront(): Int {
        if (l.isEmpty()) return -1
        val v = l.removeFirst()
        bal()
        return v
    }

    fun popMiddle(): Int {
        if (l.isEmpty()) return -1
        val v = l.removeLast()
        bal()
        return v
    }

    fun popBack(): Int {
        if (l.isEmpty()) return -1
        val v = if (r.isNotEmpty()) r.removeLast() else l.removeLast()
        bal()
        return v
    }
}
'''

SOLUTIONS["1671_minimum_number_of_removals_to_make_mountain_array"] = r'''// LeetCode 1671 - Minimum Number of Removals to Make Mountain Array
// https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array/

class Solution {
    fun minimumMountainRemovals(nums: IntArray): Int {
        fun lis(a: IntArray): IntArray {
            val d = mutableListOf<Int>()
            val out = IntArray(a.size)
            for (i in a.indices) {
                val x = a[i]
                var lo = 0
                var hi = d.size
                while (lo < hi) {
                    val mid = (lo + hi) ushr 1
                    if (d[mid] < x) lo = mid + 1 else hi = mid
                }
                if (lo == d.size) d.add(x) else d[lo] = x
                out[i] = lo + 1
            }
            return out
        }
        val l = lis(nums)
        val rev = nums.reversedArray()
        val r = lis(rev).reversedArray()
        val n = nums.size
        var best = 0
        for (i in 0 until n) {
            if (l[i] > 1 && r[i] > 1) best = maxOf(best, l[i] + r[i] - 1)
        }
        return n - best
    }
}
'''

SOLUTIONS["1672_richest_customer_wealth"] = r'''// LeetCode 1672 - Richest Customer Wealth
// https://leetcode.com/problems/richest-customer-wealth/

class Solution {
    fun maximumWealth(accounts: Array<IntArray>): Int {
        return accounts.maxOf { it.sum() }
    }
}
'''

SOLUTIONS["1673_find_the_most_competitive_subsequence"] = r'''// LeetCode 1673 - Find the Most Competitive Subsequence
// https://leetcode.com/problems/find-the-most-competitive-subsequence/

class Solution {
    fun mostCompetitive(nums: IntArray, k: Int): IntArray {
        val st = ArrayDeque<Int>()
        for (i in nums.indices) {
            val x = nums[i]
            while (st.isNotEmpty() && st.last() > x && st.size - 1 + nums.size - i >= k) {
                st.removeLast()
            }
            if (st.size < k) st.addLast(x)
        }
        return st.toIntArray()
    }
}
'''

SOLUTIONS["1674_minimum_moves_to_make_array_complementary"] = r'''// LeetCode 1674 - Minimum Moves to Make Array Complementary
// https://leetcode.com/problems/minimum-moves-to-make-array-complementary/

class Solution {
    fun minMoves(nums: IntArray, limit: Int): Int {
        val n = nums.size
        val d = IntArray(2 * limit + 2)
        for (i in 0 until n / 2) {
            val a = nums[i]
            val b = nums[n - 1 - i]
            val lo = minOf(a, b) + 1
            val hi = maxOf(a, b) + limit
            val s = a + b
            d[2] += 2
            d[lo] -= 1
            d[s] -= 1
            d[s + 1] += 1
            d[hi + 1] += 1
        }
        var ans = Int.MAX_VALUE
        var cur = 0
        for (s in 2..2 * limit) {
            cur += d[s]
            ans = minOf(ans, cur)
        }
        return ans
    }
}
'''

SOLUTIONS["1675_minimize_deviation_in_array"] = r'''// LeetCode 1675 - Minimize Deviation in Array
// https://leetcode.com/problems/minimize-deviation-in-array/

import java.util.PriorityQueue

class Solution {
    fun minimumDeviation(nums: IntArray): Int {
        val pq = PriorityQueue<Int>(compareByDescending { it })
        var mn = Int.MAX_VALUE
        for (v in nums) {
            var x = v
            if (x % 2 == 1) x *= 2
            mn = minOf(mn, x)
            pq.offer(x)
        }
        var ans = Int.MAX_VALUE
        while (true) {
            val x = pq.poll()
            ans = minOf(ans, x - mn)
            if (x % 2 == 1) return ans
            val half = x / 2
            mn = minOf(mn, half)
            pq.offer(half)
        }
    }
}
'''

SOLUTIONS["1676_lowest_common_ancestor_of_a_binary_tree_iv"] = r'''// LeetCode 1676 - Lowest Common Ancestor of a Binary Tree IV
// https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iv/

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun lowestCommonAncestor(root: TreeNode?, nodes: Array<TreeNode?>): TreeNode? {
        val targets = nodes.filterNotNull().toHashSet()
        fun dfs(node: TreeNode?): TreeNode? {
            if (node == null) return null
            val l = dfs(node.left)
            val r = dfs(node.right)
            if (node in targets || (l != null && r != null)) return node
            return l ?: r
        }
        return dfs(root)
    }
}
'''

SOLUTIONS["1678_goal_parser_interpretation"] = r'''// LeetCode 1678 - Goal Parser Interpretation
// https://leetcode.com/problems/goal-parser-interpretation/

class Solution {
    fun interpret(command: String): String {
        return command.replace("()", "o").replace("(al)", "al")
    }
}
'''

SOLUTIONS["1679_max_number_of_k_sum_pairs"] = r'''// LeetCode 1679 - Max Number of K-Sum Pairs
// https://leetcode.com/problems/max-number-of-k-sum-pairs/

class Solution {
    fun maxOperations(nums: IntArray, k: Int): Int {
        val c = HashMap<Int, Int>()
        var ans = 0
        for (x in nums) {
            val need = k - x
            val avail = c[need] ?: 0
            if (avail > 0) {
                c[need] = avail - 1
                ans++
            } else {
                c[x] = (c[x] ?: 0) + 1
            }
        }
        return ans
    }
}
'''

SOLUTIONS["1680_concatenation_of_consecutive_binary_numbers"] = r'''// LeetCode 1680 - Concatenation of Consecutive Binary Numbers
// https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/

class Solution {
    fun concatenatedBinary(n: Int): Int {
        var ans = 0L
        var bits = 0
        val mod = 1_000_000_007L
        for (x in 1..n) {
            if (x and (x - 1) == 0) bits++
            ans = ((ans shl bits) + x) % mod
        }
        return ans.toInt()
    }
}
'''

SOLUTIONS["1681_minimum_incompatibility"] = r'''// LeetCode 1681 - Minimum Incompatibility
// https://leetcode.com/problems/minimum-incompatibility/

class Solution {
    fun minimumIncompatibility(nums: IntArray, k: Int): Int {
        val n = nums.size
        val size = n / k
        val full = (1 shl n) - 1
        val groups = HashMap<Int, Int>()
        for (mask in 0 until (1 shl n)) {
            if (Integer.bitCount(mask) != size) continue
            val vals = mutableListOf<Int>()
            for (i in 0 until n) if ((mask shr i) and 1 == 1) vals.add(nums[i])
            if (vals.toSet().size == size) {
                groups[mask] = vals.maxOrNull()!! - vals.minOrNull()!!
            }
        }
        val memo = IntArray(1 shl n) { -2 }
        fun dp(mask: Int): Int {
            if (mask == full) return 0
            if (memo[mask] != -2) return memo[mask]
            var first = 0
            while ((mask shr first) and 1 == 1) first++
            var best = 1_000_000_000
            for ((g, c) in groups) {
                if (((g shr first) and 1) == 1 && g and mask == 0) {
                    val sub = dp(mask or g)
                    if (sub < 1_000_000_000) best = minOf(best, c + sub)
                }
            }
            memo[mask] = best
            return best
        }
        val ans = dp(0)
        return if (ans >= 1_000_000_000) -1 else ans
    }
}
'''

SOLUTIONS["1682_longest_palindromic_subsequence_ii"] = r'''// LeetCode 1682 - Longest Palindromic Subsequence II
// https://leetcode.com/problems/longest-palindromic-subsequence-ii/

class Solution {
    fun longestPalindromeSubseq(s: String): Int {
        val n = s.length
        val dp = Array(n) { Array(n) { IntArray(26) } }
        for (length in 2..n) {
            for (i in 0..n - length) {
                val j = i + length - 1
                for (c in 0 until 26) {
                    dp[i][j][c] = maxOf(dp[i + 1][j][c], dp[i][j - 1][c])
                }
                if (s[i] == s[j]) {
                    val c = s[i] - 'a'
                    var inner = 0
                    if (length > 2) {
                        for (x in 0 until 26) {
                            if (x != c) inner = maxOf(inner, dp[i + 1][j - 1][x])
                        }
                    }
                    dp[i][j][c] = maxOf(dp[i][j][c], inner + 2)
                }
            }
        }
        return dp[0][n - 1].maxOrNull() ?: 0
    }
}
'''

SOLUTIONS["1684_count_the_number_of_consistent_strings"] = r'''// LeetCode 1684 - Count the Number of Consistent Strings
// https://leetcode.com/problems/count-the-number-of-consistent-strings/

class Solution {
    fun countConsistentStrings(allowed: String, words: Array<String>): Int {
        val a = BooleanArray(26)
        for (c in allowed) a[c - 'a'] = true
        var ans = 0
        for (w in words) {
            if (w.all { a[it - 'a'] }) ans++
        }
        return ans
    }
}
'''

SOLUTIONS["1685_sum_of_absolute_differences_in_a_sorted_array"] = r'''// LeetCode 1685 - Sum of Absolute Differences in a Sorted Array
// https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array/

class Solution {
    fun getSumAbsoluteDifferences(nums: IntArray): IntArray {
        val total = nums.sum()
        var left = 0
        val n = nums.size
        val ans = IntArray(n)
        for (i in nums.indices) {
            val x = nums[i]
            ans[i] = x * i - left + (total - left - x) - x * (n - i - 1)
            left += x
        }
        return ans
    }
}
'''

SOLUTIONS["1686_stone_game_vi"] = r'''// LeetCode 1686 - Stone Game VI
// https://leetcode.com/problems/stone-game-vi/

class Solution {
    fun stoneGameVI(aliceValues: IntArray, bobValues: IntArray): Int {
        val order = aliceValues.indices.sortedByDescending { aliceValues[it] + bobValues[it] }
        var score = 0
        for ((t, i) in order.withIndex()) {
            score += if (t % 2 == 0) aliceValues[i] else -bobValues[i]
        }
        return when {
            score > 0 -> 1
            score < 0 -> -1
            else -> 0
        }
    }
}
'''

SOLUTIONS["1687_delivering_boxes_from_storage_to_ports"] = r'''// LeetCode 1687 - Delivering Boxes from Storage to Ports
// https://leetcode.com/problems/delivering-boxes-from-storage-to-ports/

class Solution {
    fun boxDelivering(boxes: Array<IntArray>, portsCount: Int, maxBoxes: Int, maxWeight: Int): Int {
        val n = boxes.size
        val w = IntArray(n + 1)
        val changes = IntArray(n + 1)
        for (i in 1..n) {
            w[i] = w[i - 1] + boxes[i - 1][1]
            changes[i] = changes[i - 1] + if (i > 1 && boxes[i - 1][0] != boxes[i - 2][0]) 1 else 0
        }
        val dp = IntArray(n + 1)
        val q = ArrayDeque<Int>()
        q.add(0)
        for (i in 1..n) {
            while (q.isNotEmpty() && (i - q.first() > maxBoxes || w[i] - w[q.first()] > maxWeight)) {
                q.removeFirst()
            }
            val j = q.first()
            dp[i] = dp[j] + changes[i] - changes[j + 1] + 2
            if (i < n) {
                val `val` = dp[i] - changes[i + 1]
                while (q.isNotEmpty() && dp[q.last()] - changes[q.last() + 1] >= `val`) q.removeLast()
                q.addLast(i)
            }
        }
        return dp[n]
    }
}
'''

SOLUTIONS["1688_count_of_matches_in_tournament"] = r'''// LeetCode 1688 - Count of Matches in Tournament
// https://leetcode.com/problems/count-of-matches-in-tournament/

class Solution {
    fun numberOfMatches(n: Int): Int = n - 1
}
'''

SOLUTIONS["1689_partitioning_into_minimum_number_of_deci_binary_numbers"] = r'''// LeetCode 1689 - Partitioning Into Minimum Number Of Deci-Binary Numbers
// https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/

class Solution {
    fun minPartitions(n: String): Int = n.maxOrNull()!! - '0'
}
'''

SOLUTIONS["1690_stone_game_vii"] = r'''// LeetCode 1690 - Stone Game VII
// https://leetcode.com/problems/stone-game-vii/

class Solution {
    fun stoneGameVII(stones: IntArray): Int {
        val n = stones.size
        val pre = IntArray(n + 1)
        for (i in stones.indices) pre[i + 1] = pre[i] + stones[i]
        val dp = Array(n) { IntArray(n) }
        for (length in 2..n) {
            for (i in 0..n - length) {
                val j = i + length - 1
                dp[i][j] = maxOf(
                    pre[j + 1] - pre[i + 1] - dp[i + 1][j],
                    pre[j] - pre[i] - dp[i][j - 1]
                )
            }
        }
        return dp[0][n - 1]
    }
}
'''

SOLUTIONS["1691_maximum_height_by_stacking_cuboids"] = r'''// LeetCode 1691 - Maximum Height by Stacking Cuboids
// https://leetcode.com/problems/maximum-height-by-stacking-cuboids/

class Solution {
    fun maxHeight(cuboids: Array<IntArray>): Int {
        val a = cuboids.map { it.sorted().toIntArray() }.sortedWith(
            compareBy({ it[0] }, { it[1] }, { it[2] })
        )
        val n = a.size
        val dp = IntArray(n)
        for (i in 0 until n) {
            dp[i] = a[i][2]
            for (j in 0 until i) {
                if ((0 until 3).all { d -> a[j][d] <= a[i][d] }) {
                    dp[i] = maxOf(dp[i], dp[j] + a[i][2])
                }
            }
        }
        return dp.maxOrNull() ?: 0
    }
}
'''

SOLUTIONS["1692_count_ways_to_distribute_candies"] = r'''// LeetCode 1692 - Count Ways to Distribute Candies
// https://leetcode.com/problems/count-ways-to-distribute-candies/

class Solution {
    fun waysToDistribute(n: Int, k: Int): Int {
        val mod = 1_000_000_007
        val dp = LongArray(k + 1)
        dp[0] = 1
        for (i in 1..n) {
            for (j in minOf(i, k) downTo 1) {
                dp[j] = (dp[j - 1] + j * dp[j]) % mod
            }
            dp[0] = 0
        }
        return dp[k].toInt()
    }
}
'''

SOLUTIONS["1694_reformat_phone_number"] = r'''// LeetCode 1694 - Reformat Phone Number
// https://leetcode.com/problems/reformat-phone-number/

class Solution {
    fun reformatNumber(number: String): String {
        var s = number.filter { it.isDigit() }
        val out = mutableListOf<String>()
        while (s.length > 4) {
            out.add(s.take(3))
            s = s.drop(3)
        }
        if (s.length == 4) {
            out.add(s.take(2))
            out.add(s.drop(2))
        } else if (s.isNotEmpty()) {
            out.add(s)
        }
        return out.joinToString("-")
    }
}
'''

SOLUTIONS["1695_maximum_erasure_value"] = r'''// LeetCode 1695 - Maximum Erasure Value
// https://leetcode.com/problems/maximum-erasure-value/

class Solution {
    fun maximumUniqueSubarray(nums: IntArray): Int {
        val seen = HashMap<Int, Int>()
        var left = 0
        var cur = 0
        var best = 0
        for (right in nums.indices) {
            val x = nums[right]
            val prev = seen[x]
            if (prev != null && prev >= left) {
                while (left <= prev) {
                    cur -= nums[left]
                    left++
                }
            }
            seen[x] = right
            cur += x
            best = maxOf(best, cur)
        }
        return best
    }
}
'''

SOLUTIONS["1696_jump_game_vi"] = r'''// LeetCode 1696 - Jump Game VI
// https://leetcode.com/problems/jump-game-vi/

class Solution {
    fun maxResult(nums: IntArray, k: Int): Int {
        val q = ArrayDeque<IntArray>()
        q.add(intArrayOf(0, nums[0]))
        for (i in 1 until nums.size) {
            while (q.first()[0] < i - k) q.removeFirst()
            val score = nums[i] + q.first()[1]
            while (q.isNotEmpty() && q.last()[1] <= score) q.removeLast()
            q.addLast(intArrayOf(i, score))
        }
        return q.last()[1]
    }
}
'''

SOLUTIONS["1697_checking_existence_of_edge_length_limited_paths"] = r'''// LeetCode 1697 - Checking Existence of Edge Length Limited Paths
// https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/

class Solution {
    fun distanceLimitedPathsExist(n: Int, edgeList: Array<IntArray>, queries: Array<IntArray>): BooleanArray {
        val parent = IntArray(n) { it }
        fun find(x: Int): Int {
            var cur = x
            while (cur != parent[cur]) {
                parent[cur] = parent[parent[cur]]
                cur = parent[cur]
            }
            return cur
        }
        val ans = BooleanArray(queries.size)
        val edges = edgeList.sortedBy { it[2] }
        val ordered = queries.mapIndexed { j, q -> intArrayOf(q[2], q[0], q[1], j) }
            .sortedBy { it[0] }
        var i = 0
        for (item in ordered) {
            val limit = item[0]
            val p = item[1]
            val q = item[2]
            val idx = item[3]
            while (i < edges.size && edges[i][2] < limit) {
                val a = find(edges[i][0])
                val b = find(edges[i][1])
                parent[a] = b
                i++
            }
            ans[idx] = find(p) == find(q)
        }
        return ans
    }
}
'''

SOLUTIONS["1698_number_of_distinct_substrings_in_a_string"] = r'''// LeetCode 1698 - Number of Distinct Substrings in a String
// https://leetcode.com/problems/number-of-distinct-substrings-in-a-string/

class Solution {
    fun countDistinct(s: String): Int {
        class TrieNode {
            val children = HashMap<Char, TrieNode>()
        }
        val root = TrieNode()
        var ans = 0
        for (i in s.indices) {
            var node = root
            for (j in i until s.length) {
                val c = s[j]
                val next = node.children[c]
                if (next == null) {
                    val created = TrieNode()
                    node.children[c] = created
                    ans++
                    node = created
                } else {
                    node = next
                }
            }
        }
        return ans
    }
}
'''

SQL_SKIP = {
    "1651_hopper_company_queries_iii",
    "1661_average_time_of_process_per_machine",
    "1667_fix_names_in_a_table",
    "1677_products_worth_over_invoices",
    "1683_invalid_tweets",
    "1693_daily_leads_and_partners",
    "1699_number_of_calls_between_two_persons",
}


def main() -> None:
    written = []
    for folder, content in SOLUTIONS.items():
        path = ROOT / folder / "Solution.kt"
        if not path.parent.exists():
            raise SystemExit(f"missing folder: {folder}")
        path.write_text(content, encoding="utf-8", newline="\n")
        written.append(folder)
    print(f"wrote {len(written)} Solution.kt files")
    for f in written:
        print(f"  {f}")
    print(f"sql skipped (untouched): {len(SQL_SKIP)}")


if __name__ == "__main__":
    main()
