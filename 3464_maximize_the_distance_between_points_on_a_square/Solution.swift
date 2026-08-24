// LeetCode 3464 - Maximize the Distance Between Points on a Square
// https://leetcode.com/problems/maximize-the-distance-between-points-on-a-square/

class Solution {
    func maxDistance(_ side: Int, _ points: [[Int]], _ k: Int) -> Int {
        var arr = [Int]()
        for p in points {
            let x = p[0], y = p[1]
            var d = 0
            if y == 0 { d = x }
            else if x == side { d = side + y }
            else if y == side { d = 2 * side + (side - x) }
            else { d = 3 * side + (side - y) }
            arr.append(d)
        }
        arr.sort()
        let perim = 4 * side
        var lo = 0, hi = 2 * side
        while lo < hi {
            let mid = (lo + hi + 1) / 2
            if canPlace(arr, perim, k, mid) { lo = mid }
            else { hi = mid - 1 }
        }
        return lo
    }

    private func canPlace(_ arr: [Int], _ perim: Int, _ k: Int, _ mid: Int) -> Bool {
        let n = arr.count
        for s in 0..<n {
            var cnt = 1
            var last = arr[s]
            var idx = s
            while cnt < k {
                let target = last + mid
                var found = false
                for step in 1..<n {
                    let ni = (idx + step) % n
                    let val = arr[ni]
                    let add = ni <= idx ? perim : 0
                    if val + add >= target {
                        last = val + add
                        idx = ni
                        cnt += 1
                        found = true
                        break
                    }
                }
                if !found { break }
            }
            if cnt == k && last - arr[s] <= perim - mid { return true }
        }
        return false
    }
}
