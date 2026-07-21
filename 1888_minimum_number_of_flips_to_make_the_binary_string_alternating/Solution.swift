// LeetCode 1888 - Minimum Number of Flips to Make the Binary String Alternating
// https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/

class Solution {
    func minFlips(_ s: String) -> Int {
        let chars = Array(s)
        let n = chars.count
        let doubled = chars + chars
        var alt0 = 0
        var alt1 = 0

        for i in 0..<n {
            let expected0: Character = i % 2 == 0 ? "0" : "1"
            let expected1: Character = i % 2 == 0 ? "1" : "0"
            if doubled[i] != expected0 {
                alt0 += 1
            }
            if doubled[i] != expected1 {
                alt1 += 1
            }
        }

        var answer = min(alt0, alt1)
        for i in 0..<n {
            let expectedOut0: Character = i % 2 == 0 ? "0" : "1"
            let expectedIn0: Character = (i + n) % 2 == 0 ? "0" : "1"
            if doubled[i] != expectedOut0 {
                alt0 -= 1
            }
            if doubled[i + n] != expectedIn0 {
                alt0 += 1
            }

            let expectedOut1: Character = i % 2 == 0 ? "1" : "0"
            let expectedIn1: Character = (i + n) % 2 == 0 ? "1" : "0"
            if doubled[i] != expectedOut1 {
                alt1 -= 1
            }
            if doubled[i + n] != expectedIn1 {
                alt1 += 1
            }

            answer = min(answer, alt0, alt1)
        }

        return answer
    }
}
