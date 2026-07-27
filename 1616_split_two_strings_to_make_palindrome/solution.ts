// LeetCode 1616 - Split Two Strings to Make Palindrome
// https://leetcode.com/problems/split-two-strings-to-make-palindrome/

function checkPalindromeFormation(a: string, b: string): boolean {
    const isPal = (s: string): boolean => {
        let i = 0, j = s.length - 1;
        while (i < j) {
            if (s[i++] !== s[j--]) return false;
        }
        return true;
    };
    const check = (x: string, y: string): boolean => {
        let i = 0, j = x.length - 1;
        while (i < j && x[i] === y[j]) {
            i++;
            j--;
        }
        return isPal(x.slice(i, j + 1)) || isPal(y.slice(i, j + 1));
    };
    return check(a, b) || check(b, a);
}
