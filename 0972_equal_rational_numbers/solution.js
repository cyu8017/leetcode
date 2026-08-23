// LeetCode 0972 - Equal Rational Numbers
// https://leetcode.com/problems/equal-rational-numbers/

/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isRationalEqual = function(s, t) {
    const parse = (x) => {
        if (!x.includes("(")) return x === "" ? 0.0 : Number(x);
        const lp = x.indexOf("(");
        let nonRep = x.slice(0, lp);
        const rep = x.slice(lp + 1, -1);
        if (!nonRep.includes(".")) nonRep += ".";
        const dot = nonRep.indexOf(".");
        const integer = nonRep.slice(0, dot);
        const frac = nonRep.slice(dot + 1);
        let bas = integer === "" ? 0.0 : Number(integer);
        if (frac.length > 0) {
            let denom = 1;
            for (let i = 0; i < frac.length; i++) denom *= 10;
            bas += Number(frac) / denom;
        }
        if (rep.length > 0) {
            const repVal = Number(rep);
            let cycle = 1;
            for (let i = 0; i < rep.length; i++) cycle *= 10;
            let denom = cycle - 1;
            for (let i = 0; i < frac.length; i++) denom *= 10;
            bas += repVal / denom;
        }
        return bas;
    };
    return Math.abs(parse(s) - parse(t)) < 1e-12;
};
