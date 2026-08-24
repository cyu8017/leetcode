// LeetCode 2241 - Design an ATM Machine
// https://leetcode.com/problems/design-an-atm-machine/

class ATM {

    var cnt: LongArray = LongArray(5)

    val vals = intArrayOf(20, 50, 100, 200, 500)



    constructor() {

    }


    fun deposit(banknotesCount: IntArray) {

            for (i in 0 until 5) { cnt[i] += banknotesCount[i] }

    }


    fun withdraw(amount: Int): IntArray {

            var take = IntArray(5)
            var remain = amount
            var tmp = cnt.copyOf()
            for (i in 4 downTo 0) {
                var need = remain / vals[i]
                if (need > tmp[i]) need = tmp[i]
                take[i] = need.toInt()
                remain -= need * vals[i]
            }
            if (remain != 0) return intArrayOf(-1)
            for (i in 0 until 5) { cnt[i] -= take[i] }
            return take

    }

}
