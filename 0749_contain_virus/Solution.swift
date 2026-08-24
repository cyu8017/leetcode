// LeetCode 0749 - Contain Virus
// https://leetcode.com/problems/contain-virus/

class Solution {
    func containVirus(_ isInfected: [[Int]]) -> Int {
        var grid = isInfected
        let m = grid.count, n = grid[0].count
        var walls = 0
        func key(_ r: Int, _ c: Int) -> Int { (r << 16) | c }
        func decode(_ k: Int) -> (Int, Int) { (k >> 16, k & 0xffff) }
        while true {
            var seen = Set<Int>()
            var regions = [Set<Int>]()
            var frontiers = [Set<Int>]()
            var perimeters = [Int]()
            let dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for i in 0..<m {
                for j in 0..<n {
                    let k0 = key(i, j)
                    if grid[i][j] == 1 && !seen.contains(k0) {
                        var stack = [(i, j)]
                        seen.insert(k0)
                        var region = Set<Int>()
                        var frontier = Set<Int>()
                        var perimeter = 0
                        while let (r, c) = stack.popLast() {
                            region.insert(key(r, c))
                            for (dr, dc) in dirs {
                                let nr = r + dr, nc = c + dc
                                if nr < 0 || nr >= m || nc < 0 || nc >= n { continue }
                                let nk = key(nr, nc)
                                if grid[nr][nc] == 1 && seen.insert(nk).inserted { stack.append((nr, nc)) }
                                else if grid[nr][nc] == 0 { frontier.insert(nk); perimeter += 1 }
                            }
                        }
                        regions.append(region)
                        frontiers.append(frontier)
                        perimeters.append(perimeter)
                    }
                }
            }
            if regions.isEmpty { break }
            var quarantine = 0
            for i in 1..<regions.count where frontiers[i].count > frontiers[quarantine].count {
                quarantine = i
            }
            if frontiers[quarantine].isEmpty { break }
            walls += perimeters[quarantine]
            for cell in regions[quarantine] {
                let (r, c) = decode(cell)
                grid[r][c] = -1
            }
            for index in 0..<frontiers.count where index != quarantine {
                for cell in frontiers[index] {
                    let (r, c) = decode(cell)
                    grid[r][c] = 1
                }
            }
        }
        return walls
    }
}
