// LeetCode 3709 - Design Exam Scores Tracker
// https://leetcode.com/problems/design-exam-scores-tracker/

class ExamTracker {
    var times = [Int]()
    var pre = [Int]()

    init() {
        times = [0]
        pre = [0]
    }

    func record(_ time: Int, _ score: Int) {
        times.append(time)
        pre.append(pre.last! + score)
    }

    func totalScore(_ startTime: Int, _ endTime: Int) -> Int {
        let l = lowerBound(times, startTime) - 1
        let r = lowerBound(times, endTime + 1) - 1
        return pre[r] - pre[l]
    }

    func lowerBound(_ a: [Int], _ target: Int) -> Int {
        var lo = 0, hi = a.count
        while lo < hi {
            let mid = (lo + hi) / 2
            if a[mid] < target { lo = mid + 1 } else { hi = mid }
        }
        return lo
    }
}
