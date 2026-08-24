// LeetCode 0567 - Permutation in String
// https://leetcode.com/problems/permutation-in-string/

class Solution {
    func checkInclusion(_ s1: String, _ s2: String) -> Bool {
        let a1 = Array(s1)
        let a2 = Array(s2)
        let n1 = a1.count
        let n2 = a2.count
        if n1 > n2 { return false }
        var need = Array(repeating: 0, count: 26)
        var window = Array(repeating: 0, count: 26)
        func idx(_ ch: Character) -> Int { Int(ch.asciiValue! - Character("a").asciiValue!) }
        for i in 0..<n1 {
            need[idx(a1[i])] += 1
            window[idx(a2[i])] += 1
        }
        var matches = 0
        for i in 0..<26 where need[i] == window[i] { matches += 1 }
        if matches == 26 { return true }
        if n1 == n2 { return false }
        for right in n1..<n2 {
            let add = idx(a2[right])
            let remove = idx(a2[right - n1])
            if window[add] == need[add] { matches -= 1 }
            window[add] += 1
            if window[add] == need[add] { matches += 1 }
            if window[remove] == need[remove] { matches -= 1 }
            window[remove] -= 1
            if window[remove] == need[remove] { matches += 1 }
            if matches == 26 { return true }
        }
        return false
    }
}
