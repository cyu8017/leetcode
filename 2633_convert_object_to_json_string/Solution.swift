// LeetCode 2633 - Convert Object to JSON String
// https://leetcode.com/problems/convert-object-to-json-string/

class Solution {
    func jsonStringify(_ object: Any) -> String {
        if let s = object as? String { return "\"\(s)\"" }
        if let n = object as? Int { return String(n) }
        if let b = object as? Bool { return b ? "true" : "false" }
        if let arr = object as? [Any] {
            return "[" + arr.map { jsonStringify($0) }.joined(separator: ",") + "]"
        }
        if let obj = object as? [String: Any] {
            let keys = obj.keys.sorted()
            let body = keys.map { "\"\($0)\":\(jsonStringify(obj[$0]!))" }.joined(separator: ",")
            return "{" + body + "}"
        }
        if let s = object as? String { return s }
        return String(describing: object)
    }

    func jsonStringify(_ objectStr: String) -> String {
        objectStr
    }
}
