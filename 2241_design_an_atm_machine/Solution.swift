// LeetCode 2241 - Design an ATM Machine
// https://leetcode.com/problems/design-an-atm-machine/

class ATM {
    private var cnt = [Int](repeating: 0, count: 5)
    private let vals = [20, 50, 100, 200, 500]

    init() {}

    func deposit(_ banknotesCount: [Int]) {
        for i in 0..<5 { cnt[i] += banknotesCount[i] }
    }

    func withdraw(_ amount: Int) -> [Int] {
        var take = [Int](repeating: 0, count: 5)
        var remain = amount
        var tmp = cnt
        for i in stride(from: 4, through: 0, by: -1) {
            var need = remain / vals[i]
            if need > tmp[i] { need = tmp[i] }
            take[i] = need
            remain -= need * vals[i]
        }
        if remain != 0 { return [-1] }
        for i in 0..<5 { cnt[i] -= take[i] }
        return take
    }
}
