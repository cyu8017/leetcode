// LeetCode 0736 - Parse Lisp Expression
// https://leetcode.com/problems/parse-lisp-expression/

/**
 * @param {string} expression
 * @return {number}
 */
var evaluate = function(expression) {
    const tokens = [];
    let cur = '';
    for (const ch of expression) {
        if (ch === '(' || ch === ')') {
            if (cur.length > 0) { tokens.push(cur); cur = ''; }
            tokens.push(ch);
        } else if (/\s/.test(ch)) {
            if (cur.length > 0) { tokens.push(cur); cur = ''; }
        } else cur += ch;
    }
    if (cur.length > 0) tokens.push(cur);
    let pos = 0;
    const parse = (env) => {
        const token = tokens[pos];
        if (token !== '(') {
            pos++;
            if ((token[0] >= '0' && token[0] <= '9') || (token[0] === '-' && token.length > 1))
                return parseInt(token, 10);
            for (let i = env.length - 1; i >= 0; i--) {
                if (env[i].has(token)) return env[i].get(token);
            }
            return 0;
        }
        pos++;
        const op = tokens[pos++];
        if (op === 'let') {
            env.push(new Map());
            while (tokens[pos] !== ')') {
                if (tokens[pos] === '(' || tokens[pos + 1] === ')') {
                    const value = parse(env);
                    pos++;
                    env.pop();
                    return value;
                }
                const v = tokens[pos++];
                env[env.length - 1].set(v, parse(env));
            }
        }
        if (op === 'add') {
            const left = parse(env), right = parse(env);
            pos++;
            return left + right;
        }
        if (op === 'mult') {
            const left = parse(env), right = parse(env);
            pos++;
            return left * right;
        }
        return 0;
    };
    return parse([]);
};
