// LeetCode 3941 - Password Strength
// https://leetcode.com/problems/password-strength/


class Solution {
    func passwordStrength(_ password: String) -> Int {
        var st = Set<Character>()
        for ch in password { st.insert(ch) }
        var ans = 0
        for ch in st {
            if ch.isLowercase { ans += 1 }
            else if ch.isUppercase { ans += 2 }
            else if ch.isNumber { ans += 3 }
            else { ans += 5 }
        }
        return ans
    }
}
