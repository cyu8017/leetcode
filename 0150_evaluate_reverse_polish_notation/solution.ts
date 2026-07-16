// LeetCode 0150 - Evaluate Reverse Polish Notation
// https://leetcode.com/problems/evaluate-reverse-polish-notation/

export function evalRPN(tokens: string[]): number {
  const stack: number[] = [];

  for (const token of tokens) {
    if (token === "+" || token === "-" || token === "*" || token === "/") {
      const right = stack.pop()!;
      const left = stack.pop()!;
      if (token === "+") stack.push(left + right);
      else if (token === "-") stack.push(left - right);
      else if (token === "*") stack.push(left * right);
      else stack.push(Math.trunc(left / right));
    } else {
      stack.push(Number(token));
    }
  }

  return stack[stack.length - 1];
}