// LeetCode 0483 - Smallest Good Base
// https://leetcode.com/problems/smallest-good-base/

class Solution {
    func smallestGoodBase(_ n: String) -> String {
        let num = Int(n)!
        let maxLength = Int(floor(log(Double(num)) / log(2.0))) + 1
        if maxLength >= 2 {
            for length in stride(from: maxLength, through: 2, by: -1) {
                var low = 2
                var high = num - 1
                while low <= high {
                    let mid = (low + high) / 2
                    var total = 1
                    var power = 1
                    var ok = true
                    for _ in 0..<(length - 1) {
                        power *= mid
                        total += power
                        if total > num {
                            ok = false
                            break
                        }
                    }
                    if ok && total == num {
                        return String(mid)
                    }
                    if !ok || total > num {
                        high = mid - 1
                    } else {
                        low = mid + 1
                    }
                }
            }
        }
        return String(num - 1)
    }
}
