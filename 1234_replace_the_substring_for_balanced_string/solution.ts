// LeetCode 1234 - Replace the Substring for Balanced String
// https://leetcode.com/problems/replace-the-substring-for-balanced-string/

function balancedString(s: string): number {
    const count = { Q: 0, W: 0, E: 0, R: 0 };
    for (const ch of s) count[ch]++;
    const limit = s.length / 4;
    let left = 0, answer = s.length;
    for (let right = 0; right < s.length; right++) {
        count[s[right]]--;
        while (left < s.length && count.Q <= limit && count.W <= limit && count.E <= limit && count.R <= limit) {
            answer = Math.min(answer, right - left + 1);
            count[s[left]]++;
            left++;
        }
    }
    return answer;
}
