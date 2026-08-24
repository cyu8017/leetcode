// LeetCode 2424 - Longest Uploaded Prefix
// https://leetcode.com/problems/longest-uploaded-prefix/

class LUPrefix {
    private var uploaded: [Bool]
    private var prefixLen: Int

    init(_ n: Int) {
        uploaded = [Bool](repeating: false, count: n + 2)
        prefixLen = 0
    }

    func upload(_ video: Int) {
        uploaded[video] = true
        while uploaded[prefixLen + 1] { prefixLen += 1 }
    }

    func longest() -> Int {
        prefixLen
    }
}
