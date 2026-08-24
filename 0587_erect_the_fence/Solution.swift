// LeetCode 0587 - Erect the Fence
// https://leetcode.com/problems/erect-the-fence/

class Solution {
    func outerTrees(_ trees: [[Int]]) -> [[Int]] {
        var points = trees.sorted { a, b in a[0] != b[0] ? a[0] < b[0] : a[1] < b[1] }
        if points.count <= 1 { return points }
        let lower = build(points)
        let upper = build(Array(points.reversed()))
        var seen = Set<String>()
        var unique = [[Int]]()
        for i in 0..<(lower.count - 1) { addUnique(&unique, &seen, lower[i]) }
        for i in 0..<(upper.count - 1) { addUnique(&unique, &seen, upper[i]) }
        return unique
    }

    private func build(_ ordered: [[Int]]) -> [[Int]] {
        var hull = [[Int]]()
        for point in ordered {
            while hull.count >= 2 && cross(hull[hull.count - 2], hull[hull.count - 1], point) < 0 {
                hull.removeLast()
            }
            hull.append(point)
        }
        return hull
    }

    private func cross(_ o: [Int], _ a: [Int], _ b: [Int]) -> Int {
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
    }

    private func addUnique(_ unique: inout [[Int]], _ seen: inout Set<String>, _ point: [Int]) {
        let key = "\(point[0]),\(point[1])"
        if seen.insert(key).inserted { unique.append(point) }
    }
}
