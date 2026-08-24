// LeetCode 0744 - Find Smallest Letter Greater Than Target
// https://leetcode.com/problems/find-smallest-letter-greater-than-target/

class Solution {
    func nextGreatestLetter(_ letters: [Character], _ target: Character) -> Character {
        var lo = 0, hi = letters.count
        while lo < hi {
            let mid = (lo + hi) / 2
            if letters[mid] <= target { lo = mid + 1 } else { hi = mid }
        }
        return letters[lo % letters.count]
    }
}
