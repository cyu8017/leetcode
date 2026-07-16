// LeetCode 0420 - Strong Password Checker
export function strongPasswordChecker(password: string): number {
    const length = password.length;
    let missing = 3;
    if (/[a-z]/.test(password)) missing -= 1;
    if (/[A-Z]/.test(password)) missing -= 1;
    if (/[0-9]/.test(password)) missing -= 1;

    let replace = 0;
    let oneRepeat = 0;
    let twoRepeat = 0;
    let index = 0;
    while (index < length) {
        let run = 1;
        while (index + run < length && password[index + run] === password[index]) run += 1;
        if (run >= 3) {
            replace += Math.floor(run / 3);
            if (run % 3 === 0) oneRepeat += 1;
            else if (run % 3 === 1) twoRepeat += 1;
        }
        index += run;
    }

    if (length < 6) return Math.max(6 - length, missing);
    if (length <= 20) return Math.max(missing, replace);

    let deleteCount = length - 20;
    replace -= Math.min(deleteCount, oneRepeat);
    deleteCount -= Math.min(deleteCount, oneRepeat);
    replace -= Math.min(Math.floor(deleteCount / 2), twoRepeat);
    deleteCount -= Math.min(Math.floor(deleteCount / 2), twoRepeat) * 2;
    replace -= Math.floor(deleteCount / 3);
    return length - 20 + Math.max(missing, replace);
}
