// LeetCode 2241 - Design an ATM Machine
// https://leetcode.com/problems/design-an-atm-machine/

public class ATM {
    long[] cnt = new long[5];
    int[] vals = { 20, 50, 100, 200, 500 };

    public ATM() {}

    public void Deposit(int[] banknotesCount) {
        for (int i = 0; i < 5; i++) cnt[i] += banknotesCount[i];
    }

    public int[] Withdraw(int amount) {
        int[] take = new int[5];
        long remain = amount;
        long[] tmp = (long[])cnt.Clone();
        for (int i = 4; i >= 0; i--) {
            long need = remain / vals[i];
            if (need > tmp[i]) need = tmp[i];
            take[i] = (int)need;
            remain -= need * vals[i];
        }
        if (remain != 0) return new int[] { -1 };
        for (int i = 0; i < 5; i++) cnt[i] -= take[i];
        return take;
    }
}
