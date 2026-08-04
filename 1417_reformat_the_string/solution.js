// LeetCode 1417: Reformat The String

var reformat = function(s) {
    const letters = [], digits = [];
    for (const ch of s) (/[a-z]/.test(ch) ? letters : digits).push(ch);
    if (Math.abs(letters.length - digits.length) > 1) return "";
    const first = letters.length >= digits.length ? letters : digits, second = first === letters ? digits : letters;
    let answer = "";
    for (let i = 0; i < first.length; i++) { answer += first[i]; if (i < second.length) answer += second[i]; }
    return answer;
};
