#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")

TREE = '''
class TreeNode {
    var val: Int
    var left: TreeNode?
    var right: TreeNode?
    init() { self.val = 0; self.left = nil; self.right = nil }
    init(_ val: Int) { self.val = val; self.left = nil; self.right = nil }
    init(_ val: Int, _ left: TreeNode?, _ right: TreeNode?) {
        self.val = val
        self.left = left
        self.right = right
    }
}
'''

def hdr(num, title, slug):
    return f"// LeetCode {num} - {title}\n// https://leetcode.com/problems/{slug}/\n"

FILES = {}

FILES["0880_decoded_string_at_index"] = hdr("0880", "Decoded String at Index", "decoded-string-at-index") + '''
class Solution {
    func decodeAtIndex(_ s: String, _ k: Int) -> String {
        let chars = Array(s)
        var size = 0
        for ch in chars {
            if ch.isNumber { size *= Int(String(ch))! }
            else { size += 1 }
        }
        var kk = k
        for ch in chars.reversed() {
            kk %= size
            if kk == 0 && ch.isLetter { return String(ch) }
            if ch.isNumber { size /= Int(String(ch))! }
            else { size -= 1 }
        }
        return ""
    }
}
'''

FILES["0881_boats_to_save_people"] = hdr("0881", "Boats to Save People", "boats-to-save-people") + '''
class Solution {
    func numRescueBoats(_ people: [Int], _ limit: Int) -> Int {
        let p = people.sorted()
        var i = 0, j = p.count - 1, boats = 0
        while i <= j {
            if p[i] + p[j] <= limit { i += 1 }
            j -= 1
            boats += 1
        }
        return boats
    }
}
'''

FILES["0882_reachable_nodes_in_subdivided_graph"] = hdr("0882", "Reachable Nodes In Subdivided Graph", "reachable-nodes-in-subdivided-graph") + '''
class Solution {
    func reachableNodes(_ edges: [[Int]], _ maxMoves: Int, _ n: Int) -> Int {
        var graph = Array(repeating: [Int: Int](), count: n)
        for e in edges {
            graph[e[0]][e[1]] = e[2]
            graph[e[1]][e[0]] = e[2]
        }
        var pq = [(maxMoves, 0)]
        var seen = [Int: Int]()
        while !pq.isEmpty {
            pq.sort { $0.0 > $1.0 }
            let cur = pq.removeFirst()
            let moves = cur.0, node = cur.1
            if seen[node] != nil { continue }
            seen[node] = moves
            for (nei, cnt) in graph[node] {
                let remain = moves - cnt - 1
                if seen[nei] == nil && remain >= 0 {
                    pq.append((remain, nei))
                }
            }
        }
        var ans = seen.count
        for e in edges {
            let left = seen[e[0]] ?? 0
            let right = seen[e[1]] ?? 0
            ans += min(e[2], left + right)
        }
        return ans
    }
}
'''

FILES["0883_projection_area_of_3d_shapes"] = hdr("0883", "Projection Area of 3D Shapes", "projection-area-of-3d-shapes") + '''
class Solution {
    func projectionArea(_ grid: [[Int]]) -> Int {
        let n = grid.count
        var top = 0, front = 0, side = 0
        for i in 0..<n {
            var rowMax = 0, colMax = 0
            for j in 0..<n {
                if grid[i][j] != 0 { top += 1 }
                rowMax = max(rowMax, grid[i][j])
                colMax = max(colMax, grid[j][i])
            }
            front += rowMax
            side += colMax
        }
        return top + front + side
    }
}
'''

FILES["0884_uncommon_words_from_two_sentences"] = hdr("0884", "Uncommon Words from Two Sentences", "uncommon-words-from-two-sentences") + '''
class Solution {
    func uncommonFromSentences(_ s1: String, _ s2: String) -> [String] {
        var count = [String: Int]()
        for w in (s1 + " " + s2).split(separator: " ") where !w.isEmpty {
            count[String(w), default: 0] += 1
        }
        return count.filter { $0.value == 1 }.map { $0.key }
    }
}
'''

FILES["0885_spiral_matrix_iii"] = hdr("0885", "Spiral Matrix III", "spiral-matrix-iii") + '''
class Solution {
    func spiralMatrixIII(_ rows: Int, _ cols: Int, _ rStart: Int, _ cStart: Int) -> [[Int]] {
        var ans = [[rStart, cStart]]
        if rows * cols == 1 { return ans }
        var r = rStart, c = cStart
        let dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        var steps = 1
        while ans.count < rows * cols {
            for d in 0..<4 {
                let dr = dirs[d][0], dc = dirs[d][1]
                for _ in 0..<steps {
                    r += dr
                    c += dc
                    if r >= 0 && r < rows && c >= 0 && c < cols {
                        ans.append([r, c])
                        if ans.count == rows * cols { return ans }
                    }
                }
                if d % 2 == 1 { steps += 1 }
            }
        }
        return ans
    }
}
'''

FILES["0886_possible_bipartition"] = hdr("0886", "Possible Bipartition", "possible-bipartition") + '''
class Solution {
    func possibleBipartition(_ n: Int, _ dislikes: [[Int]]) -> Bool {
        var graph = Array(repeating: [Int](), count: n + 1)
        for e in dislikes {
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])
        }
        var color = [Int: Int]()
        for start in 1...n {
            if color[start] != nil { continue }
            var queue = [start]
            color[start] = 0
            var qi = 0
            while qi < queue.count {
                let node = queue[qi]
                qi += 1
                for nei in graph[node] {
                    if color[nei] == nil {
                        color[nei] = color[node]! ^ 1
                        queue.append(nei)
                    } else if color[nei] == color[node] {
                        return false
                    }
                }
            }
        }
        return true
    }
}
'''

FILES["0887_super_egg_drop"] = hdr("0887", "Super Egg Drop", "super-egg-drop") + '''
class Solution {
    func superEggDrop(_ k: Int, _ n: Int) -> Int {
        var dp = Array(repeating: 0, count: k + 1)
        var moves = 0
        while dp[k] < n {
            moves += 1
            for eggs in stride(from: k, through: 1, by: -1) {
                dp[eggs] = dp[eggs] + dp[eggs - 1] + 1
            }
        }
        return moves
    }
}
'''

FILES["0888_fair_candy_swap"] = hdr("0888", "Fair Candy Swap", "fair-candy-swap") + '''
class Solution {
    func fairCandySwap(_ aliceSizes: [Int], _ bobSizes: [Int]) -> [Int] {
        let sumA = aliceSizes.reduce(0, +)
        let sumB = bobSizes.reduce(0, +)
        let diff = (sumA - sumB) / 2
        let bob = Set(bobSizes)
        for a in aliceSizes {
            if bob.contains(a - diff) { return [a, a - diff] }
        }
        return []
    }
}
'''

FILES["0889_construct_binary_tree_from_preorder_and_postorder_traversal"] = hdr("0889", "Construct Binary Tree from Preorder and Postorder Traversal", "construct-binary-tree-from-preorder-and-postorder-traversal") + TREE + '''
class Solution {
    func constructFromPrePost(_ preorder: [Int], _ postorder: [Int]) -> TreeNode? {
        var postIndex = [Int: Int]()
        for i in 0..<postorder.count { postIndex[postorder[i]] = i }
        func build(_ preLo: Int, _ preHi: Int, _ postLo: Int, _ postHi: Int) -> TreeNode? {
            if preLo > preHi { return nil }
            let root = TreeNode(preorder[preLo])
            if preLo == preHi { return root }
            let leftVal = preorder[preLo + 1]
            let leftPost = postIndex[leftVal]!
            let leftSize = leftPost - postLo + 1
            root.left = build(preLo + 1, preLo + leftSize, postLo, leftPost)
            root.right = build(preLo + leftSize + 1, preHi, leftPost + 1, postHi - 1)
            return root
        }
        let n = preorder.count
        return build(0, n - 1, 0, n - 1)
    }
}
'''

FILES["0890_find_and_replace_pattern"] = hdr("0890", "Find and Replace Pattern", "find-and-replace-pattern") + '''
class Solution {
    func findAndReplacePattern(_ words: [String], _ pattern: String) -> [String] {
        let target = normalize(pattern)
        return words.filter { normalize($0) == target }
    }

    private func normalize(_ s: String) -> [Int] {
        var mapping = [Character: Int]()
        var out = [Int]()
        for ch in s {
            if mapping[ch] == nil { mapping[ch] = mapping.count }
            out.append(mapping[ch]!)
        }
        return out
    }
}
'''

FILES["0891_sum_of_subsequence_widths"] = hdr("0891", "Sum of Subsequence Widths", "sum-of-subsequence-widths") + '''
class Solution {
    func sumSubseqWidths(_ nums: [Int]) -> Int {
        let mod = 1_000_000_007
        let a = nums.sorted()
        let n = a.count
        var pow2 = Array(repeating: 1, count: n)
        if n > 1 {
            for i in 1..<n { pow2[i] = (pow2[i - 1] * 2) % mod }
        }
        var ans = 0
        for i in 0..<n {
            ans = (ans + a[i] * ((pow2[i] - pow2[n - 1 - i] + mod) % mod)) % mod
        }
        return (ans + mod) % mod
    }
}
'''

FILES["0892_surface_area_of_3d_shapes"] = hdr("0892", "Surface Area of 3D Shapes", "surface-area-of-3d-shapes") + '''
class Solution {
    func surfaceArea(_ grid: [[Int]]) -> Int {
        let n = grid.count
        var area = 0
        for i in 0..<n {
            for j in 0..<n where grid[i][j] != 0 {
                area += grid[i][j] * 4 + 2
                if i > 0 { area -= min(grid[i][j], grid[i - 1][j]) * 2 }
                if j > 0 { area -= min(grid[i][j], grid[i][j - 1]) * 2 }
            }
        }
        return area
    }
}
'''

FILES["0893_groups_of_special_equivalent_strings"] = hdr("0893", "Groups of Special-Equivalent Strings", "groups-of-special-equivalent-strings") + '''
class Solution {
    func numSpecialEquivGroups(_ words: [String]) -> Int {
        var groups = Set<String>()
        for w in words {
            var even = [Character]()
            var odd = [Character]()
            for (i, ch) in w.enumerated() {
                if i % 2 == 0 { even.append(ch) }
                else { odd.append(ch) }
            }
            groups.insert(String(even.sorted()) + "|" + String(odd.sorted()))
        }
        return groups.count
    }
}
'''

FILES["0894_all_possible_full_binary_trees"] = hdr("0894", "All Possible Full Binary Trees", "all-possible-full-binary-trees") + TREE + '''
class Solution {
    private var memo = [Int: [TreeNode]]()

    func allPossibleFBT(_ n: Int) -> [TreeNode?] {
        return build(n)
    }

    private func build(_ nodes: Int) -> [TreeNode] {
        if let cached = memo[nodes] { return cached }
        var res = [TreeNode]()
        if nodes % 2 == 0 {
            memo[nodes] = res
            return res
        }
        if nodes == 1 {
            res.append(TreeNode(0))
            memo[nodes] = res
            return res
        }
        var left = 1
        while left < nodes {
            let right = nodes - 1 - left
            for L in build(left) {
                for R in build(right) {
                    res.append(TreeNode(0, L, R))
                }
            }
            left += 2
        }
        memo[nodes] = res
        return res
    }
}
'''

FILES["0895_maximum_frequency_stack"] = hdr("0895", "Maximum Frequency Stack", "maximum-frequency-stack") + '''
class FreqStack {
    private var freq = [Int: Int]()
    private var group = [Int: [Int]]()
    private var maxfreq = 0

    init() {}

    func push(_ val: Int) {
        let f = (freq[val] ?? 0) + 1
        freq[val] = f
        maxfreq = max(maxfreq, f)
        group[f, default: []].append(val)
    }

    func pop() -> Int {
        var list = group[maxfreq]!
        let val = list.removeLast()
        group[maxfreq] = list
        freq[val]! -= 1
        if list.isEmpty { maxfreq -= 1 }
        return val
    }
}
'''

FILES["0896_monotonic_array"] = hdr("0896", "Monotonic Array", "monotonic-array") + '''
class Solution {
    func isMonotonic(_ nums: [Int]) -> Bool {
        var inc = true, dec = true
        for i in 1..<nums.count {
            if nums[i] < nums[i - 1] { inc = false }
            if nums[i] > nums[i - 1] { dec = false }
        }
        return inc || dec
    }
}
'''

FILES["0897_increasing_order_search_tree"] = hdr("0897", "Increasing Order Search Tree", "increasing-order-search-tree") + TREE + '''
class Solution {
    private var cur: TreeNode?

    func increasingBST(_ root: TreeNode?) -> TreeNode? {
        let dummy = TreeNode(0)
        cur = dummy
        inorder(root)
        return dummy.right
    }

    private func inorder(_ node: TreeNode?) {
        guard let node = node else { return }
        inorder(node.left)
        node.left = nil
        cur?.right = node
        cur = node
        inorder(node.right)
    }
}
'''

FILES["0898_bitwise_ors_of_subarrays"] = hdr("0898", "Bitwise ORs of Subarrays", "bitwise-ors-of-subarrays") + '''
class Solution {
    func subarrayBitwiseORs(_ arr: [Int]) -> Int {
        var ans = Set<Int>()
        var cur = Set<Int>()
        for x in arr {
            var nxt: Set<Int> = [x]
            for y in cur { nxt.insert(x | y) }
            cur = nxt
            ans.formUnion(cur)
        }
        return ans.count
    }
}
'''

FILES["0899_orderly_queue"] = hdr("0899", "Orderly Queue", "orderly-queue") + '''
class Solution {
    func orderlyQueue(_ s: String, _ k: Int) -> String {
        if k > 1 { return String(s.sorted()) }
        var best = s
        let doubled = s + s
        let chars = Array(doubled)
        let n = s.count
        for i in 1..<n {
            let cand = String(chars[i..<(i + n)])
            if cand < best { best = cand }
        }
        return best
    }
}
'''

FILES["0900_rle_iterator"] = hdr("0900", "RLE Iterator", "rle-iterator") + '''
class RLEIterator {
    private var enc: [Int]
    private var i = 0

    init(_ encoding: [Int]) {
        enc = encoding
    }

    func next(_ n: Int) -> Int {
        var n = n
        while i < enc.count {
            if enc[i] >= n {
                enc[i] -= n
                return enc[i + 1]
            }
            n -= enc[i]
            i += 2
        }
        return -1
    }
}
'''

FILES["0901_online_stock_span"] = hdr("0901", "Online Stock Span", "online-stock-span") + '''
class StockSpanner {
    private var stack = [(Int, Int)]()

    init() {}

    func next(_ price: Int) -> Int {
        var span = 1
        while !stack.isEmpty && stack.last!.0 <= price {
            span += stack.removeLast().1
        }
        stack.append((price, span))
        return span
    }
}
'''

FILES["0902_numbers_at_most_n_given_digit_set"] = hdr("0902", "Numbers At Most N Given Digit Set", "numbers-at-most-n-given-digit-set") + '''
class Solution {
    func atMostNGivenDigitSet(_ digits: [String], _ n: Int) -> Int {
        let k = digits.count
        let s = Array(String(n))
        let m = s.count
        func ipow(_ bas: Int, _ exp: Int) -> Int {
            var r = 1, e = exp
            while e > 0 { r *= bas; e -= 1 }
            return r
        }
        func countUpTo(_ t: [Character]) -> Int {
            if t.isEmpty { return 0 }
            var first = 0
            for d in digits where d.first! < t[0] { first += 1 }
            var ways = first * ipow(k, t.count - 1)
            var found = false
            for d in digits where d.first! == t[0] { found = true; break }
            if found { ways += countUpTo(Array(t.dropFirst())) }
            return ways
        }
        var ans = 0
        if m > 1 {
            for i in 1..<m { ans += ipow(k, i) }
        }
        ans += countUpTo(s)
        return ans
    }
}
'''

FILES["0903_valid_permutations_for_di_sequence"] = hdr("0903", "Valid Permutations for DI Sequence", "valid-permutations-for-di-sequence") + '''
class Solution {
    func numPermsDISequence(_ s: String) -> Int {
        let mod = 1_000_000_007
        let chars = Array(s)
        let n = chars.count
        var dp = Array(repeating: 1, count: n + 1)
        if n >= 1 {
            for i in 1...n {
                var newDp = Array(repeating: 0, count: n + 1)
                if chars[i - 1] == "I" {
                    var postfix = 0
                    for j in stride(from: n - i, through: 0, by: -1) {
                        postfix = (postfix + dp[j + 1]) % mod
                        newDp[j] = postfix
                    }
                } else {
                    var prefix = 0
                    for j in 0...(n - i) {
                        prefix = (prefix + dp[j]) % mod
                        newDp[j] = prefix
                    }
                }
                dp = newDp
            }
        }
        return dp[0]
    }
}
'''

FILES["0904_fruit_into_baskets"] = hdr("0904", "Fruit Into Baskets", "fruit-into-baskets") + '''
class Solution {
    func totalFruit(_ fruits: [Int]) -> Int {
        var count = [Int: Int]()
        var left = 0, ans = 0
        for right in 0..<fruits.count {
            count[fruits[right], default: 0] += 1
            while count.count > 2 {
                count[fruits[left]]! -= 1
                if count[fruits[left]] == 0 { count.removeValue(forKey: fruits[left]) }
                left += 1
            }
            ans = max(ans, right - left + 1)
        }
        return ans
    }
}
'''

FILES["0905_sort_array_by_parity"] = hdr("0905", "Sort Array By Parity", "sort-array-by-parity") + '''
class Solution {
    func sortArrayByParity(_ nums: [Int]) -> [Int] {
        var nums = nums
        var i = 0
        for j in 0..<nums.count where nums[j] % 2 == 0 {
            nums.swapAt(i, j)
            i += 1
        }
        return nums
    }
}
'''

FILES["0906_super_palindromes"] = hdr("0906", "Super Palindromes", "super-palindromes") + '''
class Solution {
    func superpalindromesInRange(_ left: String, _ right: String) -> Int {
        let L = Int(left)!, R = Int(right)!
        var ans = 0
        func isPal(_ x: Int) -> Bool {
            let s = Array(String(x))
            return s == s.reversed()
        }
        for k in 1...100000 {
            let s = String(k)
            let pal = Int(s + String(s.reversed()))!
            let sq = pal * pal
            if sq > R { break }
            if sq >= L && isPal(sq) { ans += 1 }
        }
        for k in 1...100000 {
            let s = Array(String(k))
            var palChars = s
            if s.count > 1 {
                palChars += s.dropLast().reversed()
            }
            let pal = Int(String(palChars))!
            let sq = pal * pal
            if sq > R { break }
            if sq >= L && isPal(sq) { ans += 1 }
        }
        return ans
    }
}
'''

FILES["0907_sum_of_subarray_minimums"] = hdr("0907", "Sum of Subarray Minimums", "sum-of-subarray-minimums") + '''
class Solution {
    func sumSubarrayMins(_ arr: [Int]) -> Int {
        let mod = 1_000_000_007
        let n = arr.count
        var left = Array(repeating: -1, count: n)
        var right = Array(repeating: n, count: n)
        var st = [Int]()
        for i in 0..<n {
            while !st.isEmpty && arr[st.last!] > arr[i] { st.removeLast() }
            left[i] = st.isEmpty ? -1 : st.last!
            st.append(i)
        }
        st.removeAll()
        for i in stride(from: n - 1, through: 0, by: -1) {
            while !st.isEmpty && arr[st.last!] >= arr[i] { st.removeLast() }
            right[i] = st.isEmpty ? n : st.last!
            st.append(i)
        }
        var ans = 0
        for i in 0..<n {
            ans = (ans + arr[i] * (i - left[i]) * (right[i] - i)) % mod
        }
        return ans
    }
}
'''

FILES["0908_smallest_range_i"] = hdr("0908", "Smallest Range I", "smallest-range-i") + '''
class Solution {
    func smallestRangeI(_ nums: [Int], _ k: Int) -> Int {
        return max(0, (nums.max() ?? 0) - (nums.min() ?? 0) - 2 * k)
    }
}
'''

FILES["0909_snakes_and_ladders"] = hdr("0909", "Snakes and Ladders", "snakes-and-ladders") + '''
class Solution {
    func snakesAndLadders(_ board: [[Int]]) -> Int {
        let n = board.count
        let target = n * n
        func pos(_ square: Int) -> (Int, Int) {
            let s = square - 1
            let row = s / n
            let rem = s % n
            let r = n - 1 - row
            let c = row % 2 == 0 ? rem : n - 1 - rem
            return (r, c)
        }
        var q = [1]
        var seen = Array(repeating: false, count: target + 1)
        seen[1] = true
        var moves = 0
        var qi = 0
        while qi < q.count {
            let sz = q.count - qi
            for _ in 0..<sz {
                let cur = q[qi]
                qi += 1
                if cur == target { return moves }
                let lim = min(cur + 6, target)
                if cur + 1 <= lim {
                    for nxt in (cur + 1)...lim {
                        let rc = pos(nxt)
                        let dest = board[rc.0][rc.1] != -1 ? board[rc.0][rc.1] : nxt
                        if !seen[dest] {
                            seen[dest] = true
                            q.append(dest)
                        }
                    }
                }
            }
            moves += 1
        }
        return -1
    }
}
'''

FILES["0910_smallest_range_ii"] = hdr("0910", "Smallest Range II", "smallest-range-ii") + '''
class Solution {
    func smallestRangeII(_ nums: [Int], _ k: Int) -> Int {
        let a = nums.sorted()
        var ans = a.last! - a[0]
        for i in 0..<(a.count - 1) {
            let lo = min(a[0] + k, a[i + 1] - k)
            let hi = max(a.last! - k, a[i] + k)
            ans = min(ans, hi - lo)
        }
        return ans
    }
}
'''

FILES["0911_online_election"] = hdr("0911", "Online Election", "online-election") + '''
class TopVotedCandidate {
    private let times: [Int]
    private var leaders: [Int]

    init(_ persons: [Int], _ times: [Int]) {
        self.times = times
        leaders = Array(repeating: 0, count: persons.count)
        var counts = [Int: Int]()
        var leader = -1
        for i in 0..<persons.count {
            counts[persons[i], default: 0] += 1
            if leader == -1 || counts[persons[i]]! >= counts[leader]! { leader = persons[i] }
            leaders[i] = leader
        }
    }

    func q(_ t: Int) -> Int {
        var lo = 0, hi = times.count - 1
        while lo < hi {
            let mid = (lo + hi + 1) / 2
            if times[mid] <= t { lo = mid }
            else { hi = mid - 1 }
        }
        return leaders[lo]
    }
}
'''

FILES["0912_sort_an_array"] = hdr("0912", "Sort an Array", "sort-an-array") + '''
class Solution {
    func sortArray(_ nums: [Int]) -> [Int] {
        if nums.count <= 1 { return nums }
        let mid = nums.count / 2
        let left = sortArray(Array(nums[..<mid]))
        let right = sortArray(Array(nums[mid...]))
        var merged = [Int]()
        var i = 0, j = 0
        while i < left.count && j < right.count {
            if left[i] <= right[j] { merged.append(left[i]); i += 1 }
            else { merged.append(right[j]); j += 1 }
        }
        if i < left.count { merged.append(contentsOf: left[i...]) }
        if j < right.count { merged.append(contentsOf: right[j...]) }
        return merged
    }
}
'''

FILES["0913_cat_and_mouse"] = hdr("0913", "Cat and Mouse", "cat-and-mouse") + '''
class Solution {
    func catMouseGame(_ graph: [[Int]]) -> Int {
        let n = graph.count
        let mouseWin = 1, catWin = 2
        var states = Array(repeating: Array(repeating: Array(repeating: 0, count: 2), count: n), count: n)
        var outDegree = Array(repeating: Array(repeating: Array(repeating: 0, count: 2), count: n), count: n)
        var q = [(Int, Int, Int, Int)]()
        for cat in 0..<n {
            for mouse in 0..<n {
                outDegree[cat][mouse][0] = graph[mouse].count
                outDegree[cat][mouse][1] = graph[cat].filter { $0 != 0 }.count
            }
        }
        if n > 1 {
            for cat in 1..<n {
                for move in 0..<2 {
                    states[cat][0][move] = mouseWin
                    q.append((cat, 0, move, mouseWin))
                    states[cat][cat][move] = catWin
                    q.append((cat, cat, move, catWin))
                }
            }
        }
        var qi = 0
        while qi < q.count {
            let (cat, mouse, move, state) = q[qi]
            qi += 1
            if cat == 2 && mouse == 1 && move == 0 { return state }
            let prevMove = move ^ 1
            for prev in graph[prevMove == 1 ? cat : mouse] {
                let prevCat = prevMove == 1 ? prev : cat
                if prevCat == 0 { continue }
                let prevMouse = prevMove == 1 ? mouse : prev
                if states[prevCat][prevMouse][prevMove] != 0 { continue }
                if (prevMove == 0 && state == mouseWin) || (prevMove == 1 && state == catWin) || outDegree[prevCat][prevMouse][prevMove] == 1 {
                    states[prevCat][prevMouse][prevMove] = state
                    q.append((prevCat, prevMouse, prevMove, state))
                } else {
                    outDegree[prevCat][prevMouse][prevMove] -= 1
                }
            }
        }
        return states[2][1][0]
    }
}
'''

FILES["0914_x_of_a_kind_in_a_deck_of_cards"] = hdr("0914", "X of a Kind in a Deck of Cards", "x-of-a-kind-in-a-deck-of-cards") + '''
class Solution {
    func hasGroupsSizeX(_ deck: [Int]) -> Bool {
        var count = [Int: Int]()
        for x in deck { count[x, default: 0] += 1 }
        var g = 0
        func gcd(_ a: Int, _ b: Int) -> Int {
            var a = a, b = b
            while b != 0 { let t = a % b; a = b; b = t }
            return a
        }
        for c in count.values { g = gcd(g, c) }
        return g >= 2
    }
}
'''

FILES["0915_partition_array_into_disjoint_intervals"] = hdr("0915", "Partition Array into Disjoint Intervals", "partition-array-into-disjoint-intervals") + '''
class Solution {
    func partitionDisjoint(_ nums: [Int]) -> Int {
        let n = nums.count
        var minRight = Array(repeating: 0, count: n)
        minRight[n - 1] = nums[n - 1]
        for i in stride(from: n - 2, through: 0, by: -1) {
            minRight[i] = min(nums[i], minRight[i + 1])
        }
        var maxLeft = nums[0]
        for i in 1..<n {
            if maxLeft <= minRight[i] { return i }
            maxLeft = max(maxLeft, nums[i])
        }
        return n - 1
    }
}
'''

FILES["0916_word_subsets"] = hdr("0916", "Word Subsets", "word-subsets") + '''
class Solution {
    func wordSubsets(_ words1: [String], _ words2: [String]) -> [String] {
        let a = Int(Character("a").asciiValue!)
        var need = Array(repeating: 0, count: 26)
        for w in words2 {
            var cnt = Array(repeating: 0, count: 26)
            for c in w { cnt[Int(c.asciiValue!) - a] += 1 }
            for i in 0..<26 { need[i] = max(need[i], cnt[i]) }
        }
        var ans = [String]()
        for w in words1 {
            var cnt = Array(repeating: 0, count: 26)
            for c in w { cnt[Int(c.asciiValue!) - a] += 1 }
            var ok = true
            for i in 0..<26 where cnt[i] < need[i] { ok = false; break }
            if ok { ans.append(w) }
        }
        return ans
    }
}
'''

FILES["0917_reverse_only_letters"] = hdr("0917", "Reverse Only Letters", "reverse-only-letters") + '''
class Solution {
    func reverseOnlyLetters(_ s: String) -> String {
        var arr = Array(s)
        var i = 0, j = arr.count - 1
        while i < j {
            while i < j && !arr[i].isLetter { i += 1 }
            while i < j && !arr[j].isLetter { j -= 1 }
            arr.swapAt(i, j)
            i += 1
            j -= 1
        }
        return String(arr)
    }
}
'''

FILES["0918_maximum_sum_circular_subarray"] = hdr("0918", "Maximum Sum Circular Subarray", "maximum-sum-circular-subarray") + '''
class Solution {
    func maxSubarraySumCircular(_ nums: [Int]) -> Int {
        let total = nums.reduce(0, +)
        var maxSum = nums[0], minSum = nums[0], curMax = nums[0], curMin = nums[0]
        for i in 1..<nums.count {
            curMax = max(nums[i], curMax + nums[i])
            curMin = min(nums[i], curMin + nums[i])
            maxSum = max(maxSum, curMax)
            minSum = min(minSum, curMin)
        }
        if maxSum < 0 { return maxSum }
        return max(maxSum, total - minSum)
    }
}
'''

FILES["0919_complete_binary_tree_inserter"] = hdr("0919", "Complete Binary Tree Inserter", "complete-binary-tree-inserter") + TREE + '''
class CBTInserter {
    private let root: TreeNode
    private var parents = [TreeNode]()

    init(_ root: TreeNode?) {
        self.root = root!
        var q = [self.root]
        var qi = 0
        while qi < q.count {
            let node = q[qi]
            qi += 1
            if let left = node.left { q.append(left) }
            else { parents.append(node); break }
            if let right = node.right { q.append(right) }
            else { parents.append(node); break }
        }
        while qi < q.count {
            parents.append(q[qi])
            qi += 1
        }
    }

    func insert(_ val: Int) -> Int {
        let parent = parents[0]
        let child = TreeNode(val)
        if parent.left == nil {
            parent.left = child
        } else {
            parent.right = child
            parents.removeFirst()
        }
        parents.append(child)
        return parent.val
    }

    func get_root() -> TreeNode? {
        return root
    }

    func getRoot() -> TreeNode? {
        return root
    }
}
'''

FILES["0920_number_of_music_playlists"] = hdr("0920", "Number of Music Playlists", "number-of-music-playlists") + '''
class Solution {
    func numMusicPlaylists(_ n: Int, _ goal: Int, _ k: Int) -> Int {
        let mod = 1_000_000_007
        var dp = Array(repeating: Array(repeating: 0, count: n + 1), count: goal + 1)
        dp[0][0] = 1
        for i in 1...goal {
            for j in 1...min(i, n) {
                dp[i][j] = dp[i - 1][j - 1] * (n - j + 1) % mod
                if j > k { dp[i][j] = (dp[i][j] + dp[i - 1][j] * (j - k)) % mod }
            }
        }
        return dp[goal][n]
    }
}
'''

FILES["0921_minimum_add_to_make_parentheses_valid"] = hdr("0921", "Minimum Add to Make Parentheses Valid", "minimum-add-to-make-parentheses-valid") + '''
class Solution {
    func minAddToMakeValid(_ s: String) -> Int {
        var openNeed = 0, closeNeed = 0
        for ch in s {
            if ch == "(" { closeNeed += 1 }
            else if closeNeed > 0 { closeNeed -= 1 }
            else { openNeed += 1 }
        }
        return openNeed + closeNeed
    }
}
'''

FILES["0922_sort_array_by_parity_ii"] = hdr("0922", "Sort Array By Parity II", "sort-array-by-parity-ii") + '''
class Solution {
    func sortArrayByParityII(_ nums: [Int]) -> [Int] {
        var ans = Array(repeating: 0, count: nums.count)
        var even = 0, odd = 1
        for x in nums {
            if x % 2 == 0 { ans[even] = x; even += 2 }
            else { ans[odd] = x; odd += 2 }
        }
        return ans
    }
}
'''

FILES["0923_3sum_with_multiplicity"] = hdr("0923", "3Sum With Multiplicity", "3sum-with-multiplicity") + '''
class Solution {
    func threeSumMulti(_ arr: [Int], _ target: Int) -> Int {
        let mod = 1_000_000_007
        var count = Array(repeating: 0, count: 101)
        for x in arr { count[x] += 1 }
        var ans = 0
        for a in 0...100 where count[a] > 0 {
            for b in a...100 where count[b] > 0 {
                let c = target - a - b
                if c < b || c > 100 || count[c] == 0 { continue }
                if a == b && b == c {
                    ans += count[a] * (count[a] - 1) * (count[a] - 2) / 6
                } else if a == b {
                    ans += count[a] * (count[a] - 1) / 2 * count[c]
                } else if b == c {
                    ans += count[a] * count[b] * (count[b] - 1) / 2
                } else {
                    ans += count[a] * count[b] * count[c]
                }
            }
        }
        return ans % mod
    }
}
'''

FILES["0924_minimize_malware_spread"] = hdr("0924", "Minimize Malware Spread", "minimize-malware-spread") + '''
class Solution {
    func minMalwareSpread(_ graph: [[Int]], _ initial: [Int]) -> Int {
        let n = graph.count
        var parent = Array(0..<n)
        func find(_ x: Int) -> Int {
            if parent[x] != x { parent[x] = find(parent[x]) }
            return parent[x]
        }
        for i in 0..<n {
            for j in (i + 1)..<n where graph[i][j] == 1 {
                parent[find(i)] = find(j)
            }
        }
        var compSize = Array(repeating: 0, count: n)
        var malCount = Array(repeating: 0, count: n)
        var isInit = Array(repeating: false, count: n)
        for m in initial { isInit[m] = true }
        for i in 0..<n {
            let r = find(i)
            compSize[r] += 1
            if isInit[i] { malCount[r] += 1 }
        }
        var best = initial.min() ?? 0
        var bestSave = -1
        for m in initial {
            let r = find(m)
            if malCount[r] == 1 {
                let save = compSize[r] - 1
                if save > bestSave || (save == bestSave && m < best) {
                    bestSave = save
                    best = m
                }
            }
        }
        return best
    }
}
'''

FILES["0925_long_pressed_name"] = hdr("0925", "Long Pressed Name", "long-pressed-name") + '''
class Solution {
    func isLongPressedName(_ name: String, _ typed: String) -> Bool {
        let n = Array(name), t = Array(typed)
        var i = 0, j = 0
        while j < t.count {
            if i < n.count && n[i] == t[j] { i += 1; j += 1 }
            else if j > 0 && t[j] == t[j - 1] { j += 1 }
            else { return false }
        }
        return i == n.count
    }
}
'''

FILES["0926_flip_string_to_monotone_increasing"] = hdr("0926", "Flip String to Monotone Increasing", "flip-string-to-monotone-increasing") + '''
class Solution {
    func minFlipsMonoIncr(_ s: String) -> Int {
        var ones = 0, ans = 0
        for ch in s {
            if ch == "1" { ones += 1 }
            else { ans = min(ans + 1, ones) }
        }
        return ans
    }
}
'''

FILES["0927_three_equal_parts"] = hdr("0927", "Three Equal Parts", "three-equal-parts") + '''
class Solution {
    func threeEqualParts(_ arr: [Int]) -> [Int] {
        var ones = [Int]()
        for i in 0..<arr.count where arr[i] != 0 { ones.append(i) }
        let n = ones.count
        if n % 3 != 0 { return [-1, -1] }
        if n == 0 { return [0, arr.count - 1] }
        let third = n / 3
        let length = ones.last! - ones[2 * third] + 1
        let a = ones[0], b = ones[third], c = ones[2 * third]
        if a + length > arr.count || b + length > arr.count || c + length > arr.count {
            return [-1, -1]
        }
        for i in 0..<length {
            if arr[a + i] != arr[b + i] || arr[a + i] != arr[c + i] { return [-1, -1] }
        }
        return [a + length - 1, b + length]
    }
}
'''

FILES["0928_minimize_malware_spread_ii"] = hdr("0928", "Minimize Malware Spread II", "minimize-malware-spread-ii") + '''
class Solution {
    func minMalwareSpread(_ graph: [[Int]], _ initial: [Int]) -> Int {
        let n = graph.count
        let initSet = Set(initial)
        let clean = (0..<n).filter { !initSet.contains($0) }
        var parent = Array(0..<n)
        func find(_ x: Int) -> Int {
            if parent[x] != x { parent[x] = find(parent[x]) }
            return parent[x]
        }
        for i in clean {
            for j in clean where i < j && graph[i][j] == 1 {
                parent[find(i)] = find(j)
            }
        }
        var compSize = [Int: Int]()
        for node in clean {
            let r = find(node)
            compSize[r, default: 0] += 1
        }
        var touch = [Int: Set<Int>]()
        for m in initial {
            for node in clean where graph[m][node] == 1 {
                let r = find(node)
                touch[r, default: []].insert(m)
            }
        }
        var best = initial.min() ?? 0
        var bestSave = -1
        for m in initial {
            var save = 0
            for (r, ms) in touch {
                if ms.count == 1 && ms.contains(m) { save += compSize[r] ?? 0 }
            }
            if save > bestSave || (save == bestSave && m < best) {
                bestSave = save
                best = m
            }
        }
        return best
    }
}
'''

FILES["0929_unique_email_addresses"] = hdr("0929", "Unique Email Addresses", "unique-email-addresses") + '''
class Solution {
    func numUniqueEmails(_ emails: [String]) -> Int {
        var normalized = Set<String>()
        for email in emails {
            let at = email.firstIndex(of: "@")!
            var local = String(email[..<at])
            let domain = String(email[at...])
            if let plus = local.firstIndex(of: "+") {
                local = String(local[..<plus])
            }
            local = local.filter { $0 != "." }
            normalized.insert(local + domain)
        }
        return normalized.count
    }
}
'''

def main():
    written = 0
    for folder, body in FILES.items():
        path = ROOT / folder / "Solution.swift"
        existing = path.read_text()
        if "func solve()" not in existing:
            print(f"SKIP {folder}")
            continue
        path.write_text(body)
        written += 1
        print(f"WROTE {folder}")
    print(f"written={written} total={len(FILES)}")

if __name__ == "__main__":
    main()
