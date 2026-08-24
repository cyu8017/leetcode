// LeetCode 2694 - Event Emitter
// https://leetcode.com/problems/event-emitter/

class EventEmitter {
    private var handlers: [String: [([Int]) -> Void]] = [:]

    func subscribe(_ eventName: String, _ callback: @escaping ([Int]) -> Void) -> () -> Void {
        handlers[eventName, default: []].append(callback)
        var idx = handlers[eventName]!.count - 1
        return {
            if var v = self.handlers[eventName], idx >= 0, idx < v.count {
                v.remove(at: idx)
                self.handlers[eventName] = v
                idx = -1
            }
        }
    }

    func emit(_ eventName: String, _ args: [Int]) -> [Int] {
        var res: [Int] = []
        if let list = handlers[eventName] {
            for cb in list {
                cb(args)
                res.append(0)
            }
        }
        return res
    }
}

class Solution {
    func createEmitter() -> EventEmitter {
        EventEmitter()
    }
}
