// LeetCode 3508 - Implement Router
// https://leetcode.com/problems/implement-router/

class Router {
    var lim: Int
    var vis = Set<Int>()
    var q = [[Int]]()
    var idx = [Int: Int]()
    var d = [Int: [Int]]()

    func f(_ a: Int, _ b: Int, _ c: Int) -> Int {
        return (a << 46) | (b << 29) | c
    }

    init(_ memoryLimit: Int) {
        lim = memoryLimit
    }

    func addPacket(_ source: Int, _ destination: Int, _ timestamp: Int) -> Bool {
        let x = f(source, destination, timestamp)
        if vis.contains(x) { return false }
        vis.insert(x)
        if q.count >= lim { _ = forwardPacket() }
        q.append([source, destination, timestamp])
        d[destination, default: []].append(timestamp)
        return true
    }

    func forwardPacket() -> [Int] {
        if q.isEmpty { return [] }
        let packet = q.removeFirst()
        let s = packet[0], dest = packet[1], t = packet[2]
        vis.remove(f(s, dest, t))
        idx[dest, default: 0] += 1
        return [s, dest, t]
    }

    func getCount(_ destination: Int, _ startTime: Int, _ endTime: Int) -> Int {
        guard let ls = d[destination] else { return 0 }
        let k = idx[destination, default: 0]
        return lowerBound(ls, k, endTime + 1) - lowerBound(ls, k, startTime)
    }

    func lowerBound(_ a: [Int], _ from: Int, _ target: Int) -> Int {
        var lo = from, hi = a.count
        while lo < hi {
            let mid = (lo + hi) / 2
            if a[mid] < target { lo = mid + 1 } else { hi = mid }
        }
        return lo
    }
}
