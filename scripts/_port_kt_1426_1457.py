#!/usr/bin/env python3
"""Port Kotlin solutions for problems 1426-1457 (listed stubs)."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

SOLUTIONS: dict[str, str] = {
    "1426_counting_elements": '''// LeetCode 1426 - Counting Elements
// https://leetcode.com/problems/counting-elements/

class Solution {
    fun countElements(arr: IntArray): Int {
        val values = arr.toSet()
        return arr.count { it + 1 in values }
    }
}
''',
    "1427_perform_string_shifts": '''// LeetCode 1427 - Perform String Shifts
// https://leetcode.com/problems/perform-string-shifts/

class Solution {
    fun stringShift(s: String, shift: Array<IntArray>): String {
        var offset = 0
        for (pair in shift) {
            offset += if (pair[0] == 1) pair[1] else -pair[1]
        }
        val n = s.length
        offset %= n
        if (offset < 0) offset += n
        if (offset == 0) return s
        return s.substring(n - offset) + s.substring(0, n - offset)
    }
}
''',
    "1428_leftmost_column_with_at_least_a_one": '''// LeetCode 1428 - Leftmost Column With At Least A One
// https://leetcode.com/problems/leftmost-column-with-at-least-a-one/

interface BinaryMatrix {
    fun get(row: Int, col: Int): Int
    fun dimensions(): List<Int>
}

class Solution {
    fun leftMostColumnWithOne(binaryMatrix: BinaryMatrix): Int {
        val dims = binaryMatrix.dimensions()
        val rows = dims[0]
        val cols = dims[1]
        var row = 0
        var col = cols - 1
        var answer = -1
        while (row < rows && col >= 0) {
            if (binaryMatrix.get(row, col) == 1) {
                answer = col
                col--
            } else {
                row++
            }
        }
        return answer
    }
}
''',
    "1429_first_unique_number": '''// LeetCode 1429 - First Unique Number
// https://leetcode.com/problems/first-unique-number/

class FirstUnique(nums: IntArray) {
    private val freq = HashMap<Int, Int>()
    private val queue = ArrayDeque<Int>()

    init {
        for (x in nums) add(x)
    }

    fun showFirstUnique(): Int {
        while (queue.isNotEmpty() && freq[queue.first()]!! > 1) {
            queue.removeFirst()
        }
        return if (queue.isEmpty()) -1 else queue.first()
    }

    fun add(value: Int) {
        freq[value] = freq.getOrDefault(value, 0) + 1
        if (freq[value] == 1) queue.addLast(value)
    }
}
''',
    "1430_check_if_a_string_is_a_valid_sequence_from_root_to_leaves_path_in_a_binary_tree": '''// LeetCode 1430 - Check If a String Is a Valid Sequence from Root to Leaves Path in a Binary Tree
// https://leetcode.com/problems/check-if-a-string-is-a-valid-sequence-from-root-to-leaves-path-in-a-binary-tree/

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun isValidSequence(root: TreeNode?, arr: IntArray): Boolean {
        fun visit(node: TreeNode?, index: Int): Boolean {
            if (node == null || index == arr.size || node.`val` != arr[index]) return false
            if (node.left == null && node.right == null) return index == arr.size - 1
            return visit(node.left, index + 1) || visit(node.right, index + 1)
        }
        return visit(root, 0)
    }
}
''',
    "1431_kids_with_the_greatest_number_of_candies": '''// LeetCode 1431 - Kids With the Greatest Number of Candies
// https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

class Solution {
    fun kidsWithCandies(candies: IntArray, extraCandies: Int): List<Boolean> {
        val maximum = candies.maxOrNull() ?: 0
        return candies.map { it + extraCandies >= maximum }
    }
}
''',
    "1432_max_difference_you_can_get_from_changing_an_integer": '''// LeetCode 1432 - Max Difference You Can Get From Changing an Integer
// https://leetcode.com/problems/max-difference-you-can-get-from-changing-an-integer/

class Solution {
    fun maxDiff(num: Int): Int {
        val s = num.toString()
        var high = s
        for (ch in s) {
            if (ch != '9') {
                high = s.replace(ch, '9')
                break
            }
        }
        var low = s
        if (s[0] != '1') {
            low = s.replace(s[0], '1')
        } else {
            for (ch in s.substring(1)) {
                if (ch != '0' && ch != '1') {
                    low = s.replace(ch, '0')
                    break
                }
            }
        }
        return high.toInt() - low.toInt()
    }
}
''',
    "1433_check_if_a_string_can_break_another_string": '''// LeetCode 1433 - Check If a String Can Break Another String
// https://leetcode.com/problems/check-if-a-string-can-break-another-string/

class Solution {
    fun checkIfCanBreak(s1: String, s2: String): Boolean {
        val a = s1.toCharArray().sorted()
        val b = s2.toCharArray().sorted()
        val ge = a.indices.all { a[it] >= b[it] }
        val le = a.indices.all { a[it] <= b[it] }
        return ge || le
    }
}
''',
    "1434_number_of_ways_to_wear_different_hats_to_each_other": '''// LeetCode 1434 - Number of Ways to Wear Different Hats to Each Other
// https://leetcode.com/problems/number-of-ways-to-wear-different-hats-to-each-other/

class Solution {
    fun numberWays(hats: List<List<Int>>): Int {
        val mod = 1_000_000_007
        val people = hats.size
        val wearers = Array(41) { mutableListOf<Int>() }
        for (person in hats.indices) {
            for (hat in hats[person]) {
                wearers[hat].add(person)
            }
        }
        var dp = IntArray(1 shl people)
        dp[0] = 1
        for (hat in 1..40) {
            val nxt = dp.copyOf()
            for (mask in dp.indices) {
                val ways = dp[mask]
                if (ways == 0) continue
                for (person in wearers[hat]) {
                    if (mask shr person and 1 == 0) {
                        val nextMask = mask or (1 shl person)
                        nxt[nextMask] = (nxt[nextMask] + ways) % mod
                    }
                }
            }
            dp = nxt
        }
        return dp[(1 shl people) - 1]
    }
}
''',
    "1436_destination_city": '''// LeetCode 1436 - Destination City
// https://leetcode.com/problems/destination-city/

class Solution {
    fun destCity(paths: List<List<String>>): String {
        val starts = paths.map { it[0] }.toSet()
        return paths.first { it[1] !in starts }[1]
    }
}
''',
    "1437_check_if_all_1s_are_at_least_length_k_places_away": '''// LeetCode 1437 - Check If All 1's Are at Least Length K Places Away
// https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/

class Solution {
    fun kLengthApart(nums: IntArray, k: Int): Boolean {
        var previous = -k - 1
        for (i in nums.indices) {
            if (nums[i] == 1) {
                if (i - previous <= k) return false
                previous = i
            }
        }
        return true
    }
}
''',
    "1438_longest_continuous_subarray_with_absolute_diff_less_than_or_equal_to_limit": '''// LeetCode 1438 - Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
// https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/

class Solution {
    fun longestSubarray(nums: IntArray, limit: Int): Int {
        val maxq = ArrayDeque<Int>()
        val minq = ArrayDeque<Int>()
        var left = 0
        var answer = 0
        for (right in nums.indices) {
            while (maxq.isNotEmpty() && nums[maxq.last()] < nums[right]) maxq.removeLast()
            while (minq.isNotEmpty() && nums[minq.last()] > nums[right]) minq.removeLast()
            maxq.addLast(right)
            minq.addLast(right)
            while (nums[maxq.first()] - nums[minq.first()] > limit) {
                if (maxq.first() == left) maxq.removeFirst()
                if (minq.first() == left) minq.removeFirst()
                left++
            }
            answer = maxOf(answer, right - left + 1)
        }
        return answer
    }
}
''',
    "1439_find_the_kth_smallest_sum_of_a_matrix_with_sorted_rows": '''// LeetCode 1439 - Find the Kth Smallest Sum of a Matrix With Sorted Rows
// https://leetcode.com/problems/find-the-kth-smallest-sum-of-a-matrix-with-sorted-rows/

import java.util.PriorityQueue

class Solution {
    fun kthSmallest(mat: Array<IntArray>, k: Int): Int {
        var sums = mutableListOf(0)
        for (row in mat) {
            val heap = PriorityQueue<IntArray>(compareBy { it[0] })
            heap.offer(intArrayOf(sums[0] + row[0], 0, 0))
            val merged = mutableListOf<Int>()
            while (heap.isNotEmpty() && merged.size < k) {
                val cur = heap.poll()
                val value = cur[0]
                val i = cur[1]
                val j = cur[2]
                merged.add(value)
                if (j + 1 < row.size) {
                    heap.offer(intArrayOf(sums[i] + row[j + 1], i, j + 1))
                }
                if (j == 0 && i + 1 < sums.size) {
                    heap.offer(intArrayOf(sums[i + 1] + row[0], i + 1, 0))
                }
            }
            sums = merged
        }
        return sums[k - 1]
    }
}
''',
    "1441_build_an_array_with_stack_operations": '''// LeetCode 1441 - Build an Array With Stack Operations
// https://leetcode.com/problems/build-an-array-with-stack-operations/

class Solution {
    fun buildArray(target: IntArray, n: Int): List<String> {
        val answer = mutableListOf<String>()
        var current = 1
        for (value in target) {
            while (current < value) {
                answer.add("Push")
                answer.add("Pop")
                current++
            }
            answer.add("Push")
            current++
        }
        return answer
    }
}
''',
    "1442_count_triplets_that_can_form_two_arrays_of_equal_xor": '''// LeetCode 1442 - Count Triplets That Can Form Two Arrays of Equal XOR
// https://leetcode.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/

class Solution {
    fun countTriplets(arr: IntArray): Int {
        var answer = 0
        for (i in arr.indices) {
            var value = 0
            for (k in i until arr.size) {
                value = value xor arr[k]
                if (value == 0) answer += k - i
            }
        }
        return answer
    }
}
''',
    "1443_minimum_time_to_collect_all_apples_in_a_tree": '''// LeetCode 1443 - Minimum Time to Collect All Apples in a Tree
// https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/

class Solution {
    fun minTime(n: Int, edges: Array<IntArray>, hasApple: List<Boolean>): Int {
        val graph = Array(n) { mutableListOf<Int>() }
        for (e in edges) {
            graph[e[0]].add(e[1])
            graph[e[1]].add(e[0])
        }
        fun visit(node: Int, parent: Int): Int {
            var cost = 0
            for (child in graph[node]) {
                if (child != parent) {
                    val childCost = visit(child, node)
                    if (childCost > 0 || hasApple[child]) {
                        cost += childCost + 2
                    }
                }
            }
            return cost
        }
        return visit(0, -1)
    }
}
''',
    "1444_number_of_ways_of_cutting_a_pizza": '''// LeetCode 1444 - Number of Ways of Cutting a Pizza
// https://leetcode.com/problems/number-of-ways-of-cutting-a-pizza/

class Solution {
    fun ways(pizza: Array<String>, k: Int): Int {
        val mod = 1_000_000_007
        val rows = pizza.size
        val cols = pizza[0].length
        val apples = Array(rows + 1) { IntArray(cols + 1) }
        for (r in rows - 1 downTo 0) {
            for (c in cols - 1 downTo 0) {
                apples[r][c] = (if (pizza[r][c] == 'A') 1 else 0) +
                    apples[r + 1][c] + apples[r][c + 1] - apples[r + 1][c + 1]
            }
        }
        var dp = Array(rows) { r -> IntArray(cols) { c -> if (apples[r][c] > 0) 1 else 0 } }
        repeat(k - 1) {
            val nxt = Array(rows) { IntArray(cols) }
            for (r in 0 until rows) {
                for (c in 0 until cols) {
                    for (nr in r + 1 until rows) {
                        if (apples[r][c] > apples[nr][c]) {
                            nxt[r][c] = (nxt[r][c] + dp[nr][c]) % mod
                        }
                    }
                    for (nc in c + 1 until cols) {
                        if (apples[r][c] > apples[r][nc]) {
                            nxt[r][c] = (nxt[r][c] + dp[r][nc]) % mod
                        }
                    }
                }
            }
            dp = nxt
        }
        return dp[0][0]
    }
}
''',
    "1446_consecutive_characters": '''// LeetCode 1446 - Consecutive Characters
// https://leetcode.com/problems/consecutive-characters/

class Solution {
    fun maxPower(s: String): Int {
        var answer = 1
        var run = 1
        for (i in 1 until s.length) {
            run = if (s[i] == s[i - 1]) run + 1 else 1
            answer = maxOf(answer, run)
        }
        return answer
    }
}
''',
    "1447_simplified_fractions": '''// LeetCode 1447 - Simplified Fractions
// https://leetcode.com/problems/simplified-fractions/

class Solution {
    fun simplifiedFractions(n: Int): List<String> {
        val answer = mutableListOf<String>()
        for (a in 1 until n) {
            for (b in a + 1..n) {
                if (gcd(a, b) == 1) answer.add("$a/$b")
            }
        }
        return answer
    }

    private fun gcd(a: Int, b: Int): Int {
        var x = a
        var y = b
        while (y != 0) {
            val t = x % y
            x = y
            y = t
        }
        return x
    }
}
''',
    "1448_count_good_nodes_in_binary_tree": '''// LeetCode 1448 - Count Good Nodes in Binary Tree
// https://leetcode.com/problems/count-good-nodes-in-binary-tree/

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun goodNodes(root: TreeNode?): Int {
        fun visit(node: TreeNode?, maximum: Int): Int {
            if (node == null) return 0
            val good = if (node.`val` >= maximum) 1 else 0
            val nextMax = maxOf(maximum, node.`val`)
            return good + visit(node.left, nextMax) + visit(node.right, nextMax)
        }
        return visit(root, Int.MIN_VALUE)
    }
}
''',
    "1449_form_largest_integer_with_digits_that_add_up_to_target": '''// LeetCode 1449 - Form Largest Integer With Digits That Add up to Target
// https://leetcode.com/problems/form-largest-integer-with-digits-that-add-up-to-target/

class Solution {
    fun largestNumber(cost: IntArray, target: Int): String {
        val dp = arrayOfNulls<String>(target + 1)
        dp[0] = ""
        for (total in 1..target) {
            var best: String? = null
            for (digit in 1..9) {
                val price = cost[digit - 1]
                if (total >= price && dp[total - price] != null) {
                    val candidate = digit.toString() + dp[total - price]
                    if (best == null ||
                        candidate.length > best.length ||
                        (candidate.length == best.length && candidate > best)
                    ) {
                        best = candidate
                    }
                }
            }
            dp[total] = best
        }
        return dp[target] ?: "0"
    }
}
''',
    "1450_number_of_students_doing_homework_at_a_given_time": '''// LeetCode 1450 - Number of Students Doing Homework at a Given Time
// https://leetcode.com/problems/number-of-students-doing-homework-at-a-given-time/

class Solution {
    fun busyStudent(startTime: IntArray, endTime: IntArray, queryTime: Int): Int {
        var count = 0
        for (i in startTime.indices) {
            if (startTime[i] <= queryTime && queryTime <= endTime[i]) count++
        }
        return count
    }
}
''',
    "1451_rearrange_words_in_a_sentence": '''// LeetCode 1451 - Rearrange Words in a Sentence
// https://leetcode.com/problems/rearrange-words-in-a-sentence/

class Solution {
    fun arrangeWords(text: String): String {
        val words = text.lowercase().split(" ").toMutableList()
        words.sortBy { it.length }
        val joined = words.joinToString(" ")
        return joined.replaceFirstChar { it.uppercaseChar() }
    }
}
''',
    "1452_people_whose_list_of_favorite_companies_is_not_a_subset_of_another_list": '''// LeetCode 1452 - People Whose List of Favorite Companies Is Not a Subset of Another List
// https://leetcode.com/problems/people-whose-list-of-favorite-companies-is-not-a-subset-of-another-list/

class Solution {
    fun peopleIndexes(favoriteCompanies: List<List<String>>): List<Int> {
        val sets = favoriteCompanies.map { it.toSet() }
        val answer = mutableListOf<Int>()
        for (i in sets.indices) {
            val s = sets[i]
            val isSubset = sets.indices.any { j -> i != j && sets[j].containsAll(s) }
            if (!isSubset) answer.add(i)
        }
        return answer
    }
}
''',
    "1453_maximum_number_of_darts_inside_of_a_circular_dartboard": '''// LeetCode 1453 - Maximum Number of Darts Inside of a Circular Dartboard
// https://leetcode.com/problems/maximum-number-of-darts-inside-of-a-circular-dartboard/

import kotlin.math.sqrt

class Solution {
    fun numPoints(darts: Array<IntArray>, r: Int): Int {
        var ans = if (darts.isNotEmpty()) 1 else 0
        val rr = r.toDouble() * r
        for (i in darts.indices) {
            for (j in i + 1 until darts.size) {
                val x1 = darts[i][0].toDouble()
                val y1 = darts[i][1].toDouble()
                val x2 = darts[j][0].toDouble()
                val y2 = darts[j][1].toDouble()
                val dx = x2 - x1
                val dy = y2 - y1
                val d2 = dx * dx + dy * dy
                if (d2 > 4 * rr || d2 == 0.0) continue
                val d = sqrt(d2)
                val h = sqrt(rr - d2 / 4)
                val mx = (x1 + x2) / 2
                val my = (y1 + y2) / 2
                for (sign in intArrayOf(-1, 1)) {
                    val cx = mx + sign * (-dy) * h / d
                    val cy = my + sign * dx * h / d
                    var count = 0
                    for (p in darts) {
                        val px = p[0] - cx
                        val py = p[1] - cy
                        if (px * px + py * py <= rr + 1e-7) count++
                    }
                    ans = maxOf(ans, count)
                }
            }
        }
        return ans
    }
}
''',
    "1455_check_if_a_word_occurs_as_a_prefix_of_any_word_in_a_sentence": '''// LeetCode 1455 - Check If a Word Occurs As a Prefix of Any Word in a Sentence
// https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/

class Solution {
    fun isPrefixOfWord(sentence: String, searchWord: String): Int {
        val words = sentence.split(" ")
        for (i in words.indices) {
            if (words[i].startsWith(searchWord)) return i + 1
        }
        return -1
    }
}
''',
    "1456_maximum_number_of_vowels_in_a_substring_of_given_length": '''// LeetCode 1456 - Maximum Number of Vowels in a Substring of Given Length
// https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/

class Solution {
    fun maxVowels(s: String, k: Int): Int {
        val vowels = setOf('a', 'e', 'i', 'o', 'u')
        var cur = s.take(k).count { it in vowels }
        var ans = cur
        for (i in k until s.length) {
            if (s[i] in vowels) cur++
            if (s[i - k] in vowels) cur--
            ans = maxOf(ans, cur)
        }
        return ans
    }
}
''',
    "1457_pseudo_palindromic_paths_in_a_binary_tree": '''// LeetCode 1457 - Pseudo-Palindromic Paths in a Binary Tree
// https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun pseudoPalindromicPaths(root: TreeNode?): Int {
        fun dfs(node: TreeNode?, mask: Int): Int {
            if (node == null) return 0
            val next = mask xor (1 shl node.`val`)
            if (node.left == null && node.right == null) {
                return if (next and (next - 1) == 0) 1 else 0
            }
            return dfs(node.left, next) + dfs(node.right, next)
        }
        return dfs(root, 0)
    }
}
''',
}


def main() -> None:
    written = 0
    for folder, content in SOLUTIONS.items():
        path = ROOT / folder / "Solution.kt"
        if not path.parent.exists():
            print(f"MISSING folder: {folder}")
            continue
        path.write_text(content, encoding="utf-8", newline="\n")
        written += 1
        print(f"wrote {folder}")
    print(f"done: {written}/{len(SOLUTIONS)}")


if __name__ == "__main__":
    main()
