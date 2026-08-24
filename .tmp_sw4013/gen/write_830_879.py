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

LIST = '''
class ListNode {
    var val: Int
    var next: ListNode?
    init() { val = 0; next = nil }
    init(_ val: Int) { self.val = val; next = nil }
    init(_ val: Int, _ next: ListNode?) { self.val = val; self.next = next }
}
'''

def hdr(num, title, slug):
    return f"// LeetCode {num} - {title}\n// https://leetcode.com/problems/{slug}/\n"

FILES = {}

FILES["0830_positions_of_large_groups"] = hdr("0830", "Positions of Large Groups", "positions-of-large-groups") + '''
class Solution {
    func largeGroupPositions(_ s: String) -> [[Int]] {
        let chars = Array(s)
        var ans = [[Int]]()
        var i = 0
        while i < chars.count {
            var j = i
            while j < chars.count && chars[j] == chars[i] { j += 1 }
            if j - i >= 3 { ans.append([i, j - 1]) }
            i = j
        }
        return ans
    }
}
'''

FILES["0831_masking_personal_information"] = hdr("0831", "Masking Personal Information", "masking-personal-information") + '''
class Solution {
    func maskPII(_ s: String) -> String {
        if let at = s.firstIndex(of: "@") {
            let lower = s.lowercased()
            let at2 = lower.firstIndex(of: "@")!
            let name = String(lower[..<at2])
            let domain = String(lower[lower.index(after: at2)...])
            return String(name.first!) + "*****" + String(name.last!) + "@" + domain
        }
        let digits = s.filter { $0.isNumber }
        let local = String(digits.suffix(4))
        let country = digits.count - 10
        if country == 0 { return "***-***-" + local }
        return "+" + String(repeating: "*", count: country) + "-***-***-" + local
    }
}
'''

FILES["0832_flipping_an_image"] = hdr("0832", "Flipping an Image", "flipping-an-image") + '''
class Solution {
    func flipAndInvertImage(_ image: [[Int]]) -> [[Int]] {
        var image = image
        for r in 0..<image.count {
            var i = 0, j = image[r].count - 1
            while i <= j {
                let a = 1 - image[r][i], b = 1 - image[r][j]
                image[r][i] = b
                image[r][j] = a
                i += 1
                j -= 1
            }
        }
        return image
    }
}
'''

FILES["0833_find_and_replace_in_string"] = hdr("0833", "Find And Replace in String", "find-and-replace-in-string") + '''
class Solution {
    func findReplaceString(_ s: String, _ indices: [Int], _ sources: [String], _ targets: [String]) -> String {
        let chars = Array(s)
        var replaceLen = [Int: Int]()
        var replaceStr = [Int: String]()
        for k in 0..<indices.count {
            let i = indices[k]
            let src = Array(sources[k])
            if i + src.count <= chars.count && Array(chars[i..<(i + src.count)]) == src {
                replaceLen[i] = src.count
                replaceStr[i] = targets[k]
            }
        }
        var out = ""
        var i = 0
        while i < chars.count {
            if let t = replaceStr[i] {
                out += t
                i += replaceLen[i]!
            } else {
                out.append(chars[i])
                i += 1
            }
        }
        return out
    }
}
'''

FILES["0834_sum_of_distances_in_tree"] = hdr("0834", "Sum of Distances in Tree", "sum-of-distances-in-tree") + '''
class Solution {
    func sumOfDistancesInTree(_ n: Int, _ edges: [[Int]]) -> [Int] {
        var graph = Array(repeating: [Int](), count: n)
        for e in edges {
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])
        }
        var count = Array(repeating: 1, count: n)
        var ans = Array(repeating: 0, count: n)
        func post(_ node: Int, _ parent: Int) {
            for child in graph[node] where child != parent {
                post(child, node)
                count[node] += count[child]
                ans[node] += ans[child] + count[child]
            }
        }
        func reroot(_ node: Int, _ parent: Int) {
            for child in graph[node] where child != parent {
                ans[child] = ans[node] - count[child] + (n - count[child])
                reroot(child, node)
            }
        }
        post(0, -1)
        reroot(0, -1)
        return ans
    }
}
'''

FILES["0835_image_overlap"] = hdr("0835", "Image Overlap", "image-overlap") + '''
class Solution {
    func largestOverlap(_ img1: [[Int]], _ img2: [[Int]]) -> Int {
        let n = img1.count
        var ones1 = [(Int, Int)](), ones2 = [(Int, Int)]()
        for i in 0..<n {
            for j in 0..<n {
                if img1[i][j] == 1 { ones1.append((i, j)) }
                if img2[i][j] == 1 { ones2.append((i, j)) }
            }
        }
        if ones1.isEmpty || ones2.isEmpty { return 0 }
        var shifts = [Int: Int]()
        var best = 0
        for a in ones1 {
            for b in ones2 {
                let key = ((a.0 - b.0 + n) << 16) | (a.1 - b.1 + n)
                shifts[key, default: 0] += 1
                best = max(best, shifts[key]!)
            }
        }
        return best
    }
}
'''

FILES["0836_rectangle_overlap"] = hdr("0836", "Rectangle Overlap", "rectangle-overlap") + '''
class Solution {
    func isRectangleOverlap(_ rec1: [Int], _ rec2: [Int]) -> Bool {
        return !(rec1[2] <= rec2[0] || rec1[0] >= rec2[2] || rec1[3] <= rec2[1] || rec1[1] >= rec2[3])
    }
}
'''

FILES["0837_new_21_game"] = hdr("0837", "New 21 Game", "new-21-game") + '''
class Solution {
    func new21Game(_ n: Int, _ k: Int, _ maxPts: Int) -> Double {
        if k == 0 || n >= k - 1 + maxPts { return 1.0 }
        var dp = Array(repeating: 0.0, count: n + 1)
        dp[0] = 1.0
        var window = 1.0, ans = 0.0
        for i in 1...n {
            dp[i] = window / Double(maxPts)
            if i < k { window += dp[i] }
            else { ans += dp[i] }
            if i - maxPts >= 0 && i - maxPts < k { window -= dp[i - maxPts] }
        }
        return ans
    }
}
'''

FILES["0838_push_dominoes"] = hdr("0838", "Push Dominoes", "push-dominoes") + '''
class Solution {
    func pushDominoes(_ dominoes: String) -> String {
        var arr = Array(dominoes)
        let n = arr.count
        var force = Array(repeating: 0, count: n)
        var f = 0
        for i in 0..<n {
            if arr[i] == "R" { f = n }
            else if arr[i] == "L" { f = 0 }
            else { f = max(f - 1, 0) }
            force[i] += f
        }
        f = 0
        for i in stride(from: n - 1, through: 0, by: -1) {
            if arr[i] == "L" { f = n }
            else if arr[i] == "R" { f = 0 }
            else { f = max(f - 1, 0) }
            force[i] -= f
        }
        for i in 0..<n {
            if force[i] > 0 { arr[i] = "R" }
            else if force[i] < 0 { arr[i] = "L" }
            else { arr[i] = "." }
        }
        return String(arr)
    }
}
'''

FILES["0839_similar_string_groups"] = hdr("0839", "Similar String Groups", "similar-string-groups") + '''
class Solution {
    func numSimilarGroups(_ strs: [String]) -> Int {
        let n = strs.count
        var parent = Array(0..<n)
        func find(_ x: Int) -> Int {
            var x = x
            while parent[x] != x {
                parent[x] = parent[parent[x]]
                x = parent[x]
            }
            return x
        }
        func similar(_ a: String, _ b: String) -> Bool {
            let ca = Array(a), cb = Array(b)
            var d0 = -1, d1 = -1, diffs = 0
            for i in 0..<ca.count where ca[i] != cb[i] {
                diffs += 1
                if diffs > 2 { return false }
                if d0 < 0 { d0 = i } else { d1 = i }
            }
            return diffs == 0 || (diffs == 2 && ca[d0] == cb[d1] && ca[d1] == cb[d0])
        }
        var groups = n
        for i in 0..<n {
            for j in (i + 1)..<n where similar(strs[i], strs[j]) {
                let pi = find(i), pj = find(j)
                if pi != pj {
                    parent[pi] = pj
                    groups -= 1
                }
            }
        }
        return groups
    }
}
'''

FILES["0840_magic_squares_in_grid"] = hdr("0840", "Magic Squares In Grid", "magic-squares-in-grid") + '''
class Solution {
    func numMagicSquaresInside(_ grid: [[Int]]) -> Int {
        let rows = grid.count, cols = grid[0].count
        if rows < 3 || cols < 3 { return 0 }
        var ans = 0
        for i in 0..<(rows - 2) {
            for j in 0..<(cols - 2) where magic(grid, i, j) { ans += 1 }
        }
        return ans
    }

    private func magic(_ a: [[Int]], _ r: Int, _ c: Int) -> Bool {
        var vals = [Int]()
        for i in 0..<3 {
            for j in 0..<3 { vals.append(a[r + i][c + j]) }
        }
        vals.sort()
        for i in 0..<9 where vals[i] != i + 1 { return false }
        return a[r][c] + a[r][c + 1] + a[r][c + 2] == 15
            && a[r + 1][c] + a[r + 1][c + 1] + a[r + 1][c + 2] == 15
            && a[r + 2][c] + a[r + 2][c + 1] + a[r + 2][c + 2] == 15
            && a[r][c] + a[r + 1][c] + a[r + 2][c] == 15
            && a[r][c + 1] + a[r + 1][c + 1] + a[r + 2][c + 1] == 15
            && a[r][c + 2] + a[r + 1][c + 2] + a[r + 2][c + 2] == 15
            && a[r][c] + a[r + 1][c + 1] + a[r + 2][c + 2] == 15
            && a[r][c + 2] + a[r + 1][c + 1] + a[r + 2][c] == 15
    }
}
'''

FILES["0841_keys_and_rooms"] = hdr("0841", "Keys and Rooms", "keys-and-rooms") + '''
class Solution {
    func canVisitAllRooms(_ rooms: [[Int]]) -> Bool {
        var seen: Set<Int> = [0]
        var stack = [0]
        while !stack.isEmpty {
            let room = stack.removeLast()
            for key in rooms[room] where seen.insert(key).inserted {
                stack.append(key)
            }
        }
        return seen.count == rooms.count
    }
}
'''

FILES["0842_split_array_into_fibonacci_sequence"] = hdr("0842", "Split Array into Fibonacci Sequence", "split-array-into-fibonacci-sequence") + '''
class Solution {
    func splitIntoFibonacci(_ num: String) -> [Int] {
        let chars = Array(num)
        var path = [Int]()
        func dfs(_ start: Int) -> Bool {
            if start == chars.count { return path.count >= 3 }
            var val = 0
            for end in start..<chars.count {
                if chars[start] == "0" && end > start { break }
                val = val * 10 + Int(chars[end].asciiValue! - Character("0").asciiValue!)
                if val > Int32.max { break }
                if path.count >= 2 {
                    let total = path[path.count - 1] + path[path.count - 2]
                    if val < total { continue }
                    if val > total { break }
                }
                path.append(val)
                if dfs(end + 1) { return true }
                path.removeLast()
            }
            return false
        }
        _ = dfs(0)
        return path
    }
}
'''

FILES["0843_guess_the_word"] = hdr("0843", "Guess the Word", "guess-the-word") + '''
protocol Master {
    func guess(_ word: String) -> Int
}

class Solution {
    func findSecretWord(_ words: [String], _ master: Master) {
        var candidates = words
        while !candidates.isEmpty {
            var best = candidates[0]
            var bestWorst = candidates.count + 1
            for w in candidates {
                var buckets = Array(repeating: 0, count: 7)
                for c in candidates { buckets[match(w, c)] += 1 }
                let worst = buckets.max() ?? 0
                if worst < bestWorst {
                    bestWorst = worst
                    best = w
                }
            }
            let score = master.guess(best)
            if score == 6 { return }
            candidates = candidates.filter { match($0, best) == score }
        }
    }

    private func match(_ a: String, _ b: String) -> Int {
        let ca = Array(a), cb = Array(b)
        var m = 0
        for i in 0..<ca.count where ca[i] == cb[i] { m += 1 }
        return m
    }
}
'''

FILES["0844_backspace_string_compare"] = hdr("0844", "Backspace String Compare", "backspace-string-compare") + '''
class Solution {
    func backspaceCompare(_ s: String, _ t: String) -> Bool {
        return build(s) == build(t)
    }

    private func build(_ text: String) -> String {
        var stack = [Character]()
        for ch in text {
            if ch == "#" {
                if !stack.isEmpty { stack.removeLast() }
            } else {
                stack.append(ch)
            }
        }
        return String(stack)
    }
}
'''

FILES["0845_longest_mountain_in_array"] = hdr("0845", "Longest Mountain in Array", "longest-mountain-in-array") + '''
class Solution {
    func longestMountain(_ arr: [Int]) -> Int {
        let n = arr.count
        var ans = 0, i = 0
        while i < n {
            var j = i
            if j + 1 < n && arr[j] < arr[j + 1] {
                while j + 1 < n && arr[j] < arr[j + 1] { j += 1 }
                if j + 1 < n && arr[j] > arr[j + 1] {
                    while j + 1 < n && arr[j] > arr[j + 1] { j += 1 }
                    ans = max(ans, j - i + 1)
                    i = j
                    continue
                }
            }
            i += 1
        }
        return ans
    }
}
'''

FILES["0846_hand_of_straights"] = hdr("0846", "Hand of Straights", "hand-of-straights") + '''
class Solution {
    func isNStraightHand(_ hand: [Int], _ groupSize: Int) -> Bool {
        if hand.count % groupSize != 0 { return false }
        var count = [Int: Int]()
        for x in hand { count[x, default: 0] += 1 }
        let keys = count.keys.sorted()
        for start in keys {
            let need = count[start] ?? 0
            if need == 0 { continue }
            for x in start..<(start + groupSize) {
                let c = count[x] ?? 0
                if c < need { return false }
                count[x] = c - need
            }
        }
        return true
    }
}
'''

FILES["0847_shortest_path_visiting_all_nodes"] = hdr("0847", "Shortest Path Visiting All Nodes", "shortest-path-visiting-all-nodes") + '''
class Solution {
    func shortestPathLength(_ graph: [[Int]]) -> Int {
        let n = graph.count
        let target = (1 << n) - 1
        var queue = [(Int, Int, Int)]()
        var seen = Set<Int>()
        for i in 0..<n {
            queue.append((i, 1 << i, 0))
            seen.insert((i << 20) | (1 << i))
        }
        var qi = 0
        while qi < queue.count {
            let (node, mask, dist) = queue[qi]
            qi += 1
            if mask == target { return dist }
            for nxt in graph[node] {
                let nmask = mask | (1 << nxt)
                let state = (nxt << 20) | nmask
                if seen.insert(state).inserted {
                    queue.append((nxt, nmask, dist + 1))
                }
            }
        }
        return -1
    }
}
'''

FILES["0848_shifting_letters"] = hdr("0848", "Shifting Letters", "shifting-letters") + '''
class Solution {
    func shiftingLetters(_ s: String, _ shifts: [Int]) -> String {
        var arr = Array(s)
        var total = 0
        let a = Int(Character("a").asciiValue!)
        for i in stride(from: arr.count - 1, through: 0, by: -1) {
            total = (total + shifts[i]) % 26
            let v = (Int(arr[i].asciiValue!) - a + total) % 26
            arr[i] = Character(UnicodeScalar(a + v)!)
        }
        return String(arr)
    }
}
'''

FILES["0849_maximize_distance_to_closest_person"] = hdr("0849", "Maximize Distance to Closest Person", "maximize-distance-to-closest-person") + '''
class Solution {
    func maxDistToClosest(_ seats: [Int]) -> Int {
        let n = seats.count
        var prev = -1, ans = 0
        for i in 0..<n where seats[i] == 1 {
            if prev == -1 { ans = i }
            else { ans = max(ans, (i - prev) / 2) }
            prev = i
        }
        return max(ans, n - 1 - prev)
    }
}
'''

FILES["0850_rectangle_area_ii"] = hdr("0850", "Rectangle Area II", "rectangle-area-ii") + '''
class Solution {
    func rectangleArea(_ rectangles: [[Int]]) -> Int {
        let mod = 1_000_000_007
        var events = [(Int, Int, Int, Int)]()
        for r in rectangles {
            events.append((r[0], 1, r[1], r[3]))
            events.append((r[2], -1, r[1], r[3]))
        }
        events.sort { $0.0 < $1.0 }
        var active = [(Int, Int)]()
        var area = 0
        var prevX = events[0].0
        for e in events {
            let (x, typ, y1, y2) = e
            area = (area + coveredLength(active) * (x - prevX)) % mod
            if typ == 1 {
                active.append((y1, y2))
            } else {
                if let idx = active.firstIndex(where: { $0.0 == y1 && $0.1 == y2 }) {
                    active.remove(at: idx)
                }
            }
            prevX = x
        }
        return area
    }

    private func coveredLength(_ active: [(Int, Int)]) -> Int {
        if active.isEmpty { return 0 }
        let sorted = active.sorted { $0.0 < $1.0 }
        var total = 0, curStart = sorted[0].0, curEnd = sorted[0].1
        for i in 1..<sorted.count {
            let start = sorted[i].0, end = sorted[i].1
            if start > curEnd {
                total += curEnd - curStart
                curStart = start
                curEnd = end
            } else {
                curEnd = max(curEnd, end)
            }
        }
        total += curEnd - curStart
        return total
    }
}
'''

FILES["0851_loud_and_rich"] = hdr("0851", "Loud and Rich", "loud-and-rich") + '''
class Solution {
    func loudAndRich(_ richer: [[Int]], _ quiet: [Int]) -> [Int] {
        let n = quiet.count
        var graph = Array(repeating: [Int](), count: n)
        for e in richer { graph[e[1]].append(e[0]) }
        var ans = Array(repeating: -1, count: n)
        func dfs(_ person: Int) -> Int {
            if ans[person] != -1 { return ans[person] }
            var best = person
            for richerPerson in graph[person] {
                let cand = dfs(richerPerson)
                if quiet[cand] < quiet[best] { best = cand }
            }
            ans[person] = best
            return best
        }
        for i in 0..<n { _ = dfs(i) }
        return ans
    }
}
'''

FILES["0852_peak_index_in_a_mountain_array"] = hdr("0852", "Peak Index in a Mountain Array", "peak-index-in-a-mountain-array") + '''
class Solution {
    func peakIndexInMountainArray(_ arr: [Int]) -> Int {
        var lo = 0, hi = arr.count - 1
        while lo < hi {
            let mid = (lo + hi) / 2
            if arr[mid] < arr[mid + 1] { lo = mid + 1 }
            else { hi = mid }
        }
        return lo
    }
}
'''

FILES["0853_car_fleet"] = hdr("0853", "Car Fleet", "car-fleet") + '''
class Solution {
    func carFleet(_ target: Int, _ position: [Int], _ speed: [Int]) -> Int {
        let cars = zip(position, speed).sorted { $0.0 > $1.0 }
        var fleets = 0
        var maxTime = 0.0
        for car in cars {
            let time = Double(target - car.0) / Double(car.1)
            if time > maxTime {
                fleets += 1
                maxTime = time
            }
        }
        return fleets
    }
}
'''

FILES["0854_k_similar_strings"] = hdr("0854", "K-Similar Strings", "k-similar-strings") + '''
class Solution {
    func kSimilarity(_ s1: String, _ s2: String) -> Int {
        if s1 == s2 { return 0 }
        let target = Array(s2)
        var queue = [s1]
        var dist = [s1: 0]
        var qi = 0
        func neighbors(_ s: String) -> [String] {
            var arr = Array(s)
            var i = 0
            while arr[i] == target[i] { i += 1 }
            var res = [String]()
            for j in (i + 1)..<arr.count {
                if arr[j] == target[i] && arr[j] != target[j] {
                    arr.swapAt(i, j)
                    res.append(String(arr))
                    arr.swapAt(i, j)
                }
            }
            return res
        }
        while qi < queue.count {
            let cur = queue[qi]
            qi += 1
            let d = dist[cur]!
            for nxt in neighbors(cur) {
                if nxt == s2 { return d + 1 }
                if dist[nxt] == nil {
                    dist[nxt] = d + 1
                    queue.append(nxt)
                }
            }
        }
        return -1
    }
}
'''

FILES["0855_exam_room"] = hdr("0855", "Exam Room", "exam-room") + '''
class ExamRoom {
    private let n: Int
    private var seats = [Int]()

    init(_ n: Int) {
        self.n = n
    }

    func seat() -> Int {
        if seats.isEmpty {
            seats.append(0)
            return 0
        }
        var bestSeat = 0
        var bestDist = seats[0]
        var prev = seats[0]
        for cur in seats {
            if cur == prev { continue }
            let dist = (cur - prev) / 2
            if dist > bestDist {
                bestDist = dist
                bestSeat = prev + dist
            }
            prev = cur
        }
        if n - 1 - seats.last! > bestDist { bestSeat = n - 1 }
        seats.append(bestSeat)
        seats.sort()
        return bestSeat
    }

    func leave(_ p: Int) {
        if let idx = seats.firstIndex(of: p) { seats.remove(at: idx) }
    }
}
'''

FILES["0856_score_of_parentheses"] = hdr("0856", "Score of Parentheses", "score-of-parentheses") + '''
class Solution {
    func scoreOfParentheses(_ s: String) -> Int {
        var stack = [0]
        for ch in s {
            if ch == "(" {
                stack.append(0)
            } else {
                let val = stack.removeLast()
                stack[stack.count - 1] += max(2 * val, 1)
            }
        }
        return stack[0]
    }
}
'''

FILES["0857_minimum_cost_to_hire_k_workers"] = hdr("0857", "Minimum Cost to Hire K Workers", "minimum-cost-to-hire-k-workers") + '''
class Solution {
    func mincostToHireWorkers(_ quality: [Int], _ wage: [Int], _ k: Int) -> Double {
        let workers = zip(wage, quality).map { (Double($0) / Double($1), $1) }.sorted { $0.0 < $1.0 }
        var heap = [Int]()
        var totalQ = 0
        var ans = Double.greatestFiniteMagnitude
        for w in workers {
            let q = w.1
            heap.append(q)
            totalQ += q
            heap.sort()
            if heap.count > k {
                totalQ -= heap.removeLast()
            }
            if heap.count == k {
                ans = min(ans, Double(totalQ) * w.0)
            }
        }
        return ans
    }
}
'''

FILES["0858_mirror_reflection"] = hdr("0858", "Mirror Reflection", "mirror-reflection") + '''
class Solution {
    func mirrorReflection(_ p: Int, _ q: Int) -> Int {
        func gcd(_ a: Int, _ b: Int) -> Int {
            var a = a, b = b
            while b != 0 {
                let t = a % b
                a = b
                b = t
            }
            return a
        }
        var p = p, q = q
        let g = gcd(p, q)
        p /= g
        q /= g
        if p % 2 == 0 { return 2 }
        if q % 2 == 0 { return 0 }
        return 1
    }
}
'''

FILES["0859_buddy_strings"] = hdr("0859", "Buddy Strings", "buddy-strings") + '''
class Solution {
    func buddyStrings(_ s: String, _ goal: String) -> Bool {
        if s.count != goal.count { return false }
        if s == goal {
            var seen = Set<Character>()
            for ch in s {
                if !seen.insert(ch).inserted { return true }
            }
            return false
        }
        let cs = Array(s), cg = Array(goal)
        var diffs = [(Character, Character)]()
        for i in 0..<cs.count where cs[i] != cg[i] {
            diffs.append((cs[i], cg[i]))
        }
        return diffs.count == 2 && diffs[0].0 == diffs[1].1 && diffs[0].1 == diffs[1].0
    }
}
'''

FILES["0860_lemonade_change"] = hdr("0860", "Lemonade Change", "lemonade-change") + '''
class Solution {
    func lemonadeChange(_ bills: [Int]) -> Bool {
        var fives = 0, tens = 0
        for bill in bills {
            if bill == 5 {
                fives += 1
            } else if bill == 10 {
                if fives == 0 { return false }
                fives -= 1
                tens += 1
            } else {
                if tens > 0 && fives > 0 {
                    tens -= 1
                    fives -= 1
                } else if fives >= 3 {
                    fives -= 3
                } else {
                    return false
                }
            }
        }
        return true
    }
}
'''

FILES["0861_score_after_flipping_matrix"] = hdr("0861", "Score After Flipping Matrix", "score-after-flipping-matrix") + '''
class Solution {
    func matrixScore(_ grid: [[Int]]) -> Int {
        var grid = grid
        let m = grid.count, n = grid[0].count
        for r in 0..<m where grid[r][0] == 0 {
            for j in 0..<n { grid[r][j] ^= 1 }
        }
        var ans = m * (1 << (n - 1))
        for j in 1..<n {
            var ones = 0
            for i in 0..<m { ones += grid[i][j] }
            ans += max(ones, m - ones) * (1 << (n - 1 - j))
        }
        return ans
    }
}
'''

FILES["0862_shortest_subarray_with_sum_at_least_k"] = hdr("0862", "Shortest Subarray with Sum at Least K", "shortest-subarray-with-sum-at-least-k") + '''
class Solution {
    func shortestSubarray(_ nums: [Int], _ k: Int) -> Int {
        let n = nums.count
        var prefix = Array(repeating: 0, count: n + 1)
        for i in 0..<n { prefix[i + 1] = prefix[i] + nums[i] }
        var dq = [Int]()
        var ans = n + 1
        for i in 0...n {
            while !dq.isEmpty && prefix[i] - prefix[dq[0]] >= k {
                ans = min(ans, i - dq.removeFirst())
            }
            while !dq.isEmpty && prefix[i] <= prefix[dq.last!] { dq.removeLast() }
            dq.append(i)
        }
        return ans <= n ? ans : -1
    }
}
'''

FILES["0863_all_nodes_distance_k_in_binary_tree"] = hdr("0863", "All Nodes Distance K in Binary Tree", "all-nodes-distance-k-in-binary-tree") + TREE + '''
class Solution {
    func distanceK(_ root: TreeNode?, _ target: TreeNode?, _ k: Int) -> [Int] {
        guard let root = root, let target = target else { return [] }
        var graph = [ObjectIdentifier: [TreeNode]]()
        func build(_ node: TreeNode?, _ parent: TreeNode?) {
            guard let node = node else { return }
            if let parent = parent {
                graph[ObjectIdentifier(node), default: []].append(parent)
                graph[ObjectIdentifier(parent), default: []].append(node)
            }
            build(node.left, node)
            build(node.right, node)
        }
        build(root, nil)
        var queue: [TreeNode] = [target]
        var seen: Set<ObjectIdentifier> = [ObjectIdentifier(target)]
        var dist = 0
        var qi = 0
        while qi < queue.count {
            if dist == k { return queue[qi...].map { $0.val } }
            let size = queue.count - qi
            for _ in 0..<size {
                let node = queue[qi]
                qi += 1
                for nei in graph[ObjectIdentifier(node), default: []] {
                    if seen.insert(ObjectIdentifier(nei)).inserted {
                        queue.append(nei)
                    }
                }
            }
            dist += 1
        }
        return []
    }
}
'''

FILES["0864_shortest_path_to_get_all_keys"] = hdr("0864", "Shortest Path to Get All Keys", "shortest-path-to-get-all-keys") + '''
class Solution {
    func shortestPathAllKeys(_ grid: [String]) -> Int {
        let cells = grid.map { Array($0) }
        let m = cells.count, n = cells[0].count
        var allKeys = 0, sr = 0, sc = 0
        for i in 0..<m {
            for j in 0..<n {
                let ch = cells[i][j]
                if ch == "@" { sr = i; sc = j }
                else if ch >= "a" && ch <= "f" {
                    allKeys |= 1 << (Int(ch.asciiValue!) - Int(Character("a").asciiValue!))
                }
            }
        }
        var queue = [(sr, sc, 0, 0)]
        var seen: Set<Int> = [encode(sr, sc, 0)]
        let dr = [1, -1, 0, 0], dc = [0, 0, 1, -1]
        var qi = 0
        while qi < queue.count {
            let (r, c, mask, dist) = queue[qi]
            qi += 1
            if mask == allKeys { return dist }
            for k in 0..<4 {
                let nr = r + dr[k], nc = c + dc[k]
                if nr < 0 || nr >= m || nc < 0 || nc >= n || cells[nr][nc] == "#" { continue }
                let cell = cells[nr][nc]
                var nmask = mask
                if cell >= "a" && cell <= "f" {
                    nmask |= 1 << (Int(cell.asciiValue!) - Int(Character("a").asciiValue!))
                }
                if cell >= "A" && cell <= "F" {
                    let bit = 1 << (Int(cell.asciiValue!) - Int(Character("A").asciiValue!))
                    if mask & bit == 0 { continue }
                }
                let key = encode(nr, nc, nmask)
                if seen.insert(key).inserted {
                    queue.append((nr, nc, nmask, dist + 1))
                }
            }
        }
        return -1
    }

    private func encode(_ r: Int, _ c: Int, _ mask: Int) -> Int {
        return (r << 20) | (c << 10) | mask
    }
}
'''

FILES["0865_smallest_subtree_with_all_the_deepest_nodes"] = hdr("0865", "Smallest Subtree with all the Deepest Nodes", "smallest-subtree-with-all-the-deepest-nodes") + TREE + '''
class Solution {
    func subtreeWithAllDeepest(_ root: TreeNode?) -> TreeNode? {
        return dfs(root).1
    }

    private func dfs(_ node: TreeNode?) -> (Int, TreeNode?) {
        guard let node = node else { return (0, nil) }
        let left = dfs(node.left)
        let right = dfs(node.right)
        if left.0 > right.0 { return (left.0 + 1, left.1) }
        if right.0 > left.0 { return (right.0 + 1, right.1) }
        return (left.0 + 1, node)
    }
}
'''

FILES["0866_prime_palindrome"] = hdr("0866", "Prime Palindrome", "prime-palindrome") + '''
class Solution {
    func primePalindrome(_ n: Int) -> Int {
        if n <= 2 { return 2 }
        if n <= 3 { return 3 }
        if n <= 5 { return 5 }
        if n <= 7 { return 7 }
        if n <= 11 { return 11 }
        func isPrime(_ x: Int) -> Bool {
            if x < 2 { return false }
            if x % 2 == 0 { return x == 2 }
            var d = 3
            while d * d <= x {
                if x % d == 0 { return false }
                d += 2
            }
            return true
        }
        for length in 1...5 {
            let start = Int(pow(10.0, Double(length - 1)))
            let end = Int(pow(10.0, Double(length)))
            for root in start..<end {
                let s = Array(String(root))
                var pal = s
                for i in stride(from: s.count - 2, through: 0, by: -1) { pal.append(s[i]) }
                let val = Int(String(pal))!
                if val >= n && isPrime(val) { return val }
            }
        }
        return 0
    }
}
'''

FILES["0867_transpose_matrix"] = hdr("0867", "Transpose Matrix", "transpose-matrix") + '''
class Solution {
    func transpose(_ matrix: [[Int]]) -> [[Int]] {
        let m = matrix.count, n = matrix[0].count
        var ans = Array(repeating: Array(repeating: 0, count: m), count: n)
        for i in 0..<m {
            for j in 0..<n { ans[j][i] = matrix[i][j] }
        }
        return ans
    }
}
'''

FILES["0868_binary_gap"] = hdr("0868", "Binary Gap", "binary-gap") + '''
class Solution {
    func binaryGap(_ n: Int) -> Int {
        var n = n, last = -1, ans = 0, bit = 0
        while n != 0 {
            if n & 1 == 1 {
                if last != -1 { ans = max(ans, bit - last) }
                last = bit
            }
            n >>= 1
            bit += 1
        }
        return ans
    }
}
'''

FILES["0869_reordered_power_of_2"] = hdr("0869", "Reordered Power of 2", "reordered-power-of-2") + '''
class Solution {
    func reorderedPowerOf2(_ n: Int) -> Bool {
        let target = sig(n)
        for i in 0..<31 {
            if sig(1 << i) == target { return true }
        }
        return false
    }

    private func sig(_ x: Int) -> [Character] {
        return Array(String(x)).sorted()
    }
}
'''

FILES["0870_advantage_shuffle"] = hdr("0870", "Advantage Shuffle", "advantage-shuffle") + '''
class Solution {
    func advantageCount(_ nums1: [Int], _ nums2: [Int]) -> [Int] {
        var dq = nums1.sorted()
        var indexed = nums2.enumerated().map { ($0.element, $0.offset) }
        indexed.sort { $0.0 > $1.0 }
        var ans = Array(repeating: 0, count: nums1.count)
        for (val, i) in indexed {
            if dq.last! > val {
                ans[i] = dq.removeLast()
            } else {
                ans[i] = dq.removeFirst()
            }
        }
        return ans
    }
}
'''

FILES["0871_minimum_number_of_refueling_stops"] = hdr("0871", "Minimum Number of Refueling Stops", "minimum-number-of-refueling-stops") + '''
class Solution {
    func minRefuelStops(_ target: Int, _ startFuel: Int, _ stations: [[Int]]) -> Int {
        var all = stations
        all.append([target, 0])
        var heap = [Int]()
        var ans = 0, prev = 0, fuel = startFuel
        for st in all {
            let pos = st[0], gas = st[1]
            fuel -= pos - prev
            heap.sort()
            while !heap.isEmpty && fuel < 0 {
                fuel += heap.removeLast()
                ans += 1
            }
            if fuel < 0 { return -1 }
            heap.append(gas)
            prev = pos
        }
        return ans
    }
}
'''

FILES["0872_leaf_similar_trees"] = hdr("0872", "Leaf-Similar Trees", "leaf-similar-trees") + TREE + '''
class Solution {
    func leafSimilar(_ root1: TreeNode?, _ root2: TreeNode?) -> Bool {
        return leaves(root1) == leaves(root2)
    }

    private func leaves(_ node: TreeNode?) -> [Int] {
        var result = [Int]()
        func dfs(_ cur: TreeNode?) {
            guard let cur = cur else { return }
            if cur.left == nil && cur.right == nil {
                result.append(cur.val)
                return
            }
            dfs(cur.left)
            dfs(cur.right)
        }
        dfs(node)
        return result
    }
}
'''

FILES["0873_length_of_longest_fibonacci_subsequence"] = hdr("0873", "Length of Longest Fibonacci Subsequence", "length-of-longest-fibonacci-subsequence") + '''
class Solution {
    func lenLongestFibSubseq(_ arr: [Int]) -> Int {
        let n = arr.count
        var index = [Int: Int]()
        for i in 0..<n { index[arr[i]] = i }
        var dp = Array(repeating: Array(repeating: 2, count: n), count: n)
        var ans = 0
        for j in 0..<n {
            for i in 0..<j {
                if let k = index[arr[j] - arr[i]], k < i {
                    dp[i][j] = dp[k][i] + 1
                    ans = max(ans, dp[i][j])
                }
            }
        }
        return ans >= 3 ? ans : 0
    }
}
'''

FILES["0874_walking_robot_simulation"] = hdr("0874", "Walking Robot Simulation", "walking-robot-simulation") + '''
class Solution {
    func robotSim(_ commands: [Int], _ obstacles: [[Int]]) -> Int {
        var blocked = Set<Int>()
        for o in obstacles { blocked.insert(encode(o[0], o[1])) }
        let dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        var x = 0, y = 0, d = 0, best = 0
        for cmd in commands {
            if cmd == -1 { d = (d + 1) % 4 }
            else if cmd == -2 { d = (d + 3) % 4 }
            else {
                let dx = dirs[d][0], dy = dirs[d][1]
                for _ in 0..<cmd {
                    let nx = x + dx, ny = y + dy
                    if blocked.contains(encode(nx, ny)) { break }
                    x = nx
                    y = ny
                }
                best = max(best, x * x + y * y)
            }
        }
        return best
    }

    private func encode(_ x: Int, _ y: Int) -> Int {
        return ((x + 30000) << 20) | (y + 30000)
    }
}
'''

FILES["0875_koko_eating_bananas"] = hdr("0875", "Koko Eating Bananas", "koko-eating-bananas") + '''
class Solution {
    func minEatingSpeed(_ piles: [Int], _ h: Int) -> Int {
        var lo = 1, hi = piles.max() ?? 1
        while lo < hi {
            let mid = (lo + hi) / 2
            var hours = 0
            for p in piles { hours += (p + mid - 1) / mid }
            if hours <= h { hi = mid }
            else { lo = mid + 1 }
        }
        return lo
    }
}
'''

FILES["0876_middle_of_the_linked_list"] = hdr("0876", "Middle of the Linked List", "middle-of-the-linked-list") + LIST + '''
class Solution {
    func middleNode(_ head: ListNode?) -> ListNode? {
        var slow = head, fast = head
        while fast != nil && fast?.next != nil {
            slow = slow?.next
            fast = fast?.next?.next
        }
        return slow
    }
}
'''

FILES["0877_stone_game"] = hdr("0877", "Stone Game", "stone-game") + '''
class Solution {
    func stoneGame(_ piles: [Int]) -> Bool {
        return true
    }
}
'''

FILES["0878_nth_magical_number"] = hdr("0878", "Nth Magical Number", "nth-magical-number") + '''
class Solution {
    func nthMagicalNumber(_ n: Int, _ a: Int, _ b: Int) -> Int {
        let mod = 1_000_000_007
        func gcd(_ x: Int, _ y: Int) -> Int {
            var x = x, y = y
            while y != 0 {
                let t = x % y
                x = y
                y = t
            }
            return x
        }
        let lcm = a / gcd(a, b) * b
        var lo = 1, hi = n * min(a, b)
        while lo < hi {
            let mid = (lo + hi) / 2
            if mid / a + mid / b - mid / lcm >= n { hi = mid }
            else { lo = mid + 1 }
        }
        return lo % mod
    }
}
'''

FILES["0879_profitable_schemes"] = hdr("0879", "Profitable Schemes", "profitable-schemes") + '''
class Solution {
    func profitableSchemes(_ n: Int, _ minProfit: Int, _ group: [Int], _ profit: [Int]) -> Int {
        let mod = 1_000_000_007
        var dp = Array(repeating: Array(repeating: 0, count: minProfit + 1), count: n + 1)
        dp[0][0] = 1
        for i in 0..<group.count {
            let members = group[i], p = profit[i]
            for people in stride(from: n, through: members, by: -1) {
                for prof in stride(from: minProfit, through: 0, by: -1) {
                    let np = min(minProfit, prof + p)
                    dp[people][np] = (dp[people][np] + dp[people - members][prof]) % mod
                }
            }
        }
        var ans = 0
        for people in 0...n { ans = (ans + dp[people][minProfit]) % mod }
        return ans
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
