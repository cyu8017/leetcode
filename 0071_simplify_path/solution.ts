// LeetCode 0071 - Simplify Path
// https://leetcode.com/problems/simplify-path/

export function simplifyPath(path: string): string {
    const stack: string[] = [];

    for (const part of path.split("/")) {
        if (part === "" || part === ".") {
            continue;
        }
        if (part === "..") {
            if (stack.length > 0) {
                stack.pop();
            }
        } else {
            stack.push(part);
        }
    }

    return "/" + stack.join("/");
}
