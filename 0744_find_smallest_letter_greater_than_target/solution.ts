// LeetCode 0744 - Find Smallest Letter Greater Than Target
// https://leetcode.com/problems/find-smallest-letter-greater-than-target/

export function nextGreatestLetter(letters: string[], target: string): string {
    let left = 0, right = letters.length;
    while (left < right) {
        const mid = left + Math.floor((right - left) / 2);
        if (letters[mid] <= target) left = mid + 1;
        else right = mid;
    }
    return letters[left % letters.length];
}
