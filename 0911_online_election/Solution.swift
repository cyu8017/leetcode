// LeetCode 0911 - Online Election
// https://leetcode.com/problems/online-election/

class TopVotedCandidate {
    private let times: [Int]
    private var leaders: [Int]

    init(_ persons: [Int], _ times: [Int]) {
        self.times = times
        leaders = Array(repeating: 0, count: persons.count)
        var counts = [Int: Int]()
        var leader = -1
        for i in 0..<persons.count {
            counts[persons[i], default: 0] += 1
            if leader == -1 || counts[persons[i]]! >= counts[leader]! { leader = persons[i] }
            leaders[i] = leader
        }
    }

    func q(_ t: Int) -> Int {
        var lo = 0, hi = times.count - 1
        while lo < hi {
            let mid = (lo + hi + 1) / 2
            if times[mid] <= t { lo = mid }
            else { hi = mid - 1 }
        }
        return leaders[lo]
    }
}
