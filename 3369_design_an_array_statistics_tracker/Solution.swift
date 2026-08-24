// LeetCode 3369 - Design an Array Statistics Tracker
// https://leetcode.com/problems/design-an-array-statistics-tracker/

class StatisticsTracker {
    private var arr = [Int]()
    private var sum = 0
    private var freq = [Int: Int]()
    private var modeFreq = 0
    private var modes = Set<Int>()

    init() {}

    func addNumber(_ num: Int) {
        arr.append(num)
        sum += num
        freq[num, default: 0] += 1
        let f = freq[num]!
        if f > modeFreq {
            modeFreq = f
            modes = [num]
        } else if f == modeFreq {
            modes.insert(num)
        }
    }

    func removeFirst() {
        if arr.isEmpty { return }
        let num = arr.removeFirst()
        sum -= num
        freq[num]! -= 1
        if freq[num] == 0 { freq.removeValue(forKey: num) }
        modeFreq = 0
        modes.removeAll()
        for (v, ff) in freq {
            if ff > modeFreq {
                modeFreq = ff
                modes = [v]
            } else if ff == modeFreq {
                modes.insert(v)
            }
        }
    }

    func getMean() -> Int {
        if arr.isEmpty { return 0 }
        return sum / arr.count
    }

    func getMedian() -> Int {
        let tmp = arr.sorted()
        let n = tmp.count
        if n % 2 == 1 { return tmp[n / 2] }
        return tmp[n / 2 - 1]
    }

    func getMode() -> Int {
        return modes.min() ?? 0
    }
}
