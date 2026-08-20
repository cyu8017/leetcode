// LeetCode 1472 - Design Browser History
// https://leetcode.com/problems/design-browser-history/

class BrowserHistory {
    private var history: [String]
    private var index: Int

    init(_ homepage: String) {
        history = [homepage]
        index = 0
    }

    func visit(_ url: String) {
        history = Array(history[0...index])
        history.append(url)
        index += 1
    }

    func back(_ steps: Int) -> String {
        index = max(0, index - steps)
        return history[index]
    }

    func forward(_ steps: Int) -> String {
        index = min(history.count - 1, index + steps)
        return history[index]
    }
}
