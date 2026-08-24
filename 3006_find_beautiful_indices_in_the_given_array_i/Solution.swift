// LeetCode 3006 - Find Beautiful Indices in the Given Array I
// https://leetcode.com/problems/find-beautiful-indices-in-the-given-array-i/

class Solution {
    func beautifulIndices(_ s: String, _ a: String, _ b: String, _ k: Int) -> [Int] {
        var lpsA = Array(repeating: 0, count: a.count)
        var lpsB = Array(repeating: 0, count: b.count)
        buildLPS(&lpsA, a)
        buildLPS(&lpsB, b)
        var aIndex: [Int] = []
        var bIndex: [Int] = []
        kmp(s, a, lpsA, &aIndex)
        kmp(s, b, lpsB, &bIndex)
        var result: [Int] = []
        var i = 0, j = 0
        while i < aIndex.count && j < bIndex.count {
            if aIndex[i] + k >= bIndex[j] && aIndex[i] - k <= bIndex[j] {
                result.append(aIndex[i])
                i += 1
            } else if aIndex[i] - k > bIndex[j] {
                j += 1
            } else {
                i += 1
            }
        }
        return result
    }

    private func buildLPS(_ lps: inout [Int], _ pattern: String) {
        let p = Array(pattern)
        var l = 0, i = 1
        lps[0] = 0
        while i < p.count {
            if p[i] == p[l] {
                l += 1
                lps[i] = l
                i += 1
            } else if l != 0 {
                l = lps[l - 1]
            } else {
                lps[i] = l
                i += 1
            }
        }
    }

    private func kmp(_ s: String, _ pat: String, _ lps: [Int], _ index: inout [Int]) {
        let sArr = Array(s), pArr = Array(pat)
        let sLen = sArr.count, patL = pArr.count
        var i = 0, j = 0
        while sLen - i >= patL - j {
            if sArr[i] == pArr[j] {
                i += 1
                j += 1
            }
            if j == patL {
                index.append(i - patL)
                j = lps[j - 1]
            } else if i < sLen && sArr[i] != pArr[j] {
                if j != 0 { j = lps[j - 1] }
                else { i += 1 }
            }
        }
    }
}
