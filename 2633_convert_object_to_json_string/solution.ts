// LeetCode 2633 - Convert Object to JSON String
// https://leetcode.com/problems/convert-object-to-json-string/

export function jsonStringify(object: any): any {
    if (object === null) return "null";
    const t = typeof object;
    if (t === "string") return '"' + object + '"';
    if (t === "number" || t === "boolean") return String(object);
    if (Array.isArray(object)) {
        return "[" + object.map(jsonStringify).join(",") + "]";
    }
    const keys = Object.keys(object);
    return "{" + keys.map(k => '"' + k + '":' + jsonStringify(object[k])).join(",") + "}";
}
