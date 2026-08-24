// LeetCode 2299 - Strong Password Checker II
// https://leetcode.com/problems/strong-password-checker-ii/

export function strongPasswordCheckerII(password: any): any {
    if (password.length < 8) return false;
    const special = '!@#$%^&*()-+';
    let hasLower = false, hasUpper = false, hasDigit = false, hasSpecial = false;
    for (let i = 0; i < password.length; i++) {
        const c = password[i];
        if (i > 0 && c === password[i - 1]) return false;
        if (c >= 'a' && c <= 'z') hasLower = true;
        else if (c >= 'A' && c <= 'Z') hasUpper = true;
        else if (c >= '0' && c <= '9') hasDigit = true;
        else if (special.indexOf(c) >= 0) hasSpecial = true;
    }
    return hasLower && hasUpper && hasDigit && hasSpecial;
}
