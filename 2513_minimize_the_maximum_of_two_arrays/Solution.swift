// LeetCode 2513 - Minimize the Maximum of Two Arrays
// https://leetcode.com/problems/minimize-the-maximum-of-two-arrays/

class Solution {
    func minimizeSet(_ divisor1: Int, _ divisor2: Int, _ uniqueCnt1: Int, _ uniqueCnt2: Int) -> Int {
        func gcd(_ a: Int, _ b: Int) -> Int {
            var a = a, b = b
            while b != 0 {
                let t = a % b
                a = b
                b = t
            }
            return a
        }
        let lcm = divisor1 / gcd(divisor1, divisor2) * divisor2
        func ok(_ x: Int) -> Bool {
            let a = x - x / divisor1
            let b = x - x / divisor2
            let both = x - x / lcm
            return a >= uniqueCnt1 && b >= uniqueCnt2 && both >= uniqueCnt1 + uniqueCnt2
        }
        var lo = 1, hi = 1 << 62
        while lo < hi {
            let mid = (lo + hi) / 2
            if ok(mid) { hi = mid } else { lo = mid + 1 }
        }
        return lo
    }
}
