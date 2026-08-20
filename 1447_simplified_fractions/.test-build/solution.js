"use strict";
function simplifiedFractions(n) { const gcd = (a, b) => b ? gcd(b, a % b) : a, answer = []; for (let d = 2; d <= n; d++)
    for (let x = 1; x < d; x++)
        if (gcd(x, d) === 1)
            answer.push(x + "/" + d); return answer; }
