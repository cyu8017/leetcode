// LeetCode 0640 - Solve the Equation
// https://leetcode.com/problems/solve-the-equation/

export function solveEquation(equation: string): string {
    const parse = (expr) => {
        let coef = 0, constant = 0;
        const n = expr.length;
        let i = 0;
        while (i < n) {
            let sign = 1;
            if (expr[i] === "+" || expr[i] === "-") {
                sign = expr[i] === "-" ? -1 : 1;
                ++i;
            }
            let value = 0;
            let hasDigit = false;
            while (i < n && expr[i] >= "0" && expr[i] <= "9") {
                hasDigit = true;
                value = value * 10 + (expr.charCodeAt(i) - 48);
                ++i;
            }
            if (i < n && expr[i] === "x") {
                coef += sign * (hasDigit ? value : 1);
                ++i;
            } else {
                constant += sign * value;
            }
        }
        return [coef, constant];
    };
    const eq = equation.indexOf("=");
    const left = parse(equation.substring(0, eq));
    const right = parse(equation.substring(eq + 1));
    const coef = left[0] - right[0];
    const constant = right[1] - left[1];
    if (coef === 0) return constant === 0 ? "Infinite solutions" : "No solution";
    return "x=" + Math.trunc(constant / coef);
}
