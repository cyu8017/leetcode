// LeetCode 1889 - Minimum Space Wasted From Packaging
// https://leetcode.com/problems/minimum-space-wasted-from-packaging/

class Solution {
    func minWastedSpace(_ packages: [Int], _ boxes: [[Int]]) -> Int {
        var packages = packages.sorted()
        var prefix: [Int] = []
        var running = 0
        for value in packages {
            running += value
            prefix.append(running)
        }

        var answer = Int.max

        for supplier in boxes {
            let sortedBoxes = supplier.sorted()
            var start = 0
            var wasted = 0

            for box in sortedBoxes {
                let end = upperBound(packages, box, from: start)
                if end == start {
                    continue
                }
                let packageSum = prefix[end - 1] - (start > 0 ? prefix[start - 1] : 0)
                wasted += box * (end - start) - packageSum
                start = end
            }

            if start == packages.count {
                answer = min(answer, wasted)
            }
        }

        if answer == Int.max {
            return -1
        }
        return answer % 1_000_000_007
    }

    private func upperBound(_ arr: [Int], _ target: Int, from start: Int) -> Int {
        var lo = start
        var hi = arr.count
        while lo < hi {
            let mid = (lo + hi) / 2
            if arr[mid] <= target {
                lo = mid + 1
            } else {
                hi = mid
            }
        }
        return lo
    }
}
