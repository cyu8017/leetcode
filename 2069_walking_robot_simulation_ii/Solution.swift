// LeetCode 2069 - Walking Robot Simulation II
// https://leetcode.com/problems/walking-robot-simulation-ii/

class Robot {
    private let w: Int
    private let h: Int
    private let peri: Int
    private var pos = 0
    private var moved = false

    init(_ width: Int, _ height: Int) {
        w = width
        h = height
        peri = 2 * (width + height) - 4
    }

    private func getPosDir() -> (Int, Int, Int) {
        var p = pos
        if p == 0 {
            return moved ? (0, 0, 3) : (0, 0, 0)
        }
        if p <= w - 1 { return (p, 0, 0) }
        p -= w - 1
        if p <= h - 1 { return (w - 1, p, 1) }
        p -= h - 1
        if p <= w - 1 { return (w - 1 - p, h - 1, 2) }
        p -= w - 1
        return (0, h - 1 - p, 3)
    }

    func step(_ num: Int) {
        moved = true
        pos = (pos + num) % peri
    }

    func getPos() -> [Int] {
        let pd = getPosDir()
        return [pd.0, pd.1]
    }

    func getDir() -> String {
        ["East", "North", "West", "South"][getPosDir().2]
    }
}
