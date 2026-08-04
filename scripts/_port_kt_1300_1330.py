#!/usr/bin/env python3
"""Port Kotlin stubs for problems 1300-1330 (listed batch)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

SOLUTIONS: dict[str, str] = {}

SOLUTIONS["1300_sum_of_mutated_array_closest_to_target"] = r"""// LeetCode 1300 - Sum of Mutated Array Closest to Target
// https://leetcode.com/problems/sum-of-mutated-array-closest-to-target/

class Solution {
    fun findBestValue(arr: IntArray, target: Int): Int {
        var lo = 0
        var hi = arr.maxOrNull()!!
        while (lo < hi) {
            val mid = (lo + hi) / 2
            val s = arr.sumOf { minOf(it, mid) }
            if (s < target) lo = mid + 1 else hi = mid
        }
        val before = arr.sumOf { minOf(it, lo - 1) }
        val after = arr.sumOf { minOf(it, lo) }
        return if (target - before <= after - target) lo - 1 else lo
    }
}
"""

SOLUTIONS["1301_number_of_paths_with_max_score"] = r"""// LeetCode 1301 - Number of Paths with Max Score
// https://leetcode.com/problems/number-of-paths-with-max-score/

class Solution {
    fun pathsWithMaxScore(board: List<String>): IntArray {
        val mod = 1_000_000_007
        val n = board.size
        val score = Array(n) { IntArray(n) { -1 } }
        val ways = Array(n) { IntArray(n) }
        score[n - 1][n - 1] = 0
        ways[n - 1][n - 1] = 1
        for (r in n - 1 downTo 0) {
            for (c in n - 1 downTo 0) {
                if (board[r][c] == 'X' || (r == n - 1 && c == n - 1)) continue
                var best = -1
                var count = 0
                for ((nr, nc) in arrayOf(r + 1 to c, r to c + 1, r + 1 to c + 1)) {
                    if (nr < n && nc < n && score[nr][nc] >= 0) {
                        when {
                            score[nr][nc] > best -> {
                                best = score[nr][nc]
                                count = ways[nr][nc]
                            }
                            score[nr][nc] == best -> count = (count + ways[nr][nc]) % mod
                        }
                    }
                }
                if (best >= 0) {
                    val add = if (board[r][c].isDigit()) board[r][c] - '0' else 0
                    score[r][c] = best + add
                    ways[r][c] = count
                }
            }
        }
        return intArrayOf(maxOf(score[0][0], 0), ways[0][0])
    }
}
"""

SOLUTIONS["1302_deepest_leaves_sum"] = r"""// LeetCode 1302 - Deepest Leaves Sum
// https://leetcode.com/problems/deepest-leaves-sum/

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun deepestLeavesSum(root: TreeNode?): Int {
        var level = listOf(root!!)
        var answer = 0
        while (level.isNotEmpty()) {
            answer = level.sumOf { it.`val` }
            level = level.flatMap { node -> listOfNotNull(node.left, node.right) }
        }
        return answer
    }
}
"""

SOLUTIONS["1304_find_n_unique_integers_sum_up_to_zero"] = r"""// LeetCode 1304 - Find N Unique Integers Sum up to Zero
// https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/

class Solution {
    fun sumZero(n: Int): IntArray {
        val answer = mutableListOf<Int>()
        for (value in 1..n / 2) {
            answer.add(-value)
            answer.add(value)
        }
        if (n % 2 != 0) answer.add(0)
        return answer.toIntArray()
    }
}
"""

SOLUTIONS["1305_all_elements_in_two_binary_search_trees"] = r"""// LeetCode 1305 - All Elements in Two Binary Search Trees
// https://leetcode.com/problems/all-elements-in-two-binary-search-trees/

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun getAllElements(root1: TreeNode?, root2: TreeNode?): List<Int> {
        fun inorder(root: TreeNode?): List<Int> {
            if (root == null) return emptyList()
            return inorder(root.left) + root.`val` + inorder(root.right)
        }
        val a = inorder(root1)
        val b = inorder(root2)
        val answer = mutableListOf<Int>()
        var i = 0
        var j = 0
        while (i < a.size || j < b.size) {
            if (j == b.size || (i < a.size && a[i] <= b[j])) {
                answer.add(a[i++])
            } else {
                answer.add(b[j++])
            }
        }
        return answer
    }
}
"""

SOLUTIONS["1306_jump_game_iii"] = r"""// LeetCode 1306 - Jump Game III
// https://leetcode.com/problems/jump-game-iii/

class Solution {
    fun canReach(arr: IntArray, start: Int): Boolean {
        val stack = ArrayDeque<Int>()
        val seen = mutableSetOf<Int>()
        stack.add(start)
        while (stack.isNotEmpty()) {
            val i = stack.removeLast()
            if (i in seen || i !in arr.indices) continue
            if (arr[i] == 0) return true
            seen.add(i)
            stack.add(i - arr[i])
            stack.add(i + arr[i])
        }
        return false
    }
}
"""

SOLUTIONS["1307_verbal_arithmetic_puzzle"] = r"""// LeetCode 1307 - Verbal Arithmetic Puzzle
// https://leetcode.com/problems/verbal-arithmetic-puzzle/

class Solution {
    fun isSolvable(words: Array<String>, result: String): Boolean {
        if (words.maxOf { it.length } > result.length) return false
        val letters = (words.joinToString("") + result).toSet()
        if (letters.size > 10) return false
        val leading = mutableSetOf<Char>()
        for (word in words) if (word.length > 1) leading.add(word[0])
        if (result.length > 1) leading.add(result[0])
        val value = mutableMapOf<Char, Int>()
        val used = BooleanArray(10)
        val width = result.length

        fun solve(column: Int, row: Int, total: Int): Boolean {
            if (column == width) return total == 0
            if (row < words.size) {
                if (column >= words[row].length) return solve(column, row + 1, total)
                val ch = words[row][words[row].length - 1 - column]
                if (ch in value) return solve(column, row + 1, total + value[ch]!!)
                for (digit in 0..9) {
                    if (!used[digit] && (digit != 0 || ch !in leading)) {
                        value[ch] = digit
                        used[digit] = true
                        if (solve(column, row + 1, total + digit)) return true
                        used[digit] = false
                        value.remove(ch)
                    }
                }
                return false
            }
            val ch = result[result.length - 1 - column]
            val digit = total % 10
            val carry = total / 10
            if (ch in value) return value[ch] == digit && solve(column + 1, 0, carry)
            if (used[digit] || (digit == 0 && ch in leading)) return false
            value[ch] = digit
            used[digit] = true
            val ok = solve(column + 1, 0, carry)
            used[digit] = false
            value.remove(ch)
            return ok
        }

        return solve(0, 0, 0)
    }
}
"""

SOLUTIONS["1309_decrypt_string_from_alphabet_to_integer_mapping"] = r"""// LeetCode 1309 - Decrypt String from Alphabet to Integer Mapping
// https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/

class Solution {
    fun freqAlphabets(s: String): String {
        val answer = mutableListOf<Char>()
        var i = s.length - 1
        while (i >= 0) {
            if (s[i] == '#') {
                answer.add(('a'.code + s.substring(i - 2, i).toInt() - 1).toChar())
                i -= 3
            } else {
                answer.add(('a'.code + (s[i] - '0') - 1).toChar())
                i -= 1
            }
        }
        return answer.asReversed().joinToString("")
    }
}
"""

SOLUTIONS["1310_xor_queries_of_a_subarray"] = r"""// LeetCode 1310 - XOR Queries of a Subarray
// https://leetcode.com/problems/xor-queries-of-a-subarray/

class Solution {
    fun xorQueries(arr: IntArray, queries: Array<IntArray>): IntArray {
        val prefix = IntArray(arr.size + 1)
        for (i in arr.indices) prefix[i + 1] = prefix[i] xor arr[i]
        return IntArray(queries.size) { i ->
            val left = queries[i][0]
            val right = queries[i][1]
            prefix[right + 1] xor prefix[left]
        }
    }
}
"""

SOLUTIONS["1311_get_watched_videos_by_your_friends"] = r"""// LeetCode 1311 - Get Watched Videos by Your Friends
// https://leetcode.com/problems/get-watched-videos-by-your-friends/

class Solution {
    fun watchedVideosByFriends(
        watchedVideos: List<List<String>>,
        friends: Array<IntArray>,
        id: Int,
        level: Int
    ): List<String> {
        val queue = ArrayDeque<Pair<Int, Int>>()
        val seen = mutableSetOf(id)
        queue.add(id to 0)
        val people = mutableListOf<Int>()
        while (queue.isNotEmpty()) {
            val (person, distance) = queue.removeFirst()
            if (distance == level) {
                people.add(person)
                continue
            }
            for (friend in friends[person]) {
                if (friend !in seen) {
                    seen.add(friend)
                    queue.add(friend to distance + 1)
                }
            }
        }
        val counts = mutableMapOf<String, Int>()
        for (person in people) {
            for (video in watchedVideos[person]) {
                counts[video] = counts.getOrDefault(video, 0) + 1
            }
        }
        return counts.keys.sortedWith(compareBy({ counts[it]!! }, { it }))
    }
}
"""

SOLUTIONS["1312_minimum_insertion_steps_to_make_a_string_palindrome"] = r"""// LeetCode 1312 - Minimum Insertion Steps to Make a String Palindrome
// https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/

class Solution {
    fun minInsertions(s: String): Int {
        val n = s.length
        val dp = IntArray(n)
        for (left in n - 2 downTo 0) {
            var diagonal = 0
            for (right in left + 1 until n) {
                val old = dp[right]
                dp[right] = if (s[left] == s[right]) {
                    diagonal
                } else {
                    1 + minOf(dp[right], dp[right - 1])
                }
                diagonal = old
            }
        }
        return if (dp.isEmpty()) 0 else dp[n - 1]
    }
}
"""

SOLUTIONS["1313_decompress_run_length_encoded_list"] = r"""// LeetCode 1313 - Decompress Run-Length Encoded List
// https://leetcode.com/problems/decompress-run-length-encoded-list/

class Solution {
    fun decompressRLElist(nums: IntArray): IntArray {
        val answer = mutableListOf<Int>()
        var i = 0
        while (i < nums.size) {
            repeat(nums[i]) { answer.add(nums[i + 1]) }
            i += 2
        }
        return answer.toIntArray()
    }
}
"""

SOLUTIONS["1314_matrix_block_sum"] = r"""// LeetCode 1314 - Matrix Block Sum
// https://leetcode.com/problems/matrix-block-sum/

class Solution {
    fun matrixBlockSum(mat: Array<IntArray>, k: Int): Array<IntArray> {
        val m = mat.size
        val n = mat[0].size
        val prefix = Array(m + 1) { IntArray(n + 1) }
        for (r in 0 until m) {
            for (c in 0 until n) {
                prefix[r + 1][c + 1] =
                    mat[r][c] + prefix[r][c + 1] + prefix[r + 1][c] - prefix[r][c]
            }
        }
        val answer = Array(m) { IntArray(n) }
        for (r in 0 until m) {
            for (c in 0 until n) {
                val r1 = maxOf(0, r - k)
                val c1 = maxOf(0, c - k)
                val r2 = minOf(m, r + k + 1)
                val c2 = minOf(n, c + k + 1)
                answer[r][c] = prefix[r2][c2] - prefix[r1][c2] - prefix[r2][c1] + prefix[r1][c1]
            }
        }
        return answer
    }
}
"""

SOLUTIONS["1315_sum_of_nodes_with_even_valued_grandparent"] = r"""// LeetCode 1315 - Sum of Nodes with Even-Valued Grandparent
// https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun sumEvenGrandparent(root: TreeNode?): Int {
        fun dfs(node: TreeNode?, parent: TreeNode?, grandparent: TreeNode?): Int {
            if (node == null) return 0
            val add = if (grandparent != null && grandparent.`val` % 2 == 0) node.`val` else 0
            return add + dfs(node.left, node, parent) + dfs(node.right, node, parent)
        }
        return dfs(root, null, null)
    }
}
"""

SOLUTIONS["1316_distinct_echo_substrings"] = r"""// LeetCode 1316 - Distinct Echo Substrings
// https://leetcode.com/problems/distinct-echo-substrings/

class Solution {
    fun distinctEchoSubstrings(text: String): Int {
        val n = text.length
        val mod1 = 1_000_000_007L
        val mod2 = 1_000_000_009L
        val base = 911382323L
        val h1 = LongArray(n + 1)
        val h2 = LongArray(n + 1)
        val p1 = LongArray(n + 1) { 1 }
        val p2 = LongArray(n + 1) { 1 }
        for (i in text.indices) {
            val code = text[i].code.toLong()
            h1[i + 1] = (h1[i] * base + code) % mod1
            h2[i + 1] = (h2[i] * base + code) % mod2
            p1[i + 1] = p1[i] * base % mod1
            p2[i + 1] = p2[i] * base % mod2
        }
        fun hashed(left: Int, right: Int): Pair<Long, Long> {
            val length = right - left
            val a = ((h1[right] - h1[left] * p1[length]) % mod1 + mod1) % mod1
            val b = ((h2[right] - h2[left] * p2[length]) % mod2 + mod2) % mod2
            return a to b
        }
        val echoes = mutableSetOf<Triple<Int, Long, Long>>()
        for (half in 1..n / 2) {
            for (left in 0..n - 2 * half) {
                if (hashed(left, left + half) == hashed(left + half, left + 2 * half)) {
                    val h = hashed(left, left + 2 * half)
                    echoes.add(Triple(2 * half, h.first, h.second))
                }
            }
        }
        return echoes.size
    }
}
"""

SOLUTIONS["1317_convert_integer_to_the_sum_of_two_no_zero_integers"] = r"""// LeetCode 1317 - Convert Integer to the Sum of Two No-Zero Integers
// https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/

class Solution {
    fun getNoZeroIntegers(n: Int): IntArray {
        fun valid(value: Int) = '0' !in value.toString()
        for (first in 1 until n) {
            if (valid(first) && valid(n - first)) return intArrayOf(first, n - first)
        }
        return intArrayOf()
    }
}
"""

SOLUTIONS["1318_minimum_flips_to_make_a_or_b_equal_to_c"] = r"""// LeetCode 1318 - Minimum Flips to Make a OR b Equal to c
// https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/

class Solution {
    fun minFlips(a: Int, b: Int, c: Int): Int {
        var aa = a
        var bb = b
        var cc = c
        var flips = 0
        while (aa != 0 || bb != 0 || cc != 0) {
            val x = aa and 1
            val y = bb and 1
            val z = cc and 1
            flips += if (z == 0) x + y else if (x == 0 && y == 0) 1 else 0
            aa = aa shr 1
            bb = bb shr 1
            cc = cc shr 1
        }
        return flips
    }
}
"""

SOLUTIONS["1319_number_of_operations_to_make_network_connected"] = r"""// LeetCode 1319 - Number of Operations to Make Network Connected
// https://leetcode.com/problems/number-of-operations-to-make-network-connected/

class Solution {
    fun makeConnected(n: Int, connections: Array<IntArray>): Int {
        if (connections.size < n - 1) return -1
        val parent = IntArray(n) { it }
        fun find(x0: Int): Int {
            var x = x0
            while (x != parent[x]) {
                parent[x] = parent[parent[x]]
                x = parent[x]
            }
            return x
        }
        for (edge in connections) {
            val ra = find(edge[0])
            val rb = find(edge[1])
            if (ra != rb) parent[ra] = rb
        }
        return (0 until n).map { find(it) }.toSet().size - 1
    }
}
"""

SOLUTIONS["1320_minimum_distance_to_type_a_word_using_two_fingers"] = r"""// LeetCode 1320 - Minimum Distance to Type a Word Using Two Fingers
// https://leetcode.com/problems/minimum-distance-to-type-a-word-using-two-fingers/

class Solution {
    fun minimumDistance(word: String): Int {
        fun distance(a: Int, b: Int): Int {
            if (a == 26) return 0
            return kotlin.math.abs(a / 6 - b / 6) + kotlin.math.abs(a % 6 - b % 6)
        }
        val letters = word.map { it - 'A' }
        var dp = mutableMapOf(26 to 0)
        var previous = letters[0]
        for (idx in 1 until letters.size) {
            val current = letters[idx]
            val nxt = mutableMapOf<Int, Int>()
            for ((free, cost) in dp) {
                nxt[free] = minOf(nxt.getOrDefault(free, Int.MAX_VALUE / 2), cost + distance(previous, current))
                nxt[previous] = minOf(nxt.getOrDefault(previous, Int.MAX_VALUE / 2), cost + distance(free, current))
            }
            dp = nxt
            previous = current
        }
        return dp.values.minOrNull()!!
    }
}
"""

SOLUTIONS["1323_maximum_69_number"] = r"""// LeetCode 1323 - Maximum 69 Number
// https://leetcode.com/problems/maximum-69-number/

class Solution {
    fun maximum69Number(num: Int): Int {
        return num.toString().replaceFirst('6', '9').toInt()
    }
}
"""

SOLUTIONS["1324_print_words_vertically"] = r"""// LeetCode 1324 - Print Words Vertically
// https://leetcode.com/problems/print-words-vertically/

class Solution {
    fun printVertically(s: String): List<String> {
        val words = s.split(" ")
        val maxLen = words.maxOf { it.length }
        return (0 until maxLen).map { i ->
            words.joinToString("") { word -> if (i < word.length) word[i].toString() else " " }.trimEnd()
        }
    }
}
"""

SOLUTIONS["1325_delete_leaves_with_a_given_value"] = r"""// LeetCode 1325 - Delete Leaves With a Given Value
// https://leetcode.com/problems/delete-leaves-with-a-given-value/

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun removeLeafNodes(root: TreeNode?, target: Int): TreeNode? {
        if (root == null) return null
        root.left = removeLeafNodes(root.left, target)
        root.right = removeLeafNodes(root.right, target)
        if (root.left == null && root.right == null && root.`val` == target) return null
        return root
    }
}
"""

SOLUTIONS["1326_minimum_number_of_taps_to_open_to_water_a_garden"] = r"""// LeetCode 1326 - Minimum Number of Taps to Open to Water a Garden
// https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/

class Solution {
    fun minTaps(n: Int, ranges: IntArray): Int {
        val farthest = IntArray(n + 1)
        for (center in ranges.indices) {
            val radius = ranges[center]
            val left = maxOf(0, center - radius)
            val right = minOf(n, center + radius)
            farthest[left] = maxOf(farthest[left], right)
        }
        var taps = 0
        var end = 0
        var reach = 0
        for (position in 0 until n) {
            reach = maxOf(reach, farthest[position])
            if (position == end) {
                if (reach <= position) return -1
                taps++
                end = reach
            }
        }
        return taps
    }
}
"""

SOLUTIONS["1328_break_a_palindrome"] = r"""// LeetCode 1328 - Break a Palindrome
// https://leetcode.com/problems/break-a-palindrome/

class Solution {
    fun breakPalindrome(palindrome: String): String {
        if (palindrome.length == 1) return ""
        val chars = palindrome.toCharArray()
        for (i in 0 until chars.size / 2) {
            if (chars[i] != 'a') {
                chars[i] = 'a'
                return String(chars)
            }
        }
        chars[chars.size - 1] = 'b'
        return String(chars)
    }
}
"""

SOLUTIONS["1329_sort_the_matrix_diagonally"] = r"""// LeetCode 1329 - Sort the Matrix Diagonally
// https://leetcode.com/problems/sort-the-matrix-diagonally/

class Solution {
    fun diagonalSort(mat: Array<IntArray>): Array<IntArray> {
        val diagonals = mutableMapOf<Int, MutableList<Int>>()
        for (r in mat.indices) {
            for (c in mat[r].indices) {
                diagonals.getOrPut(r - c) { mutableListOf() }.add(mat[r][c])
            }
        }
        for (values in diagonals.values) values.sortDescending()
        for (r in mat.indices) {
            for (c in mat[r].indices) {
                mat[r][c] = diagonals[r - c]!!.removeAt(diagonals[r - c]!!.lastIndex)
            }
        }
        return mat
    }
}
"""

SOLUTIONS["1330_reverse_subarray_to_maximize_array_value"] = r"""// LeetCode 1330 - Reverse Subarray To Maximize Array Value
// https://leetcode.com/problems/reverse-subarray-to-maximize-array-value/

class Solution {
    fun maxValueAfterReverse(nums: IntArray): Int {
        var base = 0
        for (i in 0 until nums.size - 1) base += kotlin.math.abs(nums[i] - nums[i + 1])
        var gain = 0
        var low = Int.MAX_VALUE
        var high = Int.MIN_VALUE
        for (i in 0 until nums.size - 1) {
            val a = nums[i]
            val b = nums[i + 1]
            gain = maxOf(
                gain,
                kotlin.math.abs(nums[0] - b) - kotlin.math.abs(a - b),
                kotlin.math.abs(nums[nums.size - 1] - a) - kotlin.math.abs(a - b)
            )
            low = minOf(low, maxOf(a, b))
            high = maxOf(high, minOf(a, b))
        }
        return base + maxOf(gain, 2 * (high - low))
    }
}
"""


def main() -> None:
    written = 0
    for folder, content in SOLUTIONS.items():
        path = ROOT / folder / "Solution.kt"
        if not path.parent.exists():
            print(f"MISSING FOLDER: {folder}")
            continue
        path.write_text(content.rstrip() + "\n", encoding="utf-8")
        written += 1
        print(f"wrote {folder}/Solution.kt")
    print(f"done: {written}/{len(SOLUTIONS)}")


if __name__ == "__main__":
    main()
