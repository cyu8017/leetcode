// LeetCode 1096 - Brace Expansion II
// https://leetcode.com/problems/brace-expansion-ii/

class Solution {
    func braceExpansionII(_ expression: String) -> [String] {
        let chars = Array(expression)

        func parse(_ i: inout Int) -> Set<String> {
            var union = Set<String>()
            var cur: Set<String> = [""]
            while i < chars.count && chars[i] != "}" {
                if chars[i] == "{" {
                    i += 1
                    let nested = parse(&i)
                    var next = Set<String>()
                    for a in cur {
                        for b in nested {
                            next.insert(a + b)
                        }
                    }
                    cur = next
                } else if chars[i] == "," {
                    union.formUnion(cur)
                    cur = [""]
                    i += 1
                } else {
                    var j = i
                    while j < chars.count && chars[j].isLetter {
                        j += 1
                    }
                    let token = String(chars[i..<j])
                    var next = Set<String>()
                    for a in cur {
                        next.insert(a + token)
                    }
                    cur = next
                    i = j
                }
            }
            union.formUnion(cur)
            i += 1
            return union
        }

        var i = 0
        let result = parse(&i)
        return result.sorted()
    }
}
