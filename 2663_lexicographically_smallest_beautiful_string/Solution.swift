// LeetCode 2663 - Lexicographically Smallest Beautiful String
// https://leetcode.com/problems/lexicographically-smallest-beautiful-string/

class Solution {
    func smallestBeautifulString(_ s: String, _ k: Int) -> String {
        var b = Array(s)
        let n = b.count
        let aVal = Int(UnicodeScalar("a").value)
        for i in stride(from: n - 1, through: 0, by: -1) {
            var c = Int(b[i].asciiValue!) + 1
            while c < aVal + k {
                let ch = Character(UnicodeScalar(c)!)
                if (i > 0 && ch == b[i - 1]) || (i > 1 && ch == b[i - 2]) {
                    c += 1
                    continue
                }
                b[i] = ch
                for j in (i + 1)..<n {
                    var nc = aVal
                    while nc < aVal + k {
                        let nch = Character(UnicodeScalar(nc)!)
                        if (j > 0 && nch == b[j - 1]) || (j > 1 && nch == b[j - 2]) {
                            nc += 1
                            continue
                        }
                        b[j] = nch
                        break
                    }
                }
                return String(b)
            }
        }
        return ""
    }
}
